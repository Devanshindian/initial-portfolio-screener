# Financial Appraisal Template — Integration Reference

---

## ⭐ Read This First

**Use the Opus model for this step.** Precision-critical — one mis-read digit or swapped column breaks the entire balance sheet. Opus handles this reliably; smaller models slip on the traps documented below.

**The shape of this task (internalize before starting):**
1. Inventory documents → confirm periods, units, audited vs MIS
2. Company structure check → save `company_structure.md`
3. Extract ALL numbers in one pass (P&L + BS + Notes) → do not re-open PDFs after this
4. Write ONE Python script → fill all columns (C, D, E, F) in a single run
5. Verify BS check (Row 88 = 0) → fix if non-zero → save
6. Write `dtnw_granularities.md`

One extraction pass → one script → one verification → two markdown outputs. No partial fills, no column-by-column scripts, no re-reading PDFs mid-way.

---

## Phase 1 — Document Inventory

Before doing anything else, list every file provided and note three things for each:

| Field | What to confirm |
|---|---|
| Period covered | e.g. 9M Apr–Dec, or full FY Apr–Mar |
| Audited or MIS | Audited = signed annual report; MIS = management-provided, unaudited |
| Unit stated in header | Rupees / Lakhs / Crores — different files often use different units |

**Template uses INR Crores** (`Amt in multiples of` = 10,000,000). Convert everything before entering.

| Stated unit | Conversion |
|---|---|
| Rupees (₹) | ÷ 1,00,00,000 |
| Thousands | ÷ 10,000 |
| Lakhs | ÷ 100 |
| Millions | ÷ 10 |
| Crores | × 1 (no conversion needed) |
| 10 Crores | × 10 |

Convert at extraction time — record Crore values directly. Do not leave conversion to the script.

---

## Phase 2 — Company Structure Check

Establish legal and ownership structure before touching any financials. This determines which numbers to use and flags consolidation scope.

**Decision tree:**
- **Structure document provided** (org chart, shareholding pattern, subsidiary list) → use it directly.
- **Not provided** → web search: `"[Company name] subsidiaries corporate structure India"`. Determine whether the company is a standalone entity, a parent holding company, or a subsidiary.

**Which financials to use:**
- Consolidated preferred — state this in the report.
- Only standalone/subsidiary available → proceed, but flag explicitly: *"Analysis based on standalone financials only. Consolidated financials not provided."*
- Both available → use consolidated. Note that standalone was also reviewed.

Save output to `companies/[company_name]/company_structure.md` — see Outputs section for exact format.

---

## Phase 3 — Data Extraction (One Pass, Do Not Return)

Read all PDFs once and extract every value below. Record each figure with its source row/note reference and unit as stated. Do this for ALL documents before writing any code.

### P&L Checklist (each audited report)

- [ ] Revenue from operations — confirm net or gross of discounts/incentive payouts
- [ ] Other income
- [ ] Purchases of stock-in-trade (or raw material cost for manufacturing)
- [ ] Changes in inventories — sign exactly as shown
- [ ] Employee benefit expenses
- [ ] Finance costs
- [ ] Depreciation and amortisation
- [ ] Other expenses
- [ ] Exceptional items (if any)
- [ ] Profit before tax — verify arithmetic
- [ ] Current tax
- [ ] Deferred tax — positive = expense, negative = credit/income
- [ ] Profit for the year (total, before MI split)
- [ ] Non-controlling interest / minority interest (consolidated only)
- [ ] PAT attributable to equity shareholders (bottom line)

### Balance Sheet Checklist (each audited report)

- [ ] Equity share capital — equity component only
- [ ] Preference share capital / CCPS / OCPS if any — Row 54, not Row 51
- [ ] Reserves and surplus total — all sub-reserves: retained earnings, capital reserve, securities premium, FCTR, OCI, DRR
- [ ] Non-controlling interest (consolidated only)
- [ ] Non-current borrowings — full breakdown from Note if available
- [ ] DTL or DTA net — confirm direction (DTL = positive Row 58, DTA = negative Row 58)
- [ ] Other non-current liabilities
- [ ] Long-term provisions
- [ ] Short-term / current borrowings — full breakdown from Note
- [ ] Trade payables — MSME + others combined
- [ ] Other current liabilities — advances from customers, deferred revenue, statutory dues
- [ ] Short-term provisions
- [ ] PPE net block
- [ ] Intangible assets net block
- [ ] CWIP
- [ ] Intangibles under development
- [ ] Non-current investments
- [ ] Other non-current assets — check if any FDs > 12M are buried here
- [ ] Inventories
- [ ] Trade receivables — net of allowance for doubtful debts
- [ ] Cash and cash equivalents — check Note for breakdown; move FDs > 12M to Row 77
- [ ] Other current assets — advances to vendors, prepaid, statutory balances

### Notes to Accounts Checklist (latest audited report only — for `dtnw_granularities.md`)

These do NOT go in the template. Capture in the same reading pass, write to the second output file.

- [ ] Trade receivables ageing schedule — buckets: Not Due / <6m / 6m–1yr / 1–2yr / 2–3yr / >3yr. Verify OCR column alignment carefully.
- [ ] Inventory ageing schedule if disclosed — often absent (Schedule III does not mandate it); flag if missing
- [ ] Contingent liabilities and commitments — note whether any are likely to crystallise
- [ ] Promoter / director subordinated loans — identify within borrowings / related-party notes
- [ ] CCDs or other compulsorily-convertible instruments
- [ ] Other capitalised / fictitious assets — preliminary and pre-incorporation expenses, deferred revenue expenditure, misc. expenditure not written off
- [ ] Segment / vertical-wise revenue split if a segment note exists
- [ ] Actual tax paid and actual capex (additions) from the cash flow statement

### MIS Checklist

- [ ] All available P&L lines — missing lines are fine, set to 0
- [ ] All available BS lines
- [ ] Period covered — enter in Row 7
- [ ] Note any line where MIS label differs from standard — flag in report

### MIS Extract — Save to File
 
After extracting MIS data, write a complete faithful markdown copy of the MIS P&L to `companies/[company_name]/mis_[period].md` — every line item (all opex sub-lines, all period columns, and totals), preserving source figures exactly. Do not trim or summarise. Note the period covered (monthly vs annual) and the unit. Later sections depend on the granular lines (Section 1 Rule 3 unit economics; Section 4 margin waterfall).


---

## Phase 4 — Fill the Template (One Script)

**Template file:** `/Users/devanshasawa/Desktop/initial portfolio screener/templates/Financial Appraisal Template.xlsx`

| Sheet | Purpose |
|---|---|
| `Info and Adjustments` | Primary input sheet — enter all P&L and Balance Sheet data here |
| `Operating ratios` | Auto-calculated output — ratios, margins, leverage, efficiency |
| `Cash position estimation` | Auto-calculated — cash runway under different scenarios |
| `Sheet1 / Sheet2` | Scratch / unused |

**Only populate `Info and Adjustments`. All other sheets read from it.**

---

### Script Structure

Write a single Python script (openpyxl) that fills ALL columns in one execution:

1. Copy blank template to `companies/[company_name]/Financial_Appraisal_[company_name].xlsx`
2. Fill header rows (1–7) for each column
3. Fill all P&L input rows for each column
4. Fill all BS input rows for each column
5. Read back Row 88 (BS check) for each column — print result
6. Save

Enter each figure as `raw_value / divisor` (e.g. `71_99_25_02_630/1e7`), not a hand-rounded decimal. This avoids decimal slips and keeps the BS check at exactly 0.

---

### Column Layout

| Template Column | Content | Row 6 marker |
|---|---|---|
| Col C | Provisional / MIS (latest period, may be 9M or 12M) | "P" |
| Col D | Latest audited FY (e.g. FY25 = Mar 2025) | "A" |
| Col E | Prior audited FY (e.g. FY24 = Mar 2024) | "A" |
| Col F | FY-2 audited (e.g. FY23 = Mar 2023) | "A" if available |

---

### Header Rows (fill for each column)

| Row | Label | Notes |
|---|---|---|
| 1 | Company name | |
| 2 | Standalone / Consolidated | |
| 3 | Type of Company | Pvt / Ltd / LLP |
| 4 | Amt in multiples of | LEAVE — always `=10^7`, do not change |
| 5 | Year ended (date) | `date(YYYY,M,D)`. Audited = FY-end (31 Mar). MIS = period-end date (e.g. 31 Dec 2025) |
| 6 | Audited / Provisional | "A" for audited, "P" for MIS |
| 7 | Period (months) | 12 for full year, 9 for Apr–Dec MIS |

---

### Quick Reference — All Input Rows

AUTO = formula cell, never touch.

| Row | Label | Fill? | Notes |
|---|---|---|---|
| **P&L** | | | |
| 11 | Revenue from Operations | YES | Enter NET figure — after discounts / incentive payouts |
| 12 | Less: Excise/GST | YES | Usually 0 for post-GST companies |
| 13 | Revenue Net | AUTO | |
| 14 | Other Income | YES | |
| 15 | Total Revenue | AUTO | |
| 18 | Purchase of Stock in Trade / RM | YES | See business-type table below |
| 19 | Changes in Inventories | YES | Negative = inventory increased |
| 20 | Direct Expenses | YES | |
| 21 | Changes in Inventories (legacy) | LEAVE BLANK | Unused legacy row — always 0 |
| 22 | Employee Benefit Expenses | YES | |
| 23 | Finance Costs | YES | Do not double-count in Row 25 |
| 24 | Depreciation and Amortisation | YES | |
| 25 | Other Expenses | YES | All other operating expenses |
| 26 | Total Expenses | AUTO | |
| 27 | Profit Before Exceptional Items | AUTO | |
| 28 | Exceptional Items | YES | 0 if none |
| 29 | Profit Before Tax | YES | Enter from P&L; verify = Row 27 ± Row 28 |
| 30 | Current Tax | YES | Current year charge only — no deferred tax here |
| 31 | Deferred Tax | YES | Negative = credit (deferred tax income) |
| 32 | Total Tax | AUTO | |
| 33 | PAT Before Extraordinary | AUTO | |
| 35 | Profit/Loss for the Period | YES | "Profit for the year" from P&L |
| 36 | Minority Interest | YES | Enter as shown — may be + or − |
| 37 | Share of Profit/Loss of Associates | YES | 0 if none |
| 38 | Consolidated PAT After MI | YES | Bottom-line attributable to equity shareholders |
| **BS — Equity & Liabilities** | | | |
| 51 | Equity Share Capital | YES | Equity component ONLY — no preference shares |
| 52 | Quasi Equity (CCDs) | YES | Compulsorily Convertible Debentures only |
| 53 | Reserves and Surplus | YES | All reserves incl. FCTR, OCI, securities premium |
| 54 | Share Application Money | YES | CCPS, OCPS, warrants — equity-like instruments |
| 55 | Minority Interest | YES | Positive number (consolidated BS only) |
| 56 | Non-Current Liabilities total | AUTO | |
| 57 | Long Term Borrowings | YES | Non-current portion only |
| 58 | Deferred Tax Liabilities [Net] | YES | DTL = positive; DTA = negative |
| 59 | Other Long Term Liabilities | YES | 0 if none |
| 60 | Long Term Provisions | YES | |
| 61 | Current Liabilities total | AUTO | |
| 62 | Short Term Borrowings | YES | OD, WC loans, current portion of LT debt |
| 63 | Trade Payables | YES | MSME + others combined |
| 64 | Other Current Liabilities | YES | Advances from customers, statutory dues, deferred revenue. Also fold in any separate "Other Financial Liabilities" line |
| 65 | Short Term Provisions | YES | |
| 66 | Total Capital and Liabilities | AUTO | |
| **BS — Assets** | | | |
| 70 | Tangible + RoU Assets | YES | Net block after depreciation; add RoU separately if shown |
| 71 | Intangible Assets | YES | Net block after amortisation |
| 72 | Capital Work-in-Progress | YES | |
| 73 | Intangibles Under Development | YES | |
| 75 | Non-Current Investments | YES | |
| 76 | Long Term Loans and Advances | YES | |
| 77 | Other Non-Current Assets | YES | Incl. FDs > 12 months. Do NOT include DTA if already entered as negative in Row 58 |
| 78 | Total Non-Current Assets | AUTO | |
| 80 | Current Investments | YES | |
| 81 | Inventories | YES | |
| 82 | Trade Receivables | YES | Net of allowance |
| 83 | Cash and Cash Equivalents | YES | Free cash + FDs < 12M only. FDs > 12M go in Row 77 |
| 84 | Short Term Loans and Advances | YES | |
| 85 | Other Current Assets | YES | |
| 86 | Total Current Assets | AUTO | |
| 87 | Total Assets | AUTO | |
| 88 | **BS Check** | AUTO | Must = 0. Non-zero = something is wrong |

---

### Rows 18–20 by Business Type

Identify business type before filling these rows.

| Business Type | Row 18 | Row 19 | Row 20 |
|---|---|---|---|
| **Trading** | Purchases of stock-in-trade | Changes in inventories of stock-in-trade | 0 |
| **Manufacturing** | Raw material purchases | Changes in ALL inventory: RM + WIP + finished goods combined | Direct manufacturing costs (power, contract labour, consumables) |
| **Services** | 0 | 0 | 0 — all costs flow through Rows 22 and 25 |

For **mixed companies**: split as best as possible. If breakdown unavailable, put combined cost in the most appropriate row and flag it.

---

### P&L Line-Item Mapping

> **Source note:** India FY runs Apr 1 – Mar 31. "FY25" = year ended 31 March 2025. The latest annual report (e.g. March 2025 PDF) contains two years: FY25 and FY24.

| Row | Template Label | Source in PDF |
|---|---|---|
| 11 | Revenue From Operations (Gross) | P&L → "Revenue from operations" — use NET after discounts/incentive payouts |
| 12 | Less: Excise/GST | Only fill if revenue is reported gross of GST; usually nil post-GST |
| 14 | Other Income | P&L → "Other income" |
| 18 | Purchase of Stock in Trade | P&L → "Purchases of Stock-in-trade" |
| 19 | Changes in Inventories | P&L → "Changes in inventories" — enter exactly as shown |
| 20 | Direct Expenses | P&L → Direct cost line if any; often nil for pure trading |
| 22 | Employee Benefit Expenses | P&L → "Employee benefits expense" |
| 23 | Finance Costs | P&L → "Finance costs" — do not double-count in Row 25 |
| 24 | Depreciation And Amortisation | P&L → "Depreciation and amortization expense" |
| 25 | Other Expenses | P&L → "Other expenses" |
| 28 | Exceptional Items | P&L → "Exceptional items" if explicitly disclosed |
| 29 | Profit/Loss Before Tax | P&L → "Profit before tax" — verify = Row 27 ± Row 28 |
| 30 | Current Tax | Current year charge + any prior year adjustment. No deferred tax here |
| 31 | Deferred Tax | P&L → "Deferred Tax Credit / (Expense)" — negative = credit |
| 35 | Profit/Loss For The Period | P&L → "Profit for the year" |
| 36 | Minority Interest | Consolidated only — enter as negative if deduction from profit |
| 37 | Share Of Profit/Loss Of Associates | Negative if a loss |
| 38 | Consolidated PAT After MI | Cross-check: should = Row 35 + Row 36 + Row 37 |

---

### Balance Sheet Line-Item Mapping

**Equity and Liabilities**

| Row | Template Label | Source in PDF |
|---|---|---|
| 51 | Equity Share Capital | BS → "Share capital" → equity component only |
| 52 | Quasi Equity (CCDs) | CCDs if shown separately |
| 53 | Reserves and Surplus | BS → "Reserves and surplus" — all sub-reserves |
| 54 | Share Application Money | CCPS/OCPS, warrants, share application money — equity-like instruments |
| 55 | Minority Interest | BS → Minority interest (consolidated only) — positive number |
| 57 | Long Term Borrowings | Non-current liabilities → "Long-term borrowings" |
| 58 | Deferred Tax Liabilities [Net] | Net DTA → negative; net DTL → positive |
| 59 | Other Long Term Liabilities | Non-current liabilities → "Other long term liabilities" |
| 60 | Long Term Provisions | Non-current liabilities → "Long-term provisions" |
| 62 | Short Term Borrowings | Current liabilities → "Short-term borrowings" — OD, WC loans, bill discounting, current portion of LT debt |
| 63 | Trade Payables | MSME dues + other creditor dues combined |
| 64 | Other Current Liabilities | "Other current liabilities" + any separate "Other Financial Liabilities" (salary payable, accruals) |
| 65 | Short Term Provisions | Current liabilities → "Short-term provisions" |

**Assets**

| Row | Template Label | Source in PDF |
|---|---|---|
| 70 | Tangible + Right of Use Assets | PPE net block + RoU assets |
| 71 | Intangible Assets | Net block after amortisation |
| 72 | Capital Work-In-Progress | BS → "Capital work-in-progress" |
| 73 | Intangibles Under Development | BS → "Intangible assets under development" |
| 75 | Non-Current Investments | BS → "Non-current investments" |
| 76 | Long Term Loans And Advances | Non-current assets → "Long-term loans and advances" |
| 77 | Other Non-Current Assets | "Other non-current assets" + bank FDs > 12M. Do NOT include DTA if already in Row 58 |
| 80 | Current Investments | BS → "Current investments" |
| 81 | Inventories | BS → "Inventories" |
| 82 | Trade Receivables | Net of allowance for doubtful debts |
| 83 | Cash And Cash Equivalents | Free cash + FDs < 12M only |
| 84 | Short Term Loans And Advances | Current assets → "Short-term loans and advances" |
| 85 | Other Current Assets | BS → "Other current assets" |

---

### Structural Complexity — Watch for These While Filling

**Revenue with gross-to-net adjustments**
Some companies show gross revenue then subtract "Customer Incentive Payouts," "Discounts," or "Rebates" within Revenue from Operations. Use the NET figure in Row 11. Do not put gross in Row 11 and deductions in Row 12 — Row 12 is for GST/excise only.

**CCPS / OCPS / preference shares**
Convertible preference shares are classified as equity in Indian BS. Face value → Row 54. Securities premium from allotment → Row 53. Row 51 is for paid-up equity share capital only. Extremely common in venture-backed companies.

**Non-controlling interest (NCI)**
For consolidated financials: NCI appears in both the BS (Row 55, positive) and P&L (Row 36, enter exactly as shown — may be very small or zero). Do not confuse the two.

**Foreign Currency Translation Reserve (FCTR)**
FCTR sits inside "Other Equity" in the BS. Include it in the Row 53 total — do not show it separately.

**TRS Voucher Liability / Advance from customers / Deferred revenue**
These are liabilities to customers. They go in Row 64 (Other Current Liabilities). Common in reward voucher, SaaS, and advance-booking businesses. Can be very large — do not confuse with trade payables.

**Convertible instruments in non-current borrowings**
OCPS classified as financial liabilities (not equity) appear in Non-Current Borrowings → Row 57. Separate from CCPS/OCPS classified as equity (Row 54). Classification depends on conversion terms — check the Note.

**Bank overdraft**
Bank OD always goes in Row 62 (Short Term Borrowings), regardless of size.

**Disinvestment / hive-out of subsidiaries mid-year**
BS closing figures already reflect the removal. No adjustment needed, but flag it in the report — it distorts year-on-year comparisons.

---

### Common Pitfalls

**Brackets mean negative** — Indian statements show negatives in brackets: `(1,274)` = −1,274. Enter as negative. Applies most to inventory changes, deferred tax credits, and losses.

**DTA double-counting** — If DTA appears as a non-current asset in the BS, enter it as negative in Row 58 only. Do NOT also include it in Row 77. Side-effect: template's Total Assets will be lower than the audited BS headline by exactly the DTA amount. This is correct — the BS check will still = 0.

**Row 21 is unused** — Legacy row with no formula. Always leave blank.

**CCCPS go in Row 54, not Row 51** — Very common in venture-backed companies. Despite being called "preference shares," they are economically equity-like. Row 51 is strictly for paid-up equity share capital.

---

### MIS Filling — Key Differences

- **No standard format** — labels, detail, and what's shown varies by company. Do not assume labels mean the same thing across companies.
- **No Notes to Accounts** — borrowing schedules, debtor ageing, etc. are not available. Use whatever is given; flag gaps.
- **Partial data is expected** — set unavailable rows to 0 and flag. Do not guess or fabricate.
- **Flag mixed sources** — when any MIS figure is used alongside an audited figure, note: *"Mixed source: MIS [period] + Audited FY[X]"*
- **BS check still applies** — Row 88 = 0 must hold for MIS columns too.

---

## Phase 5 — Verification

Run the script once. Then verify:

**1. BS Check (Row 88)**
`Total Assets − Total Capital and Liabilities` must = 0 for every column. Non-zero = a line item is missing or mis-mapped. Identify the gap, fix in the script, re-run.

**2. Column-order swap trap (critical for MIS/provisional)**
A provisional PDF's extracted text often has its two columns swapped. Because both periods belong to the same entity, a swap still balances — the BS check will NOT catch it. Verify before trusting any MIS figure: match the document's prior-year column against an audited figure you already have (e.g. PPE, total assets). If it matches, the other column is the current MIS period. If it doesn't match, the columns are swapped — flip them.

**3. Revenue cross-check**
Revenue note detail should sum to the P&L revenue line.

**4. Finance costs cross-check**
Finance costs note total should match Row 23.

**5. Capital account working (Rows 100–111)**
Opening equity + PAT + new infusion = closing equity. Cross-check against share capital and reserves notes.

**6. Operating Ratios sheet**
Scan for any `#DIV/0!` or `#REF!` errors — a required input is missing. Trace back and fix.

---

## Phase 6 — D/TNW Granularities (`dtnw_granularities.md`)

The template stores only single balances. Nandan's D/TNW check (Section 2, Rule 3) needs the detail behind them. This file captures it.

**What goes here (not in the template):**
- Trade receivables ageing buckets + provisioning haircuts: Debtors 180–365d × 75%, >365d × 100%
- Inventory ageing buckets + provisioning haircuts: Inventory 180–365d × 40% (20% women's ethnic wear), >365d × 75% (40% women's ethnic wear)
- CCDs and promoter subordinated loans → reclassified from debt to quasi-equity (added to TNW, subtracted from Total Debt)
- Fictitious/soft assets: intangibles, intangibles-under-development, DTA, preliminary/pre-incorporation expenses → subtracted from TNW
- Contingent liabilities likely to crystallise → added to Total Debt

**How to produce it:**
1. Use `templates/DTNW_Granularities_Template.md` as the skeleton.
2. Fill from the **latest audited report only** — state the FY. Convert to INR Crores.
3. Verify each figure against the source PDF, especially debtor-ageing column alignment — a value in the wrong bucket changes the provision dramatically.
4. Where a schedule is absent or judgment is needed, flag explicitly rather than guessing.
5. **Apply haircuts, never waive them.** If a balance falls in a bucket that triggers a provision, apply it and flag for verification. Do not set to zero "pending verification." If the haircut produces negative TNW, that is the finding — surface it, do not soften the rule.
6. Use only the latest audited year's ageing — prior year cannot override current-year disclosure.
7. Save to `companies/[company_name]/dtnw_granularities.md`.

This file feeds Section 2 Rule 3 (D/TNW), Rule 5 (debtors > 180 days), and revenue quality in Section 5.

---

## Outputs

Three files written to `companies/[company_name]/` at the end of this step:

### 1. `company_structure.md`

2–4 sentence overview of legal and ownership structure. Must include:
- Standalone, parent holding company, or subsidiary
- Key subsidiaries (if any) and business they cover
- Whether consolidated or standalone financials were used
- Any structural flag (e.g. "Consolidated financials not provided — analysis based on standalone only")

**Format:**
```
[Company Name] is a [Pvt Ltd / Public Ltd] company incorporated in India, operating as [parent / standalone / subsidiary of X].
It operates through [N] subsidiaries covering [brief description of verticals].
This analysis uses [consolidated / standalone] financials for FY[X] and FY[X-1].
[Flag if applicable.]
```

### 2. `Financial_Appraisal_[company_name].xlsx`

Populated Financial Appraisal Template. The Operating Ratios sheet in this file is the source for all ratio inputs used in Sections 3–5. Refer back to this file — do not re-read source PDFs during those sections.

### 3. `dtnw_granularities.md`

D/TNW granularity sheet filled from the latest audited report using `templates/DTNW_Granularities_Template.md`. Captures ageing buckets, provisioning haircuts, CCD/promoter-loan reclassifications, contingent liabilities, and fictitious assets. Source for Section 2 Rule 3 and Rule 5.