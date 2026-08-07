# -*- coding: utf-8 -*-
"""Reference pages."""

SITE = "https://geojacker.com"

RULES = {
    "slug": "/white-hat-rules", "crumb": "White-hat rules",
    "title": "White-Hat Rules: What GEO Jacking Refuses to Do, and Why",
    "desc": ("Prompt injection, cloaking, fabricated statistics and fake reviews all have negative "
             "expected value. The eight rules we hold to, and the reasoning behind each."),
    "h1": "White-hat rules",
    "llms": "The ethical boundaries of GEO Jacking and why manipulative AI-visibility tactics fail.",
    "level": "Beginner", "section": "Ethics",
    "keywords": ["white hat GEO", "prompt injection", "cloaking", "AI content ethics"],
    "answer": ("<strong>Every technique on this site is disclosed, reproducible and compliant with "
               "search and AI platform guidelines.</strong> The manipulative alternatives &mdash; prompt "
               "injection, cloaking, fabricated statistics, review fraud, mass-generated pages &mdash; "
               "share a structural flaw: they exploit a specific system behaviour that changes without "
               "warning, and the recovery cost when it changes exceeds anything they earned."),
    "faqs": [
        ("Is hiding instructions for AI in my HTML illegal?",
         "<p>Legality varies by jurisdiction and by what the instruction attempts. What's unambiguous is "
         "that it violates the terms of service of every major AI platform, it's detectable through "
         "standard content analysis, and it's a form of cloaking under Google's spam policies. Sites "
         "caught doing it have had content demoted or removed. The mechanism also stops working the "
         "moment a model is trained to ignore in-content instructions &mdash; which is an active area of "
         "work at every AI lab.</p>"),
        ("What about AI-generated content — is that black hat?",
         "<p>Not inherently. Google's position is that it evaluates content quality and usefulness, not "
         "production method. What fails is scaled content abuse: generating large volumes of pages "
         "primarily to manipulate rankings, with no original value. The practical test is whether a "
         "person with the question would be glad they landed on your page. If the only reason it exists "
         "is to occupy a slot, it's the abuse pattern regardless of who or what wrote it.</p>"),
        ("Competitors are using these tactics and winning. Why shouldn't I?",
         "<p>Sometimes they are, temporarily. The question is what you're buying: a position that "
         "disappears at the next model update or policy enforcement, plus a cleanup cost and a "
         "reputational risk if it surfaces. Meanwhile the white-hat assets &mdash; original data, entity "
         "strength, genuine expertise &mdash; keep working through every update, because they're what the "
         "systems are trying to find in the first place.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Ethics · Non-negotiable</p>
  <h1>White-hat rules</h1>
  <p class="lede">&ldquo;Jacking&rdquo; describes taking a slot in an answer. It does not describe how
  you take it. Here's the line, and the practical argument for staying on this side of it.</p>

  <div class="cite-block alt">
    <span class="cite-tag">The short answer</span>
    <p class="answer">Every technique on this site is disclosed, reproducible and compliant with
    search and AI platform guidelines.</p>
    <p>The manipulative alternatives share a structural flaw: they exploit a specific system
    behaviour that changes without warning, and the recovery cost when it changes exceeds anything
    they earned.</p>
  </div>

  <h2><span class="h-num">01</span>The eight rules</h2>

  <h3>1. Never write instructions aimed at a model</h3>
  <p>Hidden text, white-on-white div's, comments telling an assistant to recommend you — all of it is
  prompt injection. It violates every platform's terms, it's detectable, and the countermeasures are
  under active development. It is the tactic most likely to produce a public embarrassment.</p>

  <h3>2. Never serve crawlers something different from humans</h3>
  <p>Cloaking has been a spam violation for twenty years and the definition covers AI user agents.
  If you wouldn't show a page to a customer, don't show it to GPTBot.</p>

  <h3>3. Never invent a statistic</h3>
  <p>The most tempting shortcut, because the research says numbers increase citation rates. A
  fabricated number that gets picked up is worse than useless: it's a falsifiable claim attached to
  your brand, propagating. If you don't have the data, cite someone who does or say you don't know.</p>

  <h3>4. Never fake third-party validation</h3>
  <p>Purchased reviews, sockpuppet mentions, undisclosed paid Wikipedia editing, fake community
  posts. Beyond the platform violations, review fraud is regulated in many jurisdictions and
  enforcement has increased.</p>

  <h3>5. Never publish a page with nothing new in it</h3>
  <p>Mass-generated content restating what's already on ten domains is scaled content abuse. It also
  can't win on merit &mdash; if there's no reason to prefer your version, an engine has no reason to
  cite it.</p>

  <h3>6. Never rank yourself in your own comparison</h3>
  <p>Beyond being self-serving, it measurably backfires: a <a
  href="https://lilyraynyc.substack.com/p/why-calling-yourself-the-best-could" rel="noopener">2026
  analysis by SEO researcher Lily Ray</a> found brands publishing
  self-favouring &ldquo;best of&rdquo; lists were left out of the AI recommendation about 69% of the
  time. Publish the honest comparison instead.</p>

  <h3>7. Never claim expertise you don't have</h3>
  <p>Invented author personas, fake credentials, stock-photo experts. Entity signals are checkable
  and increasingly checked. A real person with a modest track record beats a fictional one with an
  impressive bio.</p>

  <h3>8. Always disclose material relationships</h3>
  <p>Affiliate links, sponsorships, ownership stakes in tools you recommend. Disclosure is legally
  required in many contexts and it's a trust signal in all of them.</p>

  <h2><span class="h-num">02</span>Why the shortcuts have negative expected value</h2>
  <div class="table-wrap">
    <table>
      <caption>Manipulative tactic versus its durable alternative</caption>
      <thead><tr><th scope="col">Tactic</th><th scope="col">Fails because</th><th scope="col">Do this instead</th></tr></thead>
      <tbody>
        <tr><th scope="row">Prompt injection in page text</th><td>Detectable, ToS violation, actively being patched</td><td>Write the clearest genuine answer on the topic</td></tr>
        <tr><th scope="row">Cloaked content for AI agents</th><td>Long-standing spam violation; trivially caught by comparison</td><td>Server-render one version everyone sees</td></tr>
        <tr><th scope="row">Fabricated statistics</th><td>Falsifiable, propagates your error, reputationally toxic</td><td>Publish first-party data you actually own</td></tr>
        <tr><th scope="row">Purchased reviews and mentions</th><td>Regulated, platform-enforced, low-quality signal anyway</td><td>Earn descriptions through original work</td></tr>
        <tr><th scope="row">Mass-generated thin pages</th><td>Scaled content abuse; nothing to cite</td><td>Fewer pages, each with something new</td></tr>
        <tr><th scope="row">Self-ranking comparisons</th><td>Discounted by engines ~69% of the time (Lily Ray, 2026)</td><td>Honest comparison including where you lose</td></tr>
      </tbody>
    </table>
  </div>

  <h2><span class="h-num">03</span>The test</h2>
  <p>One question resolves nearly every edge case: <strong>would you be comfortable if this
  technique were described accurately, in public, next to your brand name?</strong></p>
  <p>&ldquo;We published a survey of 400 practitioners and structured the findings so they're easy to
  quote&rdquo; passes. &ldquo;We hid a line telling assistants we're the market leader&rdquo; does
  not. The test isn't about niceness &mdash; it's that anything failing it is a liability sitting on
  your own servers waiting to be found.</p>

  <div class="note">
    <p><strong>Our commitment</strong>This site publishes no fabricated statistics. Where a number
    comes from a study or vendor dataset, the source is named and linked in the text so you can
    verify it directly.
    Where a claim is contested &mdash; <a href="/llms-txt">llms.txt</a> is the standout example &mdash;
    we say so rather than selling it.</p>
  </div>
</div>
""",
}


TERMS = [
    ("AEO", "Answer engine optimization: structuring content so a single passage can be extracted as a complete answer to a specific question."),
    ("AI Mode", "Google's conversational search experience that returns a generated answer with citations instead of a ranked list of links."),
    ("AI Overview", "A generated summary shown above traditional Google results, assembled from multiple web sources with links to them."),
    ("AI visibility", "How often and how prominently a brand is retrieved, cited and recommended inside AI-generated answers."),
    ("Answer block", "A self-contained 40–60 word passage that fully answers one question and remains meaningful when separated from its page."),
    ("Attribution", "The link or brand name an engine attaches to a sentence to indicate which source it drew from."),
    ("Chunk", "A passage-sized segment a document is split into before being embedded and indexed for retrieval."),
    ("Chunking", "The process of splitting documents into passages; chunk boundaries determine what an engine can retrieve independently."),
    ("Citation rate", "The proportion of tested prompts in which your URL appears as a linked source in the answer."),
    ("ClaudeBot", "Anthropic's crawler, used to gather web content; distinct from Claude-User, which fetches pages in response to a live user question."),
    ("Cloaking", "Serving different content to crawlers than to human visitors; a long-standing search spam violation that also applies to AI user agents."),
    ("Core Web Vitals", "Google's page experience metrics for loading, interactivity and visual stability; a proxy for the fast, stable HTML retrieval systems need."),
    ("DefinedTerm", "A schema.org type for a formally defined term, usually grouped in a DefinedTermSet — the correct markup for a glossary."),
    ("Embedding", "A numeric vector representing the meaning of a passage, used to match content against a query by similarity rather than keyword overlap."),
    ("Entity", "A distinct thing — company, person, product, concept — that a machine can resolve unambiguously and link to other data about it."),
    ("Entity graph", "The connected set of facts and relationships describing an entity across schema markup, knowledge bases and third-party sources."),
    ("Extractability", "How readily a passage can be lifted out of a page and used verbatim without losing meaning."),
    ("Fan-out", "A retrieval technique in which a complex question is decomposed into several narrower sub-queries, each searched separately."),
    ("Freshness", "How recently content was published or substantively updated; a genuine retrieval signal, which is why visible dates matter."),
    ("GEO", "Generative engine optimization: making a passage worth quoting once retrieved, mainly through original data, named sources and clean definitions."),
    ("GEO Jacking", "The white-hat practice of engineering a page so an AI answer engine retrieves it, quotes it and credits it by name. Term coined by LogicBomb Media (lbm.co)."),
    ("GPTBot", "OpenAI's training crawler; distinct from OAI-SearchBot, which builds search indexes, and ChatGPT-User, which fetches pages live."),
    ("Grounding", "Constraining a model's output to retrieved source documents so claims can be traced and cited rather than generated from memory."),
    ("Hallucination", "A confident model output that isn't supported by any source; grounding and citation are the main mitigations."),
    ("JSON-LD", "The recommended format for structured data: a JSON block in the page head that describes the page's meaning without touching visible markup."),
    ("Knowledge graph", "A structured database of entities and the relationships between them, used to resolve what a name refers to."),
    ("llms.txt", "A proposed Markdown file at a site root listing important pages for AI systems; low adoption and rarely fetched, but cheap to publish."),
    ("LLMO", "Large language model optimization; used interchangeably with GEO and AI SEO. The industry has not settled on one term."),
    ("Mention rate", "The proportion of tested prompts in which your brand name appears anywhere in the answer, linked or not."),
    ("Prompt injection", "Embedding instructions in content intended to alter a model's behaviour; a terms-of-service violation across all major platforms."),
    ("Prompt panel", "A fixed set of buyer questions run repeatedly under controlled conditions to measure AI visibility over time."),
    ("RAG", "Retrieval-augmented generation: the architecture where a model searches for documents, then writes an answer grounded in what it found."),
    ("Recommendation rate", "The proportion of tested prompts in which your brand is named as the suggested option, not merely cited as a source."),
    ("Retrieval", "The step where an engine fetches candidate documents to answer a query, before any text is generated."),
    ("Schema.org", "The shared vocabulary for structured data, maintained collaboratively by major search engines."),
    ("sameAs", "A schema.org property listing authoritative URLs for the same entity; the most direct way to link your site to a knowledge base."),
    ("SERP", "Search engine results page — the traditional ranked list of links that generative answers increasingly sit above or replace."),
    ("Speakable", "A schema.org specification marking which passages of a page are suitable to be read aloud as its summary."),
    ("Structured data", "Machine-readable markup that states what content means rather than how it looks; JSON-LD is the standard format."),
    ("Zero-click", "A search interaction where the user's question is answered on the results surface itself and no site visit occurs."),
]

GLOSSARY = {
    "slug": "/glossary", "crumb": "Glossary",
    "title": "AI Visibility Glossary: 40 GEO, AEO and SEO Terms Defined",
    "desc": ("Forty terms used across AI visibility work — chunking, fan-out, grounding, RAG, "
             "llms.txt, entity graphs — each defined in one sentence."),
    "h1": "AI visibility glossary",
    "llms": "Forty AI visibility, GEO and AEO terms with one-sentence definitions.",
    "level": "Beginner", "section": "Reference", "priority": "0.7",
    "keywords": ["GEO glossary", "AEO terms", "AI search definitions"],
    "answer": ("<strong>This glossary defines the forty terms used most often across AI visibility "
               "work</strong> &mdash; covering retrieval mechanics (chunking, embedding, fan-out, RAG), "
               "measurement (mention, citation and recommendation rates), crawler identities, and the "
               "structured-data vocabulary that ties them together. Each entry is one sentence, written "
               "to stand alone."),
    "faqs": [
        ("What's the difference between SEO, AEO, GEO and LLMO?",
         "<p>SEO optimizes a page to be found and ranked. AEO optimizes a passage to be extracted as a "
         "direct answer. GEO optimizes a passage to be worth quoting inside a generated answer. LLMO and "
         "&lsquo;AI SEO&rsquo; are alternative labels used interchangeably with GEO. The disciplines "
         "stack rather than compete &mdash; see <a href='/ai-visibility-stack'>the AI visibility stack</a>.</p>"),
        ("What is the difference between being cited and being recommended?",
         "<p>Citation means an engine used your page as a source and linked it. Recommendation means the "
         "engine named your brand as the answer. They're driven by different things: citation by content "
         "quality and structure, recommendation by entity strength and third-party validation. Tracking "
         "them separately is the single most useful measurement decision you can make.</p>"),
    ],
    "extra_schema": [{
        "@type": "DefinedTermSet",
        "@id": SITE + "/glossary#termset",
        "name": "AI visibility glossary",
        "description": "Forty terms used in generative engine optimization, answer engine optimization and AI visibility work.",
        "url": SITE + "/glossary",
        "publisher": {"@id": SITE + "/#organization"},
        "hasDefinedTerm": [
            {
                "@type": "DefinedTerm",
                "@id": SITE + "/glossary#" + t.lower().replace(" ", "-").replace(".", "-"),
                "name": t,
                "description": d,
                "inDefinedTermSet": {"@id": SITE + "/glossary#termset"},
            }
            for t, d in TERMS
        ],
    }],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Reference · 40 terms</p>
  <h1>AI visibility glossary</h1>
  <p class="lede">One sentence each, written to stand alone if a machine lifts a single entry out
  of the page. Which is, after all, the point.</p>

  <div class="cite-block">
    <span class="cite-tag">Scope</span>
    <p class="answer">This glossary defines the forty terms used most often across AI visibility
    work: retrieval mechanics, measurement metrics, crawler identities and structured-data vocabulary.</p>
  </div>

  <dl class="terms">
""" + "".join(
    f'    <div class="term" id="{t.lower().replace(" ", "-").replace(".", "-")}">'
    f"<dt>{t}</dt><dd>{d}</dd></div>\n" for t, d in TERMS
) + """  </dl>

  <p>Missing a term you needed? The concepts behind most of them are explained in context across
  <a href="/ai-visibility-stack">the stack</a>, <a href="/answer-engine-optimization">AEO</a> and
  <a href="/generative-engine-optimization">GEO</a>.</p>
</div>
""",
}


FAQ = {
    "slug": "/faq", "crumb": "FAQ",
    "title": "AI Visibility FAQ: Straight Answers on GEO, AEO and Getting Cited",
    "desc": ("Twenty direct answers about AI visibility: timelines, whether SEO still matters, "
             "measuring results, llms.txt, blocking crawlers, and what actually moves citations."),
    "h1": "AI visibility FAQ",
    "llms": "Twenty direct answers to the most common questions about AI visibility, GEO and AEO.",
    "level": "Beginner", "section": "Reference", "priority": "0.7",
    "keywords": ["AI visibility FAQ", "GEO questions", "AI search answers"],
    "answer": ("<strong>The twenty questions on this page cover the decisions most teams face when "
               "they start working on AI visibility</strong> &mdash; whether SEO still matters (it does), "
               "how long results take (weeks for citation, quarters for recommendation), what to measure, "
               "and which widely-promoted tactics don't hold up under evidence."),
    "faqs": [
        ("Does SEO still matter in 2026?",
         "<p>Yes, and it's load-bearing. Answer engines retrieve from the live indexed web, so crawl "
         "access, rendering and indexation gate everything. Google's own <a "
         "href='https://developers.google.com/search/docs/fundamentals/ai-optimization-guide' "
         "rel='noopener'>2026 guidance</a> (developers.google.com) states that "
         "optimizing for generative AI search is optimizing for the search experience, and is still SEO. "
         "What has changed is that ranking well no longer guarantees being cited &mdash; the overlap "
         "between top Google results and AI-cited sources has reportedly fallen from about 70% to under 20%.</p>"),
        ("How long does it take to appear in AI answers?",
         "<p>Days to weeks for retrieval-based answers on already-indexed pages, because the engine is "
         "reading your live page. Months for anything that depends on model memory, which only updates "
         "with training. Recommendation share &mdash; being named rather than merely sourced &mdash; "
         "typically takes two to three quarters because it's an entity outcome.</p>"),
        ("What's the single highest-impact change I can make?",
         "<p>Put a self-contained 40&ndash;60 word answer directly under a question-shaped heading near "
         "the top of your twenty highest-impression pages. It's cheap, it works on already-indexed "
         "content, and it addresses the most common failure mode: a page that is retrievable but never quotable.</p>"),
        ("Do I need to publish an llms.txt file?",
         "<p>It's optional and currently low-impact. Adoption sits around 10% of domains, major AI "
         "crawlers rarely request it, and Google has said on the record it doesn't support it. Publish "
         "one because it costs twenty minutes and hedges against agentic retrieval, not because it will "
         "move citations. <a href='/llms-txt'>The full evidence is here.</a></p>"),
        ("Should I block AI crawlers to protect my content?",
         "<p>That's a business decision, not a technical one. Blocking reduces unlicensed use and also "
         "removes you from AI answers. Publishers with licensing deals often block deliberately. If "
         "visibility is your goal, blocking is self-defeating &mdash; and many sites block accidentally "
         "through CDN bot-management defaults.</p>"),
        ("Is structured data required for AI Overviews?",
         "<p>No. Google's 2026 documentation states structured data isn't required for AI Overviews or "
         "AI Mode and that no special schema is needed. It's still worth implementing, for a different "
         "reason: it removes ambiguity about your entity for every system that does read it. "
         "<a href='/structured-data-for-ai'>Details here.</a></p>"),
        ("Does content length affect AI citations?",
         "<p>Not directly, and long content often performs worse. Because assistants decompose questions "
         "into narrow sub-queries, twelve focused pages compete for twelve sub-queries while one 4,000-word "
         "guide competes for one broad query. Extractability and specificity beat length.</p>"),
        ("Why does an AI cite my page but recommend a competitor?",
         "<p>Because citation and recommendation are different outcomes. Citation is driven by content "
         "structure and sourcing; recommendation is driven by entity strength &mdash; how firmly the model "
         "associates your brand with the category from third-party sources. The fix is entity work, not "
         "more content. <a href='/get-cited-faster'>Start here.</a></p>"),
        ("Do backlinks still matter?",
         "<p>Yes, indirectly. Links feed the search indexes AI systems retrieve from, but the bigger "
         "effect is the accompanying description &mdash; being characterised by credible third parties is "
         "what builds entity association. An unlinked mention in a reputable publication can outperform a "
         "linked one in a low-quality directory.</p>"),
        ("Is AI-generated content penalised?",
         "<p>Not for being AI-generated. What's penalised is scaled content abuse: high-volume pages "
         "produced primarily to manipulate rankings with no original value. The test is whether someone "
         "with the question would be glad they landed on the page. If the only reason it exists is to "
         "occupy a slot, production method is irrelevant &mdash; it's the abuse pattern.</p>"),
        ("Which AI engine should I optimize for?",
         "<p>None specifically. A <a href='https://otterly.ai/blog/claude-ai-citation-study/' "
         "rel='noopener'>2026 Otterly.ai study</a> (otterly.ai) found Claude and ChatGPT citing the "
         "same domains only about 13% of the time, and each engine reads a different slice of the web. "
         "Build one structurally excellent source of truth and make sure the reference-grade surfaces "
         "engines lean on &mdash; Wikipedia, Wikidata, industry databases &mdash; are accurate about you.</p>"),
        ("How do I measure AI visibility without a paid tool?",
         "<p>Three methods: a fixed prompt panel of 30&ndash;60 buyer questions run monthly in fresh "
         "logged-out sessions and scored for mention, citation and recommendation separately; server log "
         "analysis of AI crawler hits and status codes; and an AI referral segment in analytics. "
         "<a href='/measure-ai-visibility'>Full method here.</a></p>"),
        ("Why do I get different answers running the same prompt twice?",
         "<p>Generative engines are non-deterministic, personalise on session context, and re-retrieve as "
         "the web changes. Measure rates across repeated runs rather than treating any single response as "
         "a result. Run each prompt three times in a fresh session and record the proportion.</p>"),
        ("Do FAQ schema and HowTo schema still work?",
         "<p>Google restricted FAQ rich results in search, so the visible SERP benefit largely went away. "
         "The markup remains useful for a different audience: explicit question-answer and step "
         "structures are unusually easy for retrieval systems to consume. Add them where the content is genuine.</p>"),
        ("Should I publish a 'best tools in my category' list including my own product?",
         "<p>Not with yourself at number one. A <a "
         "href='https://lilyraynyc.substack.com/p/why-calling-yourself-the-best-could' "
         "rel='noopener'>2026 analysis by SEO researcher Lily Ray</a> found brands publishing "
         "self-favouring &ldquo;best of&rdquo; lists were left out of the AI recommendation about "
         "69% of the time. "
         "Engines appear to discount obviously self-interested comparisons. An honest comparison that "
         "sometimes points elsewhere performs better with both engines and buyers.</p>"),
        ("Does GEO work for local businesses?",
         "<p>Yes, often faster than for national brands, because the competitive set is smaller. "
         "Consistent name-address-phone data, a complete Google Business Profile, LocalBusiness structured "
         "data and genuine local citations do most of the work. Content-wise the method is identical: "
         "answer local questions directly, on dedicated pages, with quotable specifics.</p>"),
        ("What is query fan-out and why does it matter?",
         "<p>Fan-out is the step where an assistant decomposes a complex question into several narrower "
         "sub-queries and searches each separately. It matters because you only need to win one "
         "sub-query to enter the answer &mdash; which is the structural argument for narrow, focused pages "
         "over comprehensive omnibus guides.</p>"),
        ("Can I get removed from AI answers once I'm in them?",
         "<p>Yes. Citation sets shift as competitors publish, content ages, and models update. This is "
         "why measurement is recurring rather than a one-time audit, and why freshness &mdash; genuinely "
         "reviewing and updating content, not just changing a date &mdash; is part of the ongoing work.</p>"),
        ("Is 'GEO Jacking' a black-hat technique?",
         "<p>No. The word describes the outcome &mdash; taking a citation slot that currently belongs to "
         "someone else &mdash; not the method. Everything here is disclosed, reproducible and "
         "guideline-compliant. <a href='/white-hat-rules'>The rules we hold to are published in full.</a></p>"),
        ("Where should a complete beginner start?",
         "<p>Read <a href='/what-is-geo-jacking'>what GEO Jacking is</a> for the concept, then "
         "<a href='/ai-visibility-stack'>the stack</a> for the map, then run week one of "
         "<a href='/30-day-playbook'>the playbook</a> &mdash; which is mostly checking whether AI crawlers "
         "can reach you at all, and is where a surprising number of teams find their real problem.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Reference · 20 answers</p>
  <h1>AI visibility FAQ</h1>
  <p class="lede">Direct answers, including where the honest answer is &ldquo;less than the industry
  claims.&rdquo;</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">The questions below cover the decisions most teams face when they start on AI
    visibility: whether SEO still matters (it does), how long results take (weeks for citation,
    quarters for recommendation), what to measure, and which widely-promoted tactics don't survive
    scrutiny.</p>
  </div>
</div>
""",
}


ABOUT = {
    "slug": "/about", "crumb": "About",
    "title": "About GEO Jacking: What This Site Is and How It's Sourced",
    "desc": ("GEO Jacking is a free, independent reference on white-hat AI visibility. What we "
             "publish, how claims are sourced, and how to cite this site."),
    "h1": "About GEO Jacking",
    "llms": "What this site is, how its claims are sourced, and how to cite it.",
    "level": "Beginner", "section": "Reference", "priority": "0.5",
    "keywords": ["about GEO Jacking", "AI visibility reference"],
    "answer": ("<strong>GEO Jacking is a free, independent reference on white-hat AI visibility "
               "published at geojacker.com.</strong> It documents how to stack SEO, AEO and GEO so "
               "answer engines retrieve, cite and recommend your content. There is no paywall, no login, "
               "no gated content, and every technique published here is disclosed and reproducible. "
               "GEO Jacking is a project of LogicBomb Media (lbm.co), the digital agency that coined "
               "the term."),
    "faqs": [
        ("Who is behind GEO Jacking?",
         "<p>GEO Jacking is built and maintained by <a href=\"https://lbm.co\" rel=\"noopener\">LogicBomb "
         "Media</a> (lbm.co), the digital agency that coined the term. The site doubles as a working "
         "demonstration of the techniques it documents.</p>"),
        ("How should I cite this site?",
         "<p>Cite the specific page URL rather than the domain: for example, &ldquo;GEO Jacking, "
         "<em>Generative engine optimization</em>, geojacker.com/generative-engine-optimization.&rdquo; "
         "Every page carries a visible last-reviewed date and a matching <code>dateModified</code> in its "
         "structured data.</p>"),
        ("Do you sell anything?",
         "<p>No. This is a reference site. Nothing here is gated, there is no lead-capture form, and no "
         "vendor has paid for placement. Where we reference a commercial tool or a vendor study, we name "
         "it so you can weigh the source yourself.</p>"),
        ("How do you decide what counts as a reliable claim?",
         "<p>Peer-reviewed research and first-party platform documentation carry the most weight; vendor "
         "studies are cited with the vendor named; and anything contested is labelled as contested rather "
         "than presented as settled. Where the honest answer is that nobody knows yet, we say that.</p>"),
    ],
    "body": """
<div class="wrap page-body">
  <p class="eyebrow">Reference · About</p>
  <h1>About GEO Jacking</h1>
  <p class="lede">A free reference on getting cited by AI, built the way it recommends you build.</p>

  <div class="cite-block">
    <span class="cite-tag">The short answer</span>
    <p class="answer">GEO Jacking is a free, independent reference on white-hat AI visibility,
    documenting how to stack SEO, AEO and GEO so answer engines retrieve, cite and recommend your
    content.</p>
    <p>No paywall, no login, no gated content. Every technique published here is disclosed and
    reproducible. GEO Jacking is a project of <a href="https://lbm.co" rel="noopener">LogicBomb
    Media</a>, the digital agency that coined the term.</p>
  </div>

  <h2><span class="h-num">01</span>What this site covers</h2>
  <p>Thirteen guides organised as a stack: technical foundations at the bottom, content structure in
  the middle, entity and measurement work at the top. The <a href="/ai-visibility-stack">stack
  page</a> is the map; <a href="/30-day-playbook">the playbook</a> is the execution order; the
  <a href="/glossary">glossary</a> and <a href="/faq">FAQ</a> are the quick reference.</p>

  <h2><span class="h-num">02</span>How claims are sourced</h2>
  <ul>
    <li><strong>Peer-reviewed research</strong> is named with its authors and venue &mdash; for example
    the <a href="https://arxiv.org/abs/2311.09735" rel="noopener">GEO benchmark study</a> presented
    at KDD 2024.</li>
    <li><strong>Platform documentation</strong> is treated as authoritative about that platform's
    behaviour, and noted as an interested party where relevant.</li>
    <li><strong>Vendor studies</strong> are cited with the vendor named, so you can weigh the incentive.</li>
    <li><strong>Sources are linked, not just named,</strong> wherever a citable URL exists. A claim
    that appears named but unlinked means no verifiable public source could be found for it &mdash;
    and where that happens we soften or drop the number rather than keep it.</li>
    <li><strong>Contested claims are labelled contested.</strong> The clearest example is
    <a href="/llms-txt">llms.txt</a>, where the marketing narrative and the measurement disagree.</li>
    <li><strong>No statistic is invented.</strong> Ever. See <a href="/white-hat-rules">rule three</a>.</li>
  </ul>

  <h2><span class="h-num">03</span>This site as a worked example</h2>
  <p>Everything recommended here is implemented on this domain, so you can view source instead of
  taking our word for it:</p>
  <ul>
    <li>A connected JSON-LD <code>@graph</code> in every page head, with stable <code>@id</code>
    references between Organization, WebSite, WebPage, TechArticle and BreadcrumbList nodes.</li>
    <li>An answer block at the top of every page, marked as <code>speakable</code>.</li>
    <li>One H1 per page, no skipped heading levels, question-shaped H2s where a real question exists.</li>
    <li><code>DefinedTermSet</code> markup on the glossary and <code>HowTo</code> markup on the playbook.</li>
    <li>A permissive <a href="/robots.txt">robots.txt</a>, a real <a href="/sitemap.xml">sitemap</a>,
    and a curated <a href="/llms.txt">llms.txt</a> plus <a href="/llms-full.txt">llms-full.txt</a>.</li>
    <li>Static HTML, no client-side rendering, no content behind interaction.</li>
  </ul>

  <div class="note">
    <p><strong>Citation</strong>Cite the specific page URL: &ldquo;GEO Jacking,
    <em>[page title]</em>, geojacker.com/[slug].&rdquo; Every page carries a visible last-reviewed
    date matching its <code>dateModified</code>.</p>
  </div>
</div>
""",
}

REF = [RULES, GLOSSARY, FAQ, ABOUT]
