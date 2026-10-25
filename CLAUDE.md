# CLAUDE.md · Repo der internen Tools der Lutz Spring GmbH

Diese Datei liest eine KI (Claude Code, Claude im Firmenaccount) vor jeder Arbeit in diesem Repo. Sie ergänzt das Firmengehirn (Projekt „Firmengehirn“, Dateien 00–08), das Vorrang hat.

## Was dieses Repo ist
Einzelne HTML-Dateien im Hauptordner, gehostet auf GitHub Pages, bedient auf iPad (Safari, Homescreen-App) und Mac. Werkzeuge: `index.html`, `auslegung.html`, `foerderung.html`, `kostenvergleich.html`, `heizkoerper.html`, `bestandsaufnahme.html`, `bad-angebot.html`. Das Repo ist öffentlich.

## Regeln, die immer gelten
- Designsystem: `DESIGNREGELN.md` (Regeln), `assets/css/design.css` (Stil), `assets/js/ls.js` (Verhalten), `styleguide.html` (Referenz). Keine eigenen Farben, Schriften, Abstände oder externen Ressourcen in einem Tool. Fehlt ein Baustein, wird er in `design.css` ergänzt und im Styleguide gezeigt.
- Nach jeder Änderung an `design.css` oder `ls.js`: `python3 _build/inline.py` (fügt beide in alle Tools ein) und `python3 _build/build.py` (Styleguide). Die Marker `<!-- design.css:start/end -->` und `<!-- ls.js:start/end -->` in den Tools nie entfernen.
- Umbau eines Tools nur nach `UMBAU-ABLAUF.md`: Feldliste (`vorlagen/feldliste-vorlage.md`) vor dem Bau, Referenzwerte (`tests/referenzwerte.md`) vor und nach dem Bau, Freigabe durch Fabian. Rechenlogik unverändert; Formular wird aufgeräumt (DESIGNREGELN.md 6.1).
- Neue Tools aus `vorlagen/tool-vorlage.html`, Druckdokumente nach `vorlagen/bericht-vorlage.html`, Startseite nach `vorlagen/index-vorlage.html`.
- Dateinamen klein, ohne Umlaute und Leerzeichen, im Hauptordner; feste Namen `kostenvergleich.html`, `heizkoerper.html` (mit „r“). Vor jedem `href` den Namen prüfen (GitHub Pages unterscheidet Groß/Klein).
- Firmenname immer „Lutz Spring GmbH“; Slogan im Text „Heizung · Sanitär · Wärmepumpen“; Richtwerte mit „≈“; Rechenwege mit Formel, Eingangswerten, Zwischenergebnissen und Einheit ausweisen.
- Fachliche Festlegungen aus dem Firmengehirn als Standardwerte: Norm-Außentemperatur −12,7 °C (Region Oranienburg), Bivalenzpunkt −7 °C, Heizgrenze 15 °C Bestand, Heizkörperauslegung 50/40/20 °C, Umrechnung 75/65/20 mit Faktor ≈ 0,40 (maßgeblich Kermi-Leistungsrechner), 15 % Reserve ist kein Standard.
- Veränderliche Werte (Fördersätze, Energiepreise, Normstände) nie fest einprogrammieren: Eingabe mit Standardwert und Datenstand (`.ls-stand`).

## Datenschutz (Repo ist öffentlich)
- Keine Kundennamen, Adressen, Telefonnummern, echten Bauvorhaben; Beispiele heißen „BV Muster“.
- Keine Einkaufspreise, Konditionen, Kalkulations- oder Kostensätze, Margen. Listenpreise der Website sind erlaubt.
- `lager.json` nur Artikel und Stückzahlen. DATANORM/DATPREIS bleiben in `.gitignore`. Prüfbefehl: `git log --all --oneline -- ':(icase)*datanorm*' ':(icase)*datpreis*'`.

## Was eine KI hier nicht tut
- Keine Rechenlogik „verbessern“, ohne dass die Referenzwerte das verlangen und Fabian es bestätigt.
- Keine Entscheidungen erfinden: Unsicheres als Frage an Fabian formulieren, nicht als Fakt einbauen. Neue Entscheidungen gehören in `06_entscheidungen.md` des Firmengehirns.
- Keine externen Bibliotheken, Fonts oder CDNs einbinden.
- Keine Altlasten löschen, ohne dass sie in `04_tool-konventionen.md` als zu löschen stehen und Fabian zugestimmt hat.

## Prüfung vor jedem Commit
1. `python3 _build/inline.py` gelaufen; kein Tool ohne Marker.
2. Referenzwerte des betroffenen Tools unverändert (oder Abweichung begründet und bestätigt).
3. Keine Personendaten, keine Preise im Diff.
4. `CHANGELOG.md` ergänzt.
5. Commit-Nachricht: `TOOLNAME: was · warum` (z. B. `heizkoerper: Umbau auf design.css 2.1 · Referenzwerte H1–H6 geprüft`).

## Ordner
```
/                   Tools (*.html), index.html, lager.json, CLAUDE.md, CHANGELOG.md, DESIGNREGELN.md, UMBAU-ABLAUF.md, styleguide.html
assets/css/         design.css
assets/js/          ls.js
assets/logo/        logo-variante-b.svg (Kopf), logo-variante-a.svg (Symbol), PDFs
assets/icons/       icons.html (Icon-Satz), apple-touch-icon.png, favicon.svg, icon-192/512.png
bilder/             Kachelbilder der Startseite, 16:9, 900 × 506
vorlagen/           tool-vorlage, bericht-vorlage, index-vorlage, feldliste-vorlage
tests/              referenzwerte.md, feldliste-*.md, pdf/
_build/             inline.py, build.py, Styleguide-Quellen
alt/                abgelöste Fassungen bis zum nächsten Umbau
```
