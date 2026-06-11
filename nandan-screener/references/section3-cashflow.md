# Section 3 — Cash Flow Analysis

Cash flow tells you what the business actually *has*, not what it earns on paper. For a debt fund, repayment comes from cash — so these ratios answer: does the business generate enough real cash to service and retire its debt, without leaning on refinancing?

---

## Source — the filled template

Read from `companies/[company_name]/Financial_Appraisal_[company_name].xlsx`, sheet `Info and Adjustments`. The template auto-builds three cash flow statements from the balance sheets and P&L:
- **Cashflow from operations** = Row 134
- **Cashflow from financing** = Row 144
- **Cashflow from investing** = Row 155

**Which column to use:** first check whether the latest MIS column has a populated Row 134 (a cash flow requires two consecutive balance sheets behind it — if the MIS had a balance sheet, the template will have built it). If Row 134 is populated in the MIS column, use that as the latest period. Otherwise fall back to the latest audited FY column. Then compute for every earlier audited year where Row 134 is also populated.

**Consistency rule:** once you have chosen a column (period), use that same column for OCF, Capex, FCF, and Total Debt throughout. Do not mix figures across columns.

---

## Core Metrics

### OCF — Operating Cash Flow
**= Row 134** — already after working-capital movements and before interest. This is the base the coverage ratios need.

### FCF — Free Cash Flow
**= OCF − Capex**, where Capex = Row 147 (tangible) + Row 148 (intangible), stored as negative cash impacts.
```
FCF = Row 134 + Row 147 + Row 148
```
FCF is what is actually left to service debt after maintaining/growing the asset base. Strong OCF with heavy capex can leave little or no FCF — that distinction is the point.

### Debt / FCF
**= Total Debt ÷ FCF**, where Total Debt = Row 57 (LT Borrowings) + Row 62 (ST Borrowings) — from the same column.

| Debt / FCF | Reading |
|---|---|
| < 2x | Very healthy — can retire debt in under 2 years |
| 2x – 4x | Comfortable — standard for stable businesses |
| 4x – 6x | Elevated — manageable if growth is strong |
| 6x – 8x | Stressed — needs consistent FCF growth |
| > 8x | Danger zone — essentially dependent on refinancing |

**Flag if Debt / FCF > 6x.** If FCF ≤ 0, the ratio is not meaningful — flag as *"FCF negative — debt cannot be retired from operating cash"*. Do not read a negative ratio as low or healthy.

### ICR — Interest Coverage (cash basis)
**= FCF ÷ Interest**, where Interest = Row 23 (same column).
```
ICR = (Row 134 + Row 147 + Row 148) ÷ Row 23
```
**Flag if ICR < 1x** — the business cannot cover even its interest from free cash flow. More reliable than EBIT-based interest cover because it uses actual cash, not accounting profit. FCF < 0 → ICR negative → fails.

### DSCR — not computed (deliberately)
DSCR = (OCF − Capex) ÷ (Interest + Principal). Principal repayments need a repayment schedule, which is rarely provided. Under the standing assumption that long-term principal is refinanced (principal = 0), DSCR collapses to exactly ICR — so it adds nothing here and is skipped.

---

## Period Basis and Trend

Compute each metric for every column where Row 134 is populated and read the trajectory — is OCF/FCF improving or deteriorating? A one-year snapshot can mislead; the trend is the signal.

---

## Output

Write to `companies/[company_name]/section3_output.md` — a metrics table and a short interpretation. No annexure — the cash flow statement already lives in the filled template.

```
Section 3 — Cash Flow Analysis

| Metric        | FY__ | FY__ | Threshold | Flag |
|---------------|------|------|-----------|------|
| OCF (₹ Cr)    |      |      | —         |      |
| Capex (₹ Cr)  |      |      | —         |      |
| FCF (₹ Cr)    |      |      | > 0       |      |
| Total Debt    |      |      | —         |      |
| Debt / FCF    |      |      | ≤ 6x      |      |
| ICR (cash)    |      |      | ≥ 1x      |      |

Interpretation: [2–3 lines — can the business service (ICR) and retire (Debt/FCF) its debt
from operating cash? Trend across years? Call out any flagged ratio and any
not-meaningful (negative-FCF) case.]
```