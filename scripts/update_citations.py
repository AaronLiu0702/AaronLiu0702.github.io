#!/usr/bin/env python3
"""
Update per-paper citation badge data for the homepage.

Papers are discovered automatically from the citation badges in
_pages/includes/pub.md, so adding a new badge there is all you need to do.

Data sources: both are queried on every run and the HIGHER count wins
(the two databases index different venues, so the max is the most
complete number):
  1. Google Scholar via SerpAPI  - real Google Scholar numbers.
       Needs repo secret SERPAPI_KEY (GOOGLE_SCHOLAR_ID optional,
       otherwise parsed from _config.yml). Free tier = 100 searches/month;
       this script uses ONE search per run, so daily updates fit easily.
  2. Semantic Scholar Graph API  - free, no key, reliable from CI.
If one source misses a paper, the other one can increase its badge but
cannot lower a previous count. Decreases require valid counts from both
sources. If both fail, the previous value is kept so badges never break.

For every paper a shields.io "endpoint" JSON is written to
badges/citations/<arxiv_id>.json. If a lookup fails, the previous value
(or, on first run, the hardcoded number from pub.md) is kept, so the
badges on the site never break.
"""

import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PUB_MD = REPO_ROOT / "_pages" / "includes" / "pub.md"
BIB_FILE = REPO_ROOT / "files" / "papers.bib"
CONFIG_YML = REPO_ROOT / "_config.yml"
OUT_DIR = REPO_ROOT / "badges" / "citations"
BADGE_COLOR = "EBB215"

# [![Citations](<any badge url>)](https://arxiv.org/abs/2510.26768)
BADGE_RE = re.compile(
    r"\[!\[Citations\]\([^)]*\)\]\(https://arxiv\.org/abs/(\d+\.\d+)(?:v\d+)?\)"
)
# hardcoded static badge, used only as a first-run seed value
SEED_RE = re.compile(
    r"badge/Citations-(\d+)-\w{6}\)\]\(https://arxiv\.org/abs/(\d+\.\d+)"
)


def http_json(url, data=None, retries=2):
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "homepage-citation-updater/1.0",
        },
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            retryable = isinstance(e, urllib.error.HTTPError) and e.code in (429, 500, 502, 503)
            if attempt < retries and (retryable or not isinstance(e, urllib.error.HTTPError)):
                time.sleep(8 * (attempt + 1))
                continue
            print(f"[warn] request failed: {url.split('?')[0]}: {e}")
            return None


def fetch_semantic_scholar(arxiv_ids, diagnostics=None):
    """One batch request for all papers -> {arxiv_id: {'title':..., 'citations':...}}"""
    url = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,citationCount"
    diagnostics = {} if diagnostics is None else diagnostics
    diagnostics["s2"] = "request failed or invalid batch response"
    data = http_json(url, data={"ids": [f"arXiv:{a}" for a in arxiv_ids]})
    if not isinstance(data, list):
        return {}
    out = {}
    for aid, item in zip(arxiv_ids, data):
        if isinstance(item, dict):
            out[aid] = {
                "title": item.get("title") or "",
                "citations": citation_count(item.get("citationCount")),
            }
    valid = sum(item["citations"] is not None for item in out.values())
    diagnostics["s2"] = f"batch returned {len(data)}/{len(arxiv_ids)} entries; {valid} valid counts"
    return out


def citation_count(value):
    """Accept non-negative integers, including the badge JSON's numeric strings."""
    if isinstance(value, int) and not isinstance(value, bool):
        return value if value >= 0 else None
    if isinstance(value, str) and re.fullmatch(r"[0-9]+", value.strip()):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip() if isinstance(t, str) else ""


def bib_titles_by_arxiv():
    """Keep Scholar title matching available before Semantic Scholar indexes a paper."""
    if not BIB_FILE.exists():
        return {}
    titles = {}
    entries = re.split(r"(?m)^\s*@\w+\s*\{", BIB_FILE.read_text(encoding="utf-8"))[1:]
    for entry in entries:
        title = re.search(r"\btitle\s*=\s*\{(.+?)\}\s*,", entry, re.I | re.S)
        aid = re.search(
            r"(?:\beprint\s*=\s*\{\s*|arxiv(?:\.org/abs/|:\s*))(\d+\.\d+)",
            entry,
            re.I,
        )
        if title and aid:
            titles[aid.group(1)] = re.sub(r"\s+", " ", title.group(1)).strip()
    return titles


def scholar_author_id():
    if os.environ.get("GOOGLE_SCHOLAR_ID"):
        return os.environ["GOOGLE_SCHOLAR_ID"]
    if CONFIG_YML.exists():
        m = re.search(r"googlescholar.*[?&]user=([\w-]+)", CONFIG_YML.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return None


def fetch_google_scholar_serpapi(author_id, api_key, diagnostics=None):
    """Author profile -> {normalized_title: citations}. One API call per run."""
    url = (
        "https://serpapi.com/search.json?engine=google_scholar_author"
        f"&author_id={author_id}&api_key={api_key}&num=100&hl=en&sort=pubdate"
    )
    diagnostics = {} if diagnostics is None else diagnostics
    diagnostics["gs"] = "request failed or invalid response"
    data = http_json(url)
    if not isinstance(data, dict):
        return {}
    metadata = data.get("search_metadata")
    if data.get("error") or (isinstance(metadata, dict) and metadata.get("status") == "Error"):
        diagnostics["gs"] = "provider reported an error"
        return {}
    if not isinstance(data.get("articles"), list):
        diagnostics["gs"] = "response has no article list"
        return {}
    out = {}
    for art in data["articles"]:
        if not isinstance(art, dict):
            continue
        cited = art.get("cited_by")
        value = citation_count(cited.get("value")) if isinstance(cited, dict) else None
        title = norm_title(art.get("title"))
        if title and value is not None:
            out[title] = max(out.get(title, value), value)
    diagnostics["gs"] = (
        f"profile returned {len(data['articles'])} articles; {len(out)} usable titles"
        if data["articles"] else "empty profile result"
    )
    return out


def match_gs_citations(gs_map, title):
    """Exact normalized-title match, then containment fallback
    (handles 'ACE-MAPPO: <title>' on arXiv vs '<title>' on Scholar)."""
    nt = norm_title(title)
    if not nt:
        return None
    if nt in gs_map:
        return gs_map[nt]
    best = None
    for gs_t, v in gs_map.items():
        shorter, longer = (nt, gs_t) if len(nt) <= len(gs_t) else (gs_t, nt)
        if len(shorter) >= 20 and shorter in longer:
            if best is None or len(gs_t) > len(best[0]):
                best = (gs_t, v)
    return best[1] if best else None


def read_previous(arxiv_id):
    path = OUT_DIR / f"{arxiv_id}.json"
    if path.exists():
        try:
            return citation_count(json.loads(path.read_text(encoding="utf-8"))["message"])
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            return None
    return None


def main():
    text = PUB_MD.read_text(encoding="utf-8")
    arxiv_ids = list(dict.fromkeys(BADGE_RE.findall(text)))
    seeds = {aid: int(n) for n, aid in SEED_RE.findall(text)}
    if not arxiv_ids:
        print("No citation badges found in pub.md")
        return
    print(f"Found {len(arxiv_ids)} citation badge(s): {', '.join(arxiv_ids)}")

    titles = bib_titles_by_arxiv()
    diagnostics = {}
    s2 = fetch_semantic_scholar(arxiv_ids, diagnostics)
    print(f"Semantic Scholar lookup: {diagnostics['s2']}")

    gs = {}
    api_key, author_id = os.environ.get("SERPAPI_KEY"), scholar_author_id()
    if api_key and author_id:
        gs = fetch_google_scholar_serpapi(author_id, api_key, diagnostics)
        print(f"Google Scholar (SerpAPI): {len(gs)} article(s) on profile {author_id}")
    else:
        missing = "SERPAPI_KEY" if not api_key else "Google Scholar author ID"
        diagnostics["gs"] = f"not configured ({missing} missing)"
    print(f"Google Scholar lookup: {diagnostics['gs']}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    updated = 0
    summary = [
        "### Citation badge update",
        "",
        f"- Google Scholar: {diagnostics['gs']}",
        f"- Semantic Scholar: {diagnostics['s2']}",
        "- `None` means no valid matched count; it does not mean zero.",
        "",
        "| arXiv | Google Scholar | Semantic Scholar | Previous | Selected | Decision |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for aid in arxiv_ids:
        info = s2.get(aid, {})
        previous = read_previous(aid)
        value, source = None, "no data; badge left untouched"
        gs_matches = [
            citation_count(match_gs_citations(gs, title))
            for title in (info.get("title"), titles.get(aid))
        ]
        gs_val = max((count for count in gs_matches if count is not None), default=None)
        s2_val = citation_count(info.get("citations"))
        candidates = [v for v in (gs_val, s2_val) if v is not None]
        if candidates:
            value = max(candidates)
            source = "max of current sources"
            if len(candidates) < 2:
                source = "single available source"
                if previous is not None and value < previous:
                    value = previous
                    source = "partial-source decrease blocked"
        else:
            if previous is not None:
                value, source = previous, "previous; no current source count"
            elif aid in seeds:
                value, source = seeds[aid], "pub.md-seed"
        summary.append(
            f"| {aid} | {gs_val} | {s2_val} | {previous} | {value} | {source} |"
        )
        print(f"  {aid}: {value} (gs={gs_val}, s2={s2_val}, previous={previous}; {source})")
        if value is None:
            continue

        path = OUT_DIR / f"{aid}.json"
        payload = {"schemaVersion": 1, "label": "Citations", "message": str(value), "color": BADGE_COLOR}
        if previous != value:
            path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            updated += 1
    print(f"Done. {updated} badge file(s) changed.")
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        try:
            with Path(summary_path).open("a", encoding="utf-8") as stream:
                stream.write("\n".join(summary) + "\n")
        except OSError as error:
            print(f"[warn] could not write Actions step summary: {error}")


if __name__ == "__main__":
    main()
