# Section 4 — P&L Analysis

Profitability metrics tell you what the business earns and where the margin is won or lost. This section is MIS-led for the contribution-margin detail, but the full waterfall is built for every available year.

---

## Sources

- **Audited years** — `companies/[company_name]/Financial_Appraisal_[company_name].xlsx`, sheet `Info and Adjustments`
- **MIS year** — `companies/[company_name]/mis_[period].md`

---

## Step 1 — Build the Margin Waterfall (all available years)

Build one combined table for all available years (audited years + MIS period). Each year gets two columns — **₹ Cr** and **% of revenue** — side by side. CM1 and CM2 = "–" for audited-only years unless the MIS contains historical breakdowns for those years.

| Level | FY__ ₹ Cr | FY__ % | FY__ ₹ Cr | FY__ % | MIS [period] ₹ Cr | MIS [period] % |
|---|---|---|---|---|---|---|
| Revenue | | | | | | |
| COGS | | | | | | |
| **Gross Margin** | | | | | | |
| CM1 costs | | | | | – | – |
| **CM1** | – | – | – | – | | |
| CM2 costs | | | | | – | – |
| **CM2** | – | – | – | – | | |
| Fixed costs | | | | | | |
| **EBITDA** | | | | | | |
| D&A | | | | | | |
| **EBIT** | | | | | | |
| Finance costs | | | | | | |
| **PBT** | | | | | | |
| Tax | | | | | | |
| **PAT** | | | | | | |

> Add as many year-pairs (₹ Cr + %) as there are available periods. CM1/CM2 = "–" on audited-only years unless MIS has historical line-item breakdowns for those years.

---

## Step 2 — How to Populate Each Year

### Audited years — pull from `Financial_Appraisal_[company_name].xlsx`

All rows reference sheet `Info and Adjustments`:

| Level | Row(s) |
|---|---|
| Revenue | Row 11 (Revenue from Operations) — exclude Other Income (Row 14) |
| COGS | Row 18 + Row 19 [+ Row 20 if manufacturing] |
| Gross Margin | Revenue − COGS |
| CM1, CM2 | "–" (not in template) — see MIS section below |
| EBITDA | Row 29 (PBT) + Row 23 (Finance) + Row 24 (Depreciation) |
| EBIT | Row 29 + Row 23 |
| PBT | Row 29 |
| Tax | Row 30 + Row 31 |
| PAT | Row 38 |

### MIS year — pull from `mis_[period].md`

Every company's MIS lists costs differently — read it line by line and drop each line into the right waterfall level using the classification below. The end goal is to produce the same waterfall structure as above, now with CM1 and CM2 populated.

**Cost classification:**

| Layer | What goes here |
|---|---|
| **CM1** (variable operating, scales per order) | Logistics / shipping / freight, payment-gateway / processing fees, packing / fulfilment consumables, platform / marketplace fees, sales commission, channel commission |
| **CM2** (CAC + other variable) | Advertising & marketing, performance spend, marketing retention, any per-sale variable not already in CM1 |
| **Fixed** (sits below CM2, in EBITDA) | Rent / lease, salaries / employee benefits, electricity / utilities, office & store / admin, professional / legal, rates & taxes / licenses / subscriptions, travel, photoshoot / display & VM, repairs, insurance, depreciation, finance costs |

**Ambiguous lines** (e.g. "other direct expenses"): assign to the most appropriate layer, state your treatment, and note whether moving it would flip a sign. If it is < ~1–2% of revenue it cannot change the read — say so.

> If the MIS contains historical year breakdowns (prior FYs broken down by cost line), use those to populate CM1/CM2 for those years as well — do not leave them as "–" if the data exists.

---

## Step 3 — Trend Analysis

### Annual trend table

Build this table first. It extends the waterfall into a trend read — margins only (% of revenue), one trend one-liner per row, plus the key cost lines:

| Metric | FY__ % | FY__ % | MIS [period] % | Trend |
|---|---|---|---|---|
| Revenue YoY growth % | — | | | e.g. "Accelerating — 18% → 34%" |
| Gross Margin % | | | | e.g. "Expanding from 38% → 42%" |
| CM1 % | – | – | | e.g. "CM1 at 28% in MIS period" |
| CM2 % | – | – | | e.g. "CM2 positive at 18% — unit economics healthy" |
| EBITDA % | | | | e.g. "Improving from −4% → +6%" |
| EBIT % | | | | |
| PBT % | | | | |
| PAT % | | | | |
| Employee cost % | | | | e.g. "Declining 24% → 19% — scale absorbing headcount" |
| Finance cost % | | | | e.g. "Rising 3% → 6% — watch for debt trap" |
| Marketing % | | | | e.g. "Stable at ~12% — CAC efficiency holding" |
| Rent / fixed overhead % | | | | e.g. "Declining 8% → 5% — operating leverage visible" |

### Quarterly trend table (only if MIS is monthly or quarterly)

| Metric | Q1 % | Q2 % | Q3 % | Q4 % | Trend |
|---|---|---|---|---|---|
| Revenue (₹ Cr) | | | | | e.g. "Accelerating through year, Q4 strongest" |
| Gross Margin % | | | | | |
| CM1 % | | | | | |
| CM2 % | | | | | |
| EBITDA % | | | | | |
| Employee cost % | | | | | |
| Finance cost % | | | | | |
| Marketing % | | | | | |
| Rent / fixed overhead % | | | | | |

If the MIS is annual only, skip this table and note: "Quarterly breakdown not available — MIS is annual."

### Key cost commentary

After building both tables, write 3–5 lines calling out the direction and implication of each key cost line — use the trend one-liners from the tables as the basis. Flag any line moving the wrong way.

**One-off / non-recurring costs:** scan the MIS for one-time items (settlements, write-offs, one-off legal/consulting, founder bonuses, prior-period adjustments). Strip them out to see the underlying trend. Report a normalised (ex-one-off) EBITDA/PBT where it changes the read. Watch a fixed line that jumps once and stays elevated — that is a step-change, not a one-off.

**Green signals:** revenue growing with margins expanding (operating leverage working); fixed costs declining as % of revenue (scalable model).

**Red flags:** revenue up but margins contracting (pricing pressure / cost inflation); finance cost growing faster than revenue (debt trap); EBITDA % negative and worsening; material share of PBT from Other Income (profit propped up by non-operating income).

---

## Step 4 — Industry Benchmarking

Web-search the sector and name real peers. Build a comparison table against the top company, a couple of listed peers, and the industry average. Include each company's revenue so the comparison is size-aware:

| Company | Revenue (₹ Cr) | Gross Margin % | EBITDA % |
|---|---|---|---|
| [Subject company] | | | |
| [Peer 1] | | | |
| [Peer 2] | | | |
| Industry average | | | |

| Variance vs industry | Action |
|---|---|
| > 5% below industry average | Flag and explain — cost structure, scale disadvantage, or business-model difference |
| > 10% below industry average | 🔴 Red flag |
| Above industry average | Positive signal — verify sustainability |

Use the peer/archetype list already built in `companies/[company_name]/section0_output.md` (Section 0 Block B) — do not re-research from scratch.

---

## Output

Write to `companies/[company_name]/section4_output.md` using this exact template:

---

```
## Section 4 — P&L Analysis

### A. Margin Waterfall

| Level        | FY__ ₹ Cr | FY__ % | FY__ ₹ Cr | FY__ % | MIS [period] ₹ Cr | MIS [period] % | Trend |
|---|---|---|---|---|---|---|---|
| Revenue      |   |   |   |   |   |   | e.g. "Growing 34% YoY; Q4 run-rate strongest (see quarterly trend)" |
| Gross Margin |   |   |   |   |   |   | e.g. "Expanding 38% → 42%; Q3/Q4 margins stronger than H1 (see quarterly trend)" |
| CM1          | – | – | – | – |   |   | e.g. "28% in MIS period — variable ops well controlled" |
| CM2          | – | – | – | – |   |   | e.g. "18% — unit economics positive; Q4 CM2 improving (see quarterly trend)" |
| EBITDA       |   |   |   |   |   |   | e.g. "Turning positive FY25; Q4 EBITDA% strongest quarter (see quarterly trend)" |
| PAT          |   |   |   |   |   |   | e.g. "Still loss-making; narrowing" |

### B. Key Findings

[4–5 lines. Cover: (1) unit economics — is CM2 positive and stable? (2) margin trajectory — expanding or contracting and why? (3) operating leverage — are fixed costs declining as % of revenue as the business scales? (4) any red flag — finance cost creeping up, Other Income propping up PBT, one-off distorting the read. Keep it sharp — this is the analyst's interpretation, not a data dump.]

### C. Industry Benchmark

| Company           | Revenue (₹ Cr) | Gross Margin % | EBITDA % |
|---|---|---|---|
| [Subject company] |                |                |          |
| [Peer 1]          |                |                |          |
| [Peer 2]          |                |                |          |
| Industry average  |                |                |          |

[One line on the variance — is it explained by scale, business model, or a structural disadvantage?]

---

### Supporting Data — Trend Tables
*(detailed; for reference)*

**Annual trend**

| Metric                     | FY__ % | FY__ % | MIS [period] % | Trend |
|---|---|---|---|---|
| Revenue YoY growth %       |        |        |                |       |
| Gross Margin %             |        |        |                |       |
| CM1 %                      |   –    |   –    |                |       |
| CM2 %                      |   –    |   –    |                |       |
| EBITDA %                   |        |        |                |       |
| EBIT %                     |        |        |                |       |
| PBT %                      |        |        |                |       |
| PAT %                      |        |        |                |       |
| Employee cost %            |        |        |                |       |
| Finance cost %             |        |        |                |       |
| Marketing %                |        |        |                |       |
| Rent / fixed overhead %    |        |        |                |       |

**Quarterly trend** *(only if MIS is monthly or quarterly; skip and note if annual)*

| Metric              | Q1 % | Q2 % | Q3 % | Q4 % | Trend |
|---|---|---|---|---|---|
| Revenue (₹ Cr)      |      |      |      |      |       |
| Gross Margin %      |      |      |      |      |       |
| CM1 %               |      |      |      |      |       |
| CM2 %               |      |      |      |      |       |
| EBITDA %            |      |      |      |      |       |
| Employee cost %     |      |      |      |      |       |
| Finance cost %      |      |      |      |      |       |
| Marketing %         |      |      |      |      |       |
| Rent / overhead %   |      |      |      |      |       |
```

---