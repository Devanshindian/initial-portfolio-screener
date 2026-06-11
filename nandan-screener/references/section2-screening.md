# Section 2 — Initial Screening Criteria

Six screening criteria. **Threshold: at least 4 of 6 must be met to proceed.**

| Rules met (of 6) | Action |
|---|---|
| 5 or 6 | **PASS** (clean) |
| exactly 4 | **PASS — borderline** (carry into Key Flags Summary) |
| 3 or fewer | **REJECT** — issue rejection notice |

> **Threshold is 4 of 6 — do not get this wrong.**
>
> Rejection is a hard stop on the **verdict**, not on the **analysis** — exactly like Section 1. Even on a Section 2 reject, continue the full analysis through Sections 3–7. The rejection is surfaced at the top of Section 2 and again in the final verdict.

**Scoring rule for unverifiable criteria:** if a rule genuinely cannot be verified after checking all listed sources, count it as **NOT met** (conservative) and flag it prominently so a human can override. Never silently pass an unverifiable rule.

---

## Rule 1 — Operating History > 2 Years

**Met if:** the company has **≥ 2 years of active operating history** as of the screening date.

- Use the date operations actually commenced — not necessarily incorporation date.
- **Sources:** pitch deck first. If not available, do a web search on the company.

---

## Rule 2 — Annualised Revenue > INR 15 Crore

**Met if:** annualised operating revenue **> ₹15 Cr** (exclude Other Income — operating revenue only).

**Step 1 — Pick the revenue figure.**
- Use the **latest full-year audited** revenue if it is the most recently completed FY.
- If MIS (`companies/[company_name]/mis_[period].md`) is more recent than the latest audited, use MIS instead.

**Step 2 — Annualise only if the figure covers less than 12 months.**

| MIS shape | What to do |
|---|---|
| Already 12 months (full-year, trailing-12M, or latest-FY) | Use as-is — no annualisation |
| Partial period (< 12 months) | `Annualised Revenue = Revenue for the period × (12 ÷ months covered)` |

Examples: 9M MIS → × 12/9; single quarter → × 12/3.

**Step 3 — Run-rate sense-check (only if monthly/quarterly data exists).** Compare the annualised figure to the most recent quarter's run-rate (avg of last 3 months × 12). Flag if the annualisation is being inflated by strong early months while the recent quarter is softening, or vice versa. If only annual data is available, this check is not possible — note it and move on.

---

## Rule 3 — Debt to Tangible Net Worth (D/TNW) ≤ 3x

**Met if: D/TNW ≤ 3x**, assessed pre-disbursement (Nandan's proposed facility is NOT included).

**Calculation 1 — D/TNW from latest audited (always required).**
Pull directly from `companies/[company_name]/dtnw_granularities.md` — Section C of that file already computes the D/TNW ratio with all adjustments applied. Apply the **≤ 3x** test.
- **Negative or zero TNW → fails outright** (see note below).

**Calculation 2 — Simplified D/E from MIS (supplementary).**
Pull from `companies/[company_name]/mis_[period].md` — use the latest available balance sheet figures.
- **Total Debt** = Long-term borrowings + Short-term borrowings + contingent liabilities likely to crystallise
- **Equity** = Paid-up equity share capital + reserves and surplus (as reported; do not apply ageing haircuts here)
- Treat CCDs and promoter subordinated loans as quasi-equity if identifiable — add to Equity, subtract from Total Debt.
- **Flag if simplified D/E > 2.5x.**
- Always show the underlying values, not just the ratio: `D/E = Y.Yx (Total Debt ₹X Cr ÷ Equity ₹Z Cr)`.

**Met / not-met is decided by Calculation 1** (the audited ≤ 3x test). Calculation 2 is a supplementary recency flag only.

### Why zero or negative TNW fails — do not read a negative ratio as "≤ 3x"

The ≤ 3x test assumes **TNW > 0**. If TNW is zero or negative, D/TNW produces a small or negative number that *looks* like a pass but is not — the ratio has stopped being a leverage signal. The ≤ 3x ceiling is a recovery-cushion idea: at 3x, the lender must recover ~75% of assets to be made whole, and that only holds while real (tangible) assets exceed debt.

| Situation | What it means |
|---|---|
| TNW > 0 | Recovery possible, cushion exists — ratio is meaningful |
| TNW = 0 | 100% recovery needed, zero margin |
| TNW < 0 | Lender takes a loss even at 100% recovery — framework collapses |

**TNW ≤ 0 → Rule 3 fails outright**, regardless of what the arithmetic ratio prints. A negative D/TNW (positive debt ÷ negative TNW) is the worst case, not a pass. *(Example: Debt ₹49 Cr ÷ TNW −₹54 Cr = −0.9x — "−0.9 ≤ 3" is a math artifact; the company is tangibly insolvent.)*

---

## Rule 4 — Founder / Promoter Experience > 4 Years

**Met if:** at least one promoter has **> 4 years of relevant** industry or domain experience.

- "Relevant" = same or adjacent industry/domain — not total years of work experience.
- **Source:** use the founder background already built in `companies/[company_name]/section0_output.md` (Section 0, Block C). Do not re-research — reuse what is already there.
- If unverifiable after all sources: flag **"Unable to verify Rule 4 — founder background not available"**, list what was checked, and count as not-met (conservative) pending human input.

---

## Rule 5 — Debtors > 180 Days < 10% of Revenue

**Met if:** receivables outstanding **> 180 days** are **≤ 10% of total revenue**.

**Sources (in order):**
1. If the user has uploaded a debtor ageing / AR ageing report in the company folder — use that directly.
2. Otherwise, use `companies/[company_name]/dtnw_granularities.md` — Section E of that file already captures the debtor ageing buckets (180–365d + >365d).

**Denominator** = total revenue of the same period as the ageing schedule.

If no ageing schedule is available from either source: flag **"Unable to verify Rule 5 — debtor ageing not available"** and count as not-met (conservative).

---

## Rule 6 — Operating Cash-Generative OR Cash Runway > 6 Months

**Met if:** the company generates cash from operations (Period Cash flow > 0), **OR** has a cash runway > 6 months.

- **Period Cash flow > 0** → business is self-funding → Rule 6 met (runway effectively unlimited).
- **Period Cash flow < 0** → business is burning → compute runway under both ST-debt scenarios; met if base-case runway > 6 months.

### Source

Use the already-filled template: `companies/[company_name]/Financial_Appraisal_[company_name].xlsx`, sheet `Info and Adjustments`, **latest populated column**. Source selection was settled at the template-fill step — nothing to re-decide here.

> **Period consistency:** every flow figure must be for the same period as Row 7 (e.g. if MIS covers 9 months, all figures are 9-month figures). Do not mix periods across line items.

> **Source consistency:** use one source (MIS or audited) consistently across all line items in this calculation. Do not mix MIS figures with audited figures within the same run.

### Period Cash Generation / (Burn)

```
EBITDA                        = Row 29 (PBT) + Row 23 (Finance costs) + Row 24 (Depreciation)
+ Working-capital cash impact  = Row 126 + Row 127 + Row 128 + Row 131  (already signed — just add)
+ Capex cash impact            = Row 147 (tangible) + Row 148 (intangible)  (already negative = cash out)
− Finance costs                = Row 23
− Cash tax                     = Row 30 (Current Tax) ONLY — exclude Row 31 (Deferred Tax is non-cash)
− Long-term principal          = 0  (assume refinanced — schedules rarely available)
− Short-term debt repayment    = Scenario 1: 0  |  Scenario 2: Row 62 (ST Borrowings)
= Period Cash Generation / (Burn)
```

### Notes on Key Line Items

**Working capital** — the four rows (126, 127, 128, 131) are auto-computed from the two most recent balance sheets already in the template. They are already signed as cash impacts — simply add them. Do not recompute manually.

**Finance costs** — use Row 23 directly from the latest column.

**Long-term principal = 0** — repayment schedules are rarely shared; always assume all long-term principal due has been refinanced.

**Cash tax = Row 30 only** — deferred tax (Row 31) is a non-cash accounting entry; no cash leaves the business.

**Capex** — Row 147 + Row 148, already stored as negative cash impacts. Add them directly.

### Runway Calculation

- **Monthly burn** = Period Cash (Burn) ÷ Row 7 (period months)
- **Unencumbered cash** = Row 172 (total cash − encumbered); if no encumbrance detail, use Row 83
- **Runway (months)** = Unencumbered cash ÷ |Monthly burn|
- Do NOT add Nandan's proposed disbursement to cash

### Two ST-Debt Scenarios — Always Present Both

| Scenario | ST repayment treatment |
|---|---|
| Scenario 1 — Refinanced (base case for pass/fail) | ST repayment = 0 |
| Scenario 2 — Fully Repaid (stress) | Subtract full ST borrowings (Row 62) |

**Decision:** Rule 6 met if Period Cash flow > 0, **or** base-case (refinanced) runway > 6 months. Flag prominently if the fully-repaid runway falls below 6 months even when the base case passes.

> **Why pre-loan:** the runway stress-tests recoverability — "if called to repay immediately, how long before the business runs out of cash?" A company burning ₹50L/month with ₹2 Cr cash has a 4-month runway; deploying ₹3 Cr of new debt does not make it 10 — the fund evaluates the pre-loan position. Hence Nandan's own disbursement is excluded.

---

## Output

Write to `companies/[company_name]/section2_output.md`. Two parts: scorecard table, then annexures.

### Part 1 — Scorecard Table

```
Section 2 — Initial Screening: [X] of 6 met → [PASS / PASS-borderline / REJECT]

| Criterion                                | Result          | Reasoning |
|------------------------------------------|-----------------|-----------|
| 1. Operating history > 2 yrs             | Met / Not met   | [N years operating; date operations commenced; source.] |
| 2. Annualised revenue > ₹15 Cr           | Met / Not met   | [₹X Cr vs ₹15 Cr. Source (MIS / audited FY). Annualisation method if applicable — e.g. "9M MIS ₹A Cr × 12/9 = ₹X Cr". Run-rate sense-check if monthly data exists.] |
| 3. D/TNW ≤ 3x                            | Met / Not met   | [D/TNW (latest audited) = X.Xx (Total Debt ₹__ Cr ÷ TNW ₹__ Cr) — from dtnw_granularities.md Section C. D/E (MIS) = Y.Yx (Total Debt ₹__ Cr ÷ Equity ₹__ Cr). Flag if D/E > 2.5x. Negative TNW → fails outright.] |
| 4. Promoter experience > 4 yrs           | Met / Not met   | [Promoter name — N yrs in (domain); from section0_output.md.] |
| 5. Debtors > 180 days < 10% of revenue   | Met / Not met   | [Debtors >180d = ₹X Cr = Z% of revenue vs 10% ceiling. Source: debtor ageing report (company folder) / dtnw_granularities.md Section E.] |
| 6. Operating-profitable OR runway > 6 mo | Met / Not met   | [Period cash flow: ₹X Cr (generative / burning). If burning: Scenario 1 (refinanced) = M months / Scenario 2 (fully repaid) = M' months vs 6-month floor.] |

Flags: [borderline note if exactly 4 met; any unverified rule counted not-met; D/E > 2.5x; fully-repaid runway < 6 months]
```

**If REJECT (≤ 3 met):** lead with the rejection notice and scorecard, then note "Full analysis continues in subsequent sections."

### Part 2 — Annexures

**Annexure A — D/TNW Calculation.**
Reproduce the D/TNW build-up from `dtnw_granularities.md` Section C: the TNW ladder, the Total Debt ladder, the D/TNW ratio (Total Debt ÷ TNW), and the supplementary MIS simplified D/E (Total Debt ÷ Equity). Show the numbers behind each ratio so the reader sees exactly what was adjusted.

**Annexure B — Debtor Ageing.**
Include only if a debtor ageing report was available (either from the company folder or from `dtnw_granularities.md` Section E). Show the ageing buckets (Not Due / <6m / 6m–1yr / 1–2yr / 2–3yr / >3yr) and the >180-day total as a % of revenue (the Rule 5 number).

**Annexure C — Cash Runway (both scenarios).**
Show the full burn build-up and runway side by side for both scenarios:

| | Scenario 1 — ST Refinanced | Scenario 2 — ST Fully Repaid |
|---|---|---|
| Period Cash Generation / (Burn) | ₹X Cr | ₹X Cr |
| Monthly burn | ₹X Cr / month | ₹X Cr / month |
| Unencumbered cash | ₹X Cr | ₹X Cr |
| Runway | X months | X months |

If the business is operating cash-generative (Period Cash flow > 0), state that and note runway is effectively unlimited.