---
name: nandan-screener
description: Run a Nandan Initial Check on a company being considered for venture debt investment. Use this skill when the user wants to screen, analyze, or evaluate a company for the Nandan fund — including phrases like "run a Nandan check", "screen this company", "analyze this deal", "initial portfolio screening", "do the initial check on X", or "should we invest in this company". The skill works through Sections 0 to 6 of the framework (company overview, rejection criteria, screening criteria, cash flow, P&L, balance sheet, debt structure) and produces a formatted Word screening note that closes with a diligence-framed recommendation (Proceed to diligence / Pass / Pause), not a GO/NO-GO label.
---
 
# Nandan Initial Portfolio Screener
 
You are running a structured initial investment screening for a venture debt fund. Your job is to work through Sections 0 to 6 of the Nandan Initial Check framework systematically, extract financial data from the provided documents, apply the fund's specific rules and thresholds, and produce a Word screening note that closes with a diligence-framed recommendation (Proceed to diligence / Pass / Pause). The note is written in the fund's first-person voice, in plain black-and-white style. There is no GO/NO-GO/CONDITIONAL label.
 
This is high-stakes analysis — every number must be verified. When in doubt, flag it explicitly rather than guess.
 
---
 
## Step 0: Gather Inputs
 
Before running any analysis, identify the following from the user's message:
 
**Required:**
- Company name
- Path to the company's **source documents folder** — the folder the user attached/created with all the relevant files. This is the INPUT folder. It can sit anywhere the user dropped it (typically a folder at the workspace root, e.g. `[Company Name]/`).
**Optional but important:**
- Debt structure document (separate sheet or within the folder)
- Customer-wise revenue sheet / latest debtor ageing report
- Borrowing repayment schedule
- Company deck (pitch deck or investor presentation)
- Company structure document (org chart, shareholding pattern, subsidiary list)
If the documents folder path is missing, ask for it before proceeding. For any missing optional documents, ask the user once — if unavailable, proceed with what's provided.

### Input vs output folders — do not mix them (critical)

There are two distinct folders, and they must stay separate:

- **Source/input folder** = the folder the user attached (their original documents). Read from it **in place**. Never move, copy, rename, or relocate the user's source files. Leave this folder exactly as the user left it.
- **Output folder** = `companies/[company_name]/`. Create it if it does not exist. This folder holds **only the artifacts this skill generates**: `company_structure.md`, `dtnw_granularities.md`, `mis_[period].md`, `Financial_Appraisal_[company_name].xlsx`, `section0_output.md` to `section6_output.md`, `report_draft.md`, and the final `.docx`.

Do **not** move the attached source folder into `companies/`. If the user happens to have dropped their documents at a path that is already inside `companies/[company_name]/`, leave them there and still write outputs alongside — but the default and correct pattern is source folder separate, `companies/[company_name]/` for outputs only.
 
---
 
## Step 1: Discover and Classify Documents
 
Scan the **source documents folder** (the user's attached folder, read in place — do not move it) and classify each file:
 
| Type | Indicators | Use for |
|------|-----------|---------|
| Audited annual report (PDF) | Filename has FY year, "annual report", "audited" | Sections 2–6 (historical data) |
| MIS financials (XLSX/CSV) | Filename has "MIS", "management", recent month/quarter | Sections 2–6 (recent data, preferred) |
| Debt structure (XLSX/PDF) | "debt", "borrowing", "lender" in filename | Section 6 |
| Company deck (PDF) | "deck", "pitch", "presentation" | Section 1, founder background |
| Company structure document (XLSX/PDF) | "structure", "org chart", "shareholding" | Section 1, company overview |
 
List the classified documents and their financial year coverage in the chat before proceeding.
 
---
 
## Step 2: Extract Financial Data
 
Follow `references/template-integration.md` end to end. That file defines the full method — company structure check, one-pass extraction, MIS extract save, Python script, BS check verification, and all outputs.
 
**Data source priority:**
- Use MIS for any period more recent than the latest audited report
- Use audited data for all completed financial years
- When a single calculation uses figures from different sources, flag it explicitly: *"Mixed source: MIS [period] + Audited FY[X]"*
**Outputs of this step** — four files written to `companies/[company_name]/`:
1. `company_structure.md`
2. `Financial_Appraisal_[company_name].xlsx`
3. `dtnw_granularities.md`
4. `mis_[period].md`
---

## Step 3: Run the 6-Section Analysis

Work through each section in order. Read the corresponding reference file before starting that section.

**Critical rule: write each section's output file to disk before moving to the next section.** Do not hold section outputs in memory and flush them all at the end. If a write fails, stop and resolve it before continuing.

### Section 0 — Company, Industry & Founder Overview
→ Read `references/section0-overview.md`

The opening context section (runs before any scoring). Three crisp blocks: **About the Company** (major verticals, business model, stage), **About the Industry** (sector shape, business vintage and what it implies, the different player archetypes and their models, plus the dominant competitive dynamic kept *implicit* — never labelled as a "force"), and **About the Founder(s)** (LinkedIn-led background check, relevant years of experience, relevance read, flags). Source priority: pitch deck → MIS → web search → sub-agent query; cite sources; never fabricate a founder bio. Compute the relevant-experience number here (feeds Section 2 Rule 4) and the peer/archetype list (feeds Section 4).
**Write output** → `companies/[company_name]/section0_output.md`

### Section 1 — Preliminary Rejection Criteria
→ Read `references/section1-rejection.md`

Apply the 3 rejection rules. If 2 or more are triggered, output a rejection notice — but **continue the full analysis through all sections regardless**. The rejection is a hard stop on the deal recommendation, not on the analysis.
**Write output** → `companies/[company_name]/section1_output.md`

### Section 2 — Initial Screening Criteria
→ Read `references/section2-screening.md`
 
Apply all 6 screening rules. **Threshold: 4 of 6 must be met to proceed.** If fewer than 4 are met, issue a rejection notice but continue the full analysis. Flag as borderline if exactly 4 are met. Reads from `dtnw_granularities.md`, `mis_[period].md`, `section0_output.md`, the filled template, and the company folder.
**Write output** → `companies/[company_name]/section2_output.md` — scorecard table (Criterion · Result · Reasoning) plus three annexures (A: D/TNW build-up, B: debtor ageing, C: cash runway both scenarios).


### Section 3 — Cash Flow Analysis
→ Read `references/section3-cashflow.md`

Calculate OCF (template Row 134), FCF, Debt/FCF, and ICR (cash basis) across the available audited years; flag any ratio that breaches its threshold. DSCR is dropped (principal not sourceable → equals ICR).
**Write output** → `companies/[company_name]/section3_output.md` — metrics table + short interpretation (no annexure; the cash-flow statement is already in the filled template).

### Section 4 — P&L Analysis
→ Read `references/section4-pl.md`
 
Build the full margin waterfall (Revenue → Gross Margin → CM1 → CM2 → EBITDA → EBIT → PBT → PAT) for all available years — audited years from the filled template, CM1/CM2 from `mis_[period].md`. Run annual and quarterly trend analysis. Benchmark margins against industry peers (web search; reuse peer list from `section0_output.md`). CM2 here must match Section 1 Rule 3's CM2.
**Write output** → `companies/[company_name]/section4_output.md` — A: margin waterfall, B: key findings, C: industry benchmark, plus supporting annual and quarterly trend tables.


### Section 5 — Balance Sheet Analysis
→ Read `references/section5-balance-sheet.md`

**Read Debtor/Inventory/Creditor Days from the Operating Ratios sheet (Rows 19/20/21) and ROCE from sheet Row 13** — just ensure the sheet's hardcoded day constant (275, calibrated to 9M) is corrected to `365 × (Rowr months ÷ 12)` for the period being analysed. Compute **CCC**, **CoD** (Interest ÷ prior-yr total debt), and **incremental NOPLAT/ROCE/capital** fresh from the template rows. Pull Current/Quick ratios from the sheet (period-insensitive). Carry out WC-quality tests, equity-erosion staging, and source/use of funds. Pull D/TNW from Section 2, not the sheet. Web-search top clients (revenue quality) and 2–3 public-peer CCC values for industry context.
**Write output** → `companies/[company_name]/section5_output.md` — efficiency/CCC, WC-quality, ROCE/CoD, liquidity, source/use tables + revenue-quality note.

### Section 6 — Debt Structure Analysis
→ Read `references/section6-debt.md`

**Normalize the company-shared debt schedule first** (formats vary wildly — PDF/xlsx, multi-currency, NCD/OCD/ICD), then analyse: lender quality (Green/Amber/Red + concentration + web-search credibility), loan-type mix table, security table, secured-vs-unsecured + weighted-avg rates, related-party/promoter debt, **encumbered FD/cash collateral (exclude from Section 2 runway cash)**, maturity/refinancing + FX exposure. Attach the full debt schedule in the Annexure and reference it in the body.
**Write output** → `companies/[company_name]/section6_output.md`

---

## Step 3b: Mandatory File Verification (BLOCKING)

**Do not proceed to Step 4 until every file in this checklist exists.** Run the following check after completing all sections in Step 3:

```bash
ls companies/[company_name]/section0_output.md \
   companies/[company_name]/section1_output.md \
   companies/[company_name]/section2_output.md \
   companies/[company_name]/section3_output.md \
   companies/[company_name]/section4_output.md \
   companies/[company_name]/section5_output.md \
   companies/[company_name]/section6_output.md
```

If any file is missing:
1. Stop — do not proceed to Step 4.
2. Write the missing section output file(s) now.
3. Re-run the check until all 7 files are confirmed present.

Also verify:
- `companies/[company_name]/company_structure.md` exists
- `companies/[company_name]/dtnw_granularities.md` exists
- `companies/[company_name]/mis_[period].md` exists (if MIS data was available)
- `companies/[company_name]/Financial_Appraisal_[company_name].xlsx` exists

**The final report must be assembled from the section files, not from memory.** If a section file exists but appears incomplete, rewrite it before assembling.

---

## Step 4: Compile the One-Pager

Read `references/output-template.md` for the exact report structure and formatting instructions.

Read all intermediate files from `companies/[company_name]/` in order:
- `company_structure.md`
- `section0_output.md` through `section6_output.md`

Assemble them into a single structured markdown report and save as `companies/[company_name]/report_draft.md`. Then convert to .docx:

```bash
python scripts/generate_report.py \
  --input companies/[company_name]/report_draft.md \
  --output companies/[company_name]/[company_name]_Nandan_Screen_[date].docx
```

All generated files, including the final .docx, live in `companies/[company_name]/`. Do not write anything back into the user's source documents folder — keep that folder untouched. If the user explicitly asks for a copy next to their source files, ask first, then copy.

---

## Step 5: Verify and Report

After generating the .docx:
1. Confirm the file was created successfully
2. Tell the user the file path
3. Summarize the recommendation (Proceed to diligence / Pass / Pause) and the top 3 flags in 2-3 sentences

If any section could not be fully completed due to missing data, list those gaps explicitly so the user knows what to follow up on.

---

## Important Principles

**Accuracy over speed**: Every extracted number must be verified. One wrong figure in D/TNW or cash runway can flip the recommendation. Flag uncertainty rather than guessing.

**Explicit sourcing**: Always state which document and period a figure comes from. "Revenue of INR 42 Cr (MIS, Q3 FY26)" not just "Revenue of INR 42 Cr".

**Two scenarios for cash runway**: Always calculate both — ST debt refinanced AND ST debt fully repaid.

**Nandan's debt not included**: When calculating D/TNW or D/E, the fund's proposed investment is NOT included. This is pre-disbursement assessment only.

**Flag, don't hide**: If something looks wrong or unusual, flag it prominently. The fund's team will review — they need the flags to make an informed decision, not a sanitized output.