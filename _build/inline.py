#!/usr/bin/env python3
"""
inline.py · fügt design.css und ls.js in jedes Tool ein, damit jedes Tool eine
einzelne, offline-fähige HTML-Datei bleibt und die Pflege trotzdem an einer Stelle liegt.

Aufruf (im Repo-Hauptordner):   python3 _build/inline.py            → alle *.html im Hauptordner
                                python3 _build/inline.py heizkoerper.html

Im Tool stehen Marker; alles dazwischen wird ersetzt:
    <!-- design.css:start --><style>…</style><!-- design.css:end -->
    <!-- ls.js:start --><script>…</script><!-- ls.js:end -->
Fehlt ein Marker, bleibt die Datei unverändert (Hinweis in der Ausgabe).
"""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
css = (root / "assets/css/design.css").read_text(encoding="utf-8").strip()
js = (root / "assets/js/ls.js").read_text(encoding="utf-8").strip()

blocks = {
    "design.css": "<!-- design.css:start -->\n<style>\n" + css + "\n</style>\n<!-- design.css:end -->",
    "ls.js": "<!-- ls.js:start -->\n<script>\n" + js + "\n</script>\n<!-- ls.js:end -->",
}

def einfuegen(path: pathlib.Path) -> str:
    s = path.read_text(encoding="utf-8")
    ergebnis = []
    for name, block in blocks.items():
        pat = re.compile(r"<!-- " + re.escape(name) + r":start -->.*?<!-- " + re.escape(name) + r":end -->", re.S)
        if pat.search(s):
            s = pat.sub(lambda m: block, s)
            ergebnis.append(name)
        # Alternativ: externe Einbindung durch Inline-Block ersetzen
        elif name == "design.css" and '<link rel="stylesheet" href="assets/css/design.css">' in s:
            s = s.replace('<link rel="stylesheet" href="assets/css/design.css">', block); ergebnis.append(name + " (link ersetzt)")
        elif name == "ls.js" and '<script src="assets/js/ls.js"></script>' in s:
            s = s.replace('<script src="assets/js/ls.js"></script>', block); ergebnis.append(name + " (script ersetzt)")
    if ergebnis:
        path.write_text(s, encoding="utf-8")
    return ", ".join(ergebnis) or "keine Marker – unverändert"

dateien = [root / a for a in sys.argv[1:]] or sorted(p for p in root.glob("*.html"))
for p in dateien:
    print(f"{p.name:32s} {einfuegen(p)}")
