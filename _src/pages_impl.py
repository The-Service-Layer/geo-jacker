# -*- coding: utf-8 -*-
"""Implementation pages."""

SITE = "https://geojacker.com"

SCHEMA = {
    "slug": "/structured-data-for-ai", "crumb": "Structured data for AI",
    "title": "Structured Data for AI: JSON-LD Patterns That Machines Actually Use",
    "desc": ("Which schema types matter for AI visibility, a copy-paste entity graph, and an honest "
             "account of what structured data can and cannot do for AI answers."),
    "h1": "Structured data for AI",
    "llms": "Practical JSON-LD patterns, a linked entity graph, and the limits of schema for AI visibility.",
    "level": "Advanced", "section": "Implementation",
    "keywords": ["JSON-LD", "schema.org", "structured data", "entity graph", "AI visibility"],
    "answer": ("<strong>Structured data doesn't make an AI cite you, but it removes ambiguity about "
               "what your page says and who is saying it.</strong> The highest-value implementation is "
               "not more schema types &mdash; it's a single connected <code>@graph</code> where every node "
               "has a stable <code>@id</code>, so machines resolve your organisation, author, page and "
               "topic as one coherent entity rather than four unrelated blobs."),
    "faqs": [
        ("Does Google require structured data for AI Overviews?",
         "<p>No. Google's <a href='https://developers.google.com/search/docs/fundamentals/ai-optimization-guide' "
         "rel='noopener'>2026 documentation on generative AI features</a> (developers.google.com) "
         "states plainly that structured "
         "data isn't required for AI Overviews or AI Mode and that there's no special schema.org markup "
         "you need to add for them. That's worth taking at face value. Schema still earns its place for "
         "a different reason: it is the cheapest way to make facts about your entity unambiguous to any "
         "system that chooses to read them, including ones that aren't Google.</p>"),
        ("Should the JSON-LD say things the page doesn't?",
         "<p>Never. Structured data must describe content that is visible on the page. Markup that "
         "contradicts or exceeds the visible content is a spam signal under Google's structured data "
         "guidelines and can trigger manual action. It's also pointless &mdash; a model reading the page "
         "will see the mismatch.</p>"),
        ("Is Microdata or RDFa still acceptable?",
         "<p>Both are still valid vocabularies, but JSON-LD is the recommended format and by far the "
         "easiest to maintain because it lives in one block rather than being woven through your markup. "
         "If you're starting fresh, use JSON-LD. If you have legacy Microdata that works, migrating is "
         "low priority.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Implementation · Machine-readable layer</p>
  <h1>Structured data for AI</h1>
  <p class="lede">Schema won't buy you a citation. It will stop a machine from guessing wrong about
  what you are, which turns out to matter more.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">Structured data doesn't make an AI cite you, but it removes ambiguity about
    what your page says and who is saying it.</p>
    <p>The highest-value implementation isn't more schema types &mdash; it's a single connected
    <code>@graph</code> where every node has a stable <code>@id</code>, so machines resolve your
    organisation, author, page and topic as one coherent entity instead of four unrelated blobs.</p>
  </div>

  <h2><span class="h-num">01</span>Start with the graph, not the types</h2>
  <p>Most sites emit three separate JSON-LD blocks that never reference each other: an Organization
  here, an Article there, a BreadcrumbList somewhere else. A parser has to infer that they're
  related. Give it explicit edges instead.</p>
  <p>The pattern: one <code>@graph</code> array per page, every node carrying an <code>@id</code>
  that is a real URL with a fragment, and references between nodes done by <code>@id</code> rather
  than by repeating the object. Every page on this site does exactly that &mdash; view source and
  read the block in the head.</p>

  <pre data-copy><code>&lt;script type="application/ld+json"&gt;
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Co",
      "url": "https://example.com/",
      "sameAs": [
        "https://www.wikidata.org/wiki/Q000000",
        "https://www.linkedin.com/company/example-co"
      ],
      "knowsAbout": ["Retrieval augmented generation", "AI visibility"]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com/",
      "publisher": { "@id": "https://example.com/#organization" }
    },
    {
      "@type": "TechArticle",
      "@id": "https://example.com/guide#article",
      "headline": "How retrieval works",
      "author": { "@id": "https://example.com/#organization" },
      "isPartOf": { "@id": "https://example.com/#website" },
      "datePublished": "2026-08-07",
      "dateModified": "2026-08-07",
      "about": { "@id": "https://example.com/#ai-visibility" }
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://example.com/#ai-visibility",
      "name": "AI visibility",
      "description": "How often a brand is retrieved and cited inside AI answers."
    }
  ]
}
&lt;/script&gt;</code></pre>

  <h2><span class="h-num">02</span>The types that earn their place</h2>
  <div class="table-wrap">
    <table>
      <caption>Schema types ranked by usefulness for AI visibility</caption>
      <thead><tr><th scope="col">Type</th><th scope="col">Use it for</th><th scope="col">Why it matters here</th></tr></thead>
      <tbody>
        <tr><th scope="row">Organization</th><td>Every page, via one shared node</td><td>Anchors your brand as a resolvable entity; <code>sameAs</code> links it to Wikidata and other authorities</td></tr>
        <tr><th scope="row">Person</th><td>Author bios and bylines</td><td>Carries expertise signals; connect to the same person node everywhere</td></tr>
        <tr><th scope="row">Article / TechArticle</th><td>Guides and posts</td><td>Supplies headline, dates, author and word count in a form nothing has to infer</td></tr>
        <tr><th scope="row">FAQPage</th><td>Genuine question-answer pairs</td><td>Explicit Q&amp;A pairing is unusually easy for retrieval systems to consume</td></tr>
        <tr><th scope="row">HowTo</th><td>Ordered procedures</td><td>Steps, tools and durations become discrete machine-readable objects</td></tr>
        <tr><th scope="row">DefinedTerm / DefinedTermSet</th><td>Glossaries</td><td>Underused and high-leverage: a formal term-to-definition mapping</td></tr>
        <tr><th scope="row">BreadcrumbList</th><td>Every non-home page</td><td>Communicates site hierarchy and topical parentage</td></tr>
        <tr><th scope="row">Dataset</th><td>Original research you publish</td><td>Makes first-party data discoverable as data, not just prose</td></tr>
        <tr><th scope="row">Product / Offer</th><td>Anything purchasable</td><td>Price, availability and specs in a form assistants can compare</td></tr>
        <tr><th scope="row">LocalBusiness</th><td>Physical locations</td><td>Hours, address and service area — heavily used in local answers</td></tr>
      </tbody>
    </table>
  </div>

  <h2><span class="h-num">03</span>Three properties worth more than they look</h2>
  <h3><code>sameAs</code></h3>
  <p>A list of authoritative URLs that refer to the same entity: Wikidata, Wikipedia, LinkedIn,
  Crunchbase, GitHub, official social profiles. This is the single most direct way to tell a machine
  &ldquo;the thing on this page and the thing in that knowledge base are the same thing.&rdquo; If you
  do one thing from this page, do this.</p>

  <h3><code>knowsAbout</code></h3>
  <p>On an <code>Organization</code> or <code>Person</code>, this declares topical expertise. It
  won't manufacture authority you don't have, but it disambiguates &mdash; a consultancy called
  &ldquo;Northstar&rdquo; that <code>knowsAbout</code> retrieval systems is clearly not the boat
  dealership with the same name.</p>

  <h3><code>speakable</code></h3>
  <p>A <code>SpeakableSpecification</code> with a CSS selector marks the passages you consider the
  canonical spoken summary of a page. Its official support is narrow, but it costs two lines and it
  states your intent about which passage is the answer. Point it at your answer block.</p>

  <h2><span class="h-num">04</span>Rules that keep you out of trouble</h2>
  <ul>
    <li><strong>Markup must match visible content.</strong> No exceptions. This is the rule that
    triggers manual actions.</li>
    <li><strong>One canonical entity node per site</strong>, reused by <code>@id</code> on every
    page. Don't redefine your Organization with slightly different values on each template.</li>
    <li><strong>Dates in ISO 8601</strong>, and <code>dateModified</code> only changes when content
    actually changes.</li>
    <li><strong>Don't mark up navigation, ads or boilerplate</strong> as content.</li>
    <li><strong>Validate before shipping</strong> with Google's Rich Results Test and the
    Schema.org validator. A single trailing comma silently kills the whole block.</li>
  </ul>

  <div class="note">
    <p><strong>Diminishing returns</strong>Adding a tenth schema type is rarely the constraint.
    A connected graph with five well-formed types and accurate <code>sameAs</code> links will
    outperform twenty types emitted as disconnected islands.</p>
  </div>

  <p>Related: <a href="/llms-txt">llms.txt, honestly</a> &mdash; the other machine-readable file
  everyone is arguing about.</p>
</div>
""",
}


LLMSTXT = {
    "slug": "/llms-txt", "crumb": "llms.txt, honestly",
    "title": "llms.txt: What the 2026 Data Actually Shows",
    "desc": ("Adoption sits around 10% of domains, major AI crawlers rarely fetch it, and Google has "
             "said it won't support it. Here's why it's still worth twenty minutes — and what it isn't."),
    "h1": "llms.txt, honestly",
    "llms": "Evidence-based assessment of llms.txt: low crawler usage, no major adoption, still cheap to ship.",
    "level": "Intermediate", "section": "Implementation",
    "keywords": ["llms.txt", "llms-full.txt", "AI crawlers", "robots.txt"],
    "answer": ("<strong>llms.txt is a proposed Markdown file at your site root that lists your most "
               "important pages so AI systems know what to read first.</strong> As of 2026 it has "
               "roughly 10% adoption, no major AI provider has committed to consuming it, Google has "
               "said on the record that it doesn't support it, and monitoring studies show AI crawlers "
               "almost never request it. Ship one anyway &mdash; it takes twenty minutes and it's a "
               "reasonable bet on agentic retrieval &mdash; but don't expect it to move citations."),
    "faqs": [
        ("Is llms.txt an official standard?",
         "<p>No. It's a community proposal with no backing from the W3C, IETF or any recognised "
         "standards body, and no enforcement mechanism. AI providers adopt it, or don't, on their own "
         "terms. Anyone describing it as a standard is overstating it.</p>"),
        ("Does llms.txt block AI crawlers?",
         "<p>No &mdash; it does the opposite of robots.txt. robots.txt tells crawlers what they may not "
         "access and is broadly respected. llms.txt suggests what AI systems should read first and "
         "carries no restrictive power at all. If your goal is to limit AI access, robots.txt and your "
         "terms of service are the tools, not this.</p>"),
        ("Should I generate a Markdown copy of every page?",
         "<p>Usually not. It's a popular approach and it introduces duplicate content at scale if those "
         "files are indexable. Duplicate Markdown mirrors dilute crawl budget and can suppress the "
         "original pages. If you do publish them, keep them out of your sitemap and consider a "
         "<code>noindex</code> header.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Implementation · Contested</p>
  <h1>llms.txt, honestly</h1>
  <p class="lede">Most write-ups of this file are selling something. Here is what the measurement
  says, followed by what we still recommend and why those two things aren't in conflict.</p>

  <div class="cite-block alt">
    <span class="cite-tag">The short answer</span>
    <p class="answer">llms.txt is a <a href="https://llmstxt.org/" rel="noopener">proposed Markdown
    file</a> at your site root that lists your most
    important pages so AI systems know what to read first. It is not a standard, and the evidence
    that it currently affects AI citations is weak.</p>
    <p>Ship one anyway. It costs twenty minutes, it can't hurt, and it's a cheap option on a future
    where agents route on machine-readable site surfaces. Just don't build a strategy on it.</p>
  </div>

  <h2><span class="h-num">01</span>What the 2026 data shows</h2>
  <ul>
    <li><strong>Adoption is around one site in ten.</strong> An <a
    href="https://seranking.com/blog/llms-txt/" rel="noopener">SE Ranking study of 300,000
    domains</a> found a 10.13% adoption rate &mdash; and among the fifty most AI-cited domains, only
    one had the file at all.</li>
    <li><strong>Crawlers barely fetch it.</strong> A <a
    href="https://limy.ai/blog/llms.txt-in-2026-the-full-guide" rel="noopener">Limy.ai monitoring
    analysis</a> of over 500 million AI bot
    events across a 90-day window found only a few hundred requests targeting <code>/llms.txt</code>
    directly. GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot and Google-Extended overwhelmingly
    crawl HTML instead.</li>
    <li><strong>Google has said no.</strong> Gary Illyes <a
    href="https://searchengineland.com/google-says-normal-seo-works-for-ranking-in-ai-overviews-and-llms-txt-wont-be-used-459422"
    rel="noopener">confirmed Google doesn't support llms.txt</a> and
    isn't planning to; John Mueller <a
    href="https://www.searchenginejournal.com/google-says-llms-txt-comparable-to-keywords-meta-tag/544804/"
    rel="noopener">compared it to the discredited keywords meta tag</a>. Google's
    <a href="https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
    rel="noopener">2026 generative-AI documentation</a> lists it among unnecessary tactics.</li>
    <li><strong>No provider has committed.</strong> As of 2026, no major AI company has publicly
    committed to reading or acting on llms.txt in production.</li>
    <li><strong>A large share of existing files are junk.</strong> The HTTP Archive's <a
    href="https://almanac.httparchive.org/en/2025/seo" rel="noopener">2025 Web Almanac</a> found
    around 40% of published files were plugin-generated defaults rather than deliberate,
    curated documents.</li>
  </ul>

  <h2><span class="h-num">02</span>So why ship one?</h2>
  <p>Three defensible reasons, none of which is &ldquo;it will get me cited.&rdquo;</p>
  <ol>
    <li><strong>The cost is near zero and the option is real.</strong> Twenty minutes buys you a
    position if agentic routing does standardise. That's a sensible asymmetric bet.</li>
    <li><strong>Writing it is a useful forcing function.</strong> Producing a one-sentence
    description of your forty most important pages surfaces duplication, orphaned content and pages
    that don't actually say anything. Several teams get more value from the audit than the file.</li>
    <li><strong>It's a business-to-agent surface, not an SEO artifact.</strong> The interesting use
    case isn't search citations &mdash; it's an agent trying to work out what your company offers and
    where the authoritative page for each thing lives.</li>
  </ol>

  <h2><span class="h-num">03</span>How to write one properly</h2>
  <p>The proposal specifies Markdown: an H1 with the site or brand name, a blockquote summary,
  optional free prose, then H2 sections listing links with a one-sentence description each. Keep it
  curated &mdash; ten to forty genuinely important pages, not a sitemap dump.</p>

  <pre data-copy><code><span class="k"># Example Co</span>

<span class="c">&gt; One-paragraph description of what the organisation does,</span>
<span class="c">&gt; who it serves, and what makes its content authoritative.</span>

Optional prose: scope of the site, what is and isn't covered,
licensing or citation preferences.

<span class="k">## Core guides</span>

- [What is X](https://example.com/what-is-x): One sentence on what this page answers.
- [How X works](https://example.com/how-x-works): One sentence on what this page answers.

<span class="k">## Reference</span>

- [Glossary](https://example.com/glossary): Definitions of 40 terms used across the site.

<span class="k">## Optional</span>

- [Full text](https://example.com/llms-full.txt): Plain-text copy of every page.</code></pre>

  <p>Our own <a href="/llms.txt">llms.txt</a> and <a href="/llms-full.txt">llms-full.txt</a> are
  live and follow this shape. Copy them.</p>

  <h3>Rules of thumb</h3>
  <ul>
    <li>Serve it as <code>text/plain</code> at the site root, exactly at <code>/llms.txt</code>.</li>
    <li>Use absolute URLs.</li>
    <li>Curate ruthlessly &mdash; the file's only advantage over a sitemap is editorial judgement.</li>
    <li>Include a last-reviewed date and actually keep it current. A stale file is worse than none.</li>
    <li>Don't duplicate every page as a Markdown mirror unless you handle indexation properly.</li>
  </ul>

  <h2><span class="h-num">04</span>How to check whether anything reads it</h2>
  <p>Don't guess. Filter your access logs for requests to <code>/llms.txt</code> and
  <code>/llms-full.txt</code> by known AI user agents. You can also embed a unique URL inside the
  file that appears nowhere else &mdash; a honeypot only an automated reader would follow &mdash; and
  watch for hits. Cloudflare's bot analytics will break this down by user agent without touching raw
  logs.</p>

  <div class="note">
    <p><strong>Priority check</strong>If you have limited hours this quarter, spend them on crawl
    access, answer structure and original data before you spend one on this file. That ordering is
    the whole argument of <a href="/ai-visibility-stack">the stack</a>.</p>
  </div>
</div>
""",
}


CITED = {
    "slug": "/get-cited-faster", "crumb": "Get cited faster",
    "title": "How to Get Cited by AI Faster: Entity Building and Citation Mechanics",
    "desc": ("Citation is a content outcome; recommendation is an entity outcome. How to build the "
             "entity signals that make AI systems name your brand, not just source your page."),
    "h1": "How to get cited faster",
    "llms": "Entity building, third-party mentions and the difference between being cited and being recommended.",
    "level": "Advanced", "section": "Implementation",
    "keywords": ["AI citations", "entity SEO", "Wikidata", "brand mentions", "digital PR"],
    "answer": ("<strong>The fastest route to AI citation is to be the most specific, best-sourced "
               "answer to a narrow question on a page an engine can already fetch.</strong> The slower, "
               "more valuable route is entity building: making your brand a resolvable, consistently "
               "described thing across Wikidata, Wikipedia, industry databases and third-party coverage, "
               "which is what turns citations into recommendations."),
    "faqs": [
        ("How long until I see citations after publishing?",
         "<p>For retrieval-based answers, days to a few weeks once the page is indexed &mdash; the engine "
         "is reading the live web, so there's no training cycle to wait for. For answers that draw on "
         "model memory rather than live retrieval, months, because that only updates when the model does. "
         "This is why restructuring existing indexed pages produces faster results than launching new ones.</p>"),
        ("Do backlinks still matter for AI visibility?",
         "<p>Indirectly and substantially. Links themselves feed the search indexes AI systems retrieve "
         "from, but the more important effect is the <em>mention</em>: being described by other credible "
         "sites is what builds the entity association a model relies on when it decides which brand to "
         "name. An unlinked mention in a reputable publication can be worth more here than a linked one "
         "in a low-quality directory.</p>"),
        ("Should I create a Wikipedia page for my company?",
         "<p>Only if you genuinely meet notability requirements, and never by paying for edits &mdash; "
         "undisclosed paid editing violates Wikipedia's terms and gets reversed. Wikidata is the more "
         "accessible starting point: it has a lower bar, it's structured, and it's widely consumed by "
         "machines. Create an accurate Wikidata item, link it from your <code>sameAs</code>, and let "
         "Wikipedia follow if and when coverage justifies it.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Implementation · Compounding</p>
  <h1>How to get cited faster</h1>
  <p class="lede">Two clocks run at once. One is fast and content-shaped. The other is slow,
  entity-shaped, and worth far more.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">The fastest route to AI citation is to be the most specific, best-sourced
    answer to a narrow question on a page an engine can already fetch.</p>
    <p>The slower and more valuable route is entity building &mdash; making your brand a resolvable,
    consistently described thing across Wikidata, Wikipedia, industry databases and third-party
    coverage. That's what converts citations into recommendations.</p>
  </div>

  <h2><span class="h-num">01</span>The fast clock: content moves in weeks</h2>
  <p>Because retrieval reads the live web, an existing indexed page that you restructure today can
  start appearing in answers within days. That makes the highest-yield first move counter-intuitive:
  don't publish new pages. Rewrite the ones already indexed.</p>
  <ol>
    <li>Take the twenty pages with existing impressions in Search Console.</li>
    <li>For each, identify the one question it should own and put a 40&ndash;60 word answer directly
    under a question-shaped H2 near the top.</li>
    <li>Replace every vague quantifier with a sourced number.</li>
    <li>Add a visible last-reviewed date and update <code>dateModified</code>.</li>
    <li>Request re-indexing and re-run your prompt panel in two weeks.</li>
  </ol>

  <h2><span class="h-num">02</span>The slow clock: entities move in quarters</h2>
  <p>An entity, in this context, is a thing a machine can resolve unambiguously: your company, your
  product, your authors. Models decide which brand to <em>name</em> based on how strongly and how
  consistently that entity is associated with a category across everything they've read.</p>

  <h3>Make yourself resolvable</h3>
  <ul>
    <li><strong>Wikidata item.</strong> Lower notability bar than Wikipedia, structured, and widely
    consumed. Include founding date, industry, headquarters, official website.</li>
    <li><strong>Consistent naming.</strong> Pick one legal name and one trading name and use them
    identically everywhere. &ldquo;Acme Inc.&rdquo;, &ldquo;Acme, Inc&rdquo; and &ldquo;ACME&rdquo;
    can resolve as three entities.</li>
    <li><strong>Complete profiles</strong> on LinkedIn, Crunchbase, G2 or your industry's equivalent,
    and any relevant standards or trade body register.</li>
    <li><strong><code>sameAs</code> everywhere.</strong> Your Organization schema should link out to
    every one of those profiles. That's the edge that ties them together.</li>
  </ul>

  <h3>Earn descriptions, not just links</h3>
  <p>What builds the association is other people <em>describing</em> you. Prioritise formats that
  produce descriptive third-party text:</p>
  <ul>
    <li>Original research that journalists can cite with a number and a name.</li>
    <li>Genuine expert commentary — respond to reporter queries with substance, not boilerplate.</li>
    <li>Conference talks and podcasts, which generate transcripts and show notes.</li>
    <li>Open-source contributions and public documentation.</li>
    <li>Honest answers in the communities engines actually read, under your real identity.</li>
  </ul>

  <h2><span class="h-num">03</span>Where engines look, and why it's uneven</h2>
  <p>Reference-grade sources carry disproportionate weight. A <a
  href="https://www.tryprofound.com/blog/chatgpt-citation-sources" rel="noopener">Profound analysis
  of ChatGPT citation behaviour</a> found Wikipedia to be ChatGPT's single most-cited domain,
  appearing in nearly one in six conversations that carry citations. Community platforms, official
  documentation
  and established trade publications also appear far more often than their raw traffic would
  suggest. Meanwhile a <a href="https://otterly.ai/blog/claude-ai-citation-study/"
  rel="noopener">2026 Otterly.ai study</a> found Claude and ChatGPT citing the same domains only
  about 13% of the time.</p>
  <p>Two conclusions follow. First, being accurately described on a small number of authoritative
  surfaces beats being mentioned in a hundred low-quality ones. Second, checking only one assistant
  will badly misrepresent your visibility.</p>

  <h2><span class="h-num">04</span>The self-ranking trap</h2>
  <p>The most common mistake in this space is publishing your own &ldquo;top ten tools in
  [category]&rdquo; with yourself at number one. A <a
  href="https://lilyraynyc.substack.com/p/why-calling-yourself-the-best-could" rel="noopener">2026
  analysis by SEO researcher Lily Ray</a> found brands doing this were left
  out of the AI recommendation roughly 69% of the time. The pattern is legible to a model, and it
  reads as promotional rather than informative.</p>
  <p>What works instead is the comparison you'd be willing to show a prospect who's already talking
  to a competitor: honest strengths, honest weaknesses, a clear statement of who each option suits.
  It converts better with humans too.</p>

  <div class="note">
    <p><strong>Sequencing</strong>Fast clock first, because it produces evidence that funds the
    slow clock. Restructure twenty existing pages this month; start the entity work the same month
    but expect to report on it next quarter.</p>
  </div>

  <p>Ready to execute? <a href="/30-day-playbook">The 30-day playbook</a> puts this in order.</p>
</div>
""",
}


PLAYBOOK = {
    "slug": "/30-day-playbook", "crumb": "The 30-day playbook",
    "title": "The 30-Day GEO Jacking Playbook: Four Weeks, Ordered by Leverage",
    "desc": ("A week-by-week plan to build AI visibility: baseline and unblock, restructure for "
             "extraction, ship structured data, then start entity building. No fluff weeks."),
    "h1": "The 30-day GEO Jacking playbook",
    "llms": "Week-by-week execution plan: baseline, restructure, mark up, build entity signals.",
    "level": "Intermediate", "section": "Implementation",
    "keywords": ["GEO playbook", "AI visibility plan", "30 day SEO sprint"],
    "answer": ("<strong>Four weeks, ordered by leverage: week one baselines and unblocks, week two "
               "restructures existing indexed pages for extraction, week three ships structured data and "
               "machine-readable files, week four starts entity building and sets up recurring "
               "measurement.</strong> The order matters more than the timeline &mdash; each week depends on "
               "the one before it."),
    "faqs": [
        ("Can a team of one do this?",
         "<p>Yes, at about ten to twelve hours a week, provided you have publishing access and someone "
         "who can edit robots.txt. The heaviest week is week two. If time is tighter, do week one "
         "properly and stretch week two across a month &mdash; skipping the baseline is the one shortcut "
         "that guarantees you can't prove anything later.</p>"),
        ("What if I have no original data to publish?",
         "<p>You almost certainly do. Support tickets, sales call objections, onboarding times, pricing "
         "you've quoted, error rates, seasonal patterns &mdash; anonymised and aggregated, all of it is "
         "publishable and none of it exists anywhere else. Start with the question your support team "
         "answers most often and count how often they answer it.</p>"),
        ("How do I know if the sprint worked?",
         "<p>Compare your week-one prompt panel against the same panel at day 30, scoring mention rate, "
         "citation rate and recommendation rate separately. Also check AI crawler hits in server logs "
         "and referral traffic from AI domains in analytics. Expect movement on citation before "
         "recommendation &mdash; the second one runs on the slow clock.</p>"),
    ],
    "extra_schema": [{
        "@type": "HowTo",
        "@id": SITE + "/30-day-playbook#howto",
        "name": "The 30-day GEO Jacking playbook",
        "description": ("A four-week plan to build AI visibility by baselining, restructuring content "
                        "for extraction, shipping structured data, and building entity signals."),
        "totalTime": "P30D",
        "supply": [
            {"@type": "HowToSupply", "name": "Server access logs"},
            {"@type": "HowToSupply", "name": "Google Search Console access"},
            {"@type": "HowToSupply", "name": "A list of 30–60 real buyer questions"},
        ],
        "tool": [
            {"@type": "HowToTool", "name": "Google Search Console"},
            {"@type": "HowToTool", "name": "Rich Results Test"},
            {"@type": "HowToTool", "name": "An analytics platform such as GA4"},
        ],
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "Week 1 — Baseline and unblock",
             "url": SITE + "/30-day-playbook#week-1",
             "text": ("Confirm AI crawlers can fetch the site, fix robots.txt and CDN bot rules, "
                      "build a 30–60 prompt panel and record who is cited today.")},
            {"@type": "HowToStep", "position": 2, "name": "Week 2 — Restructure for extraction",
             "url": SITE + "/30-day-playbook#week-2",
             "text": ("Rewrite the twenty highest-impression indexed pages so each leads with a "
                      "self-contained 40–60 word answer under a question-shaped heading.")},
            {"@type": "HowToStep", "position": 3, "name": "Week 3 — Ship the machine-readable layer",
             "url": SITE + "/30-day-playbook#week-3",
             "text": ("Deploy a connected JSON-LD entity graph, validate it, and publish llms.txt, "
                      "an accurate sitemap and a permissive robots.txt.")},
            {"@type": "HowToStep", "position": 4, "name": "Week 4 — Build the entity and measure",
             "url": SITE + "/30-day-playbook#week-4",
             "text": ("Create or correct Wikidata and directory profiles, publish one piece of "
                      "original first-party data, and re-run the prompt panel to compare against baseline.")},
        ],
    }],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Implementation · Execution</p>
  <h1>The 30-day GEO Jacking playbook</h1>
  <p class="lede">Ordered by leverage, not by comfort. Week one is unglamorous and non-negotiable;
  everything after it depends on getting it right.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">Week one baselines and unblocks, week two restructures existing indexed pages
    for extraction, week three ships structured data and machine-readable files, week four starts
    entity building and sets up recurring measurement.</p>
    <p>The order matters more than the timeline. If it takes you sixty days, fine &mdash; just don't
    reorder it.</p>
  </div>

  <h2><span class="h-num">The sprint</span>Four weeks, in order</h2>

  <ol class="steps">
    <li id="week-1">
      <h3>Week 1 — Baseline and unblock</h3>
      <p><strong>Goal: prove machines can reach you, and record where you stand.</strong></p>
      <ul>
        <li>Grep access logs for <code>GPTBot</code>, <code>OAI-SearchBot</code>,
        <code>ClaudeBot</code>, <code>PerplexityBot</code>, <code>ChatGPT-User</code> and
        <code>Google-Extended</code>. Zero hits is a red alert, not a curiosity.</li>
        <li>Audit robots.txt, WAF rules and CDN bot management. Cloudflare's <a
        href="https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/"
        rel="noopener">AI-blocking default</a> has
        silently switched off a lot of sites.</li>
        <li>Verify server-side rendering: <code>curl -A "GPTBot" https://yoursite.com/key-page</code>
        and read what comes back.</li>
        <li>Write 30&ndash;60 real buyer questions in customers' words. Pull them from support
        tickets and sales calls, not a keyword tool.</li>
        <li>Run every question through ChatGPT, Perplexity, Claude, Gemini and Google AI Mode. Record
        for each: were you mentioned, were you cited with a link, were you recommended. Three
        separate columns.</li>
      </ul>
      <p>That spreadsheet is your baseline. Without it, nothing you do this month is provable.</p>
    </li>

    <li id="week-2">
      <h3>Week 2 — Restructure for extraction</h3>
      <p><strong>Goal: make existing indexed pages quotable. This is the heavy week.</strong></p>
      <ul>
        <li>Pull the twenty pages with the most Search Console impressions. Already-indexed pages
        move fastest.</li>
        <li>For each: name the one question it should own. If it's trying to own three, plan a split.</li>
        <li>Add a self-contained 40&ndash;60 word answer immediately under a question-shaped H2 near
        the top &mdash; a passage that still makes sense with the rest of the page deleted.</li>
        <li>Fix heading hierarchy: one H1, no skipped levels, sections that stand alone.</li>
        <li>Replace vague quantifiers with sourced numbers. Link claims to primary sources.</li>
        <li>Strip cross-references: no &ldquo;as mentioned above&rdquo;, no orphaned pronouns.</li>
        <li>Add a visible last-reviewed date.</li>
      </ul>
      <p>Full detail on the technique lives in <a href="/answer-engine-optimization">AEO</a>.</p>
    </li>

    <li id="week-3">
      <h3>Week 3 — Ship the machine-readable layer</h3>
      <p><strong>Goal: remove every ambiguity a parser could have.</strong></p>
      <ul>
        <li>Deploy one connected JSON-LD <code>@graph</code> per page: Organization, WebSite,
        WebPage, Article, BreadcrumbList, linked by <code>@id</code>. Pattern is on the
        <a href="/structured-data-for-ai">structured data page</a>.</li>
        <li>Add <code>sameAs</code> to every authoritative profile you control.</li>
        <li>Add <code>FAQPage</code> where you have genuine Q&amp;A pairs, <code>HowTo</code> for
        procedures, <code>DefinedTerm</code> for glossary entries.</li>
        <li>Validate every template in the Rich Results Test and the Schema.org validator.</li>
        <li>Publish an accurate XML sitemap with real <code>lastmod</code> values.</li>
        <li>Publish <a href="/llms-txt">llms.txt</a> &mdash; curated, twenty minutes, no illusions.</li>
      </ul>
    </li>

    <li id="week-4">
      <h3>Week 4 — Build the entity and measure</h3>
      <p><strong>Goal: start the slow clock and close the loop on the fast one.</strong></p>
      <ul>
        <li>Create or correct your Wikidata item. Link it from <code>sameAs</code>.</li>
        <li>Complete every relevant directory and platform profile with identical naming.</li>
        <li>Publish one piece of genuine first-party data &mdash; a benchmark, a survey, an
        aggregate from your own operations. One good number beats five recycled posts.</li>
        <li>Fix the biggest inaccuracy about your category that you can source properly.</li>
        <li>Re-run the full prompt panel. Compare against week one across all three columns.</li>
        <li>Set up recurring measurement: monthly prompt panel, weekly AI crawler log check, an AI
        referral segment in analytics. See <a href="/measure-ai-visibility">measurement</a>.</li>
      </ul>
    </li>
  </ol>

  <h2><span class="h-num">After day 30</span>What the next quarter looks like</h2>
  <p>The sprint gets you structurally competitive. Sustained visibility comes from repetition:
  one new original-data piece a month, continuous restructuring of the next twenty pages, monthly
  prompt-panel review, and steady work on third-party descriptions of your brand. Recommendation
  share &mdash; as opposed to citation share &mdash; typically takes two to three quarters to move,
  because it's an entity outcome.</p>

  <div class="note">
    <p><strong>The one thing not to skip</strong>Week one's prompt panel. Teams that skip it spend
    the next quarter arguing about whether anything worked.</p>
  </div>
</div>
""",
}


MEASURE = {
    "slug": "/measure-ai-visibility", "crumb": "Measure AI visibility",
    "title": "How to Measure AI Visibility: Prompt Panels, Logs and Referral Data",
    "desc": ("Three measurement methods that don't require a vendor: a repeatable prompt panel, "
             "AI crawler log analysis, and an AI referral segment in analytics."),
    "h1": "How to measure AI visibility",
    "llms": "Prompt panels, server log analysis and AI referral tracking — measurement you can run yourself.",
    "level": "Intermediate", "section": "Implementation",
    "keywords": ["AI visibility measurement", "prompt panel", "AI referral traffic", "log file analysis"],
    "answer": ("<strong>Measure AI visibility with three independent methods: a repeatable prompt "
               "panel that scores mention, citation and recommendation separately; server log analysis "
               "of AI crawler activity; and an analytics segment for referral traffic from AI "
               "domains.</strong> No single method is sufficient &mdash; the panel shows what engines say, "
               "the logs show what they fetch, and referrals show what humans do next."),
    "faqs": [
        ("Why do I get different answers each time I run the same prompt?",
         "<p>Generative engines are non-deterministic, personalise on session context, and change "
         "retrieval results as the web changes. That's why the method is a <em>panel</em> &mdash; a fixed "
         "set of prompts run repeatedly, scored as rates rather than as individual results. Run each "
         "prompt three times in a fresh session and record the proportion of runs you appeared in.</p>"),
        ("Is AI referral traffic worth tracking if the volume is tiny?",
         "<p>Yes, because the composition matters more than the volume. Visitors arriving from an "
         "assistant have typically already had their question answered and are further along in a "
         "decision, so conversion rates often run well above organic search. Track it as a separate "
         "channel from day one so you have a trend line when the volume grows.</p>"),
        ("Do I need a paid AI visibility tracking tool?",
         "<p>Not to start. A spreadsheet, three browser sessions and your server logs will give you a "
         "defensible baseline. Paid tools earn their cost when you need scale &mdash; hundreds of prompts "
         "across multiple engines and markets, tracked continuously &mdash; or when you need reporting you "
         "didn't build yourself. Do the manual version first so you understand what the tool is counting.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Implementation · Proof</p>
  <h1>How to measure AI visibility</h1>
  <p class="lede">There's no Search Console for answer engines. There are three methods that
  triangulate well enough to make decisions with.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">Measure AI visibility with three independent methods: a repeatable prompt
    panel scoring mention, citation and recommendation separately; server log analysis of AI crawler
    activity; and an analytics segment for referral traffic from AI domains.</p>
    <p>The panel shows what engines say, the logs show what they fetch, and referrals show what
    humans do next. Any one alone will mislead you.</p>
  </div>

  <h2><span class="h-num">01</span>The prompt panel</h2>
  <p>The core instrument. A fixed list of buyer questions, run on a schedule, scored consistently.</p>
  <ol>
    <li><strong>Fix the prompts.</strong> 30&ndash;60 questions in customers' own words. Once set,
    don't change them &mdash; comparability is the whole point. Add new prompts to a second list.</li>
    <li><strong>Fix the conditions.</strong> Fresh session, no chat history, logged out where
    possible, same country setting. Personalisation will otherwise flatter you.</li>
    <li><strong>Run each prompt three times</strong> per engine and record the proportion of runs.</li>
    <li><strong>Score three things separately.</strong> This is where most trackers oversimplify.</li>
  </ol>

  <div class="table-wrap">
    <table>
      <caption>The three metrics, and what a gap between them tells you</caption>
      <thead><tr><th scope="col">Metric</th><th scope="col">Definition</th><th scope="col">If it's low</th></tr></thead>
      <tbody>
        <tr><th scope="row">Mention rate</th><td>Brand named anywhere in the answer</td><td>Entity association is weak — the model doesn't connect you to the category</td></tr>
        <tr><th scope="row">Citation rate</th><td>Your URL appears as a linked source</td><td>Content is not retrievable or not quotable — go back to layers 1 and 2</td></tr>
        <tr><th scope="row">Recommendation rate</th><td>You're named as the suggested option</td><td>Entity strength or third-party validation is behind competitors</td></tr>
      </tbody>
    </table>
  </div>

  <p>High citation with low recommendation is the classic pattern: your content is good enough to
  source but your brand isn't established enough to name. That's an entity problem, addressed in
  <a href="/get-cited-faster">get cited faster</a>.</p>

  <h2><span class="h-num">02</span>Log file analysis</h2>
  <p>Logs are the only place you see what machines actually did, as opposed to what they said.
  Filter for AI user agents and track four things weekly:</p>
  <ul>
    <li><strong>Hit volume by user agent</strong> — is anything crawling you at all?</li>
    <li><strong>Status codes</strong> — 403s and 429s mean a WAF or rate limiter is blocking you.</li>
    <li><strong>Which URLs get fetched</strong> — a good proxy for what engines consider important.</li>
    <li><strong>Real-time fetchers specifically</strong> — <code>ChatGPT-User</code>,
    <code>Perplexity-User</code> and <code>Claude-User</code> hits mean a human asked a question and
    an engine came to read <em>your page</em> to answer it. That's the closest thing to a live signal.</li>
  </ul>
  <pre data-copy><code><span class="c"># AI crawler hits by user agent, last 7 days</span>
grep -iE <span class="s">"GPTBot|OAI-SearchBot|ChatGPT-User|ClaudeBot|Claude-User|PerplexityBot|Google-Extended"</span> access.log \\
  | awk <span class="s">'{print $9}'</span> | sort | uniq -c | sort -rn</code></pre>

  <h2><span class="h-num">03</span>Referral traffic</h2>
  <p>Create a channel group in your analytics platform matching AI referrers: <code>chatgpt.com</code>,
  <code>chat.openai.com</code>, <code>perplexity.ai</code>, <code>claude.ai</code>,
  <code>copilot.microsoft.com</code>, <code>gemini.google.com</code>. Note that AI Overviews traffic
  generally arrives attributed as ordinary Google organic, so this segment understates the total
  effect &mdash; treat it as a floor.</p>
  <p>Watch conversion rate and pages per session, not just volume. Assistant-referred visitors
  frequently convert better than organic search because the assistant already did the qualifying.</p>

  <h2><span class="h-num">04</span>What not to measure</h2>
  <ul>
    <li><strong>A single run of a single prompt.</strong> Non-determinism makes it noise.</li>
    <li><strong>Screenshots as evidence.</strong> Useful for a slide, useless as a trend.</li>
    <li><strong>Your own logged-in sessions.</strong> Chat history contaminates results badly.</li>
    <li><strong>Total AI referral volume in isolation.</strong> It undercounts by design.</li>
  </ul>

  <div class="note">
    <p><strong>Reporting cadence that works</strong>Weekly: crawler hits and status codes. Monthly:
    full prompt panel with all three rates. Quarterly: recommendation-rate trend and entity audit.
    Anything more frequent measures noise.</p>
  </div>

  <p>Next: the boundaries we hold to — <a href="/white-hat-rules">white-hat rules</a>.</p>
</div>
""",
}

IMPL = [SCHEMA, LLMSTXT, CITED, PLAYBOOK, MEASURE]
