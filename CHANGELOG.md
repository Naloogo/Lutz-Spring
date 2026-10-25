# CHANGELOG · Interne Tools der Lutz Spring GmbH

Neueste Einträge oben. Format: Datum · Bereich · Fassung · Änderung · Nachweis.

## 2026-10-25 · index.html · Umbau Schritt 4 (Neubau aus Vorlage)
- Neue `index.html` aus `vorlagen/index-vorlage.html` (design.css 2.1, ls.js eingefügt mit `_build/inline.py`). Logo B als Inline-SVG im Kopf, kein Text-Slogan mehr (steht im Logo); Favicon `assets/icons/favicon.svg`, Homescreen-Symbol `assets/icons/apple-touch-icon.png`; Homescreen-Name bleibt „Lutz Spring“; `noindex`; Theme-Schalter.
- Alle sechs Kacheln der Altfassung erhalten, Bilder aus `bilder/`. Links unverändert: auslegung, foerderung, kostenvergleich, heizkoerper, bestandsaufnahme. Titel gekürzt (freigegeben von Fabian): „Wärmepumpen-Auslegung“ (statt „Wärmepumpen Auslegungstool“), „Förderrechner Wärmepumpe“, „Heizkörper-Auslegung“, „Angebotserstellung Bad“.
- Kachel „Angebotserstellung Bad“ sichtbar, ohne Link, Badge „in Vorbereitung“ statt „Öffnen“, bis `bad-angebot.html` gebaut ist [BESTÄTIGT, Fabian 2026-10-25]. Im Code als Kommentar vermerkt.
- `theme.css` und `logo.png` werden von der Startseite nicht mehr gebraucht; sie bleiben für die alten Tools im Hauptordner (CLAUDE.md, Übergang).
- Neu: `.claude/launch.json` (lokaler Vorschau-Server `python3 -m http.server`, Port 8731) für die Prüfung in Claude Code; ohne Wirkung auf GitHub Pages.
- Geprüft im Browser (Chromium): Hell und Dunkel, Desktop und 400 px; auf dem iPad geprüft (Fabian, Schritt 6).
- Nach iPad-Prüfung: Überschrift „Interne Werkzeuge“ und Untertitel aus dem Kopf entfernt, Kopf nur Logo und Theme-Schalter [BESTÄTIGT, Fabian 2026-10-25].

## 2026-10-25 · index.html · Umbau Schritt 1 (Altfassung festhalten)
- Altfassung (Stand 04: 2026-08-07, Slogan + Kachel „Bestandsaufnahme“; Live-Datei zusätzlich mit Kachel „Angebotserstellung Badezimmer“) gesichert als `alt/index_2026-10-25.html`.
- Inhalt der Altfassung: Kopf mit Logo (Base64-PNG) und Text-Slogan; Abschnitt „Interne Werkzeuge“; sechs Kacheln mit relativen Links: auslegung, foerderung, kostenvergleich, heizkoerper, bestandsaufnahme, bad-angebot; Fuß „Lutz Spring GmbH · Interne Anwendung · Alle Berechnungen sind Überschlagswerte …“. Keine Rechenlogik, keine Dateifunktionen, keine Datenquellen. Abhängigkeiten: `theme.css`, Favicon/Homescreen-Symbol als Base64.
- Sechs eingebettete Kachelbilder als JPEG nach `bilder/` ausgelagert (Originalbytes, unverändert): `evoblock.jpg`, `foerderung.jpg`, `kosten.jpg`, `heizkoerper.jpg`, `lager.jpg`; `bad.jpg` war 840 × 473 und wurde auf 900 × 506 gebracht. Alle 16:9, 900 × 506. Keine Personen, Klingelschilder oder Kennzeichen.

## 2026-10-25 · Repo · Übernahme
- Neues Repo `Naloogo/lutz-spring-tools` ohne Historie. Aus `Naloogo/Auslegung-WP` (Stand 4cfc7ae) übernommen: index, auslegung, bestandsaufnahme, foerderung, heizkoerper, kostenvergleich, lager.json, theme.css, logo.png, robots.txt; alte CLAUDE.md als `TOOLS-WISSEN.md`; alte Vorlage nach `alt/`. Geprüft: keine Kundendaten, keine Preise (nur öffentliche Energiepreise und KfW-Sätze).
- `bad-angebot.html` wird neu gebaut (noch kein fertiges Tool); `tests/referenzwerte.md` ist anzulegen.

## 2026-10-25 · Designsystem · 2.1
- Neue Bausteine in `design.css`: Startseiten-Kacheln, Positionsliste, Inline-Rückfrage, Dialog, Toast, Stepper, Datenstand, „So geht’s“, Karten-Tabellen (< 700 px), Diagramm-Tokens, Datei-Baustein, Berichtsvorlage; Safe-Area oben; Druck nur Kopf/Ergebnis/Bericht/Fuß, keine Seitenzahlen.
- Neu: `assets/js/ls.js` (Zahlen, Speicher, Theme, Toast, Rückfrage, Fehler, Dateien, Migration), `assets/icons/` (Icon-Satz, Homescreen-Symbol aus Logo A, Favicon), `vorlagen/bericht-vorlage.html`, `vorlagen/index-vorlage.html`, `vorlagen/feldliste-vorlage.md`, `UMBAU-ABLAUF.md`, `CLAUDE.md`, `_build/inline.py`.
- `vorlagen/tool-vorlage.html` nutzt `ls.js`, Marker, „So geht’s“, Positionsliste, „Erweitert“, Datei sichern/laden mit Zuordnung, Rückfrage bei „Neues Projekt“.
- Regeln (DESIGNREGELN.md 2.1): Einfügen von CSS/JS beim Veröffentlichen, Ausnahmen für Symbol und Kachelbilder, iPadOS 16, Scrollen zum Ergebnis, Tabellenregel, Diagrammfarben, Rückfragen/Toasts, Datenstand, Vokabular, JSON-Regel, Berichtsaufbau. Entscheidungen Fabian 2026-10-25.

## 2026-10-25 · Designsystem · 2.0.1
- Logo Variante B als Inline-SVG im Kopf; Logo-Gelb #fff200 ersetzt #f5e400; Regel 6.1 „Formulare beim Neubau aufräumen“; Vorschläge bestätigt (Raster, Druck hell, noindex, Touch 44 px, Schreibweisen, Dunkelmodus-Werte).

## 2026-10-19 · Designsystem · 2.0
- Farbwelt „Marine & Signalgelb“; `design.css` 2.0 mit Tokens hell/dunkel, Komponenten, Druck; `DESIGNREGELN.md`; `styleguide.html`; `vorlagen/tool-vorlage.html`. Ersetzt `design.css` 1.0 aus Branch `tools-ueberarbeitung`.

## Tools (Umbau auf 2.1)
| Tool | Stand alt (04) | Umbau | Feldliste | Referenzwerte | Freigabe |
|---|---|---|---|---|---|
| index.html | 2026-08-07 | umgebaut 2026-10-25 | entfällt | entfällt (Kacheln/Links erhalten) | Fabian, 2026-10-25 |
| kostenvergleich.html | 2026-07-26 | offen | – | K1–K3 | – |
| foerderung.html | – | offen | – | – | – |
| auslegung.html | 2026-08-17 | offen | – | A1–A4 | – |
| heizkoerper.html | 2026-08-14 | offen | – | H1–H6 | – |
| bestandsaufnahme.html | 2026-08-14 | offen | – | B1–B3 | – |
| bad-angebot.html | – (Neubau) | offen | – | – | – |
