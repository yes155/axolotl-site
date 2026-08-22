# -*- coding: utf-8 -*-
"""Phase 8 helper: extract clean article-body plain text per content page from
public/ so candidate links can be verified against actual prose before any
phrase-based inline link is added. Writes docs/phase8/article-text.json."""
import os, re, json, html as _html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(BASE, "public")
OUT = os.path.join(BASE, "docs", "phase8")
os.makedirs(OUT, exist_ok=True)

pages = json.load(open(os.path.join(BASE, "docs", "phase7", "pages.json"), encoding="utf-8"))
META = {"/", "/404.html", "/about", "/contact", "/privacy", "/search"}


def path_for(url):
    if url in ("/", "/404.html"):
        return os.path.join(PUB, "index.html" if url == "/" else "404.html")
    return os.path.join(PUB, url.strip("/"), "index.html")


def body_text(url):
    p = path_for(url)
    if not os.path.exists(p):
        return ""
    with open(p, encoding="utf-8", errors="ignore") as fh:
        h = fh.read()
    m = re.search(r"(?is)<body.*?>(.*?)</body>", h)
    h = m.group(1) if m else h
    h = re.sub(r"(?is)<(script|style|noscript|template|svg).*?</\1>", " ", h)
    h = re.sub(r"(?is)<footer.*?</footer>", " ", h)
    h = re.sub(r"(?is)<aside.*?</aside>", " ", h)
    h = re.sub(r"(?is)<nav.*?</nav>", " ", h)
    h = re.sub(r"(?is)<section class=\"related\".*?</section>", " ", h)
    h = re.sub(r"(?is)<ul class=\"footer.*?</ul>", " ", h)
    t = re.sub(r"<[^>]+>", " ", h)
    t = _html.unescape(t).replace("\xa0", " ")
    return re.sub(r"\s+", " ", t)


out = {}
for u in sorted(pages):
    if u in META:
        continue
    txt = body_text(u)
    out[u] = {"text": txt, "lower": txt.lower()}

with open(os.path.join(OUT, "article-text.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=0)
print("wrote", len(out), "articles")