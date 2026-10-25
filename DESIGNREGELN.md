# Designregeln für die internen Werkzeuge der Lutz Spring GmbH

Version 2.1.2 · Stand 2026-10-25 · gilt für alle bestehenden und künftigen HTML-Tools im Repo
Zugehörige Dateien: `assets/css/design.css` (Stil), `assets/js/ls.js` (gemeinsames Verhalten), `assets/icons/` (Symbole), `assets/logo/` (Logo), `styleguide.html` (lebende Referenz), `vorlagen/` (tool-vorlage, bericht-vorlage, index-vorlage, feldliste-vorlage), `UMBAU-ABLAUF.md` (Schritte je Tool), `CLAUDE.md` (Anweisungen für die KI im Repo), `CHANGELOG.md`
Kennzeichnung wie im Firmengehirn: [BESTÄTIGT] = von Fabian/GF entschieden · [VORSCHLAG] = von Claude vorgeschlagen, noch nicht bestätigt · [BELEGT] = rechnerisch oder am Datenblatt geprüft

---

## 0 · Wofür dieses Dokument

Alle Werkzeuge sollen aussehen und sich bedienen lassen wie **ein** Programm. Wer ein Tool neu baut oder ein bestehendes aus dem Repo rekonstruiert (Mensch oder KI), hält sich an diese Regeln und benutzt ausschließlich die Klassen und Variablen aus `design.css`. Eigene Farben, Schriften oder Abstände in einem Tool sind nicht erlaubt; fehlt etwas, wird es in `design.css` ergänzt und im Styleguide gezeigt, damit alle Tools es bekommen.

Leitbild: **klar, ruhig, schnell.** Gestaltung nach Apple-Maßstab heißt hier: wenige Farben, viel Weißraum, Systemschrift, Tiefe nur durch feine Linien und einen Hauch Schatten, klare Hierarchie, jede Interaktion sichtbar. Es sind Arbeitswerkzeuge: Dichte und Tempo gehen vor Schmuck. [BESTÄTIGT: „gleicher Stil, moderner, schick“, 03_design-system.md; Apple-Stil Wunsch von Fabian, 2026-10-19]

---

## 1 · Technische Basis

| Regel | Status |
|---|---|
| Einzelne HTML-Dateien, offline-fähig, laufen auf iPad/Safari (Homescreen-App) und auf dem Mac | [BESTÄTIGT] |
| Hosting GitHub Pages; Dateinamen klein, ohne Umlaute und Leerzeichen, Tools im Hauptordner; vor jedem `href` Dateinamen prüfen (Groß/Klein) | [BESTÄTIGT] |
| Eine gemeinsame Stildatei `assets/css/design.css` und ein gemeinsames Skript `assets/js/ls.js`. Beide werden beim Veröffentlichen **in jedes Tool eingefügt** (`python3 _build/inline.py`, Marker `<!-- design.css:start/end -->` und `<!-- ls.js:start/end -->`). So bleibt jedes Tool eine einzelne, offline-fähige Datei und die Pflege liegt trotzdem an einer Stelle | [BESTÄTIGT, 2026-10-25] |
| Keine externen Abhängigkeiten: keine Web-Fonts, keine CDN-Skripte, keine Icon-Bibliotheken. Icons und Logo als Inline-SVG (ersetzt das Base64-PNG; gleiche Wirkung, aber umfärbbar und verlustfrei) | [BESTÄTIGT, 2026-10-25] |
| Zwei Ausnahmen als echte Dateien im Repo: Homescreen-Symbol `assets/icons/apple-touch-icon.png` (Logo A auf Navy; iOS nimmt dafür keine Data-URI) mit `assets/icons/favicon.svg`, und die Kachelbilder der Startseite `bilder/*.jpg`. Fehlt ein Kachelbild, zeigt `ls.js` einen Platzhalter | [BESTÄTIGT, 2026-10-25] |
| Mindestversion iPadOS/Safari 16 (für `:has()`, `min()`, `<details>`, `<dialog>`) | [BESTÄTIGT, 2026-10-25] |
| Homescreen-App: Statusleiste durchscheinend, deshalb reserviert `design.css` oben, unten und seitlich die Safe-Area (`env(safe-area-inset-*)`) | [BESTÄTIGT, 2026-10-25] |
| Kein Framework (React o. Ä.). Reines HTML/CSS/JS reicht für iPad + Mac und braucht keinen Build-Schritt | [BESTÄTIGT, 2026-10-19] |
| `<meta name="robots" content="noindex, nofollow">` in jedem Tool | [BESTÄTIGT, 2026-10-25] |
| Kopf jeder Datei: `viewport-fit=cover`, `theme-color #1a2b4a`, `apple-mobile-web-app-capable`, `apple-mobile-web-app-status-bar-style black-translucent`, `apple-mobile-web-app-title` | [BESTÄTIGT: bisherige Praxis] |
| Keine veränderlichen Werte (Förderquoten, Energiepreise, Normstände) fest einprogrammieren, sondern als sichtbare, änderbare Eingabe mit Standardwert | [VORSCHLAG] |

---

## 2 · Farben

Tokens in `design.css`, Abschnitt 1. Farbwelt **„Marine & Signalgelb“** [BESTÄTIGT: Auswahl Fabian, 2026-10-19 aus drei Vorschlägen].

**Hell (Standard)**

| Token | Wert | Verwendung |
|---|---|---|
| `--ls-navy` | `#1a2b4a` | Kopfbalken, Nummernkreise, Empfehlungskarte, Primärbutton [BESTÄTIGT] |
| `--ls-yellow` | `#fff200` | Logo-Gelb [BESTÄTIGT, 2026-10-25; ersetzt #f5e400]. Logo, Markierung, Kennwerte auf Navy. **Nie als Text auf Weiß/Creme** (Kontrast 1,3:1) |
| `--ls-yellow-ink` | `#8a6d00` | „gelber“ Text auf hellem Grund, 4,9:1 [BELEGT] |
| `--ls-bg` | `#f4f3ee` | Seitenhintergrund Creme [BESTÄTIGT] |
| `--ls-surface` / `-2` / `-3` | `#ffffff` / `#faf9f5` / `#efede6` | Karten / Eingaben, Tabellenköpfe / gedrückt |
| `--ls-text` / `-2` / `-3` | `#1d1d1f` / `#6b6b70` / `#8e8e93` | Text / Labels, Sekundäres (4,8:1 auf Creme) / nur Platzhalter |
| `--ls-ok` `--ls-warn` `--ls-danger` `--ls-info` | `#1a7a36` `#b25000` `#d70015` `#1a2b4a` | Zustände; dazu je `…-bg` als helle Fläche |

**Dunkel** (folgt dem System oder `data-theme="dark"` auf `<html>`): Hintergrund `#141416`, Karten `#1e1e20`, Text `#f5f5f7`, Primärbutton Stahlblau `#4f75b8` (Navy wäre auf dunklem Grund unsichtbar), Links `#8fb3f0`, Kopfbalken `#16233d`, Gelb unverändert. Zustandsfarben heller: `#30d158` `#ff9f0a` `#ff453a`. [BESTÄTIGT, 2026-10-25; Kontraste BELEGT ≥ 4,5:1]

Regeln:
1. Farben nur über `var(--ls-…)`. Kein Hex-Wert in einem Tool.
2. Zustand wird **doppelt** codiert: Farbe **und** Text/Symbol („115 % gedeckt“, nicht nur grün). Grund: Schwarzweißdruck, Farbsehschwäche.
3. Gelb ist Marke, nicht Zustand. Warnung ist Orange. Beides nie nebeneinander als Bedeutungsträger.
6. **Logo:** Variante B (Wortmarke mit Slogan und „GmbH“, Datei `assets/logo/logo-variante-b.svg`) in allen Tools und Dokumenten [BESTÄTIGT, 2026-10-25]. Es wird als Inline-SVG mit `currentColor` eingebettet, Farbe `--ls-yellow`, mindestens 280 px breit (darunter ist der Slogan im Logo unlesbar). Das Logo steht **immer auf Navy** – im Kopfbalken hell wie dunkel und im Druck (Hintergrundfarben erzwungen). Die Navy-Umfärbung (`.ls-header__logo--navy`) ist keine zweite Logofassung für den Regelfall, sondern die Ausweichregel für Stellen ohne Navy-Fläche (z. B. ein Fuß auf Weiß, eine Kachel auf Creme); solche Stellen gibt es in den Tools derzeit nicht. Variante A (ohne Slogan) wird nicht verwendet.
4. Je Ansicht genau **ein** primärer Button in Navy/Stahlblau. Alles andere sekundär (weiß mit Rand) oder dezent.
5. Kein eigener Dunkelmodus pro Tool: wer `design.css` einbindet, bekommt ihn. Der Schalter im Kopf ist ein runder Symbolknopf ohne Text (`.ls-theme-toggle`, Mond im Hell-, Sonne im Dunkelmodus, `aria-label`), so zurückhaltend wie das Haus-Icon (Deckkraft 0,45 / 1 bei Berührung / 0,3 gedrückt); kein Textbutton [BESTÄTIGT, 2026-10-25].

---

## 3 · Schrift und Zahlen

- Systemschrift: `-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, Arial` – keine Web-Fonts [BESTÄTIGT: keine externen Abhängigkeiten].
- Größenstufen (px): 28 Seitentitel · 22 Abschnitt · 17 Kartentitel · 15 Fließtext und Eingaben · 13 Labels, dichte Tabellen · 12 Fußnoten · 32 Kennzahl. Nur diese Stufen verwenden. Zeilenhöhe 1,45.
- Gewichte: 400 Text, 500 Labels/Werte, 600 Titel und Buttons, 700 Kennzahlen. Nie 300 oder 800 im Fließtext.
- Zahlen in Spalten: `font-variant-numeric: tabular-nums` (Klasse `.ls-num`), rechtsbündig.
- Schreibweisen [BESTÄTIGT: ≈ seit 2026-10-18, übrige 2026-10-25]:
  - Richtwerte **immer** mit „≈“ (Klasse `.ls-approx` setzt es automatisch vor den Wert).
  - Einheit mit schmalem Leerzeichen: `640 W`, `50/40 °C`, `600 × 1300 mm`, `12 450 kWh`. Multiplikationszeichen „×“, nicht „x“.
  - Dezimaltrennzeichen Komma, echtes Minus „−“ (U+2212): `−12,7 °C`.
  - Tausender: schmales Leerzeichen oder Punkt, in einem Tool nur eine Variante.
  - Artikelnummern in Monospace (`<code>`), damit sie sich vom Text abheben und kopieren lassen.
  - Firmenname immer „Lutz Spring GmbH“, Slogan „Heizung · Sanitär · Wärmepumpen“ (Plural, Mittelpunkt) [BESTÄTIGT].
  - HKV = Heizkreisverteiler [BESTÄTIGT].

---

## 4 · Raster, Abstände, Form

- Inhaltsbreite max. 1400 px, mittig (`.ls-container`) [BESTÄTIGT].
- Karten im Raster `repeat(auto-fit, minmax(250px, 1fr))` (`.ls-grid`), unter 700 px einspaltig [BESTÄTIGT].
- 8-px-Raster: 4 · 8 · 12 · 16 · 24 · 32 · 48 (`--ls-s1 … s7`). Innen in Karten 24, zwischen Karten 16, zwischen Feldern 12, zwischen Abschnitten 32. [BESTÄTIGT, 2026-10-25]
- Radien: 8 Eingaben · 12 Buttons und Hinweise · 16 Karten und Kopfbalken · Pille für Badges. Kopfbalken mit runden Ecken [BESTÄTIGT].
- Schatten nur zwei Stufen (`--ls-shadow-1` Karten, `--ls-shadow-2` schwebende Elemente). Keine Verläufe, keine Glas-Effekte.
- Seitenrand mindestens 16 px, auf dem iPhone/iPad mit `env(safe-area-inset-*)`.
- Abstände kommen vom Eltern-Raster (`gap`), nicht von Margins einzelner Karten.

---

## 5 · Bauplan einer Werkzeugseite

Reihenfolge von oben nach unten (nicht benötigte Teile entfallen, die Reihenfolge bleibt):

1. **Statuszeile** (`.ls-status`) – nur, wenn externe Daten geladen wurden („Lagerbestand geladen: 14 Positionen · Stand …“).
1a. **So geht’s** (`.ls-help`, eingeklappt) – ersetzt lange Erklärtexte; enthält bei Tools mit Dateien den iPad-Hinweis (Safari statt Vorschau, Teilen-Blatt → Dateien).
2. **Kopf** (`.ls-header`) – zwei Spalten: links Logo Variante B (Slogan im Logo), rechts ein Block mit Toolname (20 px, halbfett) über Kunde/Projekt und Datum, darunter der Theme-Schalter. Kein Untertitel, kein Titelblock in der Mitte [BESTÄTIGT, 2026-10-25]. Der Kopf erscheint im Druck und ist damit die Kopfzeile des Berichts.
3. **Projekt & Verwaltung** – Kunde/Projekt (Hinweis: keine Personendaten, „BV Muster“ oder Ort + Gewerk), Raum/Position, Speichern/Laden (Datei), Export (PDF, GAEB).
3a. **Gespeicherte Positionen** (`.ls-items`) – nur bei Tools mit mehreren Räumen/Positionen: Nummer, Name, Kurzzeile, Aktionen Bearbeiten/Duplizieren/Löschen; die aktive Position ist markiert.
4. **Eingaben** – Karten mit `.ls-fields`; Standardwerte vorbelegt.
5. **Aktionen** – `.ls-toolbar` mit genau einem Primärbutton („Passende Heizkörper suchen“, „Berechnen“) und „Zurücksetzen“.
6. **Ergebnis** – zuerst Kennzahlen (`.ls-kpis`), dann Tabelle oder Liste zum Auswählen, zuletzt Details und Rechenweg.
7. **Bestellung / Bericht** – Zusammenfassung zum Drucken (Label/Wert-Liste `.ls-dl`, Bestelltabellen, Notizen `.ls-notiz`).
8. **Fuß** (`.ls-footer`) – Norm/Quelle, „Angaben ohne Gewähr – maßgeblich sind die Herstellerunterlagen“, „Lutz Spring GmbH · Interne Anwendung“.
9. **Haus-Icon** (`.ls-home`) – Rücklink zur `index.html`, 48 × 48 px, unten mittig, Deckkraft 0,45 / 1 bei Berührung / 0,3 gedrückt, im Druck ausgeblendet [BESTÄTIGT].

---

## 6 · Formulare

- Label über dem Feld (`.ls-label`), Einheit **am** Feld als Suffix (`.ls-unit`), nie im Wert oder im Label versteckt.
- Zahlenfelder als `type="text" inputmode="decimal"`: Komma und Punkt akzeptieren, keine Spin-Buttons, auf dem iPad erscheint die Zifferntastatur. Einlesen mit einer gemeinsamen Funktion (siehe Vorlage: `lesen()`), die „≈“, Leerzeichen und „−“ toleriert.
- Standardwerte aus dem Firmengehirn vorbelegen: Norm-Außentemperatur −12,7 °C (Region Oranienburg), Bivalenzpunkt −7 °C, Heizgrenze 15 °C Bestand, System 50/40 °C [BESTÄTIGT]. Der Nutzer tippt nur, was abweicht.
- Hinweis (`.ls-hint`) unter dem Feld: Herkunft oder Regel in einer Zeile („aus dem Heizlastbericht, Raumwert“, „15 % ist kein Standard, Einzelfall“).
- Fehler (`.ls-error` + `aria-invalid="true"`): sagen, **was** falsch ist und **was zu tun** ist. Kein rotes Feld ohne Text. Fokus springt ins erste fehlerhafte Feld.
- Wenige Optionen (2–4) → Segment-Steuerung `.ls-seg`; viele → `.ls-select`; Ja/Nein → `.ls-check` oder `.ls-switch` (Switch nur für sofort wirkende Schalter).
- Regler (`.ls-range`, 2.1.1) nur zusammen mit einem Zahlenfeld und nur für Werte, die im Kundengespräch durchgespielt werden (Energiepreise, JAZ, Nutzungsgrad). Das Zahlenfeld ist maßgeblich und wird geprüft; der Regler klemmt an seinen Grenzen. Verhalten: `LS.regler(rangeId, inputId, stellen)` [BESTÄTIGT, Fabian 2026-10-25].
- Touch: auf iPad/Handy wachsen Felder und Buttons automatisch auf 44 px (`pointer: coarse`). Nichts kleiner als 32 px antippbar.
- Eingaben bleiben beim Verlassen der Seite erhalten (localStorage, `LS.formularMerken`), mit „Neues Projekt“ zurücksetzbar [BESTÄTIGT: bisherige Praxis].
- Projektdateien (JSON) tragen `version`, `tool`, `exportiert`, `projekt` und die Positionsliste; Dateiname `TOOL_BV-Muster_JJJJ-MM-TT.json` ohne Personendaten (`LS.dateiname`). Beim Laden werden alte Feldnamen über eine Zuordnungstabelle im Tool (`FELD_MAPPING`) auf neue abgebildet (`LS.datei.migrieren`), damit alte Dateien weiter laden [BESTÄTIGT, 2026-10-25].
- Jedes Tool mit Dateifunktionen zeigt im „So geht’s“ den iPad-Hinweis: Sichern über das Teilen-Blatt in die Dateien-App; zum Laden das Tool in Safari öffnen, nicht in der Vorschau (Quick Look). Externe Daten wie `lager.json` laden nur über die echte Adresse, nicht lokal [BELEGT: 04].
- **Beim Neubau eines bestehenden Tools sind Anordnung und Inhalt der Formularfelder ausdrücklich zu prüfen, nicht zu kopieren.** Ziel ist ein noch aufgeräumterer, minimalistischerer Aufbau auf derselben Grundlage. Was gleich bleiben muss, ist die Rechenlogik: gleiche Eingaben müssen dieselben Ergebnisse liefern (Nachweis über `tests/referenzwerte.md`). [BESTÄTIGT, Fabian 2026-10-25; ersetzt die Regel „Formularfelder bleiben unverändert“ aus dem Redesign-Prompt 2026-08-31]

### 6.1 · Formulare beim Neubau aufräumen [BESTÄTIGT, 2026-10-25]

Beim Nachbau wird jedes Feld der Altfassung einmal befragt: Braucht der Nutzer es bei jedem Durchlauf? Kann es einen Standardwert haben? Gehört es zu einer Gruppe? Daraus folgt:

- **Reihenfolge nach Arbeitsablauf**, nicht nach Entstehungsgeschichte des Tools: erst Projekt/Raum, dann das, was den Bedarf bestimmt, dann Einbauraum und Bauform, zuletzt Sonderfälle.
- **Gruppen statt Einzelfelder**: zusammengehörige Werte (VL/RL, BH × BL, Fenster/Wand/Dach) stehen in einer Karte oder in einer Zeile mit gemeinsamem Label.
- **Standardfall sichtbar, Sonderfall eingeklappt**: Felder, die selten vom Standard abweichen (Reserve, Heizkörperexponent, Heizstab-Anteil, Anschlussseite), kommen in einen Bereich „Erweitert“ (`<details>`), der zu ist, solange die Werte Standard sind. Der eingestellte Wert bleibt als Kurzzeile lesbar („Reserve 0 %“).
- **Ein Feld, ein Zweck**: Doppelungen (gleicher Wert an zwei Stellen) und Felder, die nur eine Zwischenrechnung anzeigen, werden Ergebnis statt Eingabe.
- **Weniger Auswahl, mehr Vorbelegung**: Was aus einer anderen Eingabe folgt (z. B. Konsolenanzahl aus BL), wird berechnet und angezeigt, nicht abgefragt.
- **Beschriftungen vereinheitlichen** über alle Tools: gleiche Größe heißt überall gleich (Norm-Außentemperatur, Heizlast Φ<sub>HL</sub>, Systemtemperatur VL/RL, Bauhöhe/Baulänge).
- **Feld-IDs dürfen sich ändern**, wenn die Rechenlogik mitgezogen wird. Jede Änderung an Feldern wird in einer kurzen Tabelle „alt → neu“ im Tool-Kommentar oder im `CHANGELOG.md` festgehalten, damit gespeicherte Projektdateien (JSON) weiter geladen werden können (Import-Zuordnung alt → neu).
- **Was ein Tool fachlich abfragt, bleibt**: Kein Feld entfällt, dessen Wert in die Rechnung eingeht, ohne dass der Wert anders herkommt (Standard, Ableitung). Im Zweifel bleibt das Feld und wandert nach „Erweitert“.

---

## 7 · Ergebnisse und Zustände

- Nach „Berechnen“: auf Touchgeräten scrollt die Seite zum Ergebnis und setzt den Fokus dorthin (`LS.zumErgebnis('ergebnis')`); auf dem Mac bleibt die Position [BESTÄTIGT, 2026-10-25].
- Erst die Antwort, dann die Herleitung. Kennzahlen (`.ls-kpi`) mit Label in Kapitälchen, großem Wert, Einheit klein, einer Zeile Einordnung.
- Rechenweg ausweisen: Formel, Eingangswerte, Zwischenergebnisse, Einheit [BESTÄTIGT: Organisationsanweisung]. Als aufklappbarer Block oder Hinweiskarte, im Druck sichtbar.
- Tabellen (`.ls-table` in `.ls-table-wrap`): Kopf fixiert, Zahlen rechts, Zeile antippbar = `tr.is-clickable`, gewählte Zeile = `tr.is-selected`. Breite Tabellen scrollen **im Rahmen**, die Seite scrollt nie seitwärts.
- Auf schmalen Schirmen (< 700 px): **Auswahltabellen** (der Nutzer tippt eine Zeile an, z. B. Heizkörper-Treffer) werden zu Karten (`.ls-table--cards`, jede Zelle mit `data-label`); **Bestell- und Berichtstabellen** scrollen im Rahmen [BESTÄTIGT, 2026-10-25].
- Diagramme (`.ls-chart`, Inline-SVG oder Canvas): feste Reihenfarben mit Bedeutung über alle Tools – Wärmepumpe Navy `--ls-chart-wp`, Bestand Gas/Öl Grau `--ls-chart-alt`, Strom/PV Ocker `--ls-chart-pv`, zweite Reihe Stahlblau `--ls-chart-2`; Werte stehen am Balken, Achsen beschriftet mit Einheit, Legende nur bei mehr als einer Reihe; Zustandsfarben sind keine Reihenfarben [BESTÄTIGT, 2026-10-25].
- Deckung/Status als Badge: `ok` gedeckt (≥ 100 %), `warn` knapp, `danger` nicht gedeckt – Schwellen pro Tool fachlich festlegen und im Tool nennen, nicht raten.
- Kennzeichen wie „Bestand“ und „aus Lager“ als neutrale/Info-Badges; sie gehen in Speichern, Druck und Bestellübersicht ein [BESTÄTIGT: Funktion heizkoerper.html].
- Leerzustand (`.ls-empty`) sagt, was zu tun ist („Raum benennen, Heizlast eintragen, ‚Passende Heizkörper suchen‘ wählen“), nie nur „Keine Daten“.
- Löschen und Verwerfen fragen **inline** nach (`LS.rueckfrage`: Frage, roter Bestätigen-Button, Abbrechen); nie Browser-Dialoge (`confirm()`). Größere Hinweise als natives `<dialog class="ls-dialog">`. Nach jeder Aktion eine kurze Rückmeldung (`LS.toast('Gespeichert', 'ok')`) [BESTÄTIGT, 2026-10-25].
- Veränderliche Werte (Fördersätze, Energiepreise, Normstände) sind Eingaben mit Standardwert und sichtbarem Datenstand (`.ls-stand`: „Fördersätze Stand 01/2026 · prüfen“) [BESTÄTIGT, 2026-10-25].
- Stückzahlen (Lager) mit Stepper (`.ls-stepper`, Minus/Wert/Plus), nie als freies Textfeld.
- Hinweise (`.ls-note--info/ok/warn/danger`) mit fettem erstem Satz; Warnungen mit Symbol. Ein Hinweis, der eine Handlung verlangt, steht **vor** dem Ergebnis; Erklärungen stehen dahinter.
- Empfehlungskarte (`.ls-card--navy`) mit gelben Kennwerten nur für die eine Empfehlung des Tools, nicht für jede Zeile.
- Vorschlagscharakter sichtbar machen: Badge „Vorschlag“, Fußzeile „Angaben ohne Gewähr“. Fachliche Ergebnisse sind Vorschläge, die Verantwortung trägt die Person, die sie verwendet [BESTÄTIGT].

---

## 8 · Sprache in der Oberfläche

- Intern, knapp, sachlich; Buttons im Infinitiv/Imperativ, die sagen, was passiert: „Passende Heizkörper suchen“, „Projekt sichern (Datei)“, „Bericht drucken“. Nie „OK“, „Absenden“, „Los“.
- Keine Anrede nötig; wo eine steht: Du (intern) [BESTÄTIGT: intern Du-Form].
- Texte, die der Kunde im PDF liest (Kopf, Fuß, Empfehlung): Sie-Form für den Kunden, Wir-Form für den Betrieb, kein Werbesprech, keine Zusagen zu Einsparung, Förderhöhe oder Terminen [BESTÄTIGT].
- Fachbegriffe wie im Betrieb: Heizlast, Bivalenzpunkt, Norm-Außentemperatur, Bauhöhe/Baulänge (BH/BL), Vorlauf/Rücklauf (VL/RL), HKV.
- Fehler- und Hinweistexte ohne Entschuldigung, ohne Ausrufezeichen, mit Handlungsanweisung.
- Festes Vokabular über alle Tools [BESTÄTIGT, 2026-10-25]:
  - Buttons: „Berechnen“ / „Passende Heizkörper suchen“ (Hauptaktion), „Zurücksetzen“, „+ Position speichern“ / „+ Raum speichern“, „Neues Projekt“, „Projekt sichern (Datei)“, „Projekt laden (Datei)“, „Bericht drucken / PDF“, „GAEB (.X83) für HERO“, „Artikeldaten laden“, „Bearbeiten“, „Duplizieren“, „Löschen“, „Abbrechen“, Theme-Schalter ohne Text (Symbol).
  - Felder: „Kunde / Projekt“, „Aktueller Raum“ bzw. „Position“, „Heizlast Φ<sub>HL</sub>“, „Sicherheitsreserve“, „Raumtemperatur t<sub>L</sub>“, „Norm-Außentemperatur“, „Bivalenzpunkt“, „Heizgrenze“, „Systemtemperatur VL/RL“, „Max. Bauhöhe“ / „Max. Baulänge“, „Bauform“, „Hersteller / Baureihe“, „Notiz“.
  - Zustände: „gedeckt“, „knapp“, „nicht gedeckt“, „Bestand“, „aus Lager“, „Vorschlag“, „Empfohlen“.
  - Rückmeldungen: „Gespeichert“, „Projekt geladen“, „Projektdatei erstellt“, „Raum gelöscht“, „Neues Projekt“.

---

## 9 · Druck und PDF

Berichte entstehen über Safari „Drucken → Als PDF sichern“ und gehen in die Kundenakte [BESTÄTIGT: auslegung.html]. `design.css` regelt (Abschnitt 11):

- Gedruckt werden nur **Kopf, Ergebnis, Bericht/Bestellung und Fuß**. Formulare, Toolbars, Segmente, Hilfen, Positionslisten und das Haus-Icon nie (Ausnahme per `.ls-print-form`, wenn ein Formular bewusst gedruckt wird). Keine Seitenzahlen [BESTÄTIGT, 2026-10-25].
- Jedes Druckdokument folgt `vorlagen/bericht-vorlage.html`: Deckkopf (Logo B, Dokumenttitel, Kunde/Projekt, Datum, Anzahl) · Rahmendaten `.ls-report__meta` · je Raum/Position eine Karte mit Label/Wert-Liste und Notiz · Bestell- oder Positionstabelle mit Summenzeile `.ls-report__sum`, bei Bedarf auf neuer Seite (`.ls-page-break`) · Unterschriftszeile `.ls-report__sign` nur bei Kundenbestätigung · Fuß mit Norm, „Angaben ohne Gewähr“, Toolname und Stand [BESTÄTIGT, 2026-10-25].
- Druck immer in **Hell**, auch wenn das Tool dunkel läuft. Hintergrundfarben erzwungen (`print-color-adjust: exact`), damit Navy-Kopf, Badges und Notizfelder erhalten bleiben [BESTÄTIGT, 2026-10-25].
- A4, Ränder 12 mm. Karten, Kennzahlen, Tabellen, Notizen brechen nicht über die Seite.
- Ausgeblendet: Buttons, Toolbars, Segmente, Statuszeile, Haus-Icon und alles mit `.ls-no-print`. `.ls-print-only` für Druck-only-Inhalte (z. B. Unterschriftszeile).
- Kunde/Projekt und Datum stehen im Kopfbalken, nicht in der Browser-Kopfzeile.
- Fuß des Berichts: Norm/Quelle, „Angaben ohne Gewähr – maßgeblich sind die Herstellerunterlagen“, „Erstellt mit dem internen Auslegungstool der Lutz Spring GmbH“.
- Kein Kundenname im Dateinamen des PDFs, wenn das PDF in Claude oder ein gemeinsames Projekt gelangt (Datenschutzregel 01_unternehmen.md).

---

## 10 · Barrierefreiheit und Bedienung

- WCAG 2.2 AA: Text ≥ 4,5:1, große Schrift und Bedienelemente ≥ 3:1 [BELEGT für alle Token-Paare, 2026-10-19].
- Fokus immer sichtbar (`:focus-visible`, 2 px Navy/Hellblau). Tastaturbedienung aller Buttons und Felder; Tabellenzeilen, die klickbar sind, bekommen `tabindex="0"` und `role="button"`.
- Touch-Ziele ≥ 44 px auf Touchgeräten, ≥ 32 px mit Maus [BESTÄTIGT, 2026-10-25].
- Formularfelder immer mit `<label for>`; Fehlertexte über `aria-describedby` verknüpft.
- `prefers-reduced-motion` wird respektiert; Animationen ohnehin nur dezent (≤ 150 ms).
- Farbsehschwäche: Zustand nie nur durch Farbe (siehe 2.2).

---

## 11 · Checkliste: ein Tool rekonstruieren oder neu bauen

Der vollständige Ablauf mit „Wofür“ und „Wie“ je Schritt steht in `UMBAU-ABLAUF.md`; die Feldliste wird mit `vorlagen/feldliste-vorlage.md` erstellt.

Vorbereitung
- [ ] Altfassung lesen: Erkennungsmerkmal und Stand aus `04_tool-konventionen.md` prüfen; Rechenlogik, Felder, Standardwerte, Datenquellen notieren.
- [ ] Feldliste der Altfassung prüfen (Abschnitt 6.1): Reihenfolge, Gruppen, Standard/Erweitert, Doppelungen, Ableitbares. Ergebnis als Tabelle „alt → neu“ festhalten.
- [ ] Referenzwerte aus `tests/referenzwerte.md` bereitlegen; vorher/nachher müssen identische Ergebnisse herauskommen [BESTÄTIGT: Referenzwerte-Konzept]. Grundlage des Umbaus ist der aktuelle Stand im Git; die Reihenfolge, in der die Tools umgebaut werden, legt Fabian fest [BESTÄTIGT, 2026-10-25].

Bauen
- [ ] Von `vorlagen/tool-vorlage.html` ausgehen; Marker für `design.css` und `ls.js` stehen lassen, nach jeder Änderung `python3 _build/inline.py` ausführen; keine eigenen Farben/Schriften.
- [ ] Bauplan (Abschnitt 5) einhalten; Rechenlogik unverändert übernehmen, Formular nach der geprüften Feldliste neu anordnen.
- [ ] Laden alter Projektdateien (JSON) sicherstellen: geänderte Feldnamen beim Import zuordnen.
- [ ] Standardwerte aus dem Firmengehirn; Richtwerte mit ≈; Einheiten als Suffix.
- [ ] Genau ein Primärbutton je Ansicht; Leerzustand, Fehlertexte, Hinweise nach Abschnitt 7.
- [ ] Logo Variante B als Inline-SVG im Kopf (aus `vorlagen/tool-vorlage.html` übernehmen); kein Text-Slogan zusätzlich, er steht im Logo.
- [ ] Fuß mit Toolname und Stand, Haus-Icon, Favicon und Homescreen-Symbol im `<head>`.
- [ ] Druckdokument nach `vorlagen/bericht-vorlage.html`; veränderliche Werte mit Datenstand.

Prüfen
- [ ] Referenzwerte stimmen.
- [ ] Safari auf dem iPad (Hoch und Quer) und Mac: kein seitliches Scrollen, Felder 44 px, Tastatur „Zahlen“.
- [ ] Hell und Dunkel (Systemeinstellung umschalten).
- [ ] Druck → PDF: Kopf, Badges, Notizen sichtbar; keine Buttons; keine Karte zerschnitten.
- [ ] Dateiname klein, ohne Umlaute; `href`s geprüft; `noindex`.
- [ ] Keine Kundendaten in Beispielen und Screenshots (BV Muster).
- [ ] Änderung in `CHANGELOG.md` eintragen (sobald angelegt).

---

## 12 · Prompt-Baustein für die KI-gestützte Rekonstruktion

> Baue `TOOLNAME.html` nach den Designregeln der Lutz Spring GmbH (DESIGNREGELN.md 2.0) neu. Verwende ausschließlich `assets/css/design.css` und die Klassen aus `styleguide.html`; keine eigenen Farben, Schriften oder externen Ressourcen. Übernimm Rechenlogik, Standardwerte und Datenquellen unverändert aus der Altfassung (Datei anhängen). Das Formular baust du nicht nach, sondern neu nach Abschnitt 6.1: prüfe jedes Feld auf Reihenfolge, Gruppierung, Standardwert und Notwendigkeit, lege selten geänderte Felder nach „Erweitert“, und liefere eine Tabelle „Feld alt → neu“ mit Begründung. Alte Projektdateien (JSON) müssen weiter geladen werden können. Halte den Bauplan aus Abschnitt 5 ein, genau ein primärer Button je Ansicht, Richtwerte mit ≈, Einheiten als Suffix, Fehlertexte mit Handlungsanweisung, Leerzustände mit Anleitung. Druck in Hell nach Abschnitt 9. Prüfe gegen `tests/referenzwerte.md` und nenne jede Stelle, an der du von der Altfassung abweichen musstest.

---

## 13 · Pflege

- Änderungen an Farben, Abständen oder Komponenten nur in `design.css` + `styleguide.html` + hier, nie in einem einzelnen Tool. Versionsnummer in allen drei Dateien hochzählen.
- Neue Komponente: erst im Styleguide zeigen, dann in Tools verwenden.
- Entscheidungen zum Design gehören in `06_entscheidungen.md` des Firmengehirns.

## Änderungslog

| Datum | Wer | Änderung |
|---|---|---|
| 2026-10-25 | Claude Code (Umbau kostenvergleich), Entscheidung Fabian Esche | 2.1.1: Baustein Regler mit Zahlenfeld `.ls-range` (design.css 10.12) und `LS.regler` in ls.js; Regel in Abschnitt 6; Beispiel im Styleguide. Kennzahlen auf Navy (`.ls-card--navy .ls-kpi`). Felder einer Zeile beginnen oben (`.ls-field` align-content: start), damit Regler und Eingaben auf einer Höhe stehen. Kopf ohne Titelblock: `.ls-header__meta` darf den Titel enthalten und steht rechts bündig |
| 2026-10-25 | Claude (Firmenaccount), Entscheidung Fabian Esche | 2.1: Lückenanalyse umgesetzt – Startseiten-Kacheln, Positionsliste, Inline-Rückfrage, Dialog, Toast, Stepper, Datenstand, „So geht’s“, Karten-Tabellen, Diagramm-Tokens, Datei-Baustein, Berichtsvorlage; `ls.js`; Icon-Satz; Homescreen-Symbol aus Logo A; Einfügen von CSS/JS beim Veröffentlichen; Druck nur Bericht, keine Seitenzahlen; iPadOS 16; Vokabular; UMBAU-ABLAUF.md, Feldliste, CLAUDE.md, CHANGELOG.md |
| 2026-10-25 | Claude (Firmenaccount), Entscheidung Fabian Esche | 2.0.1: Logo Variante B als Inline-SVG überall, Logo-Gelb #fff200 ersetzt #f5e400; Vorschläge zu Raster, Druck in Hell, noindex, Touch-Zielen, Schreibweisen und Dunkelmodus-Werten bestätigt; Umbau gegen Referenzwerte und aktuellen Git-Stand, Reihenfolge durch Fabian; Regel „Formularfelder bleiben unverändert“ ersetzt durch 6.1 „Formulare beim Neubau aufräumen“ – Anordnung und Inhalt der Felder werden beim Nachbau geprüft, nur die Rechenlogik bleibt (Nachweis Referenzwerte) |
| 2026-10-19 | Claude (Firmenaccount), Entscheidung Fabian Esche | Fassung 2.0: Farbwelt „Marine & Signalgelb“ gewählt; Tokens hell/dunkel, Komponenten, Bauplan, Druck, Checkliste. Ersetzt die 1.0-Fassung von `design.css` im Branch `tools-ueberarbeitung` |
