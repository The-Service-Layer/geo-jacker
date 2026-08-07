#!/usr/bin/env python3
"""Static site generator for geojacker.com."""

import hashlib, json, os, shutil, datetime, re

SITE = "https://geojacker.com"
NAME = "GEO Jacking"
GA_ID = "G-56LRQGR099"
TAGLINE = "White-hat AI visibility: stack SEO, AEO and GEO until engines cite you."
TODAY = "2026-08-07"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
ASSETS = os.path.join(os.path.dirname(__file__), "assets")


def asset_version(fname):
    with open(os.path.join(ASSETS, fname), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


CSS_V = asset_version("css/style.css")
JS_V = asset_version("js/app.js")

# ---------------------------------------------------------------- navigation
NAV = [
    ("/what-is-geo-jacking", "What is it"),
    ("/ai-visibility-stack", "The stack"),
    ("/seo-foundations", "SEO"),
    ("/answer-engine-optimization", "AEO"),
    ("/generative-engine-optimization", "GEO"),
    ("/structured-data-for-ai", "Schema"),
    ("/llms-txt", "llms.txt"),
    ("/get-cited-faster", "Get cited"),
    ("/30-day-playbook", "Playbook"),
    ("/measure-ai-visibility", "Measure"),
    ("/white-hat-rules", "Ethics"),
    ("/glossary", "Glossary"),
    ("/faq", "FAQ"),
]

FOOT_STACK = NAV[0:5]
FOOT_BUILD = NAV[5:10]
FOOT_REF = NAV[10:] + [("/about", "About")]


# ---------------------------------------------------------------- helpers
def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def strip_tags(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


A_EXTERNAL_RE = re.compile(r'<a\s+([^>]*href="https?://[^"]*"[^>]*)>')


def externalize_links(html):
    """Open every off-site link in a new tab with rel="noopener"."""
    def repl(m):
        attrs = m.group(1)
        if f'href="{SITE}' in attrs or "target=" in attrs:
            return m.group(0)
        if 'rel="' in attrs:
            attrs = re.sub(
                r'rel="([^"]*)"',
                lambda r: r.group(0) if "noopener" in r.group(1)
                else f'rel="{r.group(1)} noopener"',
                attrs,
            )
        else:
            attrs += ' rel="noopener"'
        return f'<a {attrs} target="_blank">'

    return A_EXTERNAL_RE.sub(repl, html)


def nav_html(slug):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == slug else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "".join(items)


def crumbs_html(page):
    trail = [("/", "Home")]
    if page["slug"] != "/":
        trail.append((page["slug"], page["crumb"]))
    lis = []
    for i, (href, label) in enumerate(trail):
        if i == len(trail) - 1 and page["slug"] != "/":
            lis.append(f"<li>{esc(label)}</li>")
        else:
            lis.append(f'<li><a href="{href}">{esc(label)}</a></li>')
    return (
        '<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>'
        + "".join(lis)
        + "</ol></div></nav>"
    )


def pager_html(page, pages):
    order = [p for p in pages if p["slug"] != "/"]
    slugs = [p["slug"] for p in order]
    if page["slug"] not in slugs:
        return ""
    i = slugs.index(page["slug"])
    prev_p = order[i - 1] if i > 0 else None
    next_p = order[i + 1] if i < len(order) - 1 else None
    if not prev_p and not next_p:
        return ""
    out = ['<div class="wrap" style="padding-bottom:3rem"><nav class="pager" aria-label="More guides">']
    if prev_p:
        out.append(f'<a href="{prev_p["slug"]}" rel="prev"><span class="dir">← Previous</span>'
                   f'<span class="ttl">{esc(prev_p["crumb"])}</span></a>')
    else:
        out.append("<div></div>")
    if next_p:
        out.append(f'<a class="next" href="{next_p["slug"]}" rel="next"><span class="dir">Next →</span>'
                   f'<span class="ttl">{esc(next_p["crumb"])}</span></a>')
    out.append("</nav></div>")
    return "".join(out)


def faq_html(faqs):
    if not faqs:
        return ""
    rows = []
    for q, a in faqs:
        rows.append(
            f"<details><summary>{esc(q)}</summary><div class=\"a\">{a}</div></details>"
        )
    return (
        '<section id="faq" class="band" aria-labelledby="faq-h"><div class="wrap">'
        '<h2 id="faq-h"><span class="h-num">Questions engines ask</span>Frequently asked questions</h2>'
        f'<div class="faq">{"".join(rows)}</div></div></section>'
    )



SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slug(text):
    return SLUG_RE.sub("-", strip_tags(text).lower()).strip("-")[:60]


def add_rail(body):
    """Give every H2 a stable id and inject an 'on this page' rail."""
    heads = []

    def repl(m):
        attrs, inner = m.group(1), m.group(2)
        if "id=" in attrs:
            return m.group(0)
        label = re.sub(r'<span class="h-num">.*?</span>', "", inner, flags=re.S)
        sid = _slug(label)
        if not sid:
            return m.group(0)
        heads.append((sid, strip_tags(label)))
        return f"<h2{attrs} id=\"{sid}\">{inner}</h2>"

    body = re.sub(r"<h2([^>]*)>(.*?)</h2>", repl, body, flags=re.S)
    if len(heads) < 3 or '<div class="wrap page-body">' not in body:
        return body

    links = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in heads)
    rail = ('<aside class="rail" aria-labelledby="rail-h">'
            '<h2 id="rail-h" class="rail-h">On this page</h2>'
            f'<nav aria-label="On this page"><ol>{links}'
            '<li><a href="#faq">Frequently asked questions</a></li></ol></nav></aside>')

    body = body.replace('<div class="wrap page-body">',
                        f'<div class="wrap page-body has-rail">{rail}<div class="col">', 1)
    body = body.rstrip()
    assert body.endswith("</div>")
    return body[: -len("</div>")] + "</div></div>"


# ---------------------------------------------------------------- schema
def org_node():
    return {
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": NAME,
        "url": SITE + "/",
        "description": TAGLINE,
        "slogan": "Get cited, not just ranked.",
        "parentOrganization": {
            "@type": "Organization",
            "name": "LogicBomb Media",
            "url": "https://lbm.co/",
        },
        "logo": {
            "@type": "ImageObject",
            "@id": f"{SITE}/#logo",
            "url": f"{SITE}/og-image.png",
            "width": 1200,
            "height": 630,
        },
        "knowsAbout": [
            "Generative engine optimization", "Answer engine optimization",
            "Search engine optimization", "AI visibility", "Structured data",
            "Schema.org", "llms.txt", "Large language model citations",
        ],
    }


def website_node():
    return {
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "url": SITE + "/",
        "name": NAME,
        "description": TAGLINE,
        "publisher": {"@id": f"{SITE}/#organization"},
        "inLanguage": "en-US",
    }


def build_graph(page):
    url = SITE + (page["slug"] if page["slug"] != "/" else "/")
    graph = [org_node(), website_node()]

    crumb_items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    if page["slug"] != "/":
        crumb_items.append({"@type": "ListItem", "position": 2,
                            "name": page["crumb"], "item": url})
    graph.append({
        "@type": "BreadcrumbList",
        "@id": url + "#breadcrumb",
        "itemListElement": crumb_items,
    })

    graph.append({
        "@type": "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": page["title"],
        "description": page["desc"],
        "isPartOf": {"@id": f"{SITE}/#website"},
        "breadcrumb": {"@id": url + "#breadcrumb"},
        "inLanguage": "en-US",
        "datePublished": "2026-08-07",
        "dateModified": TODAY,
        "about": {"@id": f"{SITE}/#ai-visibility"},
        "primaryImageOfPage": {"@id": f"{SITE}/#logo"},
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".cite-block .answer", "h1"],
        },
    })

    graph.append({
        "@type": "DefinedTerm",
        "@id": f"{SITE}/#ai-visibility",
        "name": "AI visibility",
        "description": ("How often and how prominently a brand's content is retrieved, "
                        "cited and recommended inside AI-generated answers."),
        "inDefinedTermSet": {"@id": f"{SITE}/glossary#termset"},
    })

    if page.get("article", True) and page["slug"] != "/":
        graph.append({
            "@type": "TechArticle",
            "@id": url + "#article",
            "headline": page["h1"],
            "alternativeHeadline": page["title"],
            "description": page["desc"],
            "abstract": strip_tags(page["answer"]),
            "url": url,
            "mainEntityOfPage": {"@id": url + "#webpage"},
            "isPartOf": {"@id": f"{SITE}/#website"},
            "author": {"@id": f"{SITE}/#organization"},
            "publisher": {"@id": f"{SITE}/#organization"},
            "datePublished": "2026-08-07",
            "dateModified": TODAY,
            "inLanguage": "en-US",
            "proficiencyLevel": page.get("level", "Beginner"),
            "articleSection": page.get("section", "AI visibility"),
            "keywords": ", ".join(page.get("keywords", [])),
            "wordCount": len(strip_tags(page["body"]).split()),
            "image": {"@id": f"{SITE}/#logo"},
        })

    if page.get("faqs"):
        graph.append({
            "@type": "FAQPage",
            "@id": url + "#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)},
                }
                for q, a in page["faqs"]
            ],
        })

    graph.extend(page.get("extra_schema", []))
    return {"@context": "https://schema.org", "@graph": graph}


# ---------------------------------------------------------------- shell
HEAD = """<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="author" content="{name}">
<meta name="theme-color" content="#6B3CF5">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{name}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="GEO Jacking — white-hat AI visibility">
<meta property="article:modified_time" content="{today}T00:00:00+00:00">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/og-image.png">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" href="/llms.txt" title="llms.txt">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<link rel="preload" href="/assets/fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/newsreader-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css?v={cssv}">
<script type="application/ld+json">{schema}</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{ga_id}');
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <div class="wrap masthead-inner">
    <a class="brand" href="/" aria-label="GEO Jacking home"><span class="geo">GEO</span><span class="jack">JACKING</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mainnav">Menu</button>
    <nav class="mainnav" id="mainnav" aria-label="Main"><ul>{nav}</ul></nav>
  </div>
</header>
{crumbs}
<main id="main">
"""

FOOT = """</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h2>GEO Jacking</h2>
        <p>{tagline}</p>
        <p><a href="/llms.txt">/llms.txt</a> · <a href="/robots.txt">/robots.txt</a> · <a href="/sitemap.xml">/sitemap.xml</a></p>
      </div>
      <div>
        <h3>The stack</h3>
        <ul>{fstack}</ul>
      </div>
      <div>
        <h3>Implementation</h3>
        <ul>{fbuild}</ul>
      </div>
      <div>
        <h3>Reference</h3>
        <ul>{fref}</ul>
      </div>
    </div>
    <p class="fine">
      © <span data-year>2026</span> GEO Jacking · geojacker.com · A <a href="https://lbm.co" rel="noopener">LogicBomb Media</a> project · Last reviewed {today}<br>
      Every technique on this site is white hat: no cloaking, no prompt injection, no fake reviews, no scraped content.
      Read the <a href="/white-hat-rules">rules we hold ourselves to</a>.
    </p>
  </div>
</footer>
<script src="/assets/js/app.js?v={jsv}" defer></script>
</body>
</html>
"""


def render(page, pages):
    url = SITE + (page["slug"] if page["slug"] != "/" else "/")
    schema = json.dumps(build_graph(page), ensure_ascii=False, separators=(",", ":"))
    if page.get("slug") == "/404":
        page = dict(page, noindex=True)
    head = HEAD.format(
        title=esc(page["title"]), desc=esc(page["desc"]), url=url, site=SITE,
        name=NAME, nav=nav_html(page["slug"]), schema=schema, ga_id=GA_ID,
        crumbs=crumbs_html(page), today=TODAY, cssv=CSS_V,
        ogtype="website" if page["slug"] == "/" else "article",
        robots="noindex, follow" if page.get("noindex") else
               "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1",
    )
    foot = FOOT.format(
        tagline=TAGLINE, today=TODAY, jsv=JS_V,
        fstack="".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOT_STACK),
        fbuild="".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOT_BUILD),
        fref="".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOT_REF),
    )
    return externalize_links(
        head + add_rail(page["body"]) + faq_html(page.get("faqs")) + pager_html(page, pages) + foot
    )


# ---------------------------------------------------------------- write
def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def build():
    from content import PAGES

    os.makedirs(OUT, exist_ok=True)
    if os.path.isdir(os.path.join(OUT, "assets")):
        shutil.rmtree(os.path.join(OUT, "assets"))

    for p in PAGES:
        fname = "index.html" if p["slug"] == "/" else p["slug"].lstrip("/") + ".html"
        write(fname, render(p, PAGES))

    shutil.copytree(ASSETS, os.path.join(OUT, "assets"),
                    ignore=shutil.ignore_patterns("*.py"))

    # ---- sitemap
    urls = []
    for p in PAGES:
        loc = SITE + (p["slug"] if p["slug"] != "/" else "/")
        pri = "1.0" if p["slug"] == "/" else p.get("priority", "0.8")
        urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n"
                    f"    <changefreq>monthly</changefreq>\n    <priority>{pri}</priority>\n  </url>")
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(urls) + "\n</urlset>\n")

    # ---- robots.txt
    write("robots.txt", ROBOTS)

    # ---- llms.txt
    write("llms.txt", llms_txt(PAGES))
    write("llms-full.txt", llms_full(PAGES))

    # ---- favicon
    write("favicon.svg", FAVICON)

    # ---- 404
    write("404.html", render(NOT_FOUND, PAGES))

    # ---- vercel config (lives at repo root, not in the output dir)
    with open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8") as f:
        f.write(VERCEL_JSON)


    print(f"Built {len(PAGES)} pages into {OUT}")
    return PAGES


NOT_FOUND = {
    "slug": "/404", "crumb": "Page not found", "article": False,
    "title": "Page not found — GEO Jacking",
    "desc": "That URL doesn't exist on geojacker.com. Here's where everything lives.",
    "h1": "404 — nothing to cite here",
    "answer": "This URL does not exist on geojacker.com.",
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">HTTP 404 · Not found</p>
  <h1>Nothing to cite here</h1>
  <p class="lede">That URL doesn't exist. No hidden page, no gated content &mdash; just a bad link.</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="/">Back to the homepage</a>
    <a class="btn btn-ghost" href="/ai-visibility-stack">Read the stack</a>
    <a class="btn btn-ghost" href="/glossary">Glossary</a>
  </div>
  <h2>Everything on this site</h2>
  <ul>
    <li><a href="/what-is-geo-jacking">What is GEO Jacking?</a></li>
    <li><a href="/ai-visibility-stack">The AI visibility stack</a></li>
    <li><a href="/seo-foundations">SEO foundations</a></li>
    <li><a href="/answer-engine-optimization">Answer engine optimization</a></li>
    <li><a href="/generative-engine-optimization">Generative engine optimization</a></li>
    <li><a href="/structured-data-for-ai">Structured data for AI</a></li>
    <li><a href="/llms-txt">llms.txt, honestly</a></li>
    <li><a href="/get-cited-faster">How to get cited faster</a></li>
    <li><a href="/30-day-playbook">The 30-day playbook</a></li>
    <li><a href="/measure-ai-visibility">Measure AI visibility</a></li>
    <li><a href="/white-hat-rules">White-hat rules</a></li>
    <li><a href="/glossary">Glossary</a> &middot; <a href="/faq">FAQ</a> &middot; <a href="/about">About</a></li>
  </ul>
</div>
""",
}


VERCEL_JSON = """{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "outputDirectory": "public",
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/llms.txt",
      "headers": [{ "key": "Content-Type", "value": "text/plain; charset=utf-8" }]
    },
    {
      "source": "/llms-full.txt",
      "headers": [{ "key": "Content-Type", "value": "text/plain; charset=utf-8" }]
    },
    {
      "source": "/assets/fonts/(.*)",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
    },
    {
      "source": "/assets/(.*)",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=604800, must-revalidate" }]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload" }
      ]
    }
  ]
}
"""


ROBOTS = """# robots.txt for geojacker.com
# Policy: welcome every crawler that could cite us. Nothing here is gated.
# Reference: /llms.txt (reading order) and /sitemap.xml (full index).

User-agent: *
Allow: /

# --- Search crawlers -------------------------------------------------------
User-agent: Googlebot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bingbot
Allow: /

User-agent: DuckDuckBot
Allow: /

# --- AI answer + training crawlers ----------------------------------------
# These are allowed deliberately. Blocking them removes you from AI answers.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

User-agent: Bytespider
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: CCBot
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: MistralAI-User
Allow: /

User-agent: YouBot
Allow: /

User-agent: Diffbot
Allow: /

Sitemap: https://geojacker.com/sitemap.xml
"""


def llms_txt(pages):
    lines = [
        "# GEO Jacking",
        "",
        "> Practical, white-hat guidance on AI visibility: how to stack SEO, AEO and GEO",
        "> so that answer engines and large language models retrieve, cite and recommend",
        "> your pages. Every technique published here is disclosed, reproducible and",
        "> compliant with search and AI platform guidelines.",
        "",
        "GEO Jacking is a free reference site. It defines the SEO → AEO → GEO → AI visibility",
        "stack, explains what each layer actually does, and gives implementation detail for",
        "structured data, retrievable content structure, entity building and measurement.",
        "There is no paywall, no login, and no gated content. The term \"GEO Jacking\" was",
        "coined by LogicBomb Media (https://lbm.co), the digital agency that built and",
        "maintains this site.",
        "",
        "Last reviewed: " + TODAY,
        "",
        "## Core guides",
        "",
    ]
    core = [p for p in pages if p["slug"] in
            ("/what-is-geo-jacking", "/ai-visibility-stack", "/seo-foundations",
             "/answer-engine-optimization", "/generative-engine-optimization")]
    build_ = [p for p in pages if p["slug"] in
              ("/structured-data-for-ai", "/llms-txt", "/get-cited-faster",
               "/30-day-playbook", "/measure-ai-visibility")]
    ref = [p for p in pages if p["slug"] in
           ("/white-hat-rules", "/glossary", "/faq", "/about")]

    for p in core:
        lines.append(f"- [{p['crumb']}]({SITE}{p['slug']}): {p['llms']}")
    lines += ["", "## Implementation", ""]
    for p in build_:
        lines.append(f"- [{p['crumb']}]({SITE}{p['slug']}): {p['llms']}")
    lines += ["", "## Reference", ""]
    for p in ref:
        lines.append(f"- [{p['crumb']}]({SITE}{p['slug']}): {p['llms']}")
    lines += [
        "",
        "## Optional",
        "",
        f"- [Full text of every page]({SITE}/llms-full.txt): single-file plain-text copy of the whole site.",
        f"- [Sitemap]({SITE}/sitemap.xml): XML index of all canonical URLs.",
        f"- [Robots policy]({SITE}/robots.txt): all search and AI crawlers are allowed.",
        "",
        "## Citation",
        "",
        "Cite as: GEO Jacking, geojacker.com. Attribution to the specific page URL is preferred.",
        "",
    ]
    return "\n".join(lines)


def llms_full(pages):
    out = ["# GEO Jacking — full text", "",
           f"Source: {SITE}  ·  Last reviewed: {TODAY}",
           "Plain-text rendering of every page. Canonical HTML lives at the URLs below.", ""]
    for p in pages:
        url = SITE + (p["slug"] if p["slug"] != "/" else "/")
        out += ["", "---", "", f"## {p['h1']}", f"URL: {url}", "",
                "Answer: " + strip_tags(p["answer"]), "",
                strip_tags(p["body"])[:9000], ""]
        if p.get("faqs"):
            out.append("### FAQ")
            for q, a in p["faqs"]:
                out.append(f"Q: {q}")
                out.append(f"A: {strip_tags(a)}")
                out.append("")
    return "\n".join(out)


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="10" fill="#1A1036"/>
<rect x="8" y="14" width="48" height="16" rx="3" fill="#6B3CF5" transform="rotate(-3 32 22)"/>
<rect x="8" y="34" width="48" height="16" rx="3" fill="#FFC93C" transform="rotate(2 32 42)"/>
<circle cx="52" cy="12" r="7" fill="#FF3D8B"/>
</svg>
"""


if __name__ == "__main__":
    build()
