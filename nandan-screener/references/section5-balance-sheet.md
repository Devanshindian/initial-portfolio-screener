# Section 5 — Balance Sheet Analysis

The balance sheet tells you how the business is funded and how efficiently capital is used — and whether short-term money is being stretched to cover long-term assets.

---

## Source & Period Rule

- **All balance sheet and P&L data** — `companies/[company_name]/Financial_Appraisal_[company_name].xlsx`, sheet `Info and Adjustments`
- **Debtor Days, Inventory Days, Creditor Days, ROCE, Current Ratio, Quick Ratio** — `Operating Ratios` sheet (rows cited below); pull as-is but apply the period factor
- **D/TNW** — use Section 2's figure from `companies/[company_name]/dtnw_granularities.md`, not the Operating Ratios sheet

**Period factor:** the Operating Ratios sheet ships hardcoded to a 9-month fill (275 days, ×4/3). You need to correct this in the **Operating Ratios sheet only** — do not change anything in the `Info and Adjustments` sheet or the Excel template structure.
- **Days in period** = `365 × (Row 7 months ÷ 12)` → 365 for a full 12M year, ~274 for a 9M MIS
- **Annualisation factor** = `12 ÷ Row 7 months` → ×1 for 12M, ×12/9 for 9M

Apply per column in the Operating Ratios sheet. Audited years are fine at 365; only a partial MIS column needs adjustment.

---

## Step 1 — Efficiency Ratios & Cash Conversion Cycle

Pull from the `Operating Ratios` sheet for the **latest year only** (period factor applied):
- **Debtor Days** = Row 19
- **Inventory Days** = Row 20
- **Creditor Days** = Row 21

**If the latest period is less than 12 months** (check Row 7), the sheet's days figures are for that partial period — annualise them before using:
```
Annualised Debtor Days    = Sheet Debtor Days    × (12 ÷ Row 7 months)
Annualised Inventory Days = Sheet Inventory Days × (12 ÷ Row 7 months)
Annualised Creditor Days  = Sheet Creditor Days  × (12 ÷ Row 7 months)
```
*Example: Sheet shows Debtor Days = 90 for a 9M MIS → Annualised = 90 × (12/9) = 120 days.*

Use the annualised figures for all calculations below.

**CCC** = Annualised Debtor Days + Annualised Inventory Days − Annualised Creditor Days

| CCC | Reading |
|---|---|
| < 0 days | Funded by suppliers — excellent |
| 0–60 days | Healthy |
| 60–90 days | Watch — will need WC funding as it grows |
| > 90 days | 🔴 Red — every rupee of revenue growth needs a cash injection |
| > 120 days | Structural WC problem — growth is cash-destructive |

**Trend observation:** before moving to industry context, note the direction of each metric — is Debtor Days rising, falling, or stable? Same for Inventory Days and Creditor Days. A rising CCC year-on-year is a working capital deterioration signal even if the absolute level looks acceptable. (The full multi-year trend is built in Step 2 — flag here if the latest year shows a notable move.)

**Industry context:** web-search 2–3 top public companies in the same industry. For each, compute Debtor Days, Inventory Days, Creditor Days, and CCC from their published financials. This feeds directly into the output table — the subject company and peers sit side by side.

---

## Step 2 — Working Capital Quality

First build a multi-year table using the annualised latest year from Step 1, and the prior audited years directly from the `Operating Ratios` sheet (those are already full-year figures — no annualisation needed):

| Metric | FY__ | FY__ | MIS [period] annualised |
|---|---|---|---|
| Debtor Days | | | |
| Inventory Days | | | |
| Creditor Days | | | |
| CCC (days) | | | |

Use this table as the basis for the three quality checks below.

### Is the profit real?
Are Debtor Days and Inventory Days stable or improving year-on-year, or are they stretching (e.g. 30 → 45 → 60)? Stretching means the company may be booking revenue it cannot collect — profit is then suspect. Resolve this before trusting the P&L.

### Is negative OCF explained by growth?
Compute **Change in Working Capital** from `Financial_Appraisal_[company_name].xlsx` for the latest two years whose cash flows are available:
```
ΔWC = Row 126 (Increase in Inventories)
    + Row 127 (Increase in Debtors)
    − Row 131 (Increase in Trade Payables)
```
These are already signed as cash impacts in the template — just apply the formula above.

Then compute: **ΔWC ÷ Revenue Growth**

| Ratio | What it means |
|---|---|
| < 0.5x | WC very efficient — excellent signal |
| 0.5x–1.0x | WC rising proportionally with revenue — normal |
| > 1.0x | WC rising faster than revenue — collections deteriorating or inventory bloating |
| > 1.5x | 🔴 Serious — disproportionate cash needed just to grow |

*Example: Revenue grew ₹10 Cr, ΔWC = ₹8 Cr → ratio = 0.8x (proportional, acceptable). If ΔWC = ₹18 Cr → ratio = 1.8x (WC hunger outpacing growth — flag it).*

### ROCE vs cost of WC funding
Use the latest available period — MIS or audited, whichever is most recent — even if it is a partial year. ROCE and CoD are computed fully in Step 4; the question here is simply whether ROCE exceeds the cost of the working capital funding. If yes, debt-funded WC is value-accretive. If not, borrowing to fund WC destroys value.

**One-line test:** negative OCF is acceptable *only if* (a) profit is real, (b) ΔWC ÷ revenue growth is proportional, and (c) ROCE > cost of the funding raised.

**Red flag:** OCF persistently negative in a mature (not high-growth) company → the model itself is cash-destructive. Structural, not cyclical — be cautious.

---

## Step 3 — Revenue Quality (top-client concentration)

**Sources (in order):**
1. Customer-wise revenue sheet if provided in the company folder
2. Debtor ageing from `companies/[company_name]/section2_output.md` Annexure B — largest outstanding balances proxy for the biggest clients
3. If neither is available, web-search the company for named clients or disclosed customer relationships

**Web-search each named client** for quality and credibility: are they solvent, reputable, publicly known, likely to pay? Note whether they are listed/unlisted, their scale, and any adverse news. Flag concentration — a handful of clients making up a large share of revenue or receivables is a collectability and continuity risk.

---

## Step 4 — Return on Capital vs Cost of Capital

**ROCE** = pull from `Operating Ratios` sheet **Row 13** — already calculated; do not recompute the headline.

**Cost of Debt (CoD)** = Row 23 (Finance costs, annualised if partial period) ÷ prior-year total debt (prior column Row 57 + Row 62). Compute for each year with reliable financials.

**Four stages — identify which the company is in:**

| Stage | Condition | What it means |
|---|---|---|
| 1 | ROCE > CoD | Capital earns more than debt costs — ROE amplified. Healthy. |
| 2 | ROCE = CoD | Debt is neutral — ROE = ROCE |
| 3 | ROCE < CoD, but earnings still cover interest | ROE < ROCE — equity returns dragged down, but equity is not being destroyed |
| 4 | ROCE < CoD and earnings can't cover interest | 🔴 Destroying equity value — interest shortfall compounds, company eventually borrows to service existing debt |

**The line that matters is Stage 3 vs Stage 4** — can earnings cover interest? Flag Stage 4 prominently.

### Incremental ROCE vs Cost of Debt

Compute from `Financial_Appraisal_[company_name].xlsx` for the latest year with available data:

- **NOPLAT** = EBIT × (1 − effective tax rate)
  - EBIT = Row 29 (PBT) + Row 23 (Finance costs)
  - Effective tax rate = Row 32 (Total Tax) ÷ Row 29 (PBT)
- **Capital Employed** = Equity (Rows 51+52+53+54+55) + LT Debt (Row 57) + ST Debt (Row 62)
- **Incremental NOPLAT** = this year's NOPLAT − last year's
- **Incremental Capital** = this year's Capital Employed − last year's
- **Incremental ROCE** = Incremental NOPLAT ÷ Incremental Capital

🟢 if Incremental ROCE > CoD — the next rupee of capital (including Nandan's debt) is deployed productively.
🔴 if below — capital is being deployed at a return below its cost.

---

## Step 5 — Liquidity Ratios

Pull from `Operating Ratios` sheet — period-insensitive, safe to take as-is:
- **Current Ratio** = Row 16 → benchmark **> 1.2x**
- **Quick Ratio** = Row 17 → benchmark **> 1.0x**

Flag if either falls below its benchmark.

---

## Step 6 — Source & Use of Funds

Classify every balance-sheet line as short-term/long-term × source/use:

| | Short-term | Long-term |
|---|---|---|
| **Sources** | Trade payables (63), ST borrowings (62), other current liabilities incl. customer advances (64), ST provisions (65) | Equity & reserves (51–55), LT borrowings (57), DTL (58), other LT liabilities (59), LT provisions (60) |
| **Uses** | Trade receivables (82), inventory (81), cash (83), other current assets (85), current investments (80), ST loans & advances (84) | Fixed assets / net block (70), intangibles (71), CWIP (72), IAUD (73), non-current investments (75), LT loans (76), other NCA (77) |

**Cardinal rule:** short-term sources must only fund short-term uses; long-term sources may fund anything.

**Mismatch check:**
- **ST sources** = Row 63 + Row 62 + Row 64 + Row 65
- **ST uses** = Row 82 + Row 81 + Row 83 + Row 85 + Row 80 + Row 84
- **If ST sources > ST uses → 🔴 mismatch**: surplus short-term money is financing long-term assets. When the lender calls, the company must liquidate long-term assets or break its operating cycle to repay — it compounds each cycle.

---
## Output
 
Write to `companies/[company_name]/section5_output.md` using this exact template:
 
---
 
```
## Section 5 — Balance Sheet Analysis
 
### A. Efficiency & Cash Conversion Cycle
 
| Metric          | FY__ | FY__ | MIS [period] annualised |  | [Subject Co] | [Peer 1] | [Peer 2] |
|-----------------|------|------|-------------------------|--|--------------|----------|----------|
| Debtor Days     |      |      |                         |  |              |          |          |
| Inventory Days  |      |      |                         |  |              |          |          |
| Creditor Days   |      |      |                         |  |              |          |          |
| CCC (days)      |      |      |                         |  |              |          |          |
 
[One-liner: which CCC band, trend direction (improving / deteriorating), and how it compares to peers.]
 
### B. Working Capital Quality
 
| Check | Finding | Verdict |
|---|---|---|
| Profit real? | [Debtor Days trend e.g. "35 → 42 → 51 — stretching"] | 🟢 / 🔴 |
| ΔWC ÷ Revenue growth | [e.g. "ΔWC ₹8 Cr ÷ Revenue growth ₹10 Cr = 0.8x — proportional"] | 🟢 / 🔴 |
| ROCE > cost of funding? | [e.g. "ROCE 14% vs CoD 11% — debt-funded WC is value-accretive"] | 🟢 / 🔴 |
 
[One-line overall verdict on WC quality.]
 
### C. Return on Capital vs Cost of Debt
 
| Year | ROCE | CoD | ROCE − CoD | Earnings cover interest? |
|------|------|-----|------------|--------------------------|
| FY__ |      |     |            | Yes / No                 |
| FY__ |      |     |            | Yes / No                 |
 
Incremental ROCE: ₹__ Cr NOPLAT growth ÷ ₹__ Cr capital added = __% → [🟢 above / 🔴 below] CoD of __%
 
[One-liner: is the business creating or destroying value with each new rupee of capital?]
 
### D. Liquidity
 
| Ratio         | Value | Benchmark | Flag |
|---------------|-------|-----------|------|
| Current Ratio |       | > 1.2x    |      |
| Quick Ratio   |       | > 1.0x    |      |
 
### E. Source & Use of Funds
 
| | Short-term (₹ Cr) | Long-term (₹ Cr) |
|---|---|---|
| **Sources** | [ST borrowings + payables + other CL] | [Equity + LT debt + other NCL] |
| **Uses** | [Receivables + inventory + cash + other CA] | [Fixed assets + CWIP + other NCA] |
 
ST sources total: ₹__ Cr — ST uses total: ₹__ Cr → [Matched / 🔴 Mismatch — ₹__ Cr of short-term money funding long-term assets]
 
### F. Revenue Quality
 
| Client | Revenue / Receivables share | Listed / Unlisted | Credibility read |
|---|---|---|---|
| [Client 1] | __% | | [one line — solvent, reputable, any flags] |
| [Client 2] | __% | | |
| [Client 3] | __% | | |
 
[One-liner on concentration risk — is the business dangerously reliant on a handful of clients?]
```
 
---

