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
If one source misses a paper, the other one is used; if both fail,
the previous value is kept so badges never break.

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


def fetch_semantic_scholar(arxiv_ids):
    """One batch request for all papers -> {arxiv_id: {'title':..., 'citations':...}}"""
    url = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,citationCount"
    data = http_json(url, data={"ids": [f"arXiv:{a}" for a in arxiv_ids]})
    if not isinstance(data, list):
        return {}
    out = {}
    for aid, item in zip(arxiv_ids, data):
        if item:
            out[aid] = {"title": item.get("title") or "", "citations": item.get("citationCount")}
    return out


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def scholar_author_id():
    if os.environ.get("GOOGLE_SCHOLAR_ID"):
        return os.environ["GOOGLE_SCHOLAR_ID"]
    if CONFIG_YML.exists():
        m = re.search(r"googlescholar.*[?&]user=([\w-]+)", CONFIG_YML.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return None


def fetch_google_scholar_serpapi(author_id, api_key):
    """Author profile -> {normalized_title: citations}. One API call per run."""
    url = (
        "https://serpapi.com/search.json?engine=google_scholar_author"
        f"&author_id={author_id}&api_key={api_key}&num=100&hl=en&sort=pubdate"
    )
    data = http_json(url)
    if not isinstance(data, dict):
        return {}
    out = {}
    for art in data.get("articles", []):
        cited = art.get("cited_by")
        value = cited.get("value") if isinstance(cited, dict) else 0
        out[norm_title(art.get("title"))] = value or 0
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
            return int(json.loads(path.read_text(encoding="utf-8"))["message"])
        except (ValueError, KeyError, json.JSONDecodeError):
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

    s2 = fetch_semantic_scholar(arxiv_ids)

    gs = {}
    api_key, author_id = os.environ.get("SERPAPI_KEY"), scholar_author_id()
    if api_key and author_id:
        gs = fetch_google_scholar_serpapi(author_id, api_key)
        print(f"Google Scholar (SerpAPI): {len(gs)} article(s) on profile {author_id}")
    else:
        print("SERPAPI_KEY not set, using Semantic Scholar numbers only")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    updated = 0
    for aid in arxiv_ids:
        info = s2.get(aid, {})
        value, source = None, ""
        gs_val = match_gs_citations(gs, info.get("title", ""))
        s2_val = info.get("citations")
        candidates = [v for v in (gs_val, s2_val) if v is not None]
        if candidates:
            value = max(candidates)
            source = f"max(gs={gs_val}, s2={s2_val})"
        else:
            prev = read_previous(aid)
            if prev is not None:
                value, source = prev, "previous"
            elif aid in seeds:
                value, source = seeds[aid], "pub.md-seed"
        if value is None:
            print(f"  [warn] {aid}: no data from any source, badge left untouched")
            continue

        path = OUT_DIR / f"{aid}.json"
        payload = {"schemaVersion": 1, "label": "Citations", "message": str(value), "color": BADGE_COLOR}
        if read_previous(aid) != value:
            path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            updated += 1
        print(f"  {aid}: {value} ({source})")
    print(f"Done. {updated} badge file(s) changed.")


if __name__ == "__main__":
    main()
