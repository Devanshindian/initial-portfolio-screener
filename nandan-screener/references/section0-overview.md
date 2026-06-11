# Section 0 — Company, Industry & Founder Overview
 
This is the opening context section — it runs before Section 1, does no scoring, and triggers no rejection. Its job is to tell the reader what the business is, what world it operates in, and who runs it before any numbers appear. Keep each block tight — this is a primer, not an essay.
 
Two outputs produced here that feed downstream sections:
- **Relevant experience figure** (years) → feeds Section 2 Rule 4
- **Peer / archetype list** → feeds Section 4 benchmarking
---
 
## Block A — About the Company
 
**Goal:** in a few sentences, what does the company do and how does it make money.
 
Cover:
- **One-line description** — what the company sells and to whom (B2B / B2C / B2B2C), geography, channel (online / offline / both)
- **Major verticals / business lines** — each vertical with a one-line description and % of revenue if known. Call out the dominant one.
- **Business model** — how revenue is earned (product sales / subscription / commission / marketplace take-rate), transactional or recurring
- **Stage** — early-revenue / scaling / mature, and rough revenue band
### Source priority for Block A
 
Work through these in order — stop at the step that gives you the information:
 
1. **Pitch deck / investor presentation** (if provided) — primary source for one-line description, verticals, business model, stage, and any revenue split by vertical
2. **MIS** (`mis_[period].md`) — revenue line splits, segment breakdowns, any vertical-wise numbers not in the deck
3. **Web search** — company website, news, LinkedIn company page for anything still missing
4. **Sub-agent query** — if after steps 1–3 any of the cover points above are still unfilled, fire the following prompt as a sub-agent call:
```
You are a business analyst. Based on publicly available information, answer the following about [Company Name]:
 
1. What does the company sell, to whom (B2B/B2C/B2B2C), in which geography, and through which channel (online/offline/both)?
2. What are its major business verticals or product lines? Give a one-line description of each and estimate % of revenue if available.
3. How does it earn revenue — product sales, subscription, commission, marketplace take-rate, or other? Is it transactional or recurring?
4. What stage is it at — early-revenue, scaling, or mature? What is the approximate annual revenue?
 
Return only what you can verify. For anything uncertain, say "not found" rather than guessing.
Format: answer each question numbered, in 1–3 sentences each.
```
 
---
 
## Block B — About the Industry
 
**Goal:** frame the sector so the company's margins, growth, and risks can be judged in context.
 
Cover:
- **What the industry is and its shape** — market, size/growth if readily found (cite source), key demand drivers
- **Vintage of the business vs the industry** — how long the company has operated relative to how mature the industry is. Vintage matters: it shapes brand equity, operating experience, and how many demand/credit cycles the business has survived. Say what the vintage implies for resilience.
- **Player archetypes** — name the different *kinds* of players (e.g. large incumbents, listed majors, VC-funded challengers, unorganised/regional, vertically-integrated vs asset-light) with a one-line read on each archetype's model. This shows where the subject company sits in the competitive map and feeds Section 4 peer benchmarking.
- **Dominant competitive dynamic** — *only if it genuinely shapes the read.* Where a structural force dominates (e.g. buyers dictate terms, a flood of new entrants is compressing margins, a single supplier is a chokepoint), describe it in **plain business language, woven into the narrative**. **Never label it as a Porter's Five Forces element** — no "buyer power", "threat of substitutes", "five forces" headings or vocabulary. If nothing stands out, omit entirely.
### Source priority for Block B
 
1. **Pitch deck** — company's own market sizing, competitive landscape slides, positioning
2. **Web search** — `"[industry] India market size growth key players margins"`, named competitors, sector reports. Cite any figures with their source.
3. **Sub-agent query** — if after steps 1–2 the archetype map or competitive dynamic is still thin, fire the following prompt as a sub-agent call:
```
You are an industry analyst. Based on publicly available information, answer the following about the [industry name] industry in India:
 
1. What is the size and growth rate of this market? Cite the source.
2. What are the key demand drivers?
3. What are the main types of players competing in this space? For each type, name 1–2 examples and describe their business model in one line.
4. Is there a dominant competitive dynamic — e.g. buyers with strong pricing power, intense price-led rivalry, a key input supplier chokepoint, or a flood of new entrants? Describe it in plain business language.
5. How mature is this industry, and what does that mean for a company that has been operating in it for [N] years?
 
Return only what you can verify. Say "not found" for anything uncertain.
Format: answer each question numbered, in 2–4 sentences each.
```
 
---
 
## Block C — About the Founder(s)
 
**Goal:** a quick background check on who is running the business — credibility, relevant experience, and any flags.
 
Cover for each founder / key promoter:
- **Name and role**
- **Background** — education, prior companies/roles, and **years of relevant (same/adjacent industry) experience** — this is the input to Section 2 Rule 4 (threshold: >4 years relevant), compute it here
- **LinkedIn check** — search `"[Founder full name] LinkedIn"` — this query format reliably surfaces the correct profile. Note career history, tenure, prior exits/ventures, any prominent recognition. If the profile can't be located or is thin, say so explicitly ("LinkedIn profile not found / unverified") — never invent detail.
- **Relevance read** — one line on why their background does or doesn't fit this business
- **Flags** — anything adverse surfaced in search (prior failed ventures, litigation, controversy). Surface it factually; the deeper governance dig is Section 7 — don't double-score, just flag.
> **Accuracy guard:** founder background is reputational and easy to get wrong by conflating namesakes. If you're not confident a search result is the same person, say it's unconfirmed. Never fabricate a bio.
 
**Sources:** deck founder bios → `"[Founder name] LinkedIn"` search → company website "About / Team" → web search on each name. Always state the source and distinguish verified facts from unverified web findings.
 
---
 
## Output
 
Write to `companies/[company_name]/section0_output.md` in this format:
 
```
## Section 0 — Company, Industry & Founder Overview
 
### About the Company
[1–2 sentence description.]
 
| Vertical | What it is | % of revenue |
|----------|-----------|--------------|
| [Vertical 1] | [one line] | [X% / n.a.] |
| [Vertical 2] | [one line] | [X% / n.a.] |
 
Business model: [how it earns — transactional / recurring]. Stage: [early / scaling / mature], ~₹[X] Cr revenue.
 
### About the Industry
[1–2 sentences on the sector, size/growth with source.]
Vintage: [N years operating] vs a [mature/young/cyclical] industry → [what it implies for brand/experience/cycle resilience].
 
| Player archetype | Example(s) | Business model in one line |
|------------------|-----------|----------------------------|
| [e.g. Listed incumbents] | [names] | [one line] |
| [e.g. VC-funded D2C] | [names] | [one line] |
| [e.g. Unorganised/regional] | [—] | [one line] |
 
[Optional 1–2 sentences on dominant competitive dynamic — plain language, never labelled as a force.]
 
### About the Founder(s)
| Founder | Role | Background (source) | Relevant exp. | Relevance / flags |
|---------|------|---------------------|---------------|-------------------|
| [Name] | [role] | [education, prior roles; LinkedIn / deck / web] | [N yrs] | [fit read; any flag] |
 
Sources: [deck / LinkedIn / web — list what was used.]
```
 
Where a fact is web-researched, name the source inline. Where it couldn't be verified, say so rather than guessing.
 
