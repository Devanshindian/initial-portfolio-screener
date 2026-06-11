# Section 1 — Preliminary Rejection Criteria

Apply all 3 rules. If **2 or more are triggered**, issue a rejection notice — but **continue the full analysis through all sections regardless**. The rejection is a hard stop on the deal verdict, not on the analysis.

---

## Rule 1 — Deep Technology

**Triggered if:** The company's core product or primary revenue source is deep technology — meaning the technology is research/IP-stage, unproven at commercial scale, or revenue is unpredictable because the product is not yet established in the market.

### Hard Trigger Conditions (any one is sufficient)
- Revenue is nil or very low (annualised < ~INR 5 Cr) due to being pre-commercial or early-stage
- Core product is IP/patent-stage and not yet generating predictable commercial revenue
- Primary moat is unproven proprietary technology (i.e. the tech itself is the product, not what it enables)
- Revenue is fundamentally unpredictable — depends on R&D outcomes, grants, or milestone payments

### Sector Keywords — Elevated Scrutiny
If the company operates in any of these sectors, verify carefully against the Hard Trigger Conditions above:

| Sector | Notes |
|--------|-------|
| Biotechnology / Life Sciences | Gene editing, cell therapy, regenerative medicine, genomics |
| Pharma R&D | Early-stage drug discovery, clinical-stage companies |
| Defense Technology | Hardware systems, weapons systems, advanced sensors |
| Aerospace / Space Technology | Satellite design, launch vehicles, space infrastructure |
| Quantum Computing | Any commercial quantum hardware or software plays |
| Semiconductors | Chip design/fab at R&D stage (fabless SaaS model may be fine) |
| Advanced Materials | Nanotechnology, composites, novel energy materials |
| Neuro-technology | Brain-computer interfaces, neural implants |
| Clean Energy (early stage) | Fusion energy, novel battery chemistries at R&D stage |
| Advanced Robotics (hardware) | Hardware robotics at pre-revenue or very low revenue stage |
| Agri-biotech / Precision Agriculture | Early-stage biotech applied to agriculture |
| Next-gen Communications | Terahertz, advanced radio, experimental networking |

### Not Deep Tech — Do Not Trigger Rule 1
- Tech-enabled services: AI/ML-powered platforms (logistics, lending, HR, etc.)
- SaaS / fintech / edtech regardless of how sophisticated the tech is
- Companies that *use* proprietary technology but *sell* a product/service with predictable recurring revenue
- Manufacturing companies using advanced but proven technology

### How to Assess
1. Read the pitch deck (from the company folder) — what is the primary product being sold? If no pitch deck, do a web search on the company.
2. Check whether revenue is contract-based/recurring, or milestone/grant-based.
3. If the sector appears in the keyword list, verify against Hard Trigger Conditions.

---

## Rule 2 — Government Revenue Dependency

**Triggered if:** More than **30% of most recent year's revenue** comes from government or public sector clients.

### "Government" includes
- Central and State Government ministries and departments
- Public Sector Undertakings (PSUs) — e.g. ONGC, NTPC, SAIL, HAL
- Public Sector Banks (PSBs) — e.g. SBI, Bank of Baroda
- Government-owned or majority government-controlled entities at any level
- Municipal corporations and local government bodies

### How to Assess

All documents referenced below are in the company folder provided by the user.

1. **MIS file** (`companies/[company_name]/mis_[period].md`) — look for a customer-wise or segment-wise revenue breakdown. If found: **(Total revenue from govt/PSU clients) ÷ (Total revenue) × 100**.
2. **Pitch deck / business description** (from the company folder) — check for customer names or revenue mix disclosure.
3. **Debtor ageing / AR ageing report** (from the company folder, may be labelled as debtor schedule, client-wise outstanding, or AR aging) — use as a proxy: **(Total outstanding from govt/PSU clients) ÷ (Total debtors) × 100**.
4. If none of the above yields a breakdown: flag as **"Unable to verify Rule 2 — customer revenue breakdown not available"** and note what was checked.

> Whenever client names are visible from any source, do a quick web search on any unfamiliar names to confirm whether they are government-linked or private — it is often not obvious from the name alone.

### Edge Cases
- Sub-contractor arrangements: if the company serves government-linked entities indirectly, include that revenue if it can be identified (typically requires a web search on the end-client).
- Government revenue < 30% but growing rapidly toward the threshold: flag as a watch item but do not trigger the rule.

---

## Rule 3 — Negative Unit Economics

**Triggered if:** The company loses money on each unit/transaction before fixed costs — i.e. **CM2 ≤ 0** — or it is selling below COGS (**CM1 < 0**). A business that cannot cover its directly-variable costs per sale cannot fix that by scaling; debt is the wrong instrument.

### Margin Definitions

```
Revenue (net, operations only — exclude Other Income)
− COGS / cost of goods / purchases
────────────────────────────────────────────────────
= Gross Margin

− CM1 costs (variable, scales per order)
────────────────────────────────────────────────────
= CM1

− CM2 costs (CAC + other variable)
────────────────────────────────────────────────────
= CM2                    ← the trigger line

− Fixed costs            ← not relevant for Rule 3
────────────────────────────────────────────────────
= EBITDA
```

### Cost Classification

| Layer | What goes here |
|-------|---------------|
| **CM1 costs** | Logistics / shipping / freight / delivery, payment-gateway / checkout / processing fees, packing / fulfilment consumables, platform / marketplace fees, sales commission, channel / affiliate commission |
| **CM2 costs** | Advertising & marketing, performance spend, marketing retention, any per-sale variable not already in CM1 |
| **Fixed (below CM2 — exclude from Rule 3)** | Rent / lease, salaries / employee benefits, electricity / utilities, office & store running / admin, professional / legal / consulting, rates & taxes / licenses / subscriptions, travel, photoshoot / display & VM, repairs, insurance, depreciation, finance costs |

For any line that is genuinely ambiguous: state your treatment, flag it, and note whether including it would flip the sign. If the ambiguous item is < ~1–2% of revenue it cannot change the verdict — say so explicitly.

### Data Source and Period
- **MIS preferred** — use `companies/[company_name]/mis_[period].md`. Audited financials are the fallback.
- Exclude Other Income from Revenue — it is not operating revenue.
- If the MIS covers a partial year, annualise and state the basis.

### Assessment — Trend Awareness
- Always compute full-period CM2 first.
- If the MIS is monthly: also compute CM2 by quarter and read the trajectory. If the most recent quarter's CM2 has turned negative while the full period is still positive, raise a **deterioration flag** (seasonal businesses: note one soft quarter rather than over-reading it).
- If only annual MIS is available: assess on annual CM2 alone; state this limitation.

### Trigger Logic

| Condition | Action |
|-----------|--------|
| CM2 > 0 (full period) | Rule 3 NOT triggered |
| CM2 ≤ 0 (full period) | **Rule 3 TRIGGERED** |
| CM1 < 0 (selling below COGS) | **Rule 3 TRIGGERED** — auto-trigger, scale cannot repair this |
| CM2 > 0 full period but latest quarter CM2 < 0 | Rule 3 NOT triggered — raise **deterioration flag** in Key Flags |

---

## Scoring Logic

| Rules Triggered | Action |
|-----------------|--------|
| 0 | PASS — proceed to Section 2 |
| 1 | PASS with flag — carry triggered rule into Key Flags Summary, proceed to Section 2 |
| 2 or 3 | REJECT — issue rejection notice, **continue full analysis through all sections** |

> Even on rejection, the complete analysis (Sections 2–7) is still run and included in the report. The rejection notice appears at the top of Section 1 and is surfaced again in the final verdict — it does not truncate the report. No override is possible on a 2-rule rejection.

---

## Output

Write to `companies/[company_name]/section1_output.md`.

Always include a one-liner on every rule — whether it passed, flagged, or triggered.

**0 rules triggered:**
```
Section 1 — PASS

Rule 1 (Deep Tech): [one line — e.g. "Core product is a SaaS platform with predictable recurring revenue — not deep tech."]
Rule 2 (Govt Revenue): [one line — e.g. "No government clients identified; revenue is entirely B2B private."]
Rule 3 (Unit Economics): [one line — e.g. "CM2 at 24% for the period — positive unit economics confirmed."]
```

**1 rule triggered:**
```
Section 1 — PASS (with flag)

Rule 1 (Deep Tech): [one line]
Rule 2 (Govt Revenue): [one line]
Rule 3 (Unit Economics): [one line]

Flag: Rule [X] — [one sentence — carry into Key Flags Summary]
```

**2 or 3 rules triggered:**
```
Section 1 — REJECTED

Rule 1 (Deep Tech): [one line]
Rule 2 (Govt Revenue): [one line]
Rule 3 (Unit Economics): [one line]

Rules triggered: Rule [X], Rule [Y]
- Rule X: [one sentence on why it triggered]
- Rule Y: [one sentence on why it triggered]

Full analysis continues in subsequent sections.
```