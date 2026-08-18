# GEO Jacker — White-Hat AI Visibility: SEO + AEO + GEO

> **GEO Jacking is the white-hat practice of engineering a web page so an AI answer engine retrieves it, quotes it, and credits it by name.** It stacks on top of SEO and AEO rather than replacing them: SEO gets you crawled and indexed, AEO gets you a direct answer, and GEO gets you named inside the generated response.

This repository is the complete source of **[geojacker.com](https://geojacker.com)** — a free, 15-page field guide to getting cited by Google AI Overviews, ChatGPT search, Perplexity, Claude, Microsoft Copilot and Gemini — together with the zero-dependency Python generator that builds it.

The site practices what it documents, so the code doubles as a **working reference implementation** of GEO and AEO patterns you can lift directly:

- A page-level JSON-LD `@graph` (Organization, WebSite, WebPage, Article, BreadcrumbList) with stable `@id` values
- `FAQPage`, `HowTo`, `DefinedTermSet` and `ItemList` schema generated from the same source as the visible content — never out of sync
- [`llms.txt`](https://geojacker.com/llms.txt) and [`llms-full.txt`](https://geojacker.com/llms-full.txt), plus an [evidence-based writeup](https://geojacker.com/llms-txt) of what those files do and don't achieve
- A `robots.txt` that explicitly allows every major AI crawler (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, and the rest)
- Answer-first page structure: a self-contained answer passage at the top of every guide, question-shaped headings, inline source attribution
- Clean canonical URLs, a hand-rolled sitemap, and cache/security headers via `vercel.json`

## The AI visibility stack

The site's organizing model — four layers, each depending on the one below it:

| Layer | Discipline | Job | Guide |
|---|---|---|---|
| 1 | **SEO** — findability | Crawl access, indexation, speed, internal linking, canonical hygiene | [SEO foundations](https://geojacker.com/seo-foundations) |
| 2 | **AEO** — answerability | Question-shaped headings and self-contained passages that survive extraction | [Answer engine optimization](https://geojacker.com/answer-engine-optimization) |
| 3 | **GEO** — quotability | Original data, named sources and clean definitions that make a passage worth citing | [Generative engine optimization](https://geojacker.com/generative-engine-optimization) |
| 4 | **AI visibility** — the outcome | Measured citation and recommendation share across AI answer surfaces | [How to measure it](https://geojacker.com/measure-ai-visibility) |

Full explanation: [The AI visibility stack](https://geojacker.com/ai-visibility-stack).

## The guides

| Guide | What it covers |
|---|---|
| [What is GEO Jacking?](https://geojacker.com/what-is-geo-jacking) | Definition, method and ethics |
| [The AI visibility stack](https://geojacker.com/ai-visibility-stack) | How SEO, AEO and GEO layer together |
| [SEO foundations for AI visibility](https://geojacker.com/seo-foundations) | The layer everyone skips |
| [Answer engine optimization (AEO)](https://geojacker.com/answer-engine-optimization) | Writing passages that get extracted |
| [Generative engine optimization (GEO)](https://geojacker.com/generative-engine-optimization) | What the research actually shows |
| [Structured data for AI](https://geojacker.com/structured-data-for-ai) | JSON-LD patterns machines actually use |
| [llms.txt, honestly](https://geojacker.com/llms-txt) | What the 2026 data actually shows |
| [How to get cited faster](https://geojacker.com/get-cited-faster) | Entity building and citation mechanics |
| [The 30-day GEO Jacking playbook](https://geojacker.com/30-day-playbook) | Four weeks of work, ordered by leverage |
| [How to measure AI visibility](https://geojacker.com/measure-ai-visibility) | Prompt panels, log analysis and referral data |
| [White-hat rules](https://geojacker.com/white-hat-rules) | What GEO Jacking refuses to do, and why |
| [Glossary](https://geojacker.com/glossary) | 40 GEO, AEO and SEO terms defined |
| [FAQ](https://geojacker.com/faq) | 20 straight answers on getting cited |

## FAQ

**Is GEO Jacking a black-hat technique?**
No. The word "jacking" describes the outcome — taking a share of the answer that currently belongs to someone else — not the method. Everything on the site is disclosed, reproducible and compliant with search and AI platform guidelines: no cloaking, no prompt injection, no fabricated reviews, no scraped content. The [white-hat rules](https://geojacker.com/white-hat-rules) page lists exactly what's off the table.

**Do I still need SEO if I'm doing GEO?**
Yes. Answer engines retrieve from the live web, and almost every retrieval path runs through a crawler, an index and a ranking step. Google's own [guidance on generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) makes the point bluntly: optimizing for generative AI search is still SEO. GEO adds a layer; it does not remove the floor.

**How long does it take to show up in AI answers?**
Faster than classic SEO, but not instantly. Pages that are already indexed can start appearing in retrieval-based answers within days of being restructured; answers that depend on model memory move on training cycles and can take many months. Plan for a 30-day sprint on structure and a 6–12 month arc on entity strength — that's what the [30-day playbook](https://geojacker.com/30-day-playbook) sequences.

## Project structure

```
_src/                             Source — edit here, then rebuild
  build.py                        Page shell, nav, JSON-LD graph, sitemap, robots, llms.txt
  content.py                      Page registry
  pages_core.py                   Home, definition, stack, SEO, AEO, GEO
  pages_impl.py                   Schema, llms.txt, citations, playbook, measurement
  pages_ref.py                    Ethics, glossary, FAQ, about
  assets/                         CSS design system, minimal JS, 8 self-hosted woff2 subsets

public/                           Generated output — never edit directly
vercel.json                       outputDirectory, cleanUrls, cache + security headers
```

No dependencies, no framework, no build tooling beyond Python 3's standard library.

## Building

Never edit `public/` by hand — the build overwrites it. Change the source in `_src/`, then:

```bash
python3 _src/build.py     # regenerates everything into public/
```

`build.py` keeps the shell, navigation and JSON-LD graph consistent across all 15 pages. Content lives in `pages_core.py`, `pages_impl.py` and `pages_ref.py`; styling in `_src/assets/css/style.css`.

## Deploying

**Vercel** (already configured): `npm i -g vercel && vercel --prod`, then add your domain under Project → Settings → Domains. `vercel.json` sets `outputDirectory: "public"` and `cleanUrls: true`, so `/what-is-geo-jacking.html` is served at `/what-is-geo-jacking` — which is what every canonical tag and internal link uses.

**Netlify / Cloudflare Pages / S3 / any static host**: publish the `public/` folder, then configure two things `vercel.json` normally handles:

1. **Clean URLs** — strip the `.html` extension or the canonicals won't match the served URLs. Netlify and Cloudflare Pages do this automatically; Nginx: `try_files $uri $uri.html $uri/ =404;`
2. **`llms.txt` and `llms-full.txt`** must be served as `text/plain; charset=utf-8`.

## Using this as a template for your own site

Fork it, then:

- [ ] Change `SITE` in `_src/build.py` to your domain and rebuild — it drives canonicals, JSON-LD `@id` values, `sitemap.xml` and `llms.txt`.
- [ ] Replace the `sameAs` array on the Organization node with your own profiles (GitHub, LinkedIn, Wikidata, X).
- [ ] Verify the domain in Google Search Console and Bing Webmaster Tools; submit `sitemap.xml`.
- [ ] Run a few pages through the Rich Results Test and the Schema.org validator.
- [ ] Confirm your CDN isn't blocking AI crawlers — Cloudflare blocks them by default now, and that single setting undoes everything else on this list.

## Sources and sourcing policy

Every statistic on the site is attributed inline to a named, checkable source — nothing is invented. The main ones:

- The [GEO study presented at KDD 2024](https://arxiv.org/abs/2311.09735) by researchers from Princeton, Georgia Tech, IIT Delhi and the Allen Institute — the paper that defined generative engine optimization and measured which content changes move citation share.
- Google's [2026 documentation on succeeding in generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- Otterly.ai's 2026 citation study on how little source overlap there is between engines.
- Cloudflare's 2025 shift to blocking AI crawlers by default.

The [about page](https://geojacker.com/about) documents the sourcing policy in full. Every page carries a visible "last reviewed" date; update `TODAY` in `_src/build.py` when revising content.

## Quoting and reusing this content

Quote, excerpt or adapt anything from the guides — definitions, the four-layer model, the playbook structure — with attribution: a link to [geojacker.com](https://geojacker.com) or to the specific guide page. For machine consumption, [`llms-full.txt`](https://geojacker.com/llms-full.txt) is a plain-text copy of the entire site in one file.

Questions and corrections are welcome as [issues](https://github.com/The-Service-Layer/geo-jacker/issues) — the sourcing policy means factual errors get fixed, not argued with.

---

GEO Jacker is a [LogicBomb Media](https://lbm.co/) project.
