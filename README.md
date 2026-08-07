# GEO Jacking — geojacker.com

A 15-page static site about white-hat AI visibility (SEO → AEO → GEO). No build step, no
dependencies, no JavaScript framework. Every page is plain HTML served as-is.

## What's in here

```
index.html                        Home
what-is-geo-jacking.html          Definition + method
ai-visibility-stack.html          The four-layer model
seo-foundations.html              Layer 1
answer-engine-optimization.html   Layer 2
generative-engine-optimization.html  Layer 3
structured-data-for-ai.html       JSON-LD patterns
llms-txt.html                     Evidence-based take on llms.txt
get-cited-faster.html             Entity building
30-day-playbook.html              Execution plan (HowTo schema)
measure-ai-visibility.html        Measurement methods
white-hat-rules.html              Ethics
glossary.html                     40 terms (DefinedTermSet schema)
faq.html                          20 Q&As (FAQPage schema)
about.html                        Site + sourcing policy
404.html                          Not-found page (noindex)

assets/style.css                  All styling
assets/app.js                     Mobile nav + copy buttons
assets/fonts/                     8 self-hosted woff2 subsets (172 KB total)

robots.txt                        Permissive — every AI crawler explicitly allowed
sitemap.xml                       15 canonical URLs
llms.txt                          Curated reading order for AI systems
llms-full.txt                     Plain-text copy of the whole site
og-image.png                      1200×630 social preview
favicon.svg
vercel.json                       cleanUrls, cache headers, security headers
```

## Deploying

### Vercel (recommended — `vercel.json` is already configured)

```bash
npm i -g vercel
vercel --prod
```

Then add `geojacker.com` under **Project → Settings → Domains** and point your DNS at Vercel.

`vercel.json` sets `cleanUrls: true`, so `/what-is-geo-jacking.html` is served at
`/what-is-geo-jacking` — which is what every canonical tag and internal link already uses.

### Netlify / Cloudflare Pages / S3 / any static host

Upload the folder as-is. Two things to configure manually, since `vercel.json` is Vercel-specific:

1. **Clean URLs** — strip the `.html` extension, or the canonicals won't match the served URLs.
   - Netlify: automatic ("Pretty URLs" is on by default).
   - Cloudflare Pages: automatic.
   - Apache: `MultiViews` or a rewrite rule. Nginx: `try_files $uri $uri.html $uri/ =404;`
2. **`llms.txt` and `llms-full.txt` must be served as `text/plain; charset=utf-8`.**

### Before you go live

- [ ] Replace `https://geojacker.com` if you're using a different domain — it appears in
      canonicals, JSON-LD `@id` values, `sitemap.xml` and `llms.txt`. Find/replace across all files.
- [ ] Add a real `sameAs` array to the Organization node (LinkedIn, Wikidata, X, Crunchbase).
      It's currently omitted rather than filled with placeholders.
- [ ] Verify the domain in Google Search Console and Bing Webmaster Tools, submit `sitemap.xml`.
- [ ] Run three pages through the Rich Results Test and the Schema.org validator.
- [ ] Confirm your CDN isn't blocking AI crawlers. Cloudflare blocks them by default now —
      that single setting will undo everything else on this list.

## Editing

The HTML is hand-editable, but the pages were generated from a Python source in `_src/`, which
keeps the shell, navigation and JSON-LD graph consistent across all 15 pages. To change something
global (nav, footer, schema, the design system):

```bash
cd _src
python3 build.py     # regenerates every page into ../
```

- `build.py` — page shell, nav, breadcrumbs, JSON-LD graph, sitemap, robots.txt, llms.txt
- `pages_core.py` — home, definition, stack, SEO, AEO, GEO
- `pages_impl.py` — schema, llms.txt, citations, playbook, measurement
- `pages_ref.py` — ethics, glossary, FAQ, about
- `assets/style.css` — the design system (edit here, not in the output copy)

If you'd rather not touch Python, delete `_src/` and edit the HTML directly. Nothing depends on it
at runtime.

## Notes on the content

Statistics are attributed inline to their source (the KDD 2024 GEO study, Google's 2026 generative-AI
documentation, named vendor analyses) so they can be checked and updated. Nothing is invented. The
`llms.txt` page in particular reports the evidence that the file is currently low-impact rather than
overselling it — if you'd prefer a more promotional tone, that's the page to rewrite first.

Dates: every page carries `2026-08-07` as `datePublished`/`dateModified` and a visible "last
reviewed" line in the footer. Update `TODAY` in `_src/build.py` when you revise content.
