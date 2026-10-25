#!/usr/bin/env python3
"""Designsystem 2.1.2: Toolname oben rechts über Kunde/Projekt (kein Untertitel), Theme-Schalter so dezent wie das Haus-Icon.
Läuft im Repo- oder Designsystem-Ordner: python3 _build/patch-kopf.py"""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent

def patch(path, fn):
    p = root / path
    if not p.exists(): print(f"{path}: fehlt"); return
    s = p.read_text(encoding="utf-8"); n = fn(s)
    if n != s: p.write_text(n, encoding="utf-8"); print(f"{path}: geändert")
    else: print(f"{path}: unverändert")

def css(s):
    if "2.1.2" in s: return s
    s = re.sub(r"Version 2\.1\.1 · Stand 2026-10-25[^\n]*", "Version 2.1.2 · Stand 2026-10-25", s, count=1)
    # Kopf: zwei Spalten; dritte Spalte nur, wenn ein Titelblock in der Mitte steht (alte Form)
    s = s.replace("  grid-template-columns: auto 1fr auto;\n  align-items: center;\n  gap: var(--ls-s3) var(--ls-s5);",
                  "  grid-template-columns: auto 1fr;\n  align-items: center;\n  gap: var(--ls-s3) var(--ls-s5);", 1)
    s = s.replace(".ls-header__title { display: grid; gap: 2px; min-width: 0; }\n.ls-header__title h1 { color: var(--ls-on-navy); font-size: var(--ls-fs-xl); }",
                  ".ls-header:has(> .ls-header__title) { grid-template-columns: auto 1fr auto; } /* alte Form mit Titelblock in der Mitte */\n.ls-header__title { display: grid; gap: 2px; min-width: 0; }\n.ls-header__title h1 { color: var(--ls-on-navy); font-size: var(--ls-fs-xl); }\n/* Standard (2.1.2): Toolname rechts oben über Kunde/Projekt, kein Untertitel */\n.ls-header__meta .ls-header__title h1, .ls-header__meta h1 { font-size: 1.25rem; line-height: 1.2; font-weight: 600; letter-spacing: -0.01em; color: var(--ls-on-navy); margin: 0 0 2px; text-align: right; }", 1)
    s = s.replace(".ls-header__meta { display: grid; gap: 2px; justify-items: end; text-align: right; font-size: var(--ls-fs-sm); color: rgba(255,255,255,0.85); white-space: nowrap; }",
                  ".ls-header__meta { display: grid; gap: 2px; justify-items: end; justify-self: end; text-align: right; font-size: var(--ls-fs-sm); color: rgba(255,255,255,0.85); white-space: nowrap; min-width: 0; }", 1)
    s = s.replace(".ls-header__meta:nth-child(2):last-child { grid-column: 2 / -1; } /* Kopf ohne Titelblock: Meta (ggf. mit Titel) rechts bündig (2.1.1) */\n", "", 1)
    s = s.replace("@media (max-width: 699.98px) { .ls-header__meta .ls-theme-toggle { justify-self: start; } }",
                  "@media (max-width: 699.98px) { .ls-header__meta { justify-self: stretch; } .ls-header__meta .ls-theme-toggle { justify-self: start; } .ls-header__meta .ls-header__title h1, .ls-header__meta h1 { text-align: left; } }", 1)
    # Theme-Schalter so dezent wie das Haus-Icon
    s = s.replace("color: var(--ls-on-navy); opacity: .75; cursor: pointer; transition: background .12s ease, opacity .12s ease; -webkit-tap-highlight-color: transparent; }\n.ls-theme-toggle:hover { opacity: 1; background: rgba(255, 255, 255, 0.12); }\n.ls-theme-toggle:active { background: rgba(255, 255, 255, 0.2); }",
                  "color: var(--ls-on-navy); opacity: .45; cursor: pointer; transition: opacity .15s ease; -webkit-tap-highlight-color: transparent; } /* Deckkraft wie Haus-Icon: 0,45 / 1 / 0,3 */\n.ls-theme-toggle:hover, .ls-theme-toggle:focus-visible { opacity: 1; }\n.ls-theme-toggle:active { opacity: .3; }", 1)
    return s
patch("assets/css/design.css", css)

# Kopf in Vorlagen und Styleguide: Titelblock aus der Mitte in den Meta-Block, Untertitel weg
def kopf(s, titel):
    pat = re.compile(r'    <div class="ls-header__title">\n      <h1>(.*?)</h1>\n      <div class="ls-header__sub">.*?</div>\n    </div>\n    <div class="ls-header__meta">\n', re.S)
    return pat.sub(lambda m: '    <div class="ls-header__meta">\n      <h1>' + m.group(1) + '</h1>\n', s)
patch("vorlagen/tool-vorlage.html", lambda s: kopf(s, None))
patch("vorlagen/bericht-vorlage.html", lambda s: kopf(s, None))
patch("vorlagen/index-vorlage.html", lambda s: kopf(s, None))
patch("_build/styleguide-body.html", lambda s: kopf(s, None))

def body(s):
    s = s.replace('<li><b>Kopf</b> <span>Navy-Balken: Logo (Variante B, Slogan im Logo) · Toolname + Untertitel · Projekt, Datum, Schalter</span></li>',
                  '<li><b>Kopf</b> <span>Navy-Balken: links Logo (Variante B), rechts Toolname über Kunde/Projekt und Datum, darunter der Theme-Schalter; kein Untertitel</span></li>')
    return s
patch("_build/styleguide-body.html", body)

def regeln(s):
    if "2.1.2" in s: return s
    s = s.replace("Version 2.1.1 · Stand 2026-10-25", "Version 2.1.2 · Stand 2026-10-25", 1)
    s = s.replace("2. **Kopf** (`.ls-header`) – links Logo Variante B (Slogan im Logo), Mitte Toolname + ein Satz Untertitel, rechts Kunde/Projekt, Datum, optional Theme-Schalter. Der Kopf erscheint im Druck und ist damit die Kopfzeile des Berichts.",
                  "2. **Kopf** (`.ls-header`) – zwei Spalten: links Logo Variante B (Slogan im Logo), rechts ein Block mit Toolname (20 px, halbfett) über Kunde/Projekt und Datum, darunter der Theme-Schalter. Kein Untertitel, kein Titelblock in der Mitte [BESTÄTIGT, 2026-10-25]. Der Kopf erscheint im Druck und ist damit die Kopfzeile des Berichts.")
    s = s.replace("Der Schalter im Kopf ist ein runder Symbolknopf ohne Text (`.ls-theme-toggle`, Mond im Hell-, Sonne im Dunkelmodus, `aria-label`); kein Textbutton [BESTÄTIGT, 2026-10-25].",
                  "Der Schalter im Kopf ist ein runder Symbolknopf ohne Text (`.ls-theme-toggle`, Mond im Hell-, Sonne im Dunkelmodus, `aria-label`), so zurückhaltend wie das Haus-Icon (Deckkraft 0,45 / 1 bei Berührung / 0,3 gedrückt); kein Textbutton [BESTÄTIGT, 2026-10-25].")
    return s
patch("DESIGNREGELN.md", regeln)

def changelog(s):
    if "2.1.2" in s: return s
    return s.replace("## 2026-10-25 · Designsystem · 2.1.1", "## 2026-10-25 · Designsystem · 2.1.2\n- Kopf: Toolname rechts oben über Kunde/Projekt und Datum (20 px), kein Untertitel, Kopf zweispaltig; Theme-Schalter mit Deckkraft 0,45/1/0,3 wie das Haus-Icon. Vorlagen, Styleguide und umgebaute Tools angepasst [Fabian 2026-10-25].\n\n## 2026-10-25 · Designsystem · 2.1.1", 1)
patch("CHANGELOG.md", changelog)
