#!/usr/bin/env python3
"""
Build the public docs site for the Nandan screener reference files.

Reads:  nandan-screener/references/*.md  (source of truth, rendered as-is)
Writes: docs/index.html, docs/<slug>.html, docs/assets/style.css, docs/.nojekyll

Markdown is rendered at build time (python-markdown), so the published pages are
plain static HTML with no CDN, no JS renderer, and no network calls at view time.

Run:    python3 nandan-screener/scripts/build_site.py
"""

import html
import os
import re
import shutil
import tempfile

import markdown

# ---------------------------------------------------------------- config ----

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # repo root, the one anchor

REFS = os.path.join(ROOT, "nandan-screener", "references")
OUT = os.path.join(ROOT, "docs")
ASSETS = os.path.join(OUT, "assets")

SITE_TITLE = "Nandan Initial Portfolio Screener"
SITE_TAGLINE = "The screening framework, section by section."
REPO_URL = "https://github.com/Devanshindian/initial-portfolio-screener"

# Nav order and copy. Every entry maps 1:1 to a file in references/.
GROUPS = [
    ("Framework", [
        ("section0-overview.md",     "Section 0",  "Company Overview",
         "Company, industry and founder context. Runs before Section 1 and carries no score."),
        ("section1-rejection.md",    "Section 1",  "Preliminary Rejection",
         "Three hard-stop rules: deep technology, government revenue, negative unit economics. Two or more triggered is a rejection."),
        ("section2-screening.md",    "Section 2",  "Initial Screening",
         "Six screening criteria. Four must be met; exactly four is a borderline flag that still passes."),
        ("section3-cashflow.md",     "Section 3",  "Cash Flow",
         "Operating cash flow, free cash flow, Debt/FCF and interest cover, plus both runway scenarios."),
        ("section4-pl.md",           "Section 4",  "Profit and Loss",
         "Margin waterfall, trend analysis and comparison against industry benchmarks."),
        ("section5-balance-sheet.md","Section 5",  "Balance Sheet",
         "Cash conversion cycle, working capital quality, ROCE and liquidity."),
        ("section6-debt.md",         "Section 6",  "Debt Structure",
         "Lender quality, loan types, security, rates, related-party debt, encumbered deposits and maturity profile."),
    ]),
    ("Process", [
        ("template-integration.md",  "Process",    "Template Integration",
         "Populating the Financial Appraisal template from the audited PDFs, then reading the calculated ratios back out."),
    ]),
    ("Output", [
        ("output-template.md",       "Output",     "Report Template and House Style",
         "The structure of the final note, the fund's voice, and the black-and-white formatting rules."),
    ]),
]

# No "sane_lists": these files often start a list on the line straight after a
# paragraph, and GitHub renders that as a list. Matching GitHub is the point.
MD_EXTENSIONS = ["tables", "fenced_code", "toc", "attr_list", "abbr", "footnotes"]
MD_CONFIG = {"toc": {"permalink": "#", "toc_depth": "2-3"}}

# ------------------------------------------------------------------ util ----


def write_text(path, text):
    """Atomic save: a file's existence must guarantee it is complete."""
    d = os.path.dirname(path) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


def slug_of(filename):
    return filename[:-3]


def first_heading(md_text, fallback):
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def reading_time(md_text):
    words = len(md_text.split())
    return max(1, round(words / 220))


def strip_toc_permalinks(toc_html):
    """The right-rail TOC repeats the heading text; drop the trailing pilcrow links."""
    return toc_html


# ------------------------------------------------------------- templates ----

CSS = r"""
/* ---- reset ------------------------------------------------------------ */
*, *::before, *::after { box-sizing: border-box; }
body, h1, h2, h3, h4, p, ul, ol, li, figure, blockquote, table { margin: 0; padding: 0; }
ul, ol { list-style: none; }

/* ---- tokens ----------------------------------------------------------- */
:root {
  --bg: #fbfbfa;
  --panel: #ffffff;
  --ink: #1c1c1a;
  --ink-soft: #52514c;
  --ink-faint: #86847c;
  --rule: #e4e2dc;
  --rule-soft: #eeece7;
  --accent: #1f4f3f;
  --accent-soft: #eaf1ed;
  --code-bg: #f4f3ef;
  --mark: #fdf3d3;
  --shadow: 0 1px 2px rgba(28,28,26,.05), 0 8px 24px rgba(28,28,26,.05);
  --sans: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Helvetica, Arial, sans-serif;
  --serif: ui-serif, Georgia, "Iowan Old Style", "Times New Roman", serif;
  --mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #14140f;
    --panel: #1b1b17;
    --ink: #eceae2;
    --ink-soft: #b6b3a8;
    --ink-faint: #85827a;
    --rule: #2e2e28;
    --rule-soft: #24241f;
    --accent: #7fc9a9;
    --accent-soft: #1d2a24;
    --code-bg: #201f1b;
    --mark: #4a3f18;
    --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.3);
  }
}
:root[data-theme="dark"] {
  --bg: #14140f; --panel: #1b1b17; --ink: #eceae2; --ink-soft: #b6b3a8;
  --ink-faint: #85827a; --rule: #2e2e28; --rule-soft: #24241f; --accent: #7fc9a9;
  --accent-soft: #1d2a24; --code-bg: #201f1b; --mark: #4a3f18;
  --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.3);
}
:root[data-theme="light"] {
  --bg: #fbfbfa; --panel: #ffffff; --ink: #1c1c1a; --ink-soft: #52514c;
  --ink-faint: #86847c; --rule: #e4e2dc; --rule-soft: #eeece7; --accent: #1f4f3f;
  --accent-soft: #eaf1ed; --code-bg: #f4f3ef; --mark: #fdf3d3;
  --shadow: 0 1px 2px rgba(28,28,26,.05), 0 8px 24px rgba(28,28,26,.05);
}

/* ---- base ------------------------------------------------------------- */
body {
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  font-size: 16px;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

/* ---- layout ----------------------------------------------------------- */
.shell { display: grid; grid-template-columns: 268px minmax(0, 1fr); min-height: 100vh; }

.side {
  position: sticky; top: 0; align-self: start; height: 100vh; overflow-y: auto;
  background: var(--panel); border-right: 1px solid var(--rule);
  padding: 26px 20px 40px;
}
.brand { display: block; margin-bottom: 4px; }
.brand .mark {
  font-family: var(--serif); font-size: 19px; font-weight: 600;
  color: var(--ink); letter-spacing: -.01em; line-height: 1.25; display: block;
}
.brand:hover { text-decoration: none; }
.brand .sub { font-size: 12.5px; color: var(--ink-faint); display: block; margin-top: 3px; }

.filter {
  width: 100%; margin: 20px 0 18px; padding: 8px 11px;
  font: inherit; font-size: 13.5px; color: var(--ink);
  background: var(--bg); border: 1px solid var(--rule); border-radius: 7px;
}
.filter:focus { outline: 2px solid var(--accent-soft); border-color: var(--accent); }
.filter::placeholder { color: var(--ink-faint); }

.navgroup { margin-bottom: 20px; }
.navgroup > h2 {
  font-size: 10.5px; text-transform: uppercase; letter-spacing: .1em;
  color: var(--ink-faint); font-weight: 600; margin-bottom: 7px; padding-left: 10px;
}
.navgroup a {
  display: block; padding: 6px 10px; border-radius: 7px;
  color: var(--ink-soft); font-size: 14px; line-height: 1.4;
}
.navgroup a:hover { background: var(--rule-soft); color: var(--ink); text-decoration: none; }
.navgroup a.on { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
.navgroup a .kicker {
  display: block; font-size: 10.5px; letter-spacing: .06em; text-transform: uppercase;
  color: var(--ink-faint); font-weight: 600;
}
.navgroup a.on .kicker { color: var(--accent); opacity: .8; }
.navgroup li.hide { display: none; }

.sidefoot {
  margin-top: 28px; padding-top: 16px; border-top: 1px solid var(--rule);
  font-size: 12.5px; color: var(--ink-faint); display: flex; gap: 14px; flex-wrap: wrap;
}
.sidefoot button {
  font: inherit; font-size: 12.5px; color: var(--ink-faint); background: none;
  border: 0; padding: 0; cursor: pointer;
}
.sidefoot button:hover, .sidefoot a:hover { color: var(--ink); text-decoration: none; }
.sidefoot a { color: var(--ink-faint); }

.main { min-width: 0; padding: 0 0 90px; }
.wrap { max-width: 1160px; margin: 0 auto; padding: 0 40px; }

.topbar {
  display: none; position: sticky; top: 0; z-index: 20;
  background: var(--panel); border-bottom: 1px solid var(--rule);
  padding: 11px 18px; align-items: center; gap: 12px;
}
.topbar button {
  font: inherit; font-size: 14px; color: var(--ink); background: var(--bg);
  border: 1px solid var(--rule); border-radius: 7px; padding: 5px 11px; cursor: pointer;
}
.topbar .t { font-family: var(--serif); font-size: 16px; font-weight: 600; }

/* ---- doc page --------------------------------------------------------- */
.doc { display: grid; grid-template-columns: minmax(0, 1fr) 216px; gap: 48px; padding-top: 44px; }

.pagehead { margin-bottom: 30px; }
.pagehead .kicker {
  font-size: 11px; letter-spacing: .12em; text-transform: uppercase;
  color: var(--accent); font-weight: 700;
}
.pagehead h1 {
  font-family: var(--serif); font-size: 34px; line-height: 1.15; letter-spacing: -.02em;
  margin: 7px 0 10px; font-weight: 600;
}
.pagehead p { color: var(--ink-soft); font-size: 16px; max-width: 62ch; }
.meta {
  margin-top: 14px; padding-top: 13px; border-top: 1px solid var(--rule);
  font-size: 12.5px; color: var(--ink-faint); display: flex; gap: 16px; flex-wrap: wrap;
}
.meta code { background: none; padding: 0; font-size: 12.5px; color: var(--ink-faint); }

.toc { position: sticky; top: 34px; align-self: start; max-height: calc(100vh - 70px); overflow-y: auto; }
.toc > .h {
  font-size: 10.5px; text-transform: uppercase; letter-spacing: .1em;
  color: var(--ink-faint); font-weight: 600; margin-bottom: 9px;
}
.toc ul { border-left: 1px solid var(--rule); }
.toc li { margin: 0; }
.toc a {
  display: block; padding: 3px 0 3px 13px; margin-left: -1px;
  border-left: 2px solid transparent;
  font-size: 12.5px; line-height: 1.45; color: var(--ink-faint);
  overflow-wrap: anywhere;
}
.toc a:hover { color: var(--ink); text-decoration: none; border-left-color: var(--rule); }
.toc a.on { color: var(--accent); border-left-color: var(--accent); }
.toc ul ul a { padding-left: 24px; font-size: 12px; }

/* ---- rendered markdown ------------------------------------------------ */
.md { max-width: 78ch; }
.md > h1:first-child { display: none; }          /* the page head already shows it */
.md h1, .md h2, .md h3, .md h4 {
  font-family: var(--serif); font-weight: 600; letter-spacing: -.01em;
  line-height: 1.25; scroll-margin-top: 28px;
}
.md h1 { font-size: 29px; margin: 46px 0 14px; }
.md h2 {
  font-size: 24px; margin: 46px 0 14px;
  padding-bottom: 8px; border-bottom: 1px solid var(--rule);
}
.md h3 { font-size: 18.5px; margin: 32px 0 10px; }
.md h4 { font-size: 15.5px; margin: 24px 0 8px; font-family: var(--sans); color: var(--ink-soft); }
.md h2:first-child, .md h3:first-child { margin-top: 0; }

.md p { margin: 0 0 15px; }
.md strong { font-weight: 650; color: var(--ink); }
.md em { font-style: italic; }

.md ul, .md ol { margin: 0 0 15px; padding-left: 22px; }
.md ul { list-style: disc; }
.md ol { list-style: decimal; }
.md li { margin: 5px 0; }
.md li::marker { color: var(--ink-faint); }
.md ul ul, .md ol ol, .md ul ol, .md ol ul { margin: 5px 0 5px; }

.md li.task { list-style: none; margin-left: -22px; }
.md li.task input { margin-right: 8px; accent-color: var(--accent); transform: translateY(1px); }

.md hr { border: 0; border-top: 1px solid var(--rule); margin: 38px 0; }

.md blockquote {
  border-left: 3px solid var(--accent); background: var(--accent-soft);
  padding: 12px 18px; margin: 0 0 18px; border-radius: 0 8px 8px 0;
  color: var(--ink-soft);
}
.md blockquote p:last-child { margin-bottom: 0; }

.md code {
  font-family: var(--mono); font-size: .875em;
  background: var(--code-bg); border: 1px solid var(--rule-soft);
  padding: 1px 5px; border-radius: 5px; color: var(--ink);
  word-break: break-word;
}
.md pre {
  background: var(--code-bg); border: 1px solid var(--rule); border-radius: 9px;
  padding: 14px 16px; margin: 0 0 18px; overflow-x: auto;
}
.md pre code {
  background: none; border: 0; padding: 0; font-size: 13px; line-height: 1.6;
  white-space: pre; color: var(--ink-soft);
}

/* tables: the whole point of this site */
.tablewrap { overflow-x: auto; margin: 0 0 20px; border: 1px solid var(--rule); border-radius: 9px; }
.md table { border-collapse: collapse; width: 100%; font-size: 14px; background: var(--panel); }
.md thead th {
  background: var(--rule-soft); text-align: left; font-weight: 650; color: var(--ink);
  padding: 9px 13px; border-bottom: 1px solid var(--rule); white-space: nowrap;
  font-size: 13px; letter-spacing: .01em;
}
.md tbody td { padding: 9px 13px; border-bottom: 1px solid var(--rule-soft); vertical-align: top; color: var(--ink-soft); }
.md tbody tr:last-child td { border-bottom: 0; }
.md tbody tr:hover td { background: var(--rule-soft); }
.md table code { font-size: 12.5px; }

.md img { max-width: 100%; height: auto; }
.md mark { background: var(--mark); color: var(--ink); padding: 0 2px; }

.headerlink { opacity: 0; margin-left: 8px; font-size: .7em; color: var(--ink-faint); text-decoration: none; }
h1:hover .headerlink, h2:hover .headerlink, h3:hover .headerlink, h4:hover .headerlink { opacity: 1; }

.pager {
  display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap;
  margin-top: 54px; padding-top: 22px; border-top: 1px solid var(--rule);
}
.pager a {
  display: block; max-width: 46%; padding: 11px 15px;
  border: 1px solid var(--rule); border-radius: 9px; background: var(--panel);
}
.pager a:hover { border-color: var(--accent); text-decoration: none; }
.pager .lbl { display: block; font-size: 11px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-faint); }
.pager .ttl { display: block; font-size: 14.5px; color: var(--ink); margin-top: 2px; }
.pager .next { margin-left: auto; text-align: right; }

/* ---- index ------------------------------------------------------------ */
.hero { padding: 74px 0 40px; border-bottom: 1px solid var(--rule); margin-bottom: 40px; }
.hero .kicker { font-size: 11px; letter-spacing: .12em; text-transform: uppercase; color: var(--accent); font-weight: 700; }
.hero h1 {
  font-family: var(--serif); font-size: 46px; line-height: 1.08; letter-spacing: -.025em;
  font-weight: 600; margin: 12px 0 16px; max-width: 20ch;
}
.hero p { font-size: 17.5px; color: var(--ink-soft); max-width: 64ch; }
.hero .facts { display: flex; gap: 30px; flex-wrap: wrap; margin-top: 30px; }
.hero .fact .n { font-family: var(--serif); font-size: 26px; font-weight: 600; display: block; line-height: 1; }
.hero .fact .l { font-size: 12px; color: var(--ink-faint); letter-spacing: .04em; text-transform: uppercase; margin-top: 6px; display: block; }

.sect { margin-bottom: 44px; }
.sect > h2 {
  font-size: 11px; text-transform: uppercase; letter-spacing: .12em;
  color: var(--ink-faint); font-weight: 700; margin-bottom: 14px;
}
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 14px; }
.card {
  display: block; background: var(--panel); border: 1px solid var(--rule);
  border-radius: 11px; padding: 18px 19px; transition: border-color .12s ease, box-shadow .12s ease, transform .12s ease;
}
.card:hover { border-color: var(--accent); box-shadow: var(--shadow); text-decoration: none; transform: translateY(-1px); }
.card .kicker { font-size: 10.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--accent); font-weight: 700; }
.card h3 { font-family: var(--serif); font-size: 19px; font-weight: 600; margin: 6px 0 8px; color: var(--ink); letter-spacing: -.01em; }
.card p { font-size: 14px; color: var(--ink-soft); line-height: 1.55; }
.card .foot { margin-top: 12px; font-size: 12px; color: var(--ink-faint); }

.note {
  background: var(--panel); border: 1px solid var(--rule); border-left: 3px solid var(--accent);
  border-radius: 0 10px 10px 0; padding: 16px 19px; font-size: 14.5px; color: var(--ink-soft);
  max-width: 74ch;
}
.note strong { color: var(--ink); }

/* ---- responsive ------------------------------------------------------- */
@media (max-width: 1080px) {
  .doc { grid-template-columns: minmax(0, 1fr); }
  .toc { display: none; }
}
@media (max-width: 860px) {
  .shell { grid-template-columns: minmax(0, 1fr); }
  .side {
    position: fixed; z-index: 30; top: 0; left: 0; width: 280px; height: 100vh;
    transform: translateX(-100%); transition: transform .18s ease; box-shadow: var(--shadow);
  }
  .side.open { transform: none; }
  .topbar { display: flex; }
  .wrap { padding: 0 20px; }
  .doc { padding-top: 26px; }
  .hero { padding: 34px 0 30px; }
  .hero h1 { font-size: 33px; }
  .pagehead h1 { font-size: 27px; }
  .pager a { max-width: 100%; width: 100%; }
  .scrim { position: fixed; inset: 0; background: rgba(0,0,0,.35); z-index: 25; }
}
@media (min-width: 861px) { .scrim { display: none; } }
"""

JS = r"""
(function () {
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem('nps-theme'); } catch (e) {}
  if (saved) root.setAttribute('data-theme', saved);

  function currentTheme() {
    return root.getAttribute('data-theme') ||
      (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }
  var toggle = document.getElementById('theme');
  function label() { if (toggle) toggle.textContent = currentTheme() === 'dark' ? 'Light mode' : 'Dark mode'; }
  label();
  if (toggle) toggle.addEventListener('click', function () {
    var next = currentTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('nps-theme', next); } catch (e) {}
    label();
  });

  // mobile drawer
  var side = document.querySelector('.side');
  var btn = document.getElementById('menu');
  var scrim;
  function close() {
    side.classList.remove('open');
    if (scrim) { scrim.remove(); scrim = null; }
  }
  if (btn) btn.addEventListener('click', function () {
    if (side.classList.contains('open')) return close();
    side.classList.add('open');
    scrim = document.createElement('div');
    scrim.className = 'scrim';
    scrim.addEventListener('click', close);
    document.body.appendChild(scrim);
  });

  // nav filter
  var filter = document.getElementById('filter');
  if (filter) filter.addEventListener('input', function () {
    var q = filter.value.trim().toLowerCase();
    document.querySelectorAll('.navgroup li').forEach(function (li) {
      li.classList.toggle('hide', q !== '' && li.textContent.toLowerCase().indexOf(q) === -1);
    });
    document.querySelectorAll('.navgroup').forEach(function (g) {
      var any = Array.prototype.some.call(g.querySelectorAll('li'), function (li) { return !li.classList.contains('hide'); });
      g.style.display = any ? '' : 'none';
    });
  });

  // active heading in the right rail
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (links.length) {
    var map = {};
    var targets = [];
    links.forEach(function (a) {
      var el = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
      if (el) { map[el.id] = a; targets.push(el); }
    });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove('on'); });
        var a = map[en.target.id];
        if (a) a.classList.add('on');
      });
    }, { rootMargin: '0px 0px -72% 0px', threshold: 0 });
    targets.forEach(function (t) { obs.observe(t); });
  }
})();
"""


def nav_html(active_slug):
    out = []
    for group, items in GROUPS:
        out.append('<nav class="navgroup"><h2>%s</h2><ul>' % html.escape(group))
        for fname, kicker, title, _ in items:
            slug = slug_of(fname)
            cls = ' class="on"' if slug == active_slug else ""
            out.append(
                '<li><a href="%s.html"%s><span class="kicker">%s</span>%s</a></li>'
                % (slug, cls, html.escape(kicker), html.escape(title))
            )
        out.append("</ul></nav>")
    return "\n".join(out)


def shell(title, description, active_slug, body, extra_head=""):
    home_cls = ' class="on"' if active_slug == "index" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#128202;</text></svg>">
{extra_head}
</head>
<body>
<div class="topbar">
  <button id="menu" aria-label="Open navigation">Menu</button>
  <span class="t">{html.escape(SITE_TITLE)}</span>
</div>
<div class="shell">
  <aside class="side">
    <a class="brand" href="index.html"{home_cls}>
      <span class="mark">Nandan Initial<br>Portfolio Screener</span>
      <span class="sub">Screening framework reference</span>
    </a>
    <input id="filter" class="filter" type="search" placeholder="Filter sections" aria-label="Filter sections">
    {nav_html(active_slug)}
    <div class="sidefoot">
      <button id="theme" type="button">Dark mode</button>
      <a href="{REPO_URL}">Source on GitHub</a>
    </div>
  </aside>
  <main class="main">
    {body}
  </main>
</div>
<script>{JS}</script>
</body>
</html>
"""


TABLE_RE = re.compile(r"(<table>.*?</table>)", re.DOTALL)
TASK_RE = re.compile(r"<li>(\s*(?:<p>)?)\[([ xX])\]\s")

FENCE_RE = re.compile(r"^\s*(```|~~~)")
# A list that should be allowed to interrupt a paragraph: any bullet with
# content, or a numbered list starting at 1 (so a wrapped line beginning
# "2024." stays prose, exactly as CommonMark has it).
LIST_INTERRUPT_RE = re.compile(r"^\s*(?:[-*+]\s+\S|1[.)]\s+\S)")
ANY_LIST_RE = re.compile(r"^\s*(?:[-*+]\s|\d+[.)]\s)")
BLOCK_PREV_RE = re.compile(r"^\s*(?:#|\||>|---|===)")


def normalize_lists(md_text):
    """
    Let a list interrupt a paragraph, the way GitHub renders it.

    python-markdown needs a blank line before a list; CommonMark and GitHub do
    not. These files are written against the GitHub preview, so insert the blank
    line the renderer wants. Fenced blocks are skipped, and an indented previous
    line means we are inside a list item already, so leave that alone too.
    """
    lines = md_text.split("\n")
    out = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and out and LIST_INTERRUPT_RE.match(line):
            prev = out[-1]
            if (prev.strip()
                    and prev == prev.lstrip()
                    and not ANY_LIST_RE.match(prev)
                    and not BLOCK_PREV_RE.match(prev)):
                out.append("")
        out.append(line)
    return "\n".join(out)


def wrap_tables(html_body):
    """Wide tables scroll inside their own box; the page body never scrolls sideways."""
    return TABLE_RE.sub(lambda m: '<div class="tablewrap">%s</div>' % m.group(1), html_body)


def task_lists(html_body):
    """GitHub-style `- [ ]` checklists; python-markdown has no built-in for these."""
    def sub(m):
        checked = " checked" if m.group(2).lower() == "x" else ""
        return ('<li class="task">%s<input type="checkbox" disabled%s> '
                % (m.group(1), checked))
    return TASK_RE.sub(sub, html_body)


# ------------------------------------------------------------------ build ---


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(ASSETS, exist_ok=True)

    write_text(os.path.join(ASSETS, "style.css"), CSS)
    write_text(os.path.join(OUT, ".nojekyll"), "")

    flat = [(f, k, t, d) for _, items in GROUPS for (f, k, t, d) in items]

    for i, (fname, kicker, title, desc) in enumerate(flat):
        src = os.path.join(REFS, fname)
        if not os.path.exists(src):
            raise SystemExit("missing reference file: %s" % src)
        with open(src, encoding="utf-8") as f:
            md_text = f.read()

        md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)
        body_html = wrap_tables(task_lists(md.convert(normalize_lists(md_text))))
        toc = strip_toc_permalinks(md.toc)
        doc_title = first_heading(md_text, title)
        slug = slug_of(fname)

        prev_link = next_link = ""
        if i > 0:
            p = flat[i - 1]
            prev_link = ('<a class="prev" href="%s.html"><span class="lbl">Previous</span>'
                         '<span class="ttl">%s</span></a>' % (slug_of(p[0]), html.escape(p[2])))
        if i < len(flat) - 1:
            n = flat[i + 1]
            next_link = ('<a class="next" href="%s.html"><span class="lbl">Next</span>'
                         '<span class="ttl">%s</span></a>' % (slug_of(n[0]), html.escape(n[2])))

        body = f"""
    <div class="wrap">
      <div class="doc">
        <article>
          <header class="pagehead">
            <div class="kicker">{html.escape(kicker)}</div>
            <h1>{html.escape(doc_title)}</h1>
            <p>{html.escape(desc)}</p>
            <div class="meta">
              <span><code>references/{html.escape(fname)}</code></span>
              <span>{reading_time(md_text)} min read</span>
              <span><a href="{REPO_URL}/blob/main/nandan-screener/references/{html.escape(fname)}">View raw markdown</a></span>
            </div>
          </header>
          <div class="md">
{body_html}
          </div>
          <nav class="pager">{prev_link}{next_link}</nav>
        </article>
        <aside class="toc">
          <div class="h">On this page</div>
          {toc}
        </aside>
      </div>
    </div>
"""
        write_text(os.path.join(OUT, slug + ".html"),
                   shell("%s — %s" % (title, SITE_TITLE), desc, slug, body))
        print("wrote docs/%s.html" % slug)

    # ---- index ----
    cards = []
    for group, items in GROUPS:
        cards.append('<section class="sect"><h2>%s</h2><div class="cards">' % html.escape(group))
        for fname, kicker, title, desc in items:
            with open(os.path.join(REFS, fname), encoding="utf-8") as f:
                mt = f.read()
            cards.append(
                '<a class="card" href="%s.html">'
                '<div class="kicker">%s</div><h3>%s</h3><p>%s</p>'
                '<div class="foot">%s min read</div></a>'
                % (slug_of(fname), html.escape(kicker), html.escape(title),
                   html.escape(desc), reading_time(mt))
            )
        cards.append("</div></section>")

    total_words = sum(
        len(open(os.path.join(REFS, f), encoding="utf-8").read().split())
        for f, _, _, _ in flat
    )

    index_body = f"""
    <div class="wrap">
      <header class="hero">
        <div class="kicker">Venture debt screening</div>
        <h1>{html.escape(SITE_TAGLINE)}</h1>
        <p>The reference files behind the Nandan initial portfolio screener, published as they are written.
           Sections 0 to 6 are the framework itself; the process and output files cover how the financial
           template is populated and how the final note is written.</p>
        <div class="facts">
          <div class="fact"><span class="n">9</span><span class="l">Reference files</span></div>
          <div class="fact"><span class="n">7</span><span class="l">Framework sections</span></div>
          <div class="fact"><span class="n">{total_words:,}</span><span class="l">Words</span></div>
        </div>
      </header>
      {''.join(cards)}
      <div class="note">
        <strong>Reading order.</strong> Section 0 sets the context, Section 1 can stop the deal, and Section 2
        decides whether it clears the initial screen. Sections 3 to 6 are the financial work. Template
        integration sits between Section 1 and Section 2 in a live run, since Sections 3 to 5 read their
        ratios out of the populated workbook.
      </div>
    </div>
"""
    write_text(os.path.join(OUT, "index.html"),
               shell(SITE_TITLE, SITE_TAGLINE, "index", index_body))
    print("wrote docs/index.html")
    print("\nDone. %d pages in %s" % (len(flat) + 1, OUT))


if __name__ == "__main__":
    build()
