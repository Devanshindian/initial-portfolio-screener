# D/TNW Granularities — [Company Name]

> **What this file is.** The standard Financial Appraisal Template captures only *single* balances (net trade receivables, net inventory, net intangibles, total borrowings). Nandan's **Debt-to-Tangible-Net-Worth (D/TNW)** check (Section 2, Rule 3) needs more than that: ageing buckets, provisioning haircuts, and equity/debt reclassifications. **None of this is in the template, and MIS financials never contain it.** So it is extracted here, once, from the **Notes to Accounts of the latest available audited annual report** — alongside the main template fill.
>
> **Source = latest AUDITED report only.** Units → convert to **INR Crores**. Figures from Notes are often OCR'd — **verify every number against the source PDF**, especially ageing-bucket column alignment.

**Company:** _______   **Audited FY used:** FY__   **Consolidated / Standalone:** _____
**Source doc:** _______   **Unit as stated:** _____

---

## A. Tangible Net Worth (TNW) build-up

| Line | Source (note ref) | Amount (₹ Cr) |
|---|---|---|
| Equity Share Capital | BS | |
| (+) Reserves & Surplus | BS | |
| (−) Non-Controlling Interest *(consolidated: exclude — third-party equity; flag the choice)* | BS | |
| **= Equity attributable to the borrower** | | |
| (+) CCDs / compulsorily-convertible instruments treated as quasi-equity | Borrowings note | |
| (+) Promoter / Director subordinated loans — **only if not repayable before Nandan's investment** | Borrowings / related-party note | |
| (−) Deferred Tax Assets *(if a DTA exists)* | BS / DTA note | |
| (−) Intangible Assets (net) | BS | |
| (−) Intangible Assets Under Development | BS | |
| (−) Other capitalised / fictitious assets *(preliminary & pre-incorporation exp, deferred revenue expenditure, misc. expenditure not written off)* | Notes | |
| (−) Debtor provision: **180–365 days × 75%** | Debtor ageing (§D) | |
| (−) Debtor provision: **>365 days × 100%** | Debtor ageing (§D) | |
| (−) Inventory provision: **180–365 days × 40%** *(20% for women's ethnic wear)* | Inventory ageing (§D) | |
| (−) Inventory provision: **>365 days × 75%** *(40% for women's ethnic wear)* | Inventory ageing (§D) | |
| **= Tangible Net Worth (TNW)** | | |

## B. Total Debt build-up

| Line | Source (note ref) | Amount (₹ Cr) |
|---|---|---|
| Long-Term Borrowings | BS / borrowings note | |
| (+) Short-Term Borrowings | BS / borrowings note | |
| (+) Contingent Liabilities — **only if likely to crystallise** | Contingent liabilities & commitments note | |
| (−) CCDs reclassified to equity | (same as §A) | |
| (−) Promoter subordinated loans reclassified to equity | (same as §A) | |
| **= Total Debt** | | |

## C. D/TNW ratio

- **D/TNW = Total Debt ÷ TNW = ____x**  → **Flag if > 3x.**
- Pre-disbursement only — **Nandan's proposed facility is NOT included.**
- If a promoter-loan/CCD reclassification was applied, show the ratio **both ways** (with and without) and state which is the headline.

---

## D. Supporting ageing schedules (from Notes to Accounts — verify OCR)

> **⚠️ Provisioning default — apply, don't waive.** When a receivable or inventory balance sits in a bucket that triggers a haircut (180–365d, >365d), **apply the provision and flag it for verification.** Never set the provision to zero "pending verification" — the conservative lender default is to haircut, not to assume the favourable read. If applying it produces an extreme result (e.g. negative TNW), that is a finding to surface, not a reason to waive the rule. Flag the bucket for a source-PDF check, but the haircut stands until proven otherwise.
>
> **Use only the latest audited year's buckets.** Prior-year ageing does **not** govern the current year 

**Trade Receivables ageing** (Schedule III buckets):
| Not Due | <6m (0–180d) | 6m–1yr (180–365d) | 1–2yr | 2–3yr | >3yr | Total |
|---|---|---|---|---|---|---|
| | | | | | | |

**Inventory ageing** — *Schedule III does NOT mandate inventory ageing; often absent.* If not disclosed, write **"Not disclosed — inventory provisions cannot be computed"** and flag.
| <180d | 180–365d | >365d | Total |
|---|---|---|---|
| | | | |

**Trade Payables ageing** *(optional — supports CCC / creditor-days context in Section 5)*: ____

## E. Rule 5 — Debtors > 180 days as % of revenue

- Debtors > 180 days (= 180–365 + >365 buckets) = ₹____ Cr
- ÷ Total revenue ₹____ Cr = **____%**  → **Flag if > 10%.**

---

## G. Availability & flags

- What was available in the audited Notes vs. not: ____
- OCR confidence / any column-alignment doubts: ____
- Items requiring management confirmation (e.g. whether a promoter loan is subordinated / non-repayable before investment): ____
