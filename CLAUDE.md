# Nandan Initial Portfolio Screener - Project Context

## What This Project Is

A Claude skill (`nandan-screener`) that automates the Nandan venture debt fund's initial company screening framework. Investment bankers send companies to the fund; the skill runs a structured analysis across Sections 0 to 6 and produces a formatted Word (.docx) screening note. The note closes with a diligence-framed recommendation (Proceed to diligence / Pass / Pause) plus Strengths, Weaknesses, and Areas for further deep diligence. It is written in the fund's own voice, in plain black-and-white style, no GO/NO-GO label.

Status: the skill is built. Sections 0 to 6 reference files are complete, the report template and the Markdown-to-docx generator are done. Optional remaining work: a full end-to-end run on a live company, and skill-description tuning.

## How to Resume After a New Chat

If you start a fresh session in this directory, the memory index loads automatically. The two relevant memories are:
- `memory/project_screener.md` - goal, architecture, framework
- `memory/output_template_voice.md` - the report's house voice and the no-GO/NO-GO decision

Memory folder: `~/.claude/projects/-Users-devanshasawa-Desktop-initial-portfolio-screener/memory/`

---

## Directory Structure

```
initial-portfolio-screener/
├── CLAUDE.md                              ← this file
├── skill.md                              ← skill manifest + orchestration (the full workflow)
├── [CompanyName]/                         ← SOURCE docs the user attaches (INPUT, read in place, never moved)
├── templates/
│   ├── Financial Appraisal Template.xlsx  ← P&L, Balance Sheet, Operating Ratios
│   └── DTNW_Granularities_Template.md     ← skeleton for D/TNW granularities (ageing, haircuts, reclassifications)
├── companies/                             ← OUTPUT only: one folder per company, holds generated artifacts (no source docs)
│   ├── BananaClubInVogue/                 ← test company (audited FY25+FY24; MIS FY26)
│   ├── Vananam/                           ← test company (consolidated; Dec'25 MIS + FY25 + FY24)
│   ├── Monedo/                            ← test company (NBFC)
│   └── Popees/                            ← test company
└── nandan-screener/
    ├── references/
    │   ├── output-template.md             ← final report structure, house voice, and B&W formatting rules
    │   ├── section0-overview.md           ← company / industry / founder context; runs before Section 1
    │   ├── section1-rejection.md          ← 3 hard-stop rejection rules
    │   ├── template-integration.md        ← populate the xlsx from audited PDFs; read ratios back
    │   ├── section2-screening.md          ← 6 screening criteria (need 4/6)
    │   ├── section3-cashflow.md
    │   ├── section4-pl.md
    │   ├── section5-balance-sheet.md
    │   └── section6-debt.md
    ├── scripts/
    │   └── generate_report.py             ← Markdown → .docx (black-and-white house style; python-docx, no pandoc)
    └── evals/
        └── evals.json
```

Note on layout: the manifest is `skill.md` at the project root, while `references/`, `scripts/`, and `evals/` live under `nandan-screener/`. If you ever consolidate the skill into a single folder, move `skill.md` in alongside them and check the relative paths.

---

## Key Rules (critical, do not get these wrong)

### Section 1 - Preliminary Rejection (reject the deal if 2+ of 3 rules triggered)

**Rule 1 - Deep Technology**
- Triggered if: core product is IP/research-stage, revenue is unpredictable or nil/very low (under about INR 5 Cr annualised), or the company is in a deep-tech sector without proven commercial revenue.
- Deep-tech sectors: biotech, life sciences, pharma R&D, defense tech, aerospace/space, quantum computing, semiconductors (R&D stage), advanced materials, neuro-tech, clean energy (early stage), advanced robotics (hardware, pre-revenue), agri-biotech, next-gen comms.
- NOT deep tech: tech-enabled services such as AI/ML platforms, SaaS, fintech, edtech, however sophisticated.

**Rule 2 - Government Revenue**
- Triggered if: over 30% of the most recent year's revenue comes from govt/PSU/PSB clients.
- "Government" includes central and state govt, PSUs (ONGC, NTPC, SAIL etc.), public sector banks, govt-controlled entities, municipal bodies.
- Assess using the most recent year (MIS preferred over audited if more recent).

**Rule 3 - Negative Unit Economics**
- Metric: CM2 (marketing-inclusive) = Revenue minus COGS minus Logistics minus Marketing/ad minus Sales commission minus Payment processing minus Packing minus other directly-variable costs. Exclude Other Income. CM2 must be over 0.
- Triggers if CM2 at or below 0, or CM1 (Revenue minus COGS) below 0 (selling below cost auto-triggers).
- Trend-aware: with monthly MIS, compute CM2 by quarter and raise a deterioration flag (not an auto-trigger) if the latest quarter turns negative while the full period is positive. Annual-only MIS, assess on the annual figure.
- A net-loss-making company can still pass (the loss may be fixed-cost or financing-driven, not a unit problem). Full logic in `references/section1-rejection.md`.

Logic: 0 or 1 rules, pass (1 rule, carry as a flag). 2 or 3 rules, reject. Rejection is a hard stop on the deal recommendation only; the full analysis through all sections still runs and is included in the note.

### Section 2 - Initial Screening
- 4 out of 6 criteria must be met (not 3 out of 5, do not get this wrong).
- Exactly 4 met = borderline flag, still passes.

### Data Source Priority
- MIS first (more recent), audited second.
- Flag explicitly when mixing sources in a single calculation.

### Excel Template
- The skill populates the Financial Appraisal Template, then reads auto-calculated ratios back out for Sections 3 to 5.
- Nandan's proposed investment is NOT included in D/TNW or D/E calculations (pre-disbursement only).
- **Three failure modes that have actually shipped broken sheets (full detail in `references/template-integration.md` → "Hard-won gotchas"):**
  1. The blank template carries the previous company's numbers as formulas in the input cells. **Clear all input rows to 0 before writing**, or leftovers corrupt the balance sheet.
  2. openpyxl writes formulas but does not compute them, so totals / Row 88 check / Operating Ratios sheet are **blank until recalculated**. Set `fullCalcOnLoad`, recalc (LibreOffice headless if available), and verify Row 88 = 0 in the *recomputed cell* — a Python re-sum of your own inputs is not proof the sheet balances.
  3. Template bug: cell `R82` has a hardcoded `+0.1` that unbalances the adjusted FY25 column by 0.1; raw input columns C–F are unaffected. Services companies (no inventory/COGS) also throw `#DIV/0!` in Inventory/Creditor Days — expected, not a data error.

### D/TNW Granularities (Section 2 Rule 3, feeds Rule 5 too)
- The xlsx holds only single net balances. The D/TNW build-up needs detail it cannot store: ageing buckets, provisioning haircuts, CCD/promoter-loan reclassifications, contingent liabilities, fictitious assets. These come only from the latest audited Notes to Accounts (MIS never has them) and are captured in `dtnw_granularities.md` during the template-integration step.
- Provisioning default: apply the haircut, never waive it. If receivables/inventory fall in a bucket that triggers a provision (debtors 180 to 365d at 75%, over 365d at 100%; inventory 180 to 365d at 40%/20% women's ethnic, over 365d at 75%/40%), apply it and flag for verification. Do not zero it "pending verification". An extreme result (for example negative TNW) is a finding to surface, not a reason to soften the rule.
- Use only the latest audited year's ageing buckets. Receivables turn over, so a prior year cannot second-guess the current-year disclosure.
- Verify ageing-bucket OCR against the source PDF. A value in the wrong bucket changes the provision, and the result, dramatically.

### Input vs Output File Storage (critical — keep them separate)
- **Source documents (INPUT)** live in the folder the user attaches (typically a `[CompanyName]/` folder at the workspace root). Read these **in place**. Never move, copy, rename, or relocate the user's source files, and never move that folder into `companies/`. Leave the source folder exactly as the user left it.
- **Generated artifacts (OUTPUT)** go to `companies/[company_name]/` and nowhere else. This folder must contain only files this skill produces — no source documents.
- Files written per analysis (all in `companies/[company_name]/`):
  - `company_structure.md` - short structure overview (from the template-integration step)
  - `dtnw_granularities.md` - D/TNW granularities from the latest audited Notes (skeleton at `templates/DTNW_Granularities_Template.md`)
  - `mis_[period].md` - complete, faithful extract of the MIS P&L (every line item, all periods); feeds Section 1 Rule 3 and Section 4
  - `Financial_Appraisal_[company_name].xlsx` - populated template copy
  - `section0_output.md` to `section6_output.md` - one file per section
  - `report_draft.md` - compiled full markdown report
  - `[company_name]_Nandan_Screen_[date].docx` - final note (stays in `companies/[company_name]/`; do not write back into the source folder unless the user explicitly asks)
- .docx is generated via `nandan-screener/scripts/generate_report.py` (python-docx, no pandoc), in the black-and-white house style.
- PDF extraction: targeted pages only, never OCR the entire document.
- Cash runway: always calculate both scenarios (ST debt refinanced and ST debt fully repaid).

### Report Voice and Style
- The note speaks in the fund's first-person voice and reads like an analyst memo, not a machine report.
- No GO/NO-GO/CONDITIONAL label; close with a recommendation plus Strengths, Weaknesses, Areas for further deep diligence, and suggested mitigants.
- No em dashes, no emoji, black-and-white only. Full rules live in `references/output-template.md` (House Style block), which is the source of truth.

---

## Screening Framework Summary

| Section | What it checks | Reference file |
|---------|----------------|----------------|
| 0 | Company / industry / founder context (no scoring) | `references/section0-overview.md` |
| 1 | 3 hard-stop rejection rules | `references/section1-rejection.md` |
| 2 | 6 initial screening criteria (need 4/6) | `references/section2-screening.md` |
| 3 | Cash flow: OCF, FCF, Debt/FCF, ICR (DSCR dropped) | `references/section3-cashflow.md` |
| 4 | P&L: margin waterfall, trends, industry benchmarks | `references/section4-pl.md` |
| 5 | Balance sheet: CCC, WC quality, ROCE, liquidity | `references/section5-balance-sheet.md` |
| 6 | Debt structure: lender quality, loan-type/security/rates, related-party, encumbered FD, maturity/FX | `references/section6-debt.md` |
