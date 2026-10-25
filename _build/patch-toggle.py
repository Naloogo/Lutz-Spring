#!/usr/bin/env python3
"""Designsystem 2.1.1: minimalistischer Theme-Schalter (.ls-theme-toggle) statt Textbutton „Dunkel / Hell“.
Läuft im Repo- oder Designsystem-Ordner: python3 _build/patch-toggle.py"""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent

TOGGLE = '''<button type="button" class="ls-theme-toggle ls-no-print" id="themeToggle" aria-label="Dunkel- oder Hellmodus umschalten" title="Dunkel / Hell">
        <svg class="ls-theme-toggle__moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>
        <svg class="ls-theme-toggle__sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4 7 17M17 7l1.4-1.4"/></svg>
      </button>'''

OLD_BTN = re.compile(r'<button type="button" class="ls-btn ls-btn--ghost ls-btn--sm ls-no-print" id="themeToggle" aria-pressed="false">Dunkel / Hell</button>')

def patch(path, fn):
    p = root / path
    if not p.exists(): print(f"{path}: fehlt"); return
    s = p.read_text(encoding="utf-8"); n = fn(s)
    if n != s: p.write_text(n, encoding="utf-8"); print(f"{path}: geändert")
    else: print(f"{path}: unverändert")

# 1) design.css: Tokens für Symbolwechsel + Baustein
def css(s):
    if ".ls-theme-toggle" in s: return s
    s = s.replace("  --ls-gutter: 16px;\n}", "  --ls-gutter: 16px;\n\n  /* Theme-Schalter: welches Symbol sichtbar ist (hell → Mond anbieten) */\n  --ls-icon-moon: block;\n  --ls-icon-sun: none;\n}", 1)
    s = s.replace("    --ls-shadow-2: 0 6px 20px rgba(0, 0, 0, 0.45);\n  }\n}", "    --ls-shadow-2: 0 6px 20px rgba(0, 0, 0, 0.45);\n    --ls-icon-moon: none;\n    --ls-icon-sun: block;\n  }\n}", 1)
    s = s.replace(":root[data-theme=\"dark\"] {\n  color-scheme: dark;", ":root[data-theme=\"dark\"] {\n  color-scheme: dark;\n  --ls-icon-moon: none;\n  --ls-icon-sun: block;", 1)
    s = s.replace("/* Text-Wortmarke, falls (noch) kein Logo eingebettet ist */",
"""/* Theme-Schalter: runder Symbolknopf, Mond im Hell-, Sonne im Dunkelmodus; kein Text, kein Rahmen */
.ls-theme-toggle { appearance: none; border: 0; background: transparent; width: 32px; height: 32px; border-radius: var(--ls-r-pill); display: inline-grid; place-items: center; color: var(--ls-on-navy); opacity: .75; cursor: pointer; transition: background .12s ease, opacity .12s ease; -webkit-tap-highlight-color: transparent; }
.ls-theme-toggle:hover { opacity: 1; background: rgba(255, 255, 255, 0.12); }
.ls-theme-toggle:active { background: rgba(255, 255, 255, 0.2); }
.ls-theme-toggle svg { width: 18px; height: 18px; }
.ls-theme-toggle__moon { display: var(--ls-icon-moon); }
.ls-theme-toggle__sun { display: var(--ls-icon-sun); }
.ls-header__meta .ls-theme-toggle { justify-self: end; margin-top: 2px; }
@media (max-width: 699.98px) { .ls-header__meta .ls-theme-toggle { justify-self: start; } }
@media (pointer: coarse) { .ls-theme-toggle { width: 40px; height: 40px; } }

/* Text-Wortmarke, falls (noch) kein Logo eingebettet ist */""", 1)
    s = s.replace("Version 2.1 · Stand 2026-10-25", "Version 2.1.1 · Stand 2026-10-25", 1)
    return s
patch("assets/css/design.css", css)

# 2) Kopfbalken-Button in Styleguide-Quelle, Vorlagen und (falls vorhanden) umgebauten Tools
for f in ["_build/styleguide-body.html", "vorlagen/tool-vorlage.html", "vorlagen/index-vorlage.html"]:
    patch(f, lambda s: OLD_BTN.sub(TOGGLE, s))

# 3) Styleguide-Text zum Baustein
def body(s):
    if "ls-theme-toggle</code>" in s: return s
    return s.replace('<span>Farbwelt <b>Marine &amp; Signalgelb</b></span>', '<span>Farbwelt <b>Marine &amp; Signalgelb</b></span>').replace(
        "<p class=\"ls-small ls-muted ls-mt-2\">Immer mit Text im Button („Speichern“), Icon allein nur bei Platzmangel mit <code>aria-label</code>.",
        "<p class=\"ls-small ls-muted ls-mt-2\">Immer mit Text im Button („Speichern“), Icon allein nur bei Platzmangel mit <code>aria-label</code>. Ausnahme mit festem Platz: der Theme-Schalter <code>.ls-theme-toggle</code> oben rechts im Kopf, ein runder Symbolknopf ohne Text (Mond im Hell-, Sonne im Dunkelmodus), Beschriftung über <code>aria-label</code>.")
patch("_build/styleguide-body.html", body)

# 4) Regeln + Changelog
def regeln(s):
    if "ls-theme-toggle" in s: return s
    s = s.replace("5. Kein eigener Dunkelmodus pro Tool: wer `design.css` einbindet, bekommt ihn. Der Schalter im Kopf (Vorlage) ist optional.",
                  "5. Kein eigener Dunkelmodus pro Tool: wer `design.css` einbindet, bekommt ihn. Der Schalter im Kopf ist ein runder Symbolknopf ohne Text (`.ls-theme-toggle`, Mond im Hell-, Sonne im Dunkelmodus, `aria-label`); kein Textbutton [BESTÄTIGT, 2026-10-25].")
    s = s.replace("Version 2.1 · Stand 2026-10-25", "Version 2.1.1 · Stand 2026-10-25", 1)
    s = s.replace("„Dunkel / Hell“.", "Theme-Schalter ohne Text (Symbol).", 1)
    return s
patch("DESIGNREGELN.md", regeln)
def changelog(s):
    if "2.1.1" in s: return s
    return s.replace("## 2026-10-25 · Repo · Übernahme", "## 2026-10-25 · Designsystem · 2.1.1\n- Theme-Schalter als runder Symbolknopf `.ls-theme-toggle` (Mond/Sonne) statt Textbutton „Dunkel / Hell“; Tokens `--ls-icon-moon/--ls-icon-sun`; Vorlagen und Styleguide angepasst. Anlass: Backlog (Fabian, „zu klobig“).\n\n## 2026-10-25 · Repo · Übernahme", 1)
patch("CHANGELOG.md", changelog)
def backlog(s):
    if "Theme-Schalter" in s: return s
    return s.rstrip("\n") + "\n| 2026-10-25 | Fabian | Textbutton „Dunkel / Hell“ im Kopf zu klobig | Kopfbalken aller Tools | – | erledigt in 2.1.1: `.ls-theme-toggle` (Symbolknopf) |\n"
patch("BACKLOG.md", backlog)
