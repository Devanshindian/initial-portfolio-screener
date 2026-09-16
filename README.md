# Initial Portfolio Screener

A venture debt fund screens every company that lands on its desk against the same checklist.
Five analysts do it five slightly different ways, and the slow part is not the judgement, it is
the arithmetic.

This turns that checklist into something an AI runs identically every time.

## What it does

1. Reads the audited financials and the management accounts
2. Fills a standard template: P&L, balance sheet, cash flow
3. Computes every ratio the fund cares about, with fixed thresholds
4. Writes a one-page memo with a recommendation: proceed, pass, or pause

## What it checks

- **Three rejection rules** — deep tech, government revenue concentration, negative unit economics
- **Six screening criteria** — operating history, revenue, leverage, promoter experience,
  receivables quality, cash runway
- **Cash flow** — free cash flow, debt service coverage, interest cover on a cash basis
- **Balance sheet** — working capital quality, return on capital against cost of capital

## The design decision worth naming

The thresholds are fixed and deterministic. The AI does not decide whether 2.8x leverage is
acceptable; the rule does. So two runs on the same inputs give the same answer, and any number
can be walked back to the document it came from.

Where something genuinely cannot be assessed from the paperwork, it is marked
**"pending, requires deeper diligence"** rather than guessed at.

## Running it

Open the folder in an editor with Claude Code, drop the company's documents in, and follow
`GETTING_STARTED.md`.
