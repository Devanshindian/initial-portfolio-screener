# Section 6 — Debt Structure Analysis


How the company is borrowed — *who* lends, on *what terms*, against *what security*, and where the concentration / refinancing risks sit. Built from the company-shared debt document 

## Source & Step 0 — Normalize the debt schedule (do this first)

The debt document is company-shared and arrives in **any** format — PDF or xlsx, wildly different columns (some group by ST/LT, some are multi-entity & multi-currency, some are all private debentures with the rate buried in a label). So before analysing anything, **normalize every facility into one common row**:

| Field | Notes |
|---|---|
| **Lender** | name |
| **Lender category** | Bank / NBFC / AIF-or-Fund / NCD-OCD (private debenture) / ICD / Promoter-Director-Related |
| **Facility type** | CC, OD, Term Loan, WCDL, Bill Discounting, Auto Loan, NCD, OCD, ICD, Unsecured Loan |
| **Outstanding (₹ Cr)** | convert any FX (USD/AED) to INR at the stated rate — **flag the conversion** |
| **Interest rate** | from a rate/ROI column, *or* embedded in a "type heading" (e.g. "NCD ‑17%") |
| **Tenure / maturity** | months, or final-repayment date; "repayable on demand" for revolving lines / ICDs |
| **Security / collateral** | stock hypothecation, FD lien, property charge, car hypothecation, none |
| **Guarantee** | personal / corporate guarantee given |
| **Related-party flag** | director / relative / related-company / promoter ICD? |

---

## Step 1 — Lender quality / profile

Classify the lender base:

| Lender profile | Signal |
|---|---|
| 1–3 lenders, mostly large scheduled banks | 🟢 **Green** — banks are selective; their presence is credit validation |
| Mix of banks and NBFCs / AIFs | 🟡 **Amber** — banks likely at their exposure limit; higher-cost capital filling the gap |
| Only NBFCs / AIFs / ICDs — no bank exposure | 🔴 **Red** — absence of bank lending suggests banks declined |
| Single lender — promoter / holding-co ICD only | 🔴 **Red** — no third-party market validation of creditworthiness |

Plus:
- **Lender count** and **concentration** — the largest lender as a % of total debt (heavy dependence on one lender is a risk).
- **Bank vs non-bank split** — % of debt from scheduled banks.
- **Web-search any unfamiliar lenders** — reputable banks / established NBFCs / known AIFs, or obscure? Note credibility.

---

## Step 2 — Loan-type (facility) mix

| Facility type | # facilities | Outstanding ₹ Cr | % of debt | Interest-rate range | Typical tenure |
|---|---|---|---|---|---|

What kinds of debt the company runs on and on what terms (e.g. CC/OD = working capital, ~8–9%, revolving · Term loans 9–16%, 36–60M · NCD/OCD 15–18%, 24–36M · ICD/promoter, on-demand).

---

## Step 3 — Security / collateral

| Facility type | Typical security / collateral | Guarantee |
|---|---|---|

Map each facility to what's pledged — e.g. CC/OD → stock hypothecation; Term loan → FD lien / property charge; Auto loan → car hypothecation; Unsecured loan / NCD → none (sometimes a personal guarantee).

---

## Step 4 — Secured vs Unsecured + average rates

- **Secured vs unsecured split** — % of outstanding that is secured vs unsecured.
- **Weighted-average interest rate** = Σ(rate × outstanding) ÷ Σ outstanding — report it **overall and split by secured / unsecured** (secured is usually cheaper).
- **Read it neutrally** — a higher unsecured share at higher rates is **not** automatically "banks declined": founders often simply lack collateral to pledge. Just report the mix and the blended cost; don't editorialise.

--- 

## Step 5 — Related-party / promoter debt

- Amount & % of debt from **directors / relatives / related companies / promoter ICDs** (the docs flag these — a "Related" Yes/No column, a "Directors and Relatives" group, or a guarantee column).
---

## Step 6 — Maturity / refinancing + FX

- **Maturity split** — short-term revolving (CC/OD, repayable-on-demand ICDs) vs long-term (term loans, NCDs).
- **Near-term maturities** — flag if a large share of debt falls due within ~12 months → **refinancing risk** (acute if the lender profile is already amber/red or credit conditions tighten).
- **FX exposure** — any foreign-currency debt (USD / AED, as in the Vananam tracker) carries currency risk on servicing. Note the FC-denominated outstanding and the rupee-depreciation sensitivity.

---

## Annexure

**Always attach the full (normalized) debt schedule** as an annexure, and in the body simply state *"detailed debt schedule attached in the Annexure."*

---

## Output

Write to `companies/[company]/section6_output.md`:

1. **Lender profile** — verdict 🟢/🟡/🔴 + reason; lender count, concentration (largest lender %), bank vs non-bank split; web-search credibility note.
2. **Loan-type table** — facility type · # · ₹ Cr · % of debt · rate range · tenure.
3. **Security table** — facility type · typical security · guarantee.
4. **Secured vs unsecured + avg rate** — % secured / unsecured; weighted-avg rate overall and by secured/unsecured.
5. **Related-party debt** — ₹X Cr (Y%); note the D/TNW quasi-equity reclassification if applicable.
6. **Encumbered FD / cash collateral** — ₹X Cr locked → flag to exclude from Section 2 runway cash.
7. **Maturity / refinancing + FX** — ST vs LT split, near-term-maturity flag, FC debt + FX risk.
8. **Annexure pointer** — "Full debt schedule attached in the Annexure."