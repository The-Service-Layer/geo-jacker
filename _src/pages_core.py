# -*- coding: utf-8 -*-
"""Core guide pages."""

SITE = "https://geojacker.com"

HOME = {
    "slug": "/", "crumb": "Home", "article": False, "priority": "1.0",
    "title": "GEO Jacking — White-Hat AI Visibility: SEO + AEO + GEO",
    "desc": ("GEO Jacking is the white-hat practice of stacking SEO, AEO and GEO so answer "
             "engines retrieve, cite and recommend your pages. Free guides, schema recipes and a 30-day playbook."),
    "h1": "GEO Jacking: hijack the answer, honestly",
    "llms": "Home page. Defines GEO Jacking and indexes every guide on the site.",
    "keywords": ["GEO jacking", "AI visibility", "generative engine optimization",
                 "answer engine optimization", "SEO"],
    "answer": ("<strong>GEO Jacking is the white-hat practice of engineering a page so an AI "
               "answer engine retrieves it, quotes it and credits it by name.</strong> It stacks on "
               "top of SEO and AEO rather than replacing them: SEO gets you crawled and indexed, AEO "
               "gets you a direct answer, and GEO gets you named inside the generated response."),
    "faqs": [
        ("Is GEO Jacking a black-hat technique?",
         "<p>No. The word &ldquo;jacking&rdquo; describes the outcome &mdash; taking a share of the answer that "
         "currently belongs to someone else &mdash; not the method. Everything on this site is disclosed, "
         "reproducible and compliant with search and AI platform guidelines. No cloaking, no prompt "
         "injection, no fabricated reviews, no scraped content. The <a href='/white-hat-rules'>white-hat "
         "rules</a> page lists exactly what we refuse to do and why those tactics fail anyway.</p>"),
        ("Do I still need SEO if I'm doing GEO?",
         "<p>Yes, and it is not optional. Answer engines retrieve from the live web, and almost every "
         "retrieval path runs through a crawler, an index and a ranking step you already know how to "
         "influence. Google's own <a href='https://developers.google.com/search/docs/fundamentals/ai-optimization-guide' "
         "rel='noopener'>2026 guidance on generative AI features</a> (developers.google.com) makes the point bluntly: "
         "optimizing for generative AI search is optimizing for the search experience, and is therefore "
         "still SEO. GEO adds a layer; it does not remove the floor.</p>"),
        ("How long does it take to show up in AI answers?",
         "<p>Faster than classic SEO, but not instantly. Pages that are already crawled and indexed can "
         "start appearing in retrieval-based answers within days of being restructured, because the "
         "engine is reading the live page rather than waiting on a ranking change. Answers that depend on "
         "model memory rather than live retrieval move on training cycles and can take many months. Plan "
         "for a 30-day sprint on structure and a 6&ndash;12 month arc on entity strength.</p>"),
        ("Which engines does this site cover?",
         "<p>The techniques target retrieval-augmented answer surfaces generally: Google AI Overviews and "
         "AI Mode, ChatGPT search, Perplexity, Claude, Microsoft Copilot and Gemini. They overlap far less "
         "than people assume &mdash; a <a href='https://otterly.ai/blog/claude-ai-citation-study/' "
         "rel='noopener'>2026 Otterly.ai study</a> (otterly.ai) found Claude and ChatGPT citing the same "
         "domains only about 13% of the time &mdash; so the practical strategy is to optimize the underlying "
         "content structure rather than chase one engine's quirks.</p>"),
    ],
    "extra_schema": [{
        "@type": "ItemList",
        "@id": SITE + "/#guides",
        "name": "The GEO Jacking guides",
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "numberOfItems": 13,
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": SITE + s, "name": n}
            for i, (s, n) in enumerate([
                ("/what-is-geo-jacking", "What is GEO Jacking?"),
                ("/ai-visibility-stack", "The AI visibility stack"),
                ("/seo-foundations", "SEO foundations for AI visibility"),
                ("/answer-engine-optimization", "Answer engine optimization (AEO)"),
                ("/generative-engine-optimization", "Generative engine optimization (GEO)"),
                ("/structured-data-for-ai", "Structured data for AI"),
                ("/llms-txt", "llms.txt, honestly"),
                ("/get-cited-faster", "How to get cited faster"),
                ("/30-day-playbook", "The 30-day GEO Jacking playbook"),
                ("/measure-ai-visibility", "How to measure AI visibility"),
                ("/white-hat-rules", "White-hat rules"),
                ("/glossary", "Glossary"),
                ("/faq", "FAQ"),
            ])
        ],
    }],
    "body": """
<section class="wrap hero">
  <div class="hero-grid">
    <div>
      <p class="eyebrow">SEO → AEO → GEO → AI visibility</p>
      <h1>Stop optimizing for <span class="strike">ten blue links</span>.<br>Start <em>jacking the answer</em>.</h1>
      <p class="lede">Answer engines don't rank pages any more. They assemble an answer and hand out
      credit to a handful of sources. GEO Jacking is the white-hat craft of making sure one of
      those sources is you.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="/what-is-geo-jacking">Start here</a>
        <a class="btn btn-ghost" href="/30-day-playbook">Jump to the 30-day playbook</a>
      </div>
      <ul class="pipeline">
        <li>Crawled</li><li>Chunked</li><li>Retrieved</li><li>Quoted</li><li>Cited</li>
      </ul>
    </div>

    <div class="hero-side">
    <div class="engine" role="img" aria-label="Mock answer engine response citing geojacker.com as a source">
      <div class="engine-bar"><span>Answer engine</span><span class="dot">● retrieving</span></div>
      <div class="engine-body">
        <p class="engine-q">&ldquo;how do I get my site cited by ChatGPT and AI Overviews?&rdquo;</p>
        <div class="engine-a">
          <p class="engine-line">Getting cited by an AI answer engine depends on three things: being
          crawlable, being chunkable, and being quotable.</p>
          <p class="engine-line">Pages that lead with a self-contained 40&ndash;60 word answer under a
          question-shaped heading are retrieved far more often than pages that bury the answer.</p>
          <p class="engine-line">Original statistics and named sources measurably increase citation
          rates <a class="chip pop" href="/generative-engine-optimization">geojacker.com</a></p>
        </div>
      </div>
    </div>

      <p class="ev-lead">What changed, in three numbers</p>
      <div class="evidence">
        <div class="ev"><b>&lt;20%</b><span>Overlap between top Google links and AI-cited sources, down from ~70% two years earlier — <a href="https://www.prnewswire.com/news-releases/new-5w-research-overlap-between-top-google-rankings-and-ai-cited-sources-has-collapsed-from-70-to-under-20-302760132.html" rel="noopener">Brandlight, via 5W Research, 2026</a></span></div>
        <div class="ev"><b>~13%</b><span>Domains Claude and ChatGPT both cite for the same query (barely 4% of exact URLs) — <a href="https://otterly.ai/blog/claude-ai-citation-study/" rel="noopener">Otterly.ai, 2026</a></span></div>
        <div class="ev"><b>+41% / +32%</b><span>Visibility lift from adding quotations / statistics — <a href="https://arxiv.org/abs/2311.09735" rel="noopener">Aggarwal et al., KDD 2024</a></span></div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h2><span class="h-num">The premise</span>Four layers. You need all four.</h2>
    <p>Each layer solves a different failure. Skip one and the layers above it stop working &mdash;
    an engine can't cite a page it can't fetch, and it won't quote a page that never answers
    anything.</p>

    <div class="stack">
      <div class="layer l1">
        <span class="tier">LAYER 1</span>
        <h3>SEO — be findable</h3>
        <p>Crawl access, indexation, speed, internal links, canonical hygiene. The floor. Nothing above works without it.</p>
      </div>
      <div class="layer l2">
        <span class="tier">LAYER 2</span>
        <h3>AEO — be answerable</h3>
        <p>Question-shaped headings, self-contained answer blocks, entities named in plain language. Makes a passage extractable.</p>
      </div>
      <div class="layer l3">
        <span class="tier">LAYER 3</span>
        <h3>GEO — be quotable</h3>
        <p>Original data, named sources, direct quotes, clean definitions. Makes a passage worth pulling into a synthesised answer.</p>
      </div>
      <div class="layer l4">
        <span class="tier">OUTCOME</span>
        <h3>AI visibility</h3>
        <p>How often you're retrieved, cited and recommended by name across every answer surface. The thing you actually measure.</p>
      </div>
    </div>
    <p><a href="/ai-visibility-stack">Read the full breakdown of the stack →</a></p>
  </div>
</section>

<section class="wrap page-body">
  <h2><span class="h-num">Why now</span>The overlap between ranking and being cited is collapsing</h2>
  <p>For most of search history, one job covered both outcomes: rank well and you got the traffic.
  That relationship is coming apart. Brandlight analysis <a
  href="https://www.prnewswire.com/news-releases/new-5w-research-overlap-between-top-google-rankings-and-ai-cited-sources-has-collapsed-from-70-to-under-20-302760132.html"
  rel="noopener">reported through 5W Research in 2026</a> put the overlap between the top Google
  links and the sources AI systems actually cite at
  <mark>under 20%, down from roughly 70%</mark> two years earlier. Separate 2026 analyses found that
  the majority of pages cited by AI engines do not rank in Google's top ten at all &mdash; Ahrefs
  data <a href="https://www.5wpr.com/research/state-of-ai-citations-2026/" rel="noopener">reported in
  5W's State of AI Citations</a> put the share of AI-cited URLs that also rank in Google's top ten
  at just 12%.</p>
  <p>That's the opening. A page that would never crack position three can still be the passage an
  engine quotes &mdash; if it is structured to be retrieved and worth quoting. That is what this site
  teaches.</p>

  <div class="note">
    <p><strong>Honest caveat</strong>This field is young and the measurement is noisy. Where a
    claim on this site comes from a specific study or vendor dataset, we name and link it so you
    can check it yourself. Where something is contested &mdash; <a href="/llms-txt">llms.txt is the clearest
    example</a> &mdash; we say so instead of selling it.</p>
  </div>

  <h2><span class="h-num">Where to start</span>Pick your entry point</h2>
  <div class="cards three">
    <a class="card" href="/what-is-geo-jacking">
      <span class="kicker">Definition</span>
      <h3>What is GEO Jacking?</h3>
      <p>The term, the method, and why &ldquo;jacking&rdquo; describes an outcome rather than a trick.</p>
    </a>
    <a class="card" href="/generative-engine-optimization">
      <span class="kicker">Layer 3</span>
      <h3>Generative engine optimization</h3>
      <p>What the research actually shows about which content changes move citation rates.</p>
    </a>
    <a class="card" href="/structured-data-for-ai">
      <span class="kicker">Implementation</span>
      <h3>Structured data for AI</h3>
      <p>Copy-paste JSON-LD patterns, an entity graph that makes sense, and what schema can't do.</p>
    </a>
    <a class="card" href="/30-day-playbook">
      <span class="kicker">Do the work</span>
      <h3>The 30-day playbook</h3>
      <p>Four weeks, ordered by leverage. Audit, restructure, mark up, then build entity presence.</p>
    </a>
    <a class="card" href="/measure-ai-visibility">
      <span class="kicker">Proof</span>
      <h3>Measure AI visibility</h3>
      <p>Prompt panels, log-file analysis, GA4 referral segments. Numbers you can defend.</p>
    </a>
    <a class="card" href="/glossary">
      <span class="kicker">Reference</span>
      <h3>Glossary</h3>
      <p>Forty terms &mdash; chunking, fan-out, grounding, RAG &mdash; defined in one sentence each.</p>
    </a>
  </div>
</section>
""",
}


WHAT_IS = {
    "slug": "/what-is-geo-jacking", "crumb": "What is GEO Jacking?",
    "title": "What Is GEO Jacking? Definition, Method and Ethics",
    "desc": ("GEO Jacking is the white-hat practice of structuring content so AI answer engines "
             "retrieve, quote and cite it. Here's the definition, the four-step method and where the line sits."),
    "h1": "What is GEO Jacking?",
    "llms": "Definition of GEO Jacking, the four-step method, and the ethical boundary.",
    "level": "Beginner", "section": "Fundamentals",
    "keywords": ["GEO jacking definition", "AI visibility", "white hat GEO", "AI citation"],
    "answer": ("<strong>GEO Jacking is the white-hat practice of engineering a web page so that "
               "generative answer engines retrieve it, quote it, and attribute the answer to your "
               "brand.</strong> It takes citation share that currently belongs to a competitor &mdash; "
               "the &ldquo;jacking&rdquo; &mdash; using only disclosed, guideline-compliant techniques: "
               "clearer structure, better sourcing, stronger entity signals and original data."),
    "faqs": [
        ("Who coined the term GEO Jacking?",
         "<p>The term GEO Jacking was coined by <a href=\"https://lbm.co\" rel=\"noopener\">LogicBomb "
         "Media</a> (lbm.co), the digital agency behind this site. It's a portmanteau built from "
         "&ldquo;GEO&rdquo; (generative engine optimization, formalised in academic work in 2024) "
         "and the older marketing sense of &ldquo;jacking&rdquo; &mdash; as in newsjacking, the practice "
         "of inserting yourself into a conversation already in progress. LogicBomb Media uses it in that "
         "second sense: you are inserting yourself into an answer that is already being generated.</p>"),
        ("Is GEO Jacking the same as GEO?",
         "<p>Not quite. GEO is the discipline. GEO Jacking is a posture within it &mdash; specifically "
         "targeting answers that competitors currently own, rather than building visibility in the "
         "abstract. In practice that means you start from the prompts, find who gets cited today, and "
         "engineer a better source for that exact question.</p>"),
        ("Does GEO Jacking work for local businesses?",
         "<p>Yes, and often faster than for national brands, because the competitive set is smaller and "
         "the entity signals are easier to complete. Consistent name-address-phone data, a fully "
         "populated Google Business Profile, LocalBusiness structured data and a handful of genuinely "
         "local citations do a lot of work. The content side is identical: answer local questions "
         "directly, on their own pages, with specifics an engine can quote.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Fundamentals · Layer 0</p>
  <h1>What is GEO Jacking?</h1>
  <p class="lede">A short definition, the method behind it, and a clear line between the version
  that compounds and the version that gets you burned.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">GEO Jacking is the white-hat practice of engineering a web page so that
    generative answer engines retrieve it, quote it, and attribute the answer to your brand.</p>
    <p>It targets citation share that currently belongs to someone else, using only disclosed,
    guideline-compliant techniques: clearer structure, better sourcing, stronger entity signals
    and original data. It sits on top of SEO and AEO rather than replacing them.</p>
  </div>

  <h2><span class="h-num">01</span>Why the name has &ldquo;jacking&rdquo; in it</h2>
  <p>The word describes the <em>outcome</em>, not the method. When someone asks an assistant
  &ldquo;what's the best project management tool for a five-person agency?&rdquo;, the engine
  returns one answer built from maybe four to eight sources. Those slots are occupied. There is no
  page eleven to drift onto. To appear, you have to displace something.</p>
  <p>That's a meaningfully different job from ranking. Ranking is additive &mdash; a new page joins a
  list. Citation is substitutive &mdash; a new source replaces an existing one in a fixed-size answer.
  Naming that honestly is more useful than pretending AI visibility is a rising tide.</p>

  <h3>What it is not</h3>
  <p>It is not prompt injection, cloaking, or hiding instructions in HTML for a crawler to obey.
  Those techniques exist, they are detectable, they violate every major platform's terms, and they
  are trivially reversible when a model updates. <a href="/white-hat-rules">The white-hat rules
  page</a> covers each one and why the expected value is negative.</p>

  <h2><span class="h-num">02</span>The method, in four moves</h2>
  <p>Every GEO Jacking engagement reduces to the same loop. It is not complicated; it is just
  rarely done in order.</p>

  <ol class="steps">
    <li>
      <h3>Find the answer you want</h3>
      <p>Write down 30&ndash;60 real questions your buyers ask, in their words, not your keyword tool's.
      Run them through ChatGPT, Perplexity, Claude, Gemini and Google AI Mode. Record who gets cited
      for each. That list is your target set &mdash; it is far more specific than a keyword list, and
      it tells you exactly whose slot you're taking.</p>
    </li>
    <li>
      <h3>Read the incumbent like an engine would</h3>
      <p>For each cited page, ask what made it retrievable: does it answer in the first paragraph?
      Is the heading phrased as the question? Does it contain a number, a date, a named source?
      Is it a page about one thing, or a chapter buried in a 4,000-word omnibus? The pattern is
      usually obvious within a dozen examples.</p>
    </li>
    <li>
      <h3>Build a better source, not a longer one</h3>
      <p>Publish one page per question cluster. Lead with a 40&ndash;60 word answer that stands alone
      if lifted out of context &mdash; because it will be. Add the thing the incumbent lacks: your own
      data, a named expert, a concrete example, a current date. Length is not the lever. Extractability
      and specificity are.</p>
    </li>
    <li>
      <h3>Make the machine's job trivial</h3>
      <p>Clean heading hierarchy, JSON-LD that describes the same facts as the visible text, an
      entity graph that ties author to organisation to topic, and crawl access for every AI user
      agent you're willing to be cited by. Then re-run the prompt panel monthly and watch the
      citation set move.</p>
    </li>
  </ol>

  <h2><span class="h-num">03</span>Where the line sits</h2>
  <div class="ledger">
    <div class="ledger-col yes">
      <h3>Compounds</h3>
      <ul>
        <li>Original research and first-party data nobody else can publish</li>
        <li>Self-contained answers under question-shaped headings</li>
        <li>Named, dated, linked sources for every claim</li>
        <li>Consistent entity data across Wikidata, LinkedIn, Crunchbase, your own schema</li>
        <li>Genuine expert authorship with a verifiable track record</li>
        <li>Correcting outdated facts about your own category</li>
      </ul>
    </div>
    <div class="ledger-col no">
      <h3>Backfires</h3>
      <ul>
        <li>Hidden text or instructions aimed at model behaviour</li>
        <li>Serving crawlers different content than humans</li>
        <li>Fabricated statistics or invented studies</li>
        <li>Self-serving &ldquo;best of&rdquo; lists that place your own product first</li>
        <li>Mass-generated pages with no new information</li>
        <li>Fake reviews, sockpuppet mentions, purchased Wikipedia edits</li>
      </ul>
    </div>
  </div>
  <p>One item deserves emphasis: self-ranking. A <a
  href="https://lilyraynyc.substack.com/p/why-calling-yourself-the-best-could" rel="noopener">2026
  analysis by SEO researcher Lily Ray</a> found that brands publishing their
  own &ldquo;best in category&rdquo; lists were left out of the AI recommendation roughly 69% of the
  time. Engines appear to discount obviously self-interested comparison content. Publishing an honest
  comparison that sometimes recommends a competitor is, counter-intuitively, the higher-yield play.</p>

  <h2><span class="h-num">04</span>What to read next</h2>
  <p>If you want the conceptual map, go to <a href="/ai-visibility-stack">the AI visibility
  stack</a>. If you want to start work today, go to <a href="/30-day-playbook">the 30-day
  playbook</a>. If you're deciding whether any of this is real, start with
  <a href="/measure-ai-visibility">measurement</a> so you can baseline before you touch anything.</p>
</div>
""",
}


STACK = {
    "slug": "/ai-visibility-stack", "crumb": "The AI visibility stack",
    "title": "The AI Visibility Stack: How SEO, AEO and GEO Layer Together",
    "desc": ("AI visibility is the outcome; SEO, AEO and GEO are the layers that produce it. "
             "What each layer does, what breaks without it, and how to tell which one is failing."),
    "h1": "The AI visibility stack",
    "llms": "How SEO, AEO and GEO layer to produce AI visibility, and how to diagnose which layer is failing.",
    "level": "Beginner", "section": "Fundamentals",
    "keywords": ["AI visibility stack", "SEO vs AEO vs GEO", "AI search optimization"],
    "answer": ("<strong>AI visibility is not a fourth discipline &mdash; it is the outcome of three "
               "stacked ones.</strong> SEO makes a page findable, AEO makes a passage answerable, and "
               "GEO makes that passage worth quoting. Each layer depends on the one below it, so a "
               "failure at any level caps everything above it."),
    "faqs": [
        ("Is AEO just a rebrand of SEO?",
         "<p>There is real overlap, and some practitioners argue the distinction isn't worth drawing. "
         "The useful difference is the unit of optimization: SEO optimizes a <em>page</em> to rank, AEO "
         "optimizes a <em>passage</em> to be extracted as a direct answer. That changes concrete "
         "decisions &mdash; where you put the answer, how you phrase headings, whether one page should "
         "cover three questions or one. Keep the distinction if it changes your work; drop the labels if it doesn't.</p>"),
        ("Which layer should I fix first?",
         "<p>Always the lowest broken one. Check crawl access and indexation before you touch content "
         "structure, and fix content structure before you invest in original research. The diagnostic "
         "table on this page maps each symptom to the layer that causes it.</p>"),
        ("Can I skip SEO and go straight to GEO?",
         "<p>No. Answer engines overwhelmingly retrieve from the live, indexed web. If a crawler can't "
         "fetch your page, or your CDN is blocking AI user agents by default, nothing downstream matters. "
         "Cloudflare's <a href='https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/' "
         "rel='noopener'>shift to blocking AI bots by default</a> (blog.cloudflare.com, July 2025) has "
         "silently removed a large number of sites "
         "from AI answers &mdash; check your configuration before you write a single new word.</p>"),
    ],
    "extra_schema": [{
        "@type": "ItemList",
        "@id": SITE + "/ai-visibility-stack#layers",
        "name": "The four layers of AI visibility",
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "numberOfItems": 4,
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "SEO — findability",
             "description": "Crawl access, indexation, speed, internal linking and canonical hygiene."},
            {"@type": "ListItem", "position": 2, "name": "AEO — answerability",
             "description": "Question-shaped headings and self-contained answer passages that survive extraction."},
            {"@type": "ListItem", "position": 3, "name": "GEO — quotability",
             "description": "Original data, named sources and clean definitions that make a passage worth citing."},
            {"@type": "ListItem", "position": 4, "name": "AI visibility — the outcome",
             "description": "Measured citation and recommendation share across AI answer surfaces."},
        ],
    }],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Fundamentals · The map</p>
  <h1>The AI visibility stack</h1>
  <p class="lede">Three disciplines, one outcome. The value of thinking in layers is diagnostic:
  when you're not getting cited, the stack tells you which layer to go and fix.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">AI visibility is not a fourth discipline &mdash; it is the outcome of three
    stacked ones: SEO makes a page findable, AEO makes a passage answerable, and GEO makes that
    passage worth quoting.</p>
    <p>Each layer depends on the one below it. A brilliant original statistic on a page that
    returns a 403 to GPTBot has zero visibility. A perfectly crawlable page that never answers a
    question has almost as little.</p>
  </div>

  <h2><span class="h-num">The map</span>Four layers, bottom to top</h2>

  <div class="stack">
    <div class="layer l1"><span class="tier">LAYER 1</span><h3>SEO — findability</h3>
      <p>Can a machine fetch, render, parse and index this URL, and does the site's link structure tell it this page matters?</p></div>
    <div class="layer l2"><span class="tier">LAYER 2</span><h3>AEO — answerability</h3>
      <p>If a retrieval system splits this page into chunks, does any single chunk stand alone as a complete answer to a real question?</p></div>
    <div class="layer l3"><span class="tier">LAYER 3</span><h3>GEO — quotability</h3>
      <p>Given five sources that all answer the question, is there a reason to quote <em>this</em> one? A number, a date, a name, a claim nobody else made?</p></div>
    <div class="layer l4"><span class="tier">OUTCOME</span><h3>AI visibility</h3>
      <p>Measured share of citations and recommendations across ChatGPT, Perplexity, Claude, Gemini, Copilot and AI Overviews.</p></div>
  </div>

  <h2><span class="h-num">01</span>What each layer actually controls</h2>

  <div class="table-wrap">
    <table>
      <caption>Layer responsibilities and the symptom when each one fails</caption>
      <thead>
        <tr><th scope="col">Layer</th><th scope="col">Unit of work</th><th scope="col">Primary levers</th><th scope="col">Symptom when broken</th></tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">SEO</th><td>The page</td>
          <td>robots.txt, sitemaps, render budget, Core Web Vitals, internal links, canonicals</td>
          <td>Zero AI crawler hits in server logs; page absent from Google index</td>
        </tr>
        <tr>
          <th scope="row">AEO</th><td>The passage</td>
          <td>Question-shaped H2/H3, 40&ndash;60 word answer blocks, one topic per URL, tables and lists</td>
          <td>Crawlers fetch the page constantly, but you're never quoted</td>
        </tr>
        <tr>
          <th scope="row">GEO</th><td>The claim</td>
          <td>Original data, named sources, direct quotes, expert authorship, freshness dates</td>
          <td>You get cited occasionally, but competitors get the recommendation</td>
        </tr>
        <tr>
          <th scope="row">Entity</th><td>The brand</td>
          <td>Wikidata, Wikipedia, LinkedIn, consistent schema, third-party mentions</td>
          <td>Engine cites your page but names a bigger competitor as the answer</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p>That last row is the one most teams miss. Being <em>cited</em> and being <em>recommended</em>
  are separate outcomes. An engine will happily use your page as a source and then name a
  better-established brand in the sentence. Fixing that is an entity problem, not a content
  problem &mdash; see <a href="/get-cited-faster">get cited faster</a>.</p>

  <h2><span class="h-num">02</span>How a modern answer gets built</h2>
  <p>Understanding the pipeline makes the layer model concrete. When someone asks a complex
  question, most retrieval-augmented systems do roughly this:</p>
  <ol>
    <li><strong>Query fan-out.</strong> The assistant decomposes the question into several
    narrower sub-queries and searches each separately. &ldquo;Best VPN for streaming in
    Europe&rdquo; might become three searches. Your page only needs to win <em>one</em> of them.</li>
    <li><strong>Retrieval.</strong> Candidate documents are fetched from a search index, a
    proprietary index, or a live crawl.</li>
    <li><strong>Chunking and ranking.</strong> Documents are split into passages and scored for
    relevance to each sub-query. This is where page structure decides your fate: a passage that
    references &ldquo;as mentioned above&rdquo; loses its meaning the moment it's separated.</li>
    <li><strong>Synthesis.</strong> The model writes an answer from the top-scoring passages and
    attaches citations to the sentences it drew from.</li>
  </ol>
  <p>Every layer of the stack maps onto a step. SEO gets you into retrieval. AEO gets your chunk
  ranked. GEO gets your chunk chosen for the sentence that carries the citation.</p>

  <div class="note">
    <p><strong>Practical implication</strong>Query fan-out is the reason narrow pages beat
    omnibus guides. A 4,000-word &ldquo;ultimate guide&rdquo; competes for one broad query. Twelve
    focused pages compete for twelve sub-queries, and sub-queries are what the engine is actually
    searching for.</p>
  </div>

  <h2><span class="h-num">03</span>Diagnosing your own stack</h2>
  <p>Run these four checks in order and stop at the first failure.</p>
  <ol class="steps">
    <li><h3>Are AI crawlers reaching you?</h3>
      <p>Grep your access logs for <code>GPTBot</code>, <code>OAI-SearchBot</code>,
      <code>ClaudeBot</code>, <code>PerplexityBot</code> and <code>Google-Extended</code>. Zero hits
      means a robots.txt rule, a WAF rule, or a CDN bot-management default is blocking you. Fix
      this before anything else.</p></li>
    <li><h3>Does any single chunk answer a question?</h3>
      <p>Take your most important page, delete everything except one 300-word section, and read it
      cold. If it doesn't make sense standing alone, no chunk of it will either.</p></li>
    <li><h3>Is there anything only you can say?</h3>
      <p>If every claim on the page is available on ten other domains, an engine has no reason to
      prefer you. First-party data is the cheapest durable advantage most teams have and the one
      they use least.</p></li>
    <li><h3>Is your brand a resolvable entity?</h3>
      <p>Search your brand name plus your category. Do Wikidata, LinkedIn, and your own
      <code>Organization</code> schema all agree on what you are and what you do? Inconsistency
      here caps recommendation share regardless of content quality.</p></li>
  </ol>

  <p>Next: start at the bottom with <a href="/seo-foundations">SEO foundations</a>, or skip to the
  layer your diagnosis flagged.</p>
</div>
""",
}


SEO = {
    "slug": "/seo-foundations", "crumb": "SEO foundations",
    "title": "SEO Foundations for AI Visibility: The Layer Everyone Skips",
    "desc": ("AI answer engines retrieve from the indexed web. Crawl access, render budget, "
             "internal linking and indexation decide whether GEO work has anything to stand on."),
    "h1": "SEO foundations for AI visibility",
    "llms": "The technical SEO baseline AI retrieval depends on: crawl access, rendering, indexation, internal links.",
    "level": "Intermediate", "section": "Layer 1",
    "keywords": ["technical SEO", "AI crawler access", "robots.txt AI bots", "indexation"],
    "answer": ("<strong>Answer engines retrieve overwhelmingly from the live, indexed web, so classic "
               "technical SEO is the precondition for every GEO tactic.</strong> The four things that "
               "actually gate AI visibility are crawl access for AI user agents, server-rendered HTML, "
               "clean indexation, and internal links that make topical importance obvious."),
    "faqs": [
        ("Does Google treat AI search differently from normal search?",
         "<p>According to Google's own <a href='https://developers.google.com/search/docs/fundamentals/ai-optimization-guide' "
         "rel='noopener'>2026 documentation on optimizing for generative AI features</a> "
         "(developers.google.com), no "
         "&mdash; it states that optimizing for generative AI search is optimizing for the search "
         "experience, and is therefore still SEO. The same guidance explicitly pushes back on the idea "
         "that special markup or files are required. Take that as the floor, not the ceiling: other "
         "engines behave differently, and Google has an obvious interest in the answer being &lsquo;keep doing SEO&rsquo;.</p>"),
        ("Will blocking AI crawlers protect my content?",
         "<p>It will reduce your exposure and it will also remove you from AI answers. That is a genuine "
         "business trade-off, not a technical one. Publishers with licensing deals or paywalls often "
         "block deliberately. If your goal is visibility, blocking is self-defeating &mdash; and many sites "
         "block accidentally through CDN bot-management defaults rather than by choice.</p>"),
        ("Does JavaScript rendering hurt AI visibility?",
         "<p>Frequently, yes. Googlebot renders JavaScript; most AI crawlers largely do not. If your "
         "primary content only exists after client-side hydration, a fetch by GPTBot or PerplexityBot may "
         "return an empty shell. Server-side rendering or static generation is the safe default. Test by "
         "fetching your page with JavaScript disabled and reading what's left.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Layer 1 · Findability</p>
  <h1>SEO foundations for AI visibility</h1>
  <p class="lede">The least glamorous layer, and the one that silently zeroes out everything above
  it. Most &ldquo;GEO isn't working&rdquo; problems are actually crawl problems.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">Answer engines retrieve overwhelmingly from the live, indexed web, so classic
    technical SEO is the precondition for every GEO tactic.</p>
    <p>Four things gate AI visibility at this layer: crawl access for AI user agents,
    server-rendered HTML, clean indexation, and internal links that make topical importance obvious.
    Fix these before writing anything new.</p>
  </div>

  <h2><span class="h-num">01</span>Crawl access: check this today</h2>
  <p>The single most common cause of zero AI visibility is that AI crawlers cannot fetch the site.
  This is rarely deliberate. Cloudflare <a
  href="https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/"
  rel="noopener">changed its default configuration to block AI bots</a> in July 2025, which
  means a large number of sites switched themselves off without anyone making a decision.</p>

  <h3>The user agents that matter</h3>
  <p>These fall into three functional groups, and you may want different policies for each:</p>
  <ul>
    <li><strong>Live answer fetchers</strong> &mdash; <code>ChatGPT-User</code>,
    <code>Perplexity-User</code>, <code>Claude-User</code>. These fetch a page because a human just
    asked a question. Blocking these directly removes you from answers.</li>
    <li><strong>Search index builders</strong> &mdash; <code>OAI-SearchBot</code>,
    <code>PerplexityBot</code>, <code>Claude-SearchBot</code>. These build the retrieval indexes those
    answers draw from.</li>
    <li><strong>Training crawlers</strong> &mdash; <code>GPTBot</code>, <code>ClaudeBot</code>,
    <code>Google-Extended</code>, <code>CCBot</code>, <code>Applebot-Extended</code>. These feed model
    training. Allowing them affects long-run model memory rather than today's answers, and this is
    where legitimate publishers most often draw a line.</li>
  </ul>
  <p>These groupings come from each vendor's own crawler documentation, which is the authoritative
  reference for what each agent does: <a href="https://developers.openai.com/api/docs/bots"
  rel="noopener">OpenAI</a>, <a href="https://support.anthropic.com/en/articles/8896518"
  rel="noopener">Anthropic</a>, <a href="https://docs.perplexity.ai/guides/bots"
  rel="noopener">Perplexity</a> and
  <a href="https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers"
  rel="noopener">Google</a> each publish one.</p>

  <h3>A permissive robots.txt</h3>
  <pre data-copy><code><span class="c"># Allow everything that could cite us.</span>
<span class="k">User-agent:</span> *
<span class="k">Allow:</span> /

<span class="k">User-agent:</span> <span class="s">GPTBot</span>
<span class="k">Allow:</span> /

<span class="k">User-agent:</span> <span class="s">OAI-SearchBot</span>
<span class="k">Allow:</span> /

<span class="k">User-agent:</span> <span class="s">ChatGPT-User</span>
<span class="k">Allow:</span> /

<span class="k">User-agent:</span> <span class="s">ClaudeBot</span>
<span class="k">Allow:</span> /

<span class="k">User-agent:</span> <span class="s">PerplexityBot</span>
<span class="k">Allow:</span> /

<span class="k">User-agent:</span> <span class="s">Google-Extended</span>
<span class="k">Allow:</span> /

<span class="k">Sitemap:</span> https://example.com/sitemap.xml</code></pre>

  <p>Then verify it worked. robots.txt is a request, not an enforcement mechanism, and it does
  nothing about a WAF rule or a rate limiter. Check server logs for actual 200 responses to those
  user agents, not just the absence of a Disallow line. Our own live
  <a href="/robots.txt">robots.txt</a> is a working example.</p>

  <h2><span class="h-num">02</span>Rendering: what the crawler actually receives</h2>
  <p>Googlebot has run a full rendering pipeline for years. Most AI crawlers have not caught up.
  If your article body is injected client-side, an AI fetcher may retrieve a page containing your
  nav, your footer, and nothing worth citing.</p>
  <ul>
    <li>Server-render or statically generate all primary content.</li>
    <li>Keep the answer in the initial HTML payload, not behind an accordion that loads on click.</li>
    <li>Content inside <code>&lt;details&gt;</code> elements is in the DOM and is generally fine;
    content fetched on interaction is not.</li>
    <li>Test with <code>curl -A "GPTBot" https://example.com/page</code> and read the output.</li>
  </ul>

  <h2><span class="h-num">03</span>Structure the crawler reads as meaning</h2>
  <p>Heading hierarchy is not decoration. Retrieval systems use it to decide chunk boundaries, so a
  broken hierarchy produces broken chunks.</p>
  <ul>
    <li><strong>One <code>&lt;h1&gt;</code> per page</strong>, describing the page's single subject.</li>
    <li><strong><code>&lt;h2&gt;</code> for each major question or section</strong> &mdash; phrased the way
    a person would ask it where that reads naturally.</li>
    <li><strong>No skipped levels.</strong> An <code>&lt;h4&gt;</code> directly under an
    <code>&lt;h2&gt;</code> makes nesting ambiguous.</li>
    <li><strong>Semantic elements</strong>: <code>&lt;article&gt;</code>, <code>&lt;section&gt;</code>,
    <code>&lt;nav&gt;</code>, <code>&lt;table&gt;</code> with real <code>&lt;th scope&gt;</code>
    headers. Tables in particular are extracted well and quoted often.</li>
    <li><strong>Descriptive link text.</strong> &ldquo;Read our schema guide&rdquo; carries meaning;
    &ldquo;click here&rdquo; carries none.</li>
  </ul>

  <h2><span class="h-num">04</span>Internal linking as a topic map</h2>
  <p>Internal links do two jobs here. They distribute crawl priority, and they tell a machine which
  concepts belong together. A hub page that links to twelve focused sub-pages, each linking back
  with descriptive anchor text, reads as a coherent topical cluster. Twelve orphaned posts do not.</p>
  <p>Practical rules: every page reachable within three clicks of the homepage; every important
  page linked from at least three other pages; anchor text that names the target's subject; and a
  breadcrumb trail on every non-home page, marked up as <code>BreadcrumbList</code>.</p>

  <h2><span class="h-num">05</span>Speed and stability still count</h2>
  <p>An answer fetcher operating in real time has a timeout. A page that takes four seconds to
  return HTML may simply be dropped from consideration while a faster competitor is used. Core Web
  Vitals were built for user experience, but the underlying property &mdash; fast, stable, complete
  HTML on first response &mdash; matters more for machine retrieval than it ever did for ranking.</p>

  <div class="note">
    <p><strong>Baseline checklist</strong>HTTPS everywhere · one canonical URL per piece of content ·
    XML sitemap with accurate <code>lastmod</code> · no <code>noindex</code> on pages you want cited ·
    HTML served in under one second · no client-side-only content · descriptive alt text on
    informative images · consistent trailing-slash policy.</p>
  </div>

  <p>Foundation solid? Move up to <a href="/answer-engine-optimization">answer engine
  optimization</a>.</p>
</div>
""",
}


AEO = {
    "slug": "/answer-engine-optimization", "crumb": "Answer engine optimization",
    "title": "Answer Engine Optimization (AEO): Writing Passages That Get Extracted",
    "desc": ("AEO optimizes the passage, not the page. How to write self-contained answer blocks, "
             "question-shaped headings and chunk-safe content that survives retrieval."),
    "h1": "Answer engine optimization (AEO)",
    "llms": "How to structure passages so retrieval systems can extract them as standalone answers.",
    "level": "Intermediate", "section": "Layer 2",
    "keywords": ["answer engine optimization", "AEO", "featured snippets", "content chunking"],
    "answer": ("<strong>Answer engine optimization is the practice of structuring content so a single "
               "passage can be lifted out and used as a complete answer.</strong> The core move is to "
               "put a self-contained 40&ndash;60 word answer immediately under a question-shaped heading, "
               "then support it &mdash; rather than building toward a conclusion the reader has to assemble."),
    "faqs": [
        ("What's the ideal length for an answer block?",
         "<p>Roughly 40&ndash;60 words, or two to three sentences. Long enough to be complete and specific, "
         "short enough to be quoted without editing. The test is not word count though &mdash; it's whether "
         "the passage still makes sense with everything around it deleted. If it contains &lsquo;as noted "
         "above&rsquo; or an unexplained pronoun, it fails regardless of length.</p>"),
        ("Should I add an FAQ section to every page?",
         "<p>Add one where you have genuine questions with genuine answers, which is most informational "
         "pages. Don't manufacture questions to fill a schema block &mdash; padded FAQs read as thin to "
         "both readers and engines. Note also that Google restricted FAQ rich results in search, but the "
         "markup still helps machines parse question-answer pairs, which is why it remains worth adding.</p>"),
        ("Does content chunking actually matter?",
         "<p>It matters, though it's worth knowing that Google's <a "
         "href='https://developers.google.com/search/docs/fundamentals/ai-optimization-guide' "
         "rel='noopener'>2026 generative-AI guidance</a> (developers.google.com) listed "
         "manual chunking among tactics it considers unnecessary. The resolution is that you shouldn't "
         "engineer artificial chunk boundaries for a specific system &mdash; but you should write sections "
         "that stand alone, because that's good writing and it happens to survive any chunking strategy.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Layer 2 · Answerability</p>
  <h1>Answer engine optimization (AEO)</h1>
  <p class="lede">SEO optimizes a page to rank. AEO optimizes a passage to be extracted. That one
  change in unit rewrites how you structure everything.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">Answer engine optimization is the practice of structuring content so a single
    passage can be lifted out and used as a complete answer.</p>
    <p>The core move: put a self-contained 40&ndash;60 word answer immediately under a question-shaped
    heading, then support and expand it &mdash; instead of building toward a conclusion the reader has
    to assemble from the whole page.</p>
  </div>

  <h2><span class="h-num">01</span>The inverted pyramid, enforced</h2>
  <p>Journalism solved this a century ago and marketing forgot it. Answer first, context second,
  nuance third. The difference now is that the machine reading your page may only ever see the
  first block, because that's the chunk that matched.</p>

  <h3>Before</h3>
  <p><em>&ldquo;Before we can discuss schema markup, it's important to understand the history of
  structured data on the web. In 2011, the major search engines came together&hellip;&rdquo;</em></p>
  <h3>After</h3>
  <p><em>&ldquo;Schema markup is structured data added to a page's HTML that tells machines what
  the content means rather than how it looks. It uses the schema.org vocabulary, usually in JSON-LD
  format, and is the most reliable way to state facts about an entity in a form software can parse
  without guessing.&rdquo;</em></p>
  <p>The second version is quotable. The first version is a warm-up.</p>

  <h2><span class="h-num">02</span>Chunk-safe writing</h2>
  <p>Retrieval systems split documents into passages. You don't control where the splits land, so
  write as though every section might be read in isolation.</p>

  <div class="ledger">
    <div class="ledger-col yes">
      <h3>Survives extraction</h3>
      <ul>
        <li>Repeats the subject noun instead of using &ldquo;it&rdquo; or &ldquo;this&rdquo;</li>
        <li>Names the year explicitly rather than saying &ldquo;currently&rdquo;</li>
        <li>Defines an acronym on first use <em>in each major section</em></li>
        <li>Keeps a claim and its source in the same paragraph</li>
        <li>Puts the answer above any table that supports it</li>
      </ul>
    </div>
    <div class="ledger-col no">
      <h3>Breaks on extraction</h3>
      <ul>
        <li>&ldquo;As we saw above&hellip;&rdquo; / &ldquo;in the previous section&hellip;&rdquo;</li>
        <li>Numbered references to earlier list items</li>
        <li>Pronouns whose antecedent is three headings back</li>
        <li>Answers that only make sense after a long setup</li>
        <li>Key facts that live only in an image or chart</li>
      </ul>
    </div>
  </div>

  <h2><span class="h-num">03</span>Question-shaped headings</h2>
  <p>Real user questions are phrased as questions, and headings that mirror them create an obvious
  match between query and passage. This does not mean every heading becomes a question &mdash; that
  reads badly &mdash; but the ones covering a genuine user question should.</p>
  <div class="table-wrap">
    <table>
      <caption>Rewriting headings for retrieval</caption>
      <thead><tr><th scope="col">Generic heading</th><th scope="col">Question-shaped heading</th></tr></thead>
      <tbody>
        <tr><td>Pricing</td><td>How much does X cost per user per month?</td></tr>
        <tr><td>Integrations</td><td>Which tools does X integrate with natively?</td></tr>
        <tr><td>Getting started</td><td>How long does it take to set X up?</td></tr>
        <tr><td>Comparison</td><td>What's the difference between X and Y?</td></tr>
        <tr><td>Requirements</td><td>What do I need before I can use X?</td></tr>
      </tbody>
    </table>
  </div>

  <h2><span class="h-num">04</span>One page, one job</h2>
  <p>Because assistants fan a question out into narrow sub-queries, narrow pages win more often
  than broad ones. A single page trying to serve &ldquo;what is it&rdquo;, &ldquo;how much does it
  cost&rdquo; and &ldquo;how does it compare&rdquo; will be beaten on each sub-query by a page
  dedicated to it.</p>
  <p>Split when a section could stand as its own page with its own H1 and its own answer block.
  Consolidate when two pages answer the same question with different words &mdash; that's cannibalisation,
  and it splits your signals across two mediocre candidates instead of one strong one.</p>

  <h2><span class="h-num">05</span>Formats that get extracted disproportionately</h2>
  <ul>
    <li><strong>Definition blocks.</strong> &ldquo;X is a Y that does Z.&rdquo; The single most
    reliably quoted sentence pattern on the web.</li>
    <li><strong>Comparison tables.</strong> Machine-parseable, quotable row by row, and hard to
    paraphrase away from the source.</li>
    <li><strong>Numbered procedures.</strong> Ordered lists with one action per step map cleanly onto
    &ldquo;how do I&hellip;&rdquo; queries and onto <code>HowTo</code> markup.</li>
    <li><strong>Direct answers to yes/no questions.</strong> Start with &ldquo;Yes&rdquo; or
    &ldquo;No&rdquo;, then qualify. Most content never actually says the word.</li>
    <li><strong>Short FAQ pairs.</strong> One question, one complete answer, no cross-references.</li>
  </ul>

  <div class="note">
    <p><strong>The read-aloud test</strong>Take any section of your page, read it aloud to someone
    who hasn't seen the rest, and ask whether they got a complete answer. If they ask a clarifying
    question, an engine would have needed the same clarification &mdash; and it can't ask.</p>
  </div>

  <p>Passages extractable? Now make them worth choosing:
  <a href="/generative-engine-optimization">generative engine optimization</a>.</p>
</div>
""",
}


GEO = {
    "slug": "/generative-engine-optimization", "crumb": "Generative engine optimization",
    "title": "Generative Engine Optimization (GEO): What the Research Actually Shows",
    "desc": ("GEO is the practice of making a passage worth quoting. The Princeton-led KDD study, "
             "what moved citation rates, and how to apply it without fabricating anything."),
    "h1": "Generative engine optimization (GEO)",
    "llms": "What GEO is, what the foundational KDD 2024 study measured, and how to apply it honestly.",
    "level": "Advanced", "section": "Layer 3",
    "keywords": ["generative engine optimization", "GEO", "AI citations", "Princeton GEO study"],
    "answer": ("<strong>Generative engine optimization is the practice of making a passage worth "
               "quoting once it has already been retrieved.</strong> The foundational academic study "
               "&mdash; Aggarwal et al., published at KDD 2024 by researchers from Princeton, Georgia "
               "Tech, Allen Institute and IIT Delhi &mdash; tested optimization strategies across 10,000 "
               "queries and found that adding quotations, statistics and citations produced the largest "
               "visibility gains, in the region of 30&ndash;41%."),
    "faqs": [
        ("What did the Princeton GEO study actually test?",
         "<p>Researchers built a benchmark of roughly 10,000 queries across 25 domains, applied nine "
         "content modifications to source websites, and measured the change in visibility inside "
         "generated answers using a position-adjusted word count metric. The strategies that helped most "
         "were adding quotations from credible sources, adding statistics, adding citations, and "
         "improving fluency. Keyword stuffing did not help. Results were validated against a live "
         "generative engine, not only in the lab.</p>"),
        ("Is GEO different from AEO or LLMO?",
         "<p>Largely a labelling question. AEO usually refers to winning direct answers to specific "
         "questions; GEO covers any inclusion in generated content including longer synthesis and "
         "comparisons; LLMO and &lsquo;AI SEO&rsquo; are used interchangeably with both. Day to day the "
         "tactics overlap almost completely. Use whichever term your organisation understands and don't "
         "let the taxonomy debate consume time better spent on the work.</p>"),
        ("Do I need original research to compete?",
         "<p>Not strictly, but it's the most durable advantage available. Anyone can restate the same "
         "twelve facts; nobody else can publish your support-ticket analysis, your pricing benchmark, or "
         "your survey of 200 customers. Original data is also the thing most likely to be cited by other "
         "sites, which compounds into the entity signals that drive recommendations rather than mere citations.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Layer 3 · Quotability</p>
  <h1>Generative engine optimization (GEO)</h1>
  <p class="lede">Retrieval gets you into the candidate set. GEO decides whether the model reaches
  for your passage when it writes the sentence that carries a citation.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">Generative engine optimization is the practice of making a passage worth
    quoting once it has already been retrieved.</p>
    <p>The foundational study &mdash; <a href="https://arxiv.org/abs/2311.09735"
    rel="noopener">Aggarwal et al.</a>, presented at KDD 2024 by researchers from
    Princeton, Georgia Tech, the Allen Institute for AI and IIT Delhi &mdash; tested content changes
    across roughly 10,000 queries and found that adding quotations, statistics and citations drove the
    largest visibility gains, in the region of 30&ndash;41%.</p>
  </div>

  <h2><span class="h-num">01</span>What the research found</h2>
  <p>The study's value isn't the exact percentages, which will drift as models change. It's the
  direction: the things that increase citation are the things that make a passage <em>evidentially
  stronger</em>, not the things that make it more keyword-dense.</p>

  <div class="table-wrap">
    <table>
      <caption>Reported visibility lift by content strategy — <a href="https://arxiv.org/abs/2311.09735" rel="noopener">Aggarwal et al., KDD 2024</a></caption>
      <thead><tr><th scope="col">Strategy</th><th scope="col">Reported lift</th><th scope="col">What it means in practice</th></tr></thead>
      <tbody>
        <tr><th scope="row">Add quotations</th><td>~41%</td><td>Quote a named expert or primary document directly, with attribution</td></tr>
        <tr><th scope="row">Add statistics</th><td>~32%</td><td>Replace vague quantifiers with specific, sourced numbers</td></tr>
        <tr><th scope="row">Add citations</th><td>~30%</td><td>Link claims to the original source, not to another blog post</td></tr>
        <tr><th scope="row">Improve fluency</th><td>~28%</td><td>Clearer sentences, better transitions, less hedging</td></tr>
        <tr><th scope="row">Keyword stuffing</th><td>No gain</td><td>The tactic that defined a decade of SEO does nothing here</td></tr>
      </tbody>
    </table>
  </div>

  <p>Read the last row twice. The mechanism has changed. A generative engine is not counting term
  frequency; it is selecting passages that let it write a confident, attributable sentence.</p>

  <h2><span class="h-num">02</span>Turning that into edits</h2>

  <h3>Replace every vague quantifier</h3>
  <p>&ldquo;Many companies&rdquo; is unquotable. &ldquo;61% of the 340 B2B marketers we surveyed in
  March 2026&rdquo; is quotable, checkable and specific enough that a model can use it without
  hedging. If you don't have your own number, cite someone who does &mdash; by name, with a date and a
  link.</p>

  <h3>Quote humans, not paraphrases</h3>
  <p>A direct quotation from a named person with a stated role gives an engine an attributable
  fragment. &ldquo;According to Dr. Lena Ortiz, head of retrieval at &hellip;&rdquo; carries more weight
  than the same idea expressed anonymously.</p>

  <h3>Cite upstream</h3>
  <p>Link to the primary source: the paper, the filing, the official documentation. Citing another
  blog that cites the paper puts you a hop further from the fact and makes you the weaker candidate.</p>

  <h3>Date everything</h3>
  <p>Freshness is a genuine ranking signal in retrieval, and undated content is risky for an engine
  to assert. Put a visible <em>last reviewed</em> date on the page and mirror it in
  <code>dateModified</code>. Update it only when you actually change something.</p>

  <h2><span class="h-num">03</span>Citation is not recommendation</h2>
  <p>This distinction decides a lot of budgets. An engine may pull a fact from your page and then
  name a larger competitor as the recommended option in the same answer. Citation is a content
  outcome. Recommendation is an entity outcome &mdash; it depends on how strongly the model associates
  your brand with the category, which is built from third-party mentions, reference-grade sources
  and consistent identity data across the web.</p>
  <p>One measured example of how this goes wrong: a <a
  href="https://lilyraynyc.substack.com/p/why-calling-yourself-the-best-could" rel="noopener">2026
  analysis by Lily Ray</a> found that brands publishing
  their own &ldquo;best in category&rdquo; lists were excluded from the recommendation about 69% of
  the time. Self-interested comparison content appears to be discounted. Building the entity is the
  work that fixes this &mdash; see <a href="/get-cited-faster">get cited faster</a>.</p>

  <h2><span class="h-num">04</span>Engines disagree with each other</h2>
  <p>Do not optimize for one assistant. A <a
  href="https://otterly.ai/blog/claude-ai-citation-study/" rel="noopener">2026 Otterly.ai study</a>
  found Claude and ChatGPT citing the same domains only around 13% of the time &mdash; and barely 4%
  of identical URLs &mdash; and <a
  href="https://www.tryprofound.com/blog/chatgpt-citation-sources" rel="noopener">Profound's
  citation analysis</a> reported that ChatGPT leans heavily
  on encyclopedic sources &mdash; with Wikipedia its single most-cited domain.
  Each engine reads a different slice of the web through a different index.</p>
  <p>The practical response is not to build five strategies. It's to build one source of truth that
  is structurally excellent, and then to make sure the reference-grade surfaces engines lean on
  &mdash; Wikipedia, Wikidata, industry databases, well-moderated communities &mdash; contain accurate
  information about you.</p>

  <div class="note">
    <p><strong>Where this site's numbers come from</strong>The KDD 2024 figures are from the
    published GEO benchmark study, <a href="https://arxiv.org/abs/2311.09735"
    rel="noopener">&ldquo;GEO: Generative Engine Optimization&rdquo;</a> (Aggarwal et al.,
    arxiv.org/abs/2311.09735). The overlap, self-ranking and engine-disagreement figures come
    from 2026 vendor and industry analyses summarised in the trade press; they are directionally
    consistent across sources but have not been independently replicated. Treat percentages as
    signposts, not constants.</p>
  </div>

  <p>Next, the machine-readable layer: <a href="/structured-data-for-ai">structured data for AI</a>.</p>
</div>
""",
}

CORE = [HOME, WHAT_IS, STACK, SEO, AEO, GEO]
