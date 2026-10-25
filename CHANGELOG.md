# CHANGELOG · Interne Tools der Lutz Spring GmbH

Neueste Einträge oben. Format: Datum · Bereich · Fassung · Änderung · Nachweis.

## 2026-10-25 · Designsystem · 2.1.2
- Kopf: Toolname rechts oben über Kunde/Projekt und Datum (20 px, halbfett), kein Untertitel, Kopf zweispaltig (Logo links, Block rechts); Theme-Schalter mit Deckkraft 0,45 / 1 / 0,3 wie das Haus-Icon. Vorlagen, Styleguide, index.html und kostenvergleich.html angepasst [Fabian 2026-10-25]. `_build/patch-kopf.py`.

## 2026-10-25 · Designsystem · 2.1.1 (Theme-Schalter)
- Theme-Schalter als runder Symbolknopf `.ls-theme-toggle` (Mond/Sonne) statt Textbutton „Dunkel / Hell“; Tokens `--ls-icon-moon/--ls-icon-sun`; in Vorlagen, Styleguide, index.html und kostenvergleich.html. Anlass: Backlog (Fabian, „zu klobig“). `_build/patch-toggle.py`.

## 2026-10-25 · kostenvergleich.html · Nachbesserung nach Durchsicht (Fabian)
- Weitere Baureihen in der Auswahl (gruppiert): Aeroblock WAB 8-A/11-A/14-B, Geoblock WGB 8/14, WWP LA 20/30-A R / 43/60-A R; Tabelle `GERAETE` im Tool mit SCOP, Leistung und Quelle je Gerät. Belegt: WWP LA W35/W55 (Fachinformation 83603701, 07/2026), WAB W35 (weishaupt.de 10/2026) + ηs/Leistung (83601801, 01/2026), WGB W35 (83600601, 09/2021) + ηs. SCOP W55 für WAB und WGB ist nirgends veröffentlicht (Weishaupt-Website, Fachinformationen, Anleitungen, HSB Schweiz geprüft); auf Wunsch von Fabian („notfalls errechnet“) aus der ηs zurückgerechnet: SCOP = (ηs + 3) × 2,5 ÷ 100 (Verordnung (EU) 813/2013), an sechs belegten Weishaupt-Paaren auf ≤ 0,4 Prozentpunkte geprüft; Werte WAB 8-A ≈ 3,58 · 11-A ≈ 3,53 · 14-B ≈ 3,83 · WGB 8 ≈ 3,63 · WGB 14 ≈ 3,83, im Tool mit Herleitung am Feld, im Bericht und im Fuß; Selbstprüfung beim Start. Referenzfälle K5 (WWP LA 20/30-A R, W35) und K6 (WAB 11-A, W50). Heruntergeladene Unterlagen im Firmengehirn unter `06_datenblaetter/` mit Übersicht (nicht im Repo). Auswahlwerte heißen jetzt „WEB 9/14“ statt „9/14“ (keine Projektdateien betroffen). Werte in 05_fachwissen.md eingetragen.
- Kopf: nur „Kostenvergleich“ als Titel, rechts über Kunde/Projekt und Datum; der Untertitel entfällt [Fabian 2026-10-25]. Dafür in design.css 2.1.1: Kopf ohne Titelblock, `.ls-header__meta` darf den Titel tragen.
- Regler in der PV-Karte standen nicht auf einer Höhe: Ursache war `align-content` der Felder (Zeilen wurden gestreckt). Fix in design.css 2.1.1 (`.ls-field { align-content: start }`), gilt für alle Tools.
- „Erweitert“ (Heizstab-Anteil) steht jetzt in der Karte Wärmepumpe; die Toolbar „Bericht drucken / PDF · Zurücksetzen“ steht am Formularende [BESTÄTIGT, Fabian 2026-10-25, 06].
- Heizflächen-Option „Heizkörper · W50“ statt W55: Wir legen auf 50 °C aus. Der SCOP W50 wird linear zwischen den Datenblattpunkten W35 und W55 interpoliert, auf 2 Stellen gerundet und im Tool als ≈ mit Herkunft ausgewiesen (Funktion `scopFuer`). Kein Datenblattwert; Nachfrage bei Weishaupt als offener Punkt 07/21. Neuer Referenzfall K4 (erwartet = gemessen); K2 bleibt über „manuell, JAZ 3,79“ reproduzierbar und wurde so nachgemessen. PDF `tests/pdf/kostenvergleich_K4_neu.pdf`.
- Standardwerte bestätigt: Strom 30 ct/kWh, Gas 14 ct/kWh (bewusst am oberen Rand, Hinweis am Feld), Heizöl 1,80 €/L.

## 2026-10-25 · kostenvergleich.html · Umbau Schritt 4–8 (Neubau, Referenzwerte neu, Prüfung, Doku)
- Neue `kostenvergleich.html` aus `vorlagen/tool-vorlage.html` (design.css 2.1.1, ls.js eingefügt mit `_build/inline.py`). Bauplan: Kopf mit Logo B, „So geht’s“, Projekt (Kunde / Projekt ohne Personendaten), Karten Wärmebedarf · Wärmepumpe · Bestandsanlage · Photovoltaik · Erweitert (Heizstab), Ergebnis mit Kennzahlen, Balkendiagramm (`.ls-chart`, Farben WP Navy / Bestand Grau / WP+PV Ocker), Empfehlungskarte Navy mit Badge „Vorschlag“, Bericht „Grundlage und Rechenweg“ (`.ls-report`, `.ls-dl`, erscheint im Druck), Fuß, Haus-Icon. `noindex`, Homescreen-Metadaten, Theme-Schalter.
- Rechenteil unverändert aus der Altfassung (effektive JAZ, ct/kWh Wärme, Jahreskosten, PV, Ersparnis); SCOP-Tabelle WEB 7/10–13/20 aus Weishaupt Fachinformation 83603801. Live-Rechnung bei jeder Eingabe; Primärbutton „Bericht drucken / PDF“, „Zurücksetzen“, „Neues Projekt“ mit Rückfrage; Eingaben im Browser gemerkt (`LS.formularMerken`); keine Dateifunktionen.
- Gewollte Abweichungen [BESTÄTIGT, Fabian 2026-10-25, in 06]: SCOP exakt (Altfassung rundete über den Regler auf 0,1); Heizöl in €/L statt ct/L; Preisbereiche Strom 10–50 ct/kWh, Gas 5–50 ct/kWh, Öl 0,40–2,50 €/L; Standardwerte Strom 30 ct/kWh, Gas 14 ct/kWh (bewusst am oberen Rand, Markt Brandenburg 10/2026 ≈ 12 ct/kWh), Öl 1,80 €/L [alle BESTÄTIGT, Fabian 2026-10-25]; Datenstand 10/2026 als `.ls-stand` an beiden Karten. Energiepreis und Nutzungsgrad je ein Feld, das mit Gas/Öl umschaltet (Standard 92 % / 88 %). Negative Ersparnis als „Mehrkosten pro Jahr“.
- Designsystem 2.1.1 (gleiche Sitzung, da Baustein fehlte): Regler mit Zahlenfeld `.ls-range` (design.css 10.12) + `LS.regler` (ls.js); Kennzahlen in der Navy-Karte `.ls-card--navy .ls-kpi` (vorher Inline-Stil im Styleguide). Styleguide neu gebaut, `inline.py` über alle Tools (index.html dadurch mit 2.1.1).
- Referenzwerte K1–K3 in der Neufassung gemessen (`tests/referenzwerte.md`, Spalte „neu“): K1 identisch mit alt; K2/K3 entsprechen der exakten Formel (gewollt). PDFs `tests/pdf/kostenvergleich_K1_neu.pdf` bis `K3_neu.pdf`.
- Geprüft im Browser (Chromium): Hell und Dunkel, Desktop und 400 px (kein seitliches Scrollen, Diagramm folgt der Breite), Druck (nur Kopf, Ergebnis, Bericht, Fuß). Offen: Prüfung auf dem iPad und in Safari durch Fabian (Schritt 6), Freigabe (Schritt 9). Zwei Gestaltungspunkte für das Designsystem in `BACKLOG.md` (Kopf im Druck, Fuß auf Folgeseite).
- Datenschutz geprüft: keine Personendaten, nur öffentliche Energiepreise mit Quelle und Datenstand, keine Kalkulationswerte.

## 2026-10-25 · kostenvergleich.html · Umbau Schritt 3 (Referenzwerte mit der Altfassung gemessen)
- K1–K3 in der unveränderten Altfassung gemessen (lokaler Server, Chromium, Eingaben per Skript), Spalte „alt“ in `tests/referenzwerte.md` gefüllt; PDFs `tests/pdf/kostenvergleich_K1_alt.pdf` bis `K3_alt.pdf`.
- Befund: Die Altfassung rundet übernommene SCOP-Werte über den JAZ-Regler (Schritt 0,1) auf 3,8 / 5,1 statt 3,79 / 5,09; K2/K3 weichen deshalb um wenige € von der exakten Formel ab. Entscheidung für den Neubau offen (Feldliste, Frage 8).
- Feldliste von Fabian freigegeben („passt“, 2026-10-25); die Vorschläge zu den offenen Fragen 2–5 und 7 gelten damit als angenommen, Frage 1 (Datenstand Energiepreise) bleibt offen.

## 2026-10-25 · kostenvergleich.html · Umbau Schritt 1 (Altfassung festhalten) und Schritt 2 (Feldliste)
- Altfassung (Stand 04: 2026-07-26, Erkennungsmerkmal Haus-Icon stimmt; Live-Datei nutzt zusätzlich `theme.css`, Stand im Git = Grundlage) gesichert als `alt/kostenvergleich_2026-10-25.html` (byteidentisch).
- Zweck: Jahresheizkosten Wärmepumpe gegen Gas oder Öl (Umschalter), optional PV-Block; Ersteinschätzung für das Kundengespräch, Druck als PDF.
- Datenquellen: eingebettete SCOP-Tabelle `webData` (EN 14825, WEB 7/10, 9/14, 10/15, 13/20 bei W35/W55 und Nennwärmeleistung A−7/W35) aus Weishaupt Fachinformation 83603801; Standardwerte Strom 27 ct/kWh, Gas 11 ct/kWh, Öl 95 ct/L, Nutzungsgrad Gas 92 %, Öl 88 %, Heizwert Öl 10 kWh/L, PV 8 kWp · 950 kWh/kWp · 25 % Deckung. Keine externe Datei, keine Dateifunktionen (kein Sichern/Laden, kein localStorage), keine Kunde/Projekt-Angabe, kein `noindex`, keine Homescreen-Metadaten.
- Rechenteil (wird unverändert übernommen): `webData`, `applyWebModel()` (SCOP-Übernahme, JAZ gesperrt), `calc()` (effektive JAZ mit Heizstab-Anteil, Wärmegestehungskosten ct/kWh, Jahreskosten, PV-Ertrag/-Deckung/-Ersparnis, Ersparnis absolut und in %), `fmtEUR`/`fmtCt` (Rundung). Alles andere (Schieberegler, Emoji, Farben, Balken, Druck-CSS) ist Oberfläche.
- Feldliste `tests/feldliste-kostenvergleich.md` angelegt (15 Felder alt, Vorschlag neu mit Gruppen, „Erweitert“, offene Fragen). Testfälle K1–K3 in `tests/referenzwerte.md` angelegt (erfundene Werte, Spalte „alt“ wird in Schritt 3 gemessen). Freigabe durch Fabian steht aus.

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
| kostenvergleich.html | 2026-07-26 | gebaut 2026-10-25 (Schritt 1–8), Freigabe offen | tests/feldliste-kostenvergleich.md (freigegeben) | K1–K6 alt und neu gemessen (K2/K3 gewollt abweichend: SCOP exakt; K4 neu für W50, K5 für WWP LA, K6 für WAB) | – (Schritt 9) |
| foerderung.html | – | offen | – | – | – |
| auslegung.html | 2026-08-17 | offen | – | A1–A4 | – |
| heizkoerper.html | 2026-08-14 | offen | – | H1–H6 | – |
| bestandsaufnahme.html | 2026-08-14 | offen | – | B1–B3 | – |
| bad-angebot.html | – (Neubau) | offen | – | – | – |
