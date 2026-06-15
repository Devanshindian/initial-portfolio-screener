# Getting Started - Running a Nandan Initial Screening (for complete beginners)

This guide takes you from a blank computer to a finished Word (.docx) screening note.
No coding knowledge needed. Just follow each step in order. Take your time.

You will install one free program (VS Code), connect your Claude account to it,
download this project, drop a company's documents into a folder, paste one prompt,
and Claude will produce the screening note for you.

**What you need before you start**
- A laptop or desktop (Windows or Mac).
- An internet connection.
- A Claude Pro account (the paid plan, claude.ai). Have your login email and password ready.
- The company's documents saved on your computer (audited financials, MIS, debt schedule, ageing report, pitch deck, shareholding). PDF and Excel are fine.

Roughly 20-30 minutes the first time. After that, each new company takes a couple of minutes to set up.

---

## Part 1 - Install VS Code

VS Code (full name "Visual Studio Code") is a free app from Microsoft. It is the window in which Claude will work.

1. Open your web browser and go to: **https://code.visualstudio.com**
2. Click the big blue **Download** button. The site detects your computer and gives you the right version (Windows or Mac).
3. Open the file you just downloaded:
   - **Windows:** open the downloaded file named like `VSCodeUserSetup-....exe`. Click through: tick "I accept the agreement", keep clicking **Next**, and importantly tick the box **"Add to PATH"** if it appears, then **Install**, then **Finish**.
   - **Mac:** open the downloaded `.zip`, which gives you a "Visual Studio Code" app icon. Drag that icon into your **Applications** folder. Then open it from Applications (if Mac warns "downloaded from the internet", click **Open**).
4. VS Code opens to a Welcome screen. That is it for this part. You can close any pop-ups.

---

## Part 2 - Connect Claude to VS Code

Claude works inside VS Code through a free add-on called **Claude Code**. You will sign in with your Claude Pro account.

1. In VS Code, look at the **left edge**. There is a vertical strip of icons. Click the one that looks like **four squares** (one square breaking away). That is the **Extensions** panel. (Shortcut: press `Ctrl+Shift+X` on Windows, or `Cmd+Shift+X` on Mac.)
2. In the search box at the top of that panel, type: **Claude Code**
3. Find the result called **Claude Code** published by **Anthropic** (it has a verified blue tick). Click the blue **Install** button next to it.
4. After it installs, a Claude panel or a prompt to sign in will appear. If it does not appear automatically, press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows), type **Claude**, and choose **Claude: Sign In** (or **Focus on Claude Code View**).
5. Choose to sign in with your **Claude subscription account** (not an API key). Your web browser will open.
6. In the browser, log in with your **Claude Pro** email and password, then click **Authorize**. You will see a "you can return to VS Code" message.
7. Go back to VS Code. You should now see a **Claude** chat box, usually on the right side or bottom. This is where you will type instructions.

That is the whole setup. You only do Parts 1 and 2 once, ever.

> If asked to install "Node.js" or a "command line tool", say yes / allow it. The extension may set up a small helper the first time. It is safe.

---

## Part 3 - Download this project

This project contains the screening framework Claude will follow. You get it from GitHub.

**The link:** https://github.com/Devanshindian/initial-portfolio-screener

The easy way (no commands):
1. Open that link in your browser.
2. Click the green **`< > Code`** button near the top right.
3. Click **Download ZIP**.
4. Find the downloaded ZIP (usually in your **Downloads** folder) and unzip it:
   - **Windows:** right-click the ZIP, choose **Extract All**, then **Extract**.
   - **Mac:** double-click the ZIP. It creates a folder.
5. You now have a folder called **initial-portfolio-screener**. Move it somewhere easy to find, like your **Desktop**.
6. In VS Code, go to the top menu: **File → Open Folder...**, then select that **initial-portfolio-screener** folder and click **Open**. If VS Code asks "Do you trust the authors", click **Yes, I trust the authors**.

You should now see the project's files listed in the left panel (names like `CLAUDE.md`, `skill.md`, `nandan-screener`, `companies`, `templates`).

> Tip: opening the folder is important. Claude only "sees" the folder you have open. Always open the `initial-portfolio-screener` folder before you start.

---

## Part 4 - Add the company's documents

Do this **outside VS Code first**, then bring the folder in.

**Step 1 - Create a folder on your computer**

- **Mac:** open **Finder**, go to your Desktop (or wherever you keep your files), and create a new folder. Name it after the company with no spaces, for example **`Popees`**.
- **Windows:** open **File Explorer**, go to your Desktop, right-click on empty space, choose **New → Folder**, and name it **`Popees`**.

**Step 2 - Copy the company's documents into that folder**

Drop whatever you have into your new `Popees` folder:
- Audited annual reports (last 2 years)
- MIS / provisional financials (latest year, ideally all 12 months)
- Debt or borrowing schedule
- Customer-wise revenue or debtor ageing report
- Pitch deck
- Company structure / shareholding

You do not need every document. Claude will use what is there and tell you what is missing.

**Step 3 - Move that folder into the project**

- In the same Finder / File Explorer window, navigate to **Desktop → initial-portfolio-screener → companies**.
- Copy and paste (or drag) your `Popees` folder into the `companies` folder.

Alternatively, you can drag the folder straight from your Desktop onto the **`companies`** entry in the VS Code left panel.

**Where the outputs go**

Once Claude runs, it fills that same `companies/Popees/` folder with everything it produces. You will find intermediate files for each section (`section0_output.md` through `section6_output.md`), a filled Excel financial model, and the finished screening note. The final Word document is named after the company and the date, for example:

`Popees_Nandan_Screen_2026-06-11.docx`

That `.docx` file is your deliverable. Open it in Microsoft Word or Apple Pages.

---

## Part 5 - The prompt (copy, fill in the blanks, paste)

Now you simply tell Claude what to do. Click into the **Claude** chat box in VS Code and paste the prompt below, after filling in the blanks for your company.

**Blank template (copy this and edit the parts in [brackets]):**

```
Run a Nandan initial check on [COMPANY NAME].

Documents are in the folder companies/[COMPANY NAME]/
- Audited annual reports: [which years, e.g. FY25 and FY24]
- MIS financials: [file name and what period it covers]
- Debt / borrowing schedule: [yes / no]
- Customer-wise revenue or debtor ageing report: [yes / no]
- Pitch deck: [yes / no]
- Company structure / shareholding: [yes / no]

Deal terms (if known):
- Ask: [amount in Cr, or "check pitch deck"]
- Tenure: [months, or "check pitch deck if given"]
- Securities offered: [details, or "not known"]

Run the full Sections 0 to 6 framework and produce the .docx screening note.
```

**Worked example, already filled in for Popees** (this is exactly what a finished, ready-to-paste prompt looks like):

```
Run a Nandan initial check on Popees.

Documents are in the folder companies/Popees/
- Audited annual reports: FY25 and FY24
- MIS financials: the file named "Projections 5 Years" has provisionals through 31 March 2026 (all 12 months)
- Debt / borrowing schedule: yes
- Customer-wise revenue or debtor ageing report: yes
- Pitch deck: yes
- Company structure / shareholding: yes

Deal terms (if known):
- Ask: check the pitch deck
- Tenure: check the pitch deck if given
- Securities offered: check the pitch deck / debt schedule

Run the full Sections 0 to 6 framework and produce the .docx screening note.
```

A note on the "Deal terms" lines: if your friend does not know the ask, the tenure, or what security is being offered, he does not need to hunt for it. He just writes "check the pitch deck" (as above) and Claude will pull whatever is in the documents. If he *does* know a number, he types it in, for example `Ask: 20 Cr` or `Tenure: 24 months`. Either way is fine.

Press **Enter** to send.

---

## Part 6 - Let it run, then open your note

1. Claude will start working. It reads the documents, fills a financial template, and writes the note section by section. This takes several minutes. You will see it thinking and listing steps.
2. **Claude will ask for permission** to read files, run small scripts, and create the document. When it shows an **Allow / Approve** button, click **Allow** (you can choose "allow for this session" to avoid repeated clicks). This is normal and safe; it is only working inside your project folder.
3. If Claude asks you a question (for example, a missing number or which financials to use), just answer in the chat in plain English.
4. When it finishes, the screening note appears inside **`companies/[COMPANY NAME]/`** with a name like **`Popees_Nandan_Screen_2026-06-11.docx`**.
5. To open it: find that file in the left panel, right-click it, and choose **Reveal in Finder** (Mac) or **Reveal in File Explorer** (Windows). Then double-click it to open in Microsoft Word or Pages.

That is your finished initial screening note: Sections 0 to 6, a recommendation, strengths, weaknesses, and areas for diligence.

---

## Part 7 - Doing the next company

You never repeat Parts 1, 2 or 3. For each new company:
1. Make a new folder under `companies/` named after the company.
2. Drop that company's documents in.
3. Paste the prompt from Part 5 with the new company's details.
4. Approve the steps, open the .docx.

---

## If something goes wrong

- **"I don't see a Claude box."** Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows), type "Claude", and pick the option to open / focus the Claude view. Make sure the Claude Code extension shows as installed in the Extensions panel.
- **"Claude says it can't find the files."** Check two things: that you opened the `initial-portfolio-screener` folder (Part 3, step 6), and that your documents are inside `companies/[COMPANY NAME]/` with the company name spelled the same way as in your prompt.
- **"It keeps asking for permission."** That is normal. Click Allow. Choosing "allow for this session" reduces the clicks.
- **"It stopped halfway."** Just type "continue" in the Claude box.
- **"Which folder name do I use?"** Avoid spaces and punctuation. `Popees` is good; `Popees Baby Care!` is not.
- **Sign-in problems.** Make sure you are logging in with the Claude Pro account, and that you clicked Authorize in the browser. You can sign out and back in from the Claude panel's settings.

---

## What is actually happening (optional, for the curious)

This project is a set of written instructions (a "framework") that tells Claude how the Nandan fund screens a company: a company and founder overview (Section 0), a quick rejection check (Section 1), six pass/fail criteria (Section 2), then cash flow, profit and loss, balance sheet, and debt analysis (Sections 3 to 6). Claude reads those instructions automatically when you open the folder, applies them to the documents you provided, fills a financial model, and writes the note in the fund's own voice. You are not programming anything; you are handing Claude a recipe and the ingredients, and it cooks.

---

## How the screening works - overview

```
  Your documents
  (audited reports, MIS, debt schedule, pitch deck, ageing report)
         |
         v
  +-----------------------+
  |  Section 0            |
  |  Company & Founder    |  Business model, industry, promoter background,
  |  Overview             |  deal structure. No scoring - sets context.
  +-----------------------+
         |
         v
  +-----------------------+
  |  Section 1            |  Three hard-stop rules:
  |  Rejection Check      |  1. Deep technology / pre-revenue
  |                       |  2. Government revenue above 30%
  |                       |  3. Negative unit economics (CM2)
  +-----------------------+
         |                        |
    0 or 1 rules             2 or 3 rules
    triggered                triggered
         |                        |
         |                  HARD STOP on recommendation
         |                  (full analysis still runs and
         |                   appears in the note)
         v
  +-----------------------+
  |  Section 2            |  Six criteria - company must pass 4 out of 6.
  |  Initial Screening    |  Revenue scale, growth rate, EBITDA margin,
  |                       |  D/TNW, working capital quality, management.
  +-----------------------+
         |
         v
  +-----------------------+
  |  Section 3            |  Operating cash flow, free cash flow,
  |  Cash Flow            |  Debt/FCF coverage, interest coverage ratio.
  +-----------------------+
         |
         v
  +-----------------------+
  |  Section 4            |  Margin waterfall (gross to PAT), trend
  |  P&L Analysis         |  analysis, industry benchmarks.
  +-----------------------+
         |
         v
  +-----------------------+
  |  Section 5            |  Cash conversion cycle, working capital
  |  Balance Sheet        |  quality, ROCE, liquidity ratios.
  +-----------------------+
         |
         v
  +-----------------------+
  |  Section 6            |  Lender quality, loan types, security,
  |  Debt Structure       |  interest rates, related-party loans,
  |                       |  maturity profile, FX exposure.
  +-----------------------+
         |
         v
  +-------------------------------------------+
  |  Final Screening Note (.docx)             |
  |                                           |
  |  Recommendation: Proceed to diligence     |
  |                  Pause                    |
  |                  Pass                     |
  |                                           |
  |  + Strengths                              |
  |  + Weaknesses                             |
  |  + Areas for further deep diligence       |
  |  + Suggested mitigants                    |
  +-------------------------------------------+

  Saved to: companies/[CompanyName]/[CompanyName]_Nandan_Screen_[date].docx
```
