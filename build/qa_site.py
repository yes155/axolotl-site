"""
Pre-publish QA for the generated MyAxolotl static site.

Fatal checks:
- duplicate or missing page titles
- duplicate or missing canonicals
- canonical URL does not match generated route
- missing H1 / multiple H1s
- broken internal page links
- missing local image/CSS/JS/icon assets
- article page missing a hero image
- article hero uses an auto-generated placeholder
- interactive tool page missing the shared theme scope
- sitemap duplicate URLs or omission of an indexable generated page

Warnings:
- duplicate meta descriptions
- title/meta description lengths outside practical search-snippet ranges
- article pages with no internal inlinks
- images without alt text

Writes public/qa-report.json and exits non-zero when errors exist.
"""

from __future__ import annotations

import json
import os
import re
import sys
import html as html_lib
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
SITE_URL = "https://myaxolotl.us"
SITE_HOST = urlparse(SITE_URL).netloc


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts = []
        self.in_title = False
        self.h1_count = 0
        self.h1_parts = []
        self.in_h1 = False
        self.canonicals = []
        self.meta_descriptions = []
        self.links = []
        self.local_assets = []
        self.images = []
        self.article_page = False
        self.article_hero = False
        self.tool_page = False
        self.noindex = False

    @staticmethod
    def attrs_dict(attrs):
        return {k.lower(): (v or "") for k, v in attrs}

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        a = self.attrs_dict(attrs)
        classes = set(a.get("class", "").split())

        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
            self.in_h1 = True
        elif tag == "link":
            rel = set(a.get("rel", "").lower().split())
            href = a.get("href", "")
            if "canonical" in rel:
                self.canonicals.append(href)
            if href and (
                "stylesheet" in rel
                or "icon" in rel
                or href.startswith("/css/")
                or href.startswith("/js/")
                or href.startswith("/images/")
            ):
                self.local_assets.append(href)
        elif tag == "meta":
            name = a.get("name", "").lower()
            if name == "description":
                self.meta_descriptions.append(a.get("content", "").strip())
            if name == "robots" and "noindex" in a.get("content", "").lower():
                self.noindex = True
        elif tag == "a":
            href = a.get("href", "")
            if href:
                self.links.append(href)
        elif tag == "img":
            src = a.get("src", "")
            alt = a.get("alt", "")
            if src:
                self.local_assets.append(src)
            self.images.append({"src": src, "alt": alt, "classes": sorted(classes)})
            if "hero-img" in classes:
                self.article_hero = True
        elif tag == "script":
            src = a.get("src", "")
            if src:
                self.local_assets.append(src)

        if "article-page" in classes:
            self.article_page = True
        if "article-hero" in classes:
            self.article_hero = True
        if tag == "body" and "tool-page" in classes:
            self.tool_page = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)
        if self.in_h1:
            self.h1_parts.append(data)

    @property
    def title(self):
        return " ".join("".join(self.title_parts).split()).strip()

    @property
    def h1(self):
        return " ".join("".join(self.h1_parts).split()).strip()


def route_for_file(path: Path) -> str | None:
    rel = path.relative_to(PUBLIC).as_posix()
    if rel == "index.html":
        return "/"
    if rel == "404.html":
        return None
    if rel.endswith("/index.html"):
        return "/" + rel[:-10]
    # Standalone verification or utility HTML is not an indexable generated page.
    return None


def expected_canonical(route: str) -> str:
    if route == "/":
        return SITE_URL + "/"
    return SITE_URL + route.lstrip("/") if route.startswith("//") else SITE_URL + route


def normalize_local_target(raw: str, current_route: str) -> tuple[str, str] | None:
    raw = html_lib.unescape(raw.strip())
    if not raw or raw.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    if raw.startswith("//"):
        return None

    parsed = urlparse(raw)
    if parsed.scheme in ("http", "https"):
        if parsed.netloc.lower() != SITE_HOST:
            return None
        path = parsed.path or "/"
    elif parsed.scheme:
        return None
    else:
        # Resolve relative links against the public route, not filesystem paths.
        base = SITE_URL + current_route
        resolved = urlparse(urljoin(base, raw))
        if resolved.netloc.lower() != SITE_HOST:
            return None
        path = resolved.path or "/"

    path = re.sub(r"/+", "/", path)
    return path, raw


def target_exists(path: str) -> bool:
    decoded = path
    if decoded == "/":
        return (PUBLIC / "index.html").is_file()

    rel = decoded.lstrip("/")
    candidate = PUBLIC / rel
    if path.endswith("/"):
        return (candidate / "index.html").is_file()
    if candidate.is_file():
        return True
    if (candidate / "index.html").is_file():
        return True
    return False


def asset_exists(raw: str, current_route: str) -> bool:
    raw = html_lib.unescape(raw.strip())
    if not raw or raw.startswith(("data:", "http://", "https://", "//")):
        if raw.startswith((SITE_URL + "/",)):
            parsed = urlparse(raw)
            raw = parsed.path
        else:
            return True

    parsed = urlparse(raw)
    path = parsed.path
    if not path:
        return True
    if path.startswith("/"):
        candidate = PUBLIC / path.lstrip("/")
    else:
        route_dir = current_route if current_route.endswith("/") else current_route + "/"
        resolved = urlparse(urljoin(SITE_URL + route_dir, path)).path
        candidate = PUBLIC / resolved.lstrip("/")
    return candidate.is_file()


def main():
    errors = []
    warnings = []
    pages = {}
    title_map = defaultdict(list)
    canonical_map = defaultdict(list)
    meta_map = defaultdict(list)
    inlinks = Counter()

    html_files = sorted(PUBLIC.rglob("*.html"))
    indexable_files = []

    for path in html_files:
        route = route_for_file(path)
        if route is None:
            continue

        raw = path.read_text(encoding="utf-8", errors="replace")
        parser = PageParser()
        parser.feed(raw)

        if parser.noindex:
            continue

        indexable_files.append(path)
        pages[route] = {
            "path": path.relative_to(PUBLIC).as_posix(),
            "title": parser.title,
            "h1": parser.h1,
            "canonical": parser.canonicals[0] if len(parser.canonicals) == 1 else "",
            "meta": parser.meta_descriptions[0] if len(parser.meta_descriptions) == 1 else "",
            "article": parser.article_page,
        }

        if not parser.title:
            errors.append(f"{route}: missing <title>")
        else:
            title_map[parser.title.casefold()].append(route)
            if len(parser.title) < 25 or len(parser.title) > 70:
                warnings.append(f"{route}: title length {len(parser.title)}")

        if len(parser.canonicals) != 1:
            errors.append(f"{route}: expected 1 canonical, found {len(parser.canonicals)}")
        else:
            canonical = parser.canonicals[0].rstrip("/") + "/"
            exp = expected_canonical(route).rstrip("/") + "/"
            canonical_map[canonical.casefold()].append(route)
            if canonical != exp:
                errors.append(f"{route}: canonical mismatch: {canonical} != {exp}")

        if len(parser.meta_descriptions) != 1 or not parser.meta_descriptions[0]:
            errors.append(f"{route}: expected one non-empty meta description")
        else:
            meta = parser.meta_descriptions[0]
            meta_map[meta.casefold()].append(route)
            if len(meta) < 70 or len(meta) > 180:
                warnings.append(f"{route}: meta description length {len(meta)}")

        if parser.h1_count != 1:
            errors.append(f"{route}: expected exactly 1 H1, found {parser.h1_count}")

        if parser.article_page:
            if not parser.article_hero:
                errors.append(f"{route}: article has no hero image")
            for img in parser.images:
                if "hero-img" in img["classes"] and "placeholder" in img["src"].lower():
                    errors.append(f"{route}: article hero is a generated placeholder: {img['src']}")

        if route.startswith("/tools/") and route != "/tools/" and not parser.tool_page:
            errors.append(f"{route}: interactive tool is missing the tool-page theme scope")

        for img in parser.images:
            if not img["alt"].strip():
                warnings.append(f"{route}: image missing alt text: {img['src']}")

        for asset in parser.local_assets:
            if not asset_exists(asset, route):
                errors.append(f"{route}: missing local asset {asset}")

        for href in parser.links:
            normalized = normalize_local_target(href, route)
            if normalized is None:
                continue
            target, original = normalized
            # Local assets linked with <a> are checked as files, not pages.
            if re.search(r"\.(?:webp|png|jpe?g|gif|svg|pdf|xml|txt|css|js|zip)$", target, re.I):
                if not target_exists(target):
                    errors.append(f"{route}: broken local file link {original}")
                continue
            if not target_exists(target):
                errors.append(f"{route}: broken internal link {original} -> {target}")
            else:
                normalized_route = target
                if normalized_route != "/" and not normalized_route.endswith("/"):
                    # Normalize extensionless directory links to trailing slash for inlink counting.
                    candidate = PUBLIC / normalized_route.lstrip("/")
                    if (candidate / "index.html").is_file():
                        normalized_route += "/"
                inlinks[normalized_route] += 1

    for title, routes in title_map.items():
        if len(routes) > 1:
            errors.append("duplicate title: " + " | ".join(routes))

    for canonical, routes in canonical_map.items():
        if len(routes) > 1:
            errors.append("duplicate canonical: " + " | ".join(routes))

    for meta, routes in meta_map.items():
        if len(routes) > 1:
            warnings.append("duplicate meta description: " + " | ".join(routes))

    # Sitemap validation.
    sitemap_path = PUBLIC / "sitemap.xml"
    sitemap_urls = []
    if not sitemap_path.is_file():
        errors.append("missing public/sitemap.xml")
    else:
        try:
            root = ET.parse(sitemap_path).getroot()
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            sitemap_urls = [
                (loc.text or "").strip()
                for loc in root.findall("sm:url/sm:loc", ns)
                if (loc.text or "").strip()
            ]
        except Exception as exc:
            errors.append(f"sitemap parse error: {exc}")

    def norm_site_url(url: str) -> str:
        parsed = urlparse(url.strip())
        path = parsed.path or "/"
        if path != "/":
            path = path.rstrip("/") + "/"
        return f"{parsed.scheme.lower()}://{parsed.netloc.lower()}{path}"

    normalized_sitemap = [norm_site_url(url) for url in sitemap_urls]
    sitemap_counts = Counter(normalized_sitemap)
    for url, count in sitemap_counts.items():
        if count > 1:
            errors.append(f"duplicate sitemap URL: {url}")

    sitemap_set = set(normalized_sitemap)
    for route, info in pages.items():
        canonical = info["canonical"]
        if canonical and norm_site_url(canonical) not in sitemap_set:
            errors.append(f"{route}: canonical missing from sitemap: {canonical}")

    # Orphan check is a warning: some trust/profile pages may intentionally have few links.
    for route, info in pages.items():
        if info["article"] and inlinks[route] == 0:
            warnings.append(f"{route}: article has zero internal inlinks")

    report = {
        "status": "PASS" if not errors else "FAIL",
        "html_pages_checked": len(indexable_files),
        "article_pages_checked": sum(1 for x in pages.values() if x["article"]),
        "sitemap_urls": len(sitemap_urls),
        "errors": errors,
        "warnings": warnings,
    }
    (PUBLIC / "qa-report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(
        f"QA {report['status']}: {report['html_pages_checked']} indexable HTML pages, "
        f"{report['article_pages_checked']} article pages, "
        f"{len(errors)} errors, {len(warnings)} warnings."
    )
    for item in errors:
        print("ERROR:", item)
    for item in warnings[:100]:
        print("WARN:", item)
    if len(warnings) > 100:
        print(f"WARN: ... {len(warnings) - 100} additional warnings in public/qa-report.json")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
