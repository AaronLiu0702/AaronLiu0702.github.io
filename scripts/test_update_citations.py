#!/usr/bin/env python3
"""Offline regression tests for citation provider parsing and badge updates."""

import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "update_citations", Path(__file__).with_name("update_citations.py")
)
updater = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(updater)

ARXIV_ID = "2604.11778"
BIB_TITLE = (
    "General365: Benchmarking General Reasoning in Large Language Models "
    "Across Diverse and Challenging Tasks"
)
S2_TITLE = (
    "General365: Benchmarking General Reasoning in LLMs "
    "Across Diverse and Challenging Tasks"
)


class CitationProviderTests(unittest.TestCase):
    def test_counts_distinguish_real_zero_from_missing_or_invalid_data(self):
        for raw, expected in [(0, 0), (6, 6), ("0", 0), (" 12 ", 12)]:
            with self.subTest(raw=raw):
                self.assertEqual(updater.citation_count(raw), expected)
        for raw in [None, True, False, -1, 1.0, "-1", "1.0", "unknown", {}]:
            with self.subTest(raw=raw):
                self.assertIsNone(updater.citation_count(raw))

    def test_google_duplicates_keep_largest_and_missing_counts_are_not_zero(self):
        response = {"articles": [
            {"title": BIB_TITLE, "cited_by": {"value": 6}},
            {"title": BIB_TITLE.upper() + ".", "cited_by": {"value": 2}},
            {"title": "A real zero", "cited_by": {"value": 0}},
            {"title": "No citation object"},
            {"title": "No citation count", "cited_by": {}},
            {"title": "An invalid count", "cited_by": {"value": True}},
        ]}
        with patch.object(updater, "http_json", return_value=response):
            counts = updater.fetch_google_scholar_serpapi("test-author", "test-placeholder")
        self.assertEqual(counts, {
            updater.norm_title(BIB_TITLE): 6,
            updater.norm_title("A real zero"): 0,
        })

    def test_semantic_scholar_validates_counts_but_keeps_title_for_matching(self):
        response = [
            {"title": "Real zero", "citationCount": 0},
            {"title": S2_TITLE, "citationCount": False},
            {"title": "Negative count", "citationCount": -1},
            None,
        ]
        diagnostics = {}
        with patch.object(updater, "http_json", return_value=response):
            counts = updater.fetch_semantic_scholar(["1.1", "2.2", "3.3", "4.4"], diagnostics)
        self.assertEqual(counts["1.1"]["citations"], 0)
        self.assertIsNone(counts["2.2"]["citations"])
        self.assertEqual(counts["2.2"]["title"], S2_TITLE)
        self.assertIsNone(counts["3.3"]["citations"])
        self.assertNotIn("4.4", counts)
        self.assertIn("4/4 entries; 1 valid counts", diagnostics["s2"])

    def test_google_error_cannot_supply_a_current_count(self):
        response = {
            "search_metadata": {"status": "Error"},
            "error": "Failed to retrieve profile",
            "articles": [{"title": BIB_TITLE, "cited_by": {"value": 6}}],
        }
        diagnostics = {}
        with patch.object(updater, "http_json", return_value=response):
            result = updater.fetch_google_scholar_serpapi("test-author", "test-placeholder", diagnostics)
        self.assertEqual(result, {})
        self.assertEqual(diagnostics["gs"], "provider reported an error")

    def test_google_empty_result_is_distinct_from_a_failed_request(self):
        for response, expected in [
            (None, "request failed or invalid response"),
            ({"articles": []}, "empty profile result"),
        ]:
            with self.subTest(response=response):
                diagnostics = {}
                with patch.object(updater, "http_json", return_value=response):
                    result = updater.fetch_google_scholar_serpapi("test-author", "test-placeholder", diagnostics)
                self.assertEqual(result, {})
                self.assertEqual(diagnostics["gs"], expected)


class CitationUpdateTests(unittest.TestCase):
    def run_update(self, s2_count, gs_count, previous, gs_title=BIB_TITLE):
        """Exercise discovery, both provider parsers, selection, disk writes, and report."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            publication = root / "pub.md"
            publication.write_text(
                "[![Citations](https://example.test/badge)]"
                f"(https://arxiv.org/abs/{ARXIV_ID})\n", encoding="utf-8"
            )
            bib = root / "papers.bib"
            bib.write_text(
                "@article{general365,\n"
                f"  title={{{BIB_TITLE}}},\n"
                f"  eprint={{{ARXIV_ID}}},\n}}\n", encoding="utf-8"
            )
            badges = root / "badges"
            badges.mkdir()
            badge = badges / f"{ARXIV_ID}.json"
            if previous is not None:
                badge.write_text(json.dumps({
                    "schemaVersion": 1, "label": "Citations",
                    "message": str(previous), "color": updater.BADGE_COLOR,
                }) + "\n", encoding="utf-8")
            before = badge.read_bytes() if badge.exists() else None
            summary = root / "summary.md"
            summary.write_text("Earlier step\n", encoding="utf-8")

            def response(url, data=None, retries=2):
                if url.startswith("https://api.semanticscholar.org/"):
                    self.assertEqual(data, {"ids": [f"arXiv:{ARXIV_ID}"]})
                    return [None if s2_count is None else {
                        "title": S2_TITLE, "citationCount": s2_count,
                    }]
                if url.startswith("https://serpapi.com/"):
                    return {
                        "search_metadata": {"status": "Success"},
                        "articles": [] if gs_count is None else [{
                            "title": gs_title, "cited_by": {"value": gs_count},
                        }],
                    }
                self.fail("Unexpected provider request")

            environment = {
                "SERPAPI_KEY": "test-placeholder",
                "GOOGLE_SCHOLAR_ID": "test-author",
                "GITHUB_STEP_SUMMARY": str(summary),
            }
            with patch.object(updater, "PUB_MD", publication), \
                 patch.object(updater, "BIB_FILE", bib), \
                 patch.object(updater, "OUT_DIR", badges), \
                 patch.object(updater, "http_json", side_effect=response), \
                 patch.dict(updater.os.environ, environment, clear=True), \
                 redirect_stdout(io.StringIO()) as log:
                updater.main()

            after = badge.read_bytes() if badge.exists() else None
            value = json.loads(after)["message"] if after else None
            return value, before == after, log.getvalue(), summary.read_text(encoding="utf-8")

    def test_missing_semantic_scholar_does_not_replace_six_with_google_two(self):
        value, unchanged, log, summary = self.run_update(None, 2, 6)
        self.assertEqual(value, "6")
        self.assertTrue(unchanged)
        self.assertIn("gs=2, s2=None, previous=6", log)
        self.assertIn("partial-source decrease blocked", log)
        self.assertIn("Earlier step", summary)
        self.assertIn(f"| {ARXIV_ID} | 2 | None | 6 | 6 |", summary)

    def test_missing_google_does_not_lower_the_previous_count(self):
        value, unchanged, _, _ = self.run_update(2, None, 6)
        self.assertEqual(value, "6")
        self.assertTrue(unchanged)

    def test_complete_sources_can_confirm_a_lower_count(self):
        value, unchanged, log, _ = self.run_update(2, 1, 6)
        self.assertEqual(value, "2")
        self.assertFalse(unchanged)
        self.assertNotIn("decrease blocked", log)

    def test_current_source_max_can_increase_a_badge(self):
        value, _, log, _ = self.run_update(6, 2, 2)
        self.assertEqual(value, "6")
        self.assertIn("gs=2, s2=6, previous=2", log)

    def test_complete_real_zero_counts_can_reset_a_badge(self):
        value, _, _, _ = self.run_update(0, 0, 6)
        self.assertEqual(value, "0")

    def test_single_source_can_increase_a_count(self):
        value, _, _, _ = self.run_update(9, None, 6)
        self.assertEqual(value, "9")

    def test_first_valid_zero_count_creates_a_badge(self):
        value, _, _, _ = self.run_update(None, 0, None)
        self.assertEqual(value, "0")

    def test_missing_counts_leave_existing_badge_untouched(self):
        value, unchanged, _, _ = self.run_update(None, None, 6)
        self.assertEqual(value, "6")
        self.assertTrue(unchanged)

    def test_missing_counts_do_not_create_an_invented_zero(self):
        value, unchanged, _, _ = self.run_update(None, None, None)
        self.assertIsNone(value)
        self.assertTrue(unchanged)

    def test_invalid_counts_cannot_approve_a_partial_source_decrease(self):
        for invalid in [True, False, -1, 1.5, "unknown"]:
            with self.subTest(source="Semantic Scholar", invalid=invalid):
                value, unchanged, _, _ = self.run_update(invalid, 2, 6)
                self.assertEqual(value, "6")
                self.assertTrue(unchanged)
            with self.subTest(source="Google Scholar", invalid=invalid):
                value, unchanged, _, _ = self.run_update(2, invalid, 6)
                self.assertEqual(value, "6")
                self.assertTrue(unchanged)

    def test_bibtex_title_matches_when_semantic_scholar_uses_llms_abbreviation(self):
        value, _, log, _ = self.run_update(6, 8, 2, gs_title=BIB_TITLE)
        self.assertEqual(value, "8")
        self.assertIn("gs=8, s2=6, previous=2", log)


if __name__ == "__main__":
    unittest.main()
