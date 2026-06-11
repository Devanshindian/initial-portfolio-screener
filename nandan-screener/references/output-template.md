# Output Report Template - Nandan Initial Screening

This file is the compiler's instruction for assembling the final screening note. Read every intermediate output (`company_structure.md`, `section0_output.md` to `section6_output.md`) and weave them into one document in the structure below.

Body order: header, then Section 0, then Sections 1 to 6, then Key Flags, then Recommendation, then Annexures.

Each section's table shapes are mirrored from the section reference files (`section0-overview.md` to `section6-debt.md`). Keep each section's content and tables intact to the maximum extent. Your job here is presentation: better language, connective narrative, and one consistent voice across the whole note. Every heading must appear even when data is thin. Mark genuinely missing pieces as *"Data not available at initial screening stage."* When the section reference and this template disagree on a table shape, the reference file is the source of truth.

(Note on dashes: headings and prose use a plain hyphen, never an em dash. The only dash convention kept is the short "–" marker in the Section 4 waterfall, which means "not computed on audited-only years". See the writing rules below.)

---

## House Style / Voice

The note is written as the fund speaking in the first person. It reads like an analyst's memo to the investment committee, not a detached machine report. Follow these rules throughout.

**What the voice is**

1. Fund voice. Use "we". For example "We shall proceed with diligence", "we would like an escrow on municipal inflows", "Our focus in diligence will be". The recommendation and the interpretive lines are the fund's own read.
2. Source every figure inline. Never a bare number. Write "Revenue ₹91.7 Cr (MIS, 11M audited plus March provisional)", not "Revenue ₹91.7 Cr". Flag any figure that mixes sources in one calculation, for example "Mixed source: MIS [period] plus Audited FY[X]".
3. Frame weaknesses peer-relative, not just flagged. A weak number is only half the story. Say whether it is structural to the sector or specific to this company. Benchmark against a named listed peer and, where useful, sector examples. For instance "272 debtor days vs Antony Waste's ~110, high, but municipal-waste collection runs long sector-wide". This is what separates a screen from a checklist.
4. Be honest about gaps and name the diligence step. When a number is proxied or a document is missing, say so and say how diligence will close it. For example "No customer-wise revenue sheet shared yet, so concentration is proxied from the debtor ageing, to be reconfirmed on a revenue basis in DD".
5. Let tables carry interpretation. Every table gets a Comment or Notes column or a one-line read beneath it. The reader should never have to compute the takeaway themselves.
6. Read naturally. Connect the tables with short narrative. Do not stack tables with no prose between them. The note should flow, not feel like a form that was filled in.

**How to write so it does not read like AI**

7. No em dashes or en dashes in prose. This is the single biggest tell. Use a comma, a colon, parentheses, or just start a new sentence. Write "high, but explained by scale", not "high — but explained by scale".
8. No emoji, no icons, no decorative symbols, no colour words standing in for icons. Severity is said in plain words (Fatal, Critical, High, Medium, Low) and structure comes from headings and spacing, not colour.
9. Avoid the AI vocabulary and constructions that give writing away:
   - Inflated words: delve, leverage (as a verb), robust, comprehensive, seamless, pivotal, crucial, vital, testament, underscore, navigate, landscape, realm, tapestry, boasts, harness, foster, garner, myriad, plethora, vibrant, ecosystem (unless literally a business ecosystem).
   - Antithesis cliches: "it's not just X, it's Y", "not only X but also Y", "this isn't about X, it's about Y".
   - Transition stacking: Moreover, Furthermore, Additionally, In addition, Notably at the start of sentence after sentence.
   - Empty hedges and closers: "It's worth noting that", "It's important to note", "In conclusion", "Overall", "Ultimately".
   - Forced rule-of-three lists where two items would do.
   - Vague intensifiers: significantly, substantially, a wide range of.
10. Plain sentences. Mostly short and declarative, like someone typing the memo quickly. Vary sentence length so it is not metronomic. Do not bold every other phrase, and do not Title Case headings.
11. A little natural imperfection is fine and wanted. The odd missing comma, a comma splice here and there, a sentence that starts with "And" or "But". This makes it read human. Numbers, names, and figures must always be exact, never approximate the maths to look casual.

---

## Report Structure

```
# [COMPANY NAME] - Nandan Initial Screening Note

Date: [DD Month YYYY]
Prepared by: Nandan Fund, Initial Screener
Ask: [INR X to Y Crore] or [Not provided]
Tenure: [N months] or [Not provided]
Securities offered: [PG, pledge of shares, charge, FD, ...] or [Not provided]
Financials used: [Consolidated / Standalone], [audited FYs plus MIS period]
Recommendation: [Proceed to diligence] / [Pass] / [Pause, pending listed items]

---

## Section 0 - Company, Industry and Founder Overview

### About the Company
[1 to 2 sentence description: what it sells, to whom (B2B, B2C, B2B2C), geography, channel.]

| Vertical | What it is | % of revenue |
|----------|-----------|--------------|
| [Vertical 1] | [one line] | [X% / n.a.] |
| [Vertical 2] | [one line] | [X% / n.a.] |

Business model: [transactional or recurring, how revenue is earned]. Stage: [early / scaling / mature], about ₹[X] Cr revenue.

(Legal and ownership: [standalone / parent / subsidiary of X], [N] subsidiaries, [consolidated or standalone] financials used. From company_structure.md.)

### About the Industry
[1 to 2 sentences on the sector, size and growth with source.]
Vintage: [N years operating] against a [mature / young / cyclical] industry. [What it implies for brand, operating experience, cycle resilience.]

| Player archetype | Example(s) | Business model in one line |
|------------------|-----------|----------------------------|
| [Listed incumbents] | [names] | [one line] |
| [VC-funded D2C / challengers] | [names] | [one line] |
| [Unorganised / regional] | [n.a.] | [one line] |

[Optional 1 to 2 sentences on the dominant competitive dynamic, in plain language, woven in, never labelled as a "force". Omit if nothing dominates.]

### About the Founder(s)
| Founder | Role | Background (LinkedIn-verified) | Relevant exp. | Relevance / flags |
|---------|------|-------------------------------|---------------|-------------------|
| [Name] | [role] | [education, prior roles, source] | [N yrs] | [fit read, any flag] |

Sources: [deck, LinkedIn, web].

---

## Section 1 - Preliminary Rejection Check

(Three rules. We reject the deal if two or more are triggered, though the full note still runs regardless.)

| Rule | Triggered? | Finding |
|------|-----------|---------|
| 1, Deep Technology | Yes / No | [brief, sourced reason] |
| 2, Government Revenue (over 30%) | Yes / No | [for example "about ₹89.6 Cr of ₹91.7 Cr revenue (98%) is municipal, almost entirely government"] |
| 3, Negative Unit Economics (CM2 at or below 0, or CM1 below 0) | Yes / No | [CM2 = ₹X Cr (Y% of rev), quarterly trend if monthly MIS] |

Outcome: [PASS, 0 of 3] / [PASS with flag, 1 of 3] / [REJECTED, 2 or more triggered].
[If one rule: one-line flag carried to Key Flags. If reject: "The full analysis below still runs. The rejection is surfaced again in our recommendation."]

---

## Section 2 - Initial Screening Criteria

(Six criteria. We need at least four met. Five or six is clean, exactly four is borderline, three or fewer is a screen-out.)

| # | Criterion | Met? | Basis |
|---|-----------|------|-------|
| 1 | Operating history over 2 yrs | Met / Not met | [N yrs, later of incorporation or ops-commencement, source] |
| 2 | Annualised revenue over ₹15 Cr | Met / Not met | [₹X Cr vs ₹15 Cr, source, how annualised, run-rate check] |
| 3 | D/TNW at or below 3x | Met / Not met | [D/TNW (audited) = X.Xx (Debt ₹__ over TNW ₹__). D/E (MIS) = Y.Yx (Debt ₹__ over Equity ₹__). Decided on the audited 3x test. Negative TNW fails. See Annexure A] |
| 4 | Promoter experience over 4 yrs | Met / Not met | [name, N yrs in domain, from Section 0] |
| 5 | Debtors over 180 days below 10% of revenue | Met / Not met | [₹X Cr = Z% of revenue vs 10%, audited FY ageing. See Annexure B] |
| 6 | Operating-profitable or runway over 6 mo | Met / Not met | [cash-generative? else runway M mo (refinanced) / M' mo (repaid) vs 6-mo floor. See Annexure C] |

Outcome: [X] of 6 met, [PASS / PASS, borderline / SCREEN-OUT].
[Flags: borderline if exactly four, any "Not met, unverified" rule, simplified D/E over 2.5x, fully-repaid runway under 6 mo. If screen-out: "We continue the analysis below. The screen result is reflected in our recommendation."]

The D/TNW that drives criterion 3 is built up in full in Annexure A. The working below summarises it.

| Adjusted Tangible Net Worth build | ₹ Cr |
|-----------------------------------|------|
| Equity plus Reserves and Surplus | [__] |
| (+) CCDs / quasi-equity | [__] |
| (−) Intangibles, DTA, fictitious assets | ([__]) |
| (−) Debtor ageing haircuts (180 to 365d at 75%, over 365d at 100%) | ([__]) |
| Adjusted Tangible Net Worth | [__] |
| Total existing debt (excl. CCDs, Nandan's proposed debt excluded) | [__] |
| D / TNW | [X.Xx] |

---

## Section 3 - Cash Flow Analysis

For a debt fund, repayment comes from cash. So the question here is whether the business throws off enough real cash to service (ICR) and retire (Debt to FCF) its borrowings without leaning on refinancing.

| Metric | FY[X] | FY[X-1] | Threshold | Flag |
|--------|-------|---------|-----------|------|
| OCF (₹ Cr) | | | n.a. | |
| Capex (₹ Cr) | | | n.a. | |
| FCF (₹ Cr) | | | over 0 | |
| Total Debt (₹ Cr) | | | n.a. | |
| Debt / FCF | | | 6x or below | [flag if over 6x, "FCF negative" if FCF at or below 0] |
| ICR, cash basis (FCF over Interest) | | | 1x or above | [flag if below 1x] |

Our read: [2 to 3 lines. Can the business cover interest and retire debt from operating cash? What is the trend across years? Call out any flagged or not-meaningful (negative-FCF) ratio.]
(DSCR is dropped. Principal is rarely sourceable, and with LT principal assumed refinanced it collapses to ICR.)

---

## Section 4 - P&L Analysis

MIS-led for the contribution-margin detail, with the full waterfall built for every available year.

### A. Margin Waterfall

| Level | FY[X-1] ₹ Cr | FY[X-1] % | FY[X] ₹ Cr | FY[X] % | MIS [period] ₹ Cr | MIS [period] % | Trend |
|-------|---|---|---|---|---|---|-------|
| Revenue | | | | | | | [YoY growth, Q-trajectory note] |
| Gross Margin | | | | | | | [GM% trend, fatal if negative] |
| CM1 | – | – | – | – | | | [MIS only, variable ops, critical if negative] |
| CM2 | – | – | – | – | | | [MIS only, unit economics, high concern if negative] |
| EBITDA | | | | | | | [EBITDA% trend, flag if negative] |
| PAT | | | | | | | [trend read] |

(CM1 and CM2 are "–" on audited-only years. CM2 here equals Section 1 Rule 3 CM2.)

### B. Key Findings
[4 to 5 lines, our interpretation. (1) Unit economics, is CM2 positive and stable? (2) Margin trajectory, expanding or contracting, and why? (3) Operating leverage, are fixed costs falling as a percentage of revenue with scale? (4) Any red flag, finance cost creeping up, Other Income propping up PBT, a one-off distorting the read.]

### C. Industry Benchmark

| Company | Revenue (₹ Cr) | Gross Margin % | EBITDA % | Notes |
|---------|----------------|----------------|----------|-------|
| [Subject] | | | | |
| [Peer 1] | | | | [scale or model difference] |
| [Peer 2] | | | | |
| Industry average | | | | |

[One line on the variance, framed structurally. Over 5% below industry, explain (scale, model, cost structure). Over 10% below, treat as a red flag. Above, positive, but verify it is sustainable.]

#### Supporting Data, Trend Tables
(detailed, for reference)

Annual trend (% of revenue)

| Metric | FY[X-1] % | FY[X] % | MIS [period] % | Trend |
|--------|-----------|---------|----------------|-------|
| Revenue YoY growth % | | | | |
| Gross Margin % | | | | |
| CM1 % | – | – | | |
| CM2 % | – | – | | |
| EBITDA % | | | | |
| EBIT % | | | | |
| PBT % | | | | |
| PAT % | | | | |
| Employee cost % | | | | |
| Finance cost % | | | | |
| Marketing % | | | | |
| Rent / fixed overhead % | | | | |

Quarterly trend (only if MIS is monthly or quarterly, else note "MIS is annual, quarterly breakdown not available")

| Metric | Q1 % | Q2 % | Q3 % | Q4 % | Trend |
|--------|------|------|------|------|-------|
| Revenue (₹ Cr) | | | | | |
| Gross Margin % | | | | | |
| CM1 % | | | | | |
| CM2 % | | | | | |
| EBITDA % | | | | | |
| Employee cost % | | | | | |
| Finance cost % | | | | | |
| Marketing % | | | | | |
| Rent / overhead % | | | | | |

---

## Section 5 - Balance Sheet Analysis

How the business is funded and how efficiently capital is used, and whether short-term money is being stretched to cover long-term assets.

### A. Efficiency and Cash Conversion Cycle

| Metric | FY[X-1] | FY[X] | MIS [period] annualised | | [Subject Co] | [Peer 1] | [Peer 2] |
|--------|---------|-------|-------------------------|--|--------------|----------|----------|
| Debtor Days | | | | | | | |
| Inventory Days | | | | | | | |
| Creditor Days | | | | | | | |
| CCC (days) | | | | | | | |

[One line: which CCC band, trend direction, and how it sits against peers. Flag if over 90 days, and say whether the level is sector-structural or company-specific.]

### B. Working-Capital Quality

| Check | Finding | Read |
|-------|---------|------|
| Profit real? | [Debtor or Inventory days trend, for example "35, 42, 51, stretching"] | OK / Concern |
| ΔWC over Revenue growth | [for example "ΔWC ₹8 Cr over ₹10 Cr growth = 0.8x, proportional"] | OK / Concern |
| ROCE over cost of funding? | [for example "ROCE 14% vs CoD 11%, debt-funded WC is value-accretive"] | OK / Concern |

[One-line overall verdict on working-capital quality.]

### C. Return on Capital vs Cost of Debt

| Year | ROCE | CoD | ROCE minus CoD | Earnings cover interest? | Stage (1 to 4) |
|------|------|-----|----------------|--------------------------|----------------|
| [FY] | | | | Yes / No | |

Incremental: NOPLAT change ₹[X] Cr over Capital change ₹[X] Cr = Incremental ROCE [X]% vs CoD [X]%, above or below cost.
[One line: is each new rupee of capital, including Nandan's, being deployed above or below its cost?]

### D. Liquidity

| Ratio | Value | Benchmark | Flag |
|-------|-------|-----------|------|
| Current Ratio | | over 1.2x | |
| Quick Ratio | | over 1.0x | |

[One line if the headline ratios overstate liquidity, for example current assets that are mostly receivables.]

### E. Source and Use of Funds

| | Short-term (₹ Cr) | Long-term (₹ Cr) |
|---|---|---|
| Sources | [ST borrowings plus payables plus other CL] | [Equity plus LT debt plus other NCL] |
| Uses | [Receivables plus inventory plus cash plus other CA] | [Fixed assets plus CWIP plus other NCA] |

ST sources ₹[X] Cr vs ST uses ₹[X] Cr, [Matched / Mismatch, ₹[X] Cr of short-term money funding long-term assets].

### F. Revenue Quality (top clients)

| Client | Revenue / receivables share | Listed / Unlisted | Credibility read |
|--------|------------------------------|-------------------|------------------|
| [Name] | [X%] | | [solvency, reputation, any flag] |

[One line on concentration. Is the business dangerously reliant on a handful of clients, and how does that read against the sector?]

---

## Section 6 - Debt Structure

Who lends, on what terms, against what security, and where the concentration or refinancing risk sits.

Lender profile: [Green / Amber / Red], [reason]. Lenders: [N], largest [X]% of debt, banks [X]% vs non-banks [X]%. [Web-search credibility note.] Total debt ₹[X] Cr vs BS borrowings ₹[X] Cr [reconciliation flag if a gap].

Loan-type mix:

| Facility type | # | Outstanding (₹ Cr) | % of debt | Rate range | Typical tenure |
|---------------|---|--------------------|-----------|------------|----------------|
| [CC, OD, Term, NCD, OCD, ICD, ...] | | | | | |

Security:

| Facility type | Typical security / collateral | Guarantee |
|---------------|-------------------------------|-----------|
| [type] | [stock, FD lien, property, none] | [personal, corporate, none] |

- Secured vs unsecured: [X]% / [X]%. Weighted-avg rate: [X]% (secured [X]%, unsecured [X]%). Reported neutrally. A higher unsecured share is often just a lack of collateral to pledge, not banks declining.
- Related-party or promoter debt: ₹[X] Cr ([X]%), [quasi-equity treatment in D/TNW if applicable].
- Encumbered FD or cash collateral: ₹[X] Cr locked, excluded from the Section 2 runway cash.
- Maturity and FX: ST-revolving [X]%, LT [X]%. Near-term maturities [flag if large, refinancing risk]. Foreign-currency debt [₹X Cr, FX risk, or none].

Full reformatted debt schedule attached in Annexure D.

---

## Key Flags

Priority order. Each line feeds the Weaknesses in our recommendation. Severity is stated in words: Fatal, Critical, High, Medium, Low.

| Flag | Severity | Section | Detail |
|------|----------|---------|--------|
| [description] | [Fatal / Critical / High / Medium / Low] | [#] | [one line, peer-relative where it matters] |

---

## Recommendation

[We shall proceed with due diligence.] / [We recommend passing on this opportunity.] / [We suggest pausing, pending the items below.]

[2 to 4 sentences in the fund's voice setting out the headline read. What makes this investable or not, and the one or two issues that dominate the decision. Where Section 1 or Section 2 screened the deal out, say so here and why.]

Strengths
- [bullet, sourced]
- [bullet]

Weaknesses
- [bullet, framed peer-relative or structural-vs-specific where possible]
- [bullet]

Areas for further deep diligence
- [what diligence must confirm, for example "customer and contract concentration on a revenue basis", "contract-wise collection track record plus two prior audited years", "cash runway"]

Suggested structure or mitigants
- [concrete asks, for example escrow or account-control on key inflows, single-client exposure covenant cap, first or second charge, additional security]

---

## Annexures

Annexure A, D/TNW Build-up (from `dtnw_granularities.md`): the TNW ladder (Equity and reserves, less intangibles, IAUD, DTA, other fictitious assets, ageing haircuts, equals TNW), the Total Debt ladder (LT plus ST borrowings plus contingent liabilities likely to crystallise, less CCDs and promoter subordinated loans), the D/TNW ratio with values, and the supplementary MIS simplified D/E with values.

Annexure B, Debtor Ageing (from the latest audited Notes via `dtnw_granularities.md`): Not Due, under 6m, 6m to 1yr, 1 to 2yr, 2 to 3yr, over 3yr buckets, and the over-180-day total as a percentage of revenue (the Rule 5 number).

Annexure C, Cash Runway (both scenarios): burn build-up and runway for Scenario 1 (ST refinanced) and Scenario 2 (ST fully repaid), side by side. Period Cash Generation or Burn, monthly burn, unencumbered cash, runway in months. If operating cash-generative, state runway is effectively unlimited.

Annexure D, Debt Schedule: the full reformatted debt schedule from Section 6 (all lenders, amounts, rates, tenures, security, repayment).

---

Data sources used in this note:
- [Source 1]: [document name, financial year, section]
- [Source 2]: [document name, period]
```

---

## Formatting Notes for generate_report.py

Black and white only. No colour, no shaded banners, no icons or emoji. Structure comes from headings, spacing, and horizontal rules, not from colour.

- Heading hierarchy: H1 for the company name, H2 for section titles (including "Section 0 ..."), H3 and H4 for subsections (A, B, C ...). Use sentence case for headings, not Title Case.
- Separate every section with a horizontal rule and clear vertical spacing so the eye can navigate by structure.
- Tables: plain Word "Table Grid", thin black borders, no fill. A light grey header row is acceptable but optional. Keep the Comment or Notes columns, they carry the read.
- Severity and ratings are words, never symbols: Fatal, Critical, High, Medium, Low for flags, and Green, Amber, Red spelled out for the lender profile.
- Font: a single neutral typeface throughout (Calibri or Times New Roman), 11pt body, 14pt H1, 12pt H2, all in black. Page margins 2cm on all sides.
- Footer, plain text: Nandan Fund, Confidential. [Company Name]. Initial Screening. [Date].
- Do not add any em dash or en dash in generated prose. The renderer should not "prettify" hyphens into dashes.
