# Feldliste · foerderung.html (Förderrechner Wärmepumpe)

Stand: 2026-10-26 · Erstellt von: Claude Code (Sitzung Umbau foerderung) · Geprüft von Fabian: ☐ (Datum)
Zweck: Vor dem Neubau nach DESIGNREGELN.md 6.1 jedes Feld der Altfassung befragen. Erst nach Freigabe bauen.
Alle Beispielwerte erfunden, keine Kundendaten. Altfassung: `alt/foerderung_2026-10-26.html` (byteidentisch mit dem Stand im Git, Commit f754073).

## Fragen je Feld
1. Geht der Wert in die Rechnung ein? Wenn nein: Ergebnis oder weg.
2. Hat er einen Standardwert aus dem Firmengehirn? Dann vorbelegen.
3. Ändert ihn der Nutzer bei jedem Durchlauf? Wenn nein: „Erweitert“.
4. Folgt er aus einer anderen Eingabe? Dann berechnen und anzeigen.
5. Gehört er zu einer Gruppe? Dann gemeinsame Karte oder Zeile.

## Was die Altfassung rechnet (bleibt unverändert)
Quellen laut Code-Kommentar: KfW-Merkblatt 458 „BEG Heizungsförderung für Privatpersonen – Wohngebäude“, Stand 07/2026, gültig ab 21.07.2026 · IKZ 8/2026, Tabelle 1. Im Firmengehirn gibt es dazu keinen Eintrag (05/06/07 ohne Treffer zu „Förderung“); die Sätze gelten als [UNGEPRÜFT im Firmengehirn], Quelle nur im Code. Rechenmodell wie in `TOOLS-WISSEN.md`, Abschnitt „Förderungsrechner“:
- Absenkungsstufen `stufen(d)`: 0 vor dem 01.02.2027, danach je Halbjahr (01.02. / 01.08.) eine Stufe mehr.
- Klimageschwindigkeitsbonus = max(0; 16 − 4 × Stufen) % · Höchstbetrag 1. WE = max(22 000; 28 000 − 750 × Stufen) €.
- Förderhöchstbetrag = Höchstbetrag 1. WE + 15 000 € × WE 2–6 + 8 000 € × WE ab 7.
- Grundförderung 30 %; ab 01.01.2027 15 % + 15 % nur mit Haken „made in EU“ (angekündigt, nicht im Merkblatt; allein in `grundsatz()`).
- Einkommensbonus nach anzusetzendem Einkommen (zvE − 10 000 € bei Kind): ≤ 30 000 → 40 % · ≤ 40 000 → 30 % · ≤ 50 000 → 10 % · darüber 0 %. Obergrenze 70 %, bei 40 % Bonus 80 %.
- Klimabonus nur bei Selbstnutzung und Austausch von Öl, Kohle/Holz, Nachtspeicher oder einer mindestens 20 Jahre alten Gasheizung (Alter = Antragsjahr − Baujahr).
- förderfähig = min(Kosten; Förderhöchstbetrag) · Anteil je WE = förderfähig ÷ WE · selbstgenutzte WE × min(Grund + Klima + Einkommen; Obergrenze) · übrige WE × Grundförderung. Mindestinvestition 300 € brutto (Kosten werden auf 300 angehoben).
- Fristen: nächster Stichtag, Tage bis dahin, Werte danach; Stufentabelle 21.07.2026 bis 01.08.2030 (9 Zeilen).
- EE-Hinweis: bei Altanlage „Erneuerbare“ und Baujahr nach 2008 angekündigter Wegfall ab 2027 (allein im Hinweiskasten).
- Die Altfassung rechnet live bei jeder Eingabe; es gibt keinen Button „Berechnen“, kein Sichern/Laden, keinen Browser-Speicher, keine Druckansicht.

## Felder

| Nr. | Feld (alt) | id (alt) | Einheit | Standard | Bereich (alt) | Pflicht | Herkunft des Werts | Gruppe (neu) | Standard / Erweitert / Ergebnis / entfällt | Feld (neu) | id (neu) | Begründung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | – (neu) | – | – | leer | – | nein | Nutzer; ohne Personendaten („BV Muster“, Ort + Gewerk) | Projekt | Standard | Kunde / Projekt | projekt | Bauplan Abschnitt 5: steht im Kopf und im PDF; keine Rechenwirkung |
| 1 | Tag der Antragstellung | datum | Datum | heute | gültiges Datum; ungültig → heute | ja | Geplanter Antrag bei der KfW; maßgeblich für alle Sätze | Antrag | Standard | Tag der Antragstellung | antragsdatum | unverändert `type="date"`; Hinweis „maßgeblich ist der Antrag, nicht der Einbau“ |
| 2 | Wohneinheiten (Schieberegler) | we | – | 1 | 1–20, Schritt 1 | ja | Gebäude des Kunden | Gebäude und Kosten | Standard | Wohneinheiten im Gebäude | wohneinheiten | Regler + Zahlenfeld als `.ls-range` (`LS.regler`), Zahlenfeld maßgeblich. **Befund:** die Altfassung rechnet mit dem Reglerwert, nicht mit dem Zahlenfeld; Eingaben über 20 werden stillschweigend auf 20 geklemmt. Neu: Prüfbereich 1–20 mit Fehlertext (Rechnung innerhalb des Bereichs identisch) |
| 3 | Wohneinheiten (Zahlenfeld) | we-zahl | – | 1 | 1–20 | ja | wie 2 | Gebäude und Kosten | → Feld 2 | – | wohneinheiten | Doppelung (6.1 „Ein Feld, ein Zweck“); im `.ls-range` ist das Zahlenfeld der Wert |
| 4 | Investitionskosten brutto (Regler) | kosten | € | 30 000 | 5 000–120 000, Schritt 500 | ja | Angebot / Kostenschätzung | Gebäude und Kosten | → Feld 5 | – | kosten | Doppelung |
| 5 | Investitionskosten brutto (Zahlenfeld) | kosten-zahl | € | 30 000 | ab 300, Schritt 500; Rechnung hebt auf 300 an | ja | wie 4 | Gebäude und Kosten | Standard | Investitionskosten brutto | kosten | `.ls-range` 5 000–120 000 (Regler klemmt), Zahlenfeld maßgeblich ohne obere Grenze wie alt; Hinweis „Mindestinvestition 300 € brutto“ bleibt als Ergebnis-Hinweis |
| 6 | Wird eine Wohneinheit selbst bewohnt? | wahl-selbst (Buttons ja/nein) | – | ja | ja / nein | ja | Nutzung des Kunden | Gebäude und Kosten | Standard | Selbstnutzung | selbstnutzung | zwei Optionen → `.ls-seg` „Selbst bewohnt / Vermietet“; blendet die Karte Einkommen ein/aus wie alt |
| 7 | Wärmepumpe made in EU | eu | – | aus | an/aus; nur sichtbar ab Antrag 01.01.2027 | nein | Hersteller/Fertigung (angekündigte Regel) | Gebäude und Kosten | Standard (nur sichtbar ab 2027) | Wärmepumpe aus EU-Fertigung | madeInEu | `.ls-check`; Hinweis „angekündigt, nicht im Merkblatt 458“ bleibt |
| 8 | Was wird ersetzt? | wahl-alt (Buttons oel/gas/kohle/nacht/ee/keine) | – | Ölheizung | Öl, Gas, Kohle/Holz, Nachtspeicher, Erneuerbare, Keine/Neubau | ja | Bestandsanlage des Kunden | Bestehende Heizung | Standard | Bestandsanlage | altanlage | sechs Optionen → nach Regel 6 `.ls-select`; siehe offene Frage 3 (`.ls-seg` mit sechs Einträgen scrollt seitlich, BACKLOG 2026-10-25) |
| 9 | Baujahr der Anlage (Regler) | baujahr | Jahr | 2005 | 1970–aktuelles Jahr | ja (außer „Keine“) | Typenschild / Kunde | Bestehende Heizung | → Feld 10 | – | baujahr | Doppelung |
| 10 | Baujahr der Anlage (Zahlenfeld) | baujahr-zahl | Jahr | 2005 | 1900–aktuelles Jahr | ja (außer „Keine“) | wie 9 | Bestehende Heizung | Standard (ausgeblendet bei „Keine / Neubau“) | Baujahr der Bestandsanlage | baujahr | `.ls-range` 1970–aktuelles Jahr, Zahlenfeld maßgeblich; Alter „rund n Jahre“ wird daneben angezeigt (Ergebnis, wie alt) |
| 11 | Zu versteuerndes Haushaltseinkommen (Regler) | einkommen | €/a | 45 000 | 0–90 000, Schritt 500 | ja (bei Selbstnutzung) | Einkommensteuerbescheide, Durchschnitt zweier Jahre | Einkommen | → Feld 12 | – | einkommen | Doppelung |
| 12 | Zu versteuerndes Haushaltseinkommen (Zahlenfeld) | einkommen-zahl | €/a | 45 000 | ab 0, Schritt 500 | ja (bei Selbstnutzung) | wie 11 | Einkommen | Standard (nur bei Selbstnutzung) | Zu versteuerndes Haushaltseinkommen (Durchschnitt) | einkommen | `.ls-range` 0–90 000, Zahlenfeld maßgeblich; Hinweis „Durchschnitt der Steuerjahre 2 und 3 vor dem Antrag“ |
| 13 | Zu versteuerndes Einkommen Jahr A (3 Jahre vor Antrag) | jahr-a | €/a | leer | ab 0 | nein | Steuerbescheid | Einkommen | Erweitert | Einkommen Steuerjahr (Antragsjahr − 3) | einkommenJahrA | selten genutzt; in `<details>` „Beide Steuerjahre einzeln eingeben“; Mittelwert wird in Feld 12 geschrieben (wie alt); Beschriftung mit Jahreszahl aus Feld 1 |
| 14 | Zu versteuerndes Einkommen Jahr B (2 Jahre vor Antrag) | jahr-b | €/a | leer | ab 0 | nein | Steuerbescheid | Einkommen | Erweitert | Einkommen Steuerjahr (Antragsjahr − 2) | einkommenJahrB | wie 13 |
| 15 | Mindestens ein minderjähriges Kind im Haushalt | kind | – | aus | an/aus | nein | Haushalt des Kunden | Einkommen | Standard (nur bei Selbstnutzung) | Minderjähriges, kindergeldberechtigtes Kind im Haushalt | kind | `.ls-check`; Hinweis „mindert das anzusetzende Einkommen um 10 000 €“ |
| 16 | – (Konstanten im Code) | HB_1WE_START, HB_1WE_MIN, HB_SCHRITT, HB_WE_2_6, HB_WE_AB7, GRUND, KLIMA_START, KLIMA_STUFE, MINDEST; Familienzuschlag 10 000, Obergrenzen 70/80, Einkommensstufen 30/40/50 T€ → 40/30/10 % | €, %, Punkte | wie Code | – | – | Merkblatt 458 (07/2026) | Fördersätze | Erweitert (Vorschlag, offene Frage 1) | Fördersätze Stand 07/2026 | hb1we, hb1weMin, hbSchritt, hbWe2bis6, hbWeAb7, grundsatz, klimaStart, klimaStufe, mindest, familienzuschlag, obergrenze, obergrenzeErhoeht, einkStufe1/2/3, einkBonus1/2/3 | CLAUDE.md und UMBAU-ABLAUF: veränderliche Fördersätze nie fest einprogrammieren, sondern Eingabe mit Standardwert und `.ls-stand` („Fördersätze Stand 07/2026 · prüfen“). Standardwerte = heutige Konstanten, Referenzwerte dadurch unverändert. Stichtage (21.07.2026, 01.02.2027, 01.01.2027) bleiben im Code, weil sie die Struktur der Stufen sind |

## Reihenfolge der Gruppen (neu)
1. Projekt (Kunde / Projekt; Hinweis „keine Personendaten“) und Tag der Antragstellung
2. Gebäude und Kosten (Wohneinheiten, Investitionskosten, Selbstnutzung, ab 2027: EU-Fertigung)
3. Bestehende Heizung (Bestandsanlage, Baujahr mit Alter)
4. Einkommen (nur bei Selbstnutzung: Haushaltseinkommen, Kind; Erweitert: beide Steuerjahre einzeln)
5. Erweitert · Fördersätze (eingeklappt, Kurzzeile „Stand 07/2026, Standardwerte“; offene Frage 1)
6. Aktionen: Primärbutton „Bericht drucken / PDF“, „Zurücksetzen“ (Live-Rechnung bleibt, offene Frage 2)
7. Ergebnis, Bericht, Fuß (siehe unten)

## Ergebnis (Abschnitt 7 DESIGNREGELN)
- Empfehlungskarte (`.ls-card--navy`) mit der einen Kennzahl „Voraussichtlicher Zuschuss ≈ … €“ und Unterzeile „von … € förderfähigen Kosten“; Badge „Vorschlag“; Hinweis „Verbindlich ist allein der Förderbescheid der KfW“ (keine Zusage zur Förderhöhe, Organisationsanweisung).
- Kennzahlen (`.ls-kpis`): Förderhöchstbetrag · Förderfähige Kosten · Fördersatz (mit Zusatz „gedeckelt auf 70/80 %“ bzw. „ohne Selbstnutzung“) · bei mehreren WE: Zuschuss selbst bewohnte WE und übrige WE.
- Hinweise vor dem Ergebnis (`.ls-note--warn`): Kosten über dem Förderhöchstbetrag („… € bleiben unberücksichtigt“), Mindestinvestition 300 €.
- Bausteine des Fördersatzes als Label/Wert-Liste (`.ls-dl`): Grundförderung, Klimageschwindigkeitsbonus, Einkommensbonus, Summe, Obergrenze.
- Rechenweg (aufklappbar, im Druck sichtbar): die vier Erklärtexte der Altfassung (`erklaerung1` … `erklaerung4`) bleiben inhaltlich erhalten, weil sie aus dem Ergebnis erzeugt werden; Monospace-Rechnungen werden `<pre>`-Blöcke im Rechenweg. Sie-Form bleibt, weil der Kunde mitliest.
- Fristen: Satz „Die heutigen Bedingungen gelten noch n Tage …“ als `.ls-note--info`, Stufentabelle als `.ls-table` (Kopf fixiert, Zahlen rechts), aktuelle Zeile `tr.is-selected` mit Badge „jetzt“.
- EE-Hinweis (`.ls-note--warn`, nur bei Bestandsanlage „Erneuerbare“) mit aufklappbarer Quelle, Text wie alt.
- Bericht nach `vorlagen/bericht-vorlage.html`: Kopf (Logo B, „Förderrechner Wärmepumpe“, Kunde/Projekt, Antragsdatum), Eingaben als Label/Wert-Liste, Zuschuss, Bausteine, Rechenweg, Fristentabelle, Hinweise, Fuß mit Quelle, Stand 07/2026 und „Angaben ohne Gewähr – verbindlich ist der Förderbescheid“. Die Altfassung hat keine Druckansicht; das ist neu, ohne Rechenwirkung.
- Emoji/Symbole der Altfassung (⚠, ←, ─) entfallen; Zustände als Badge und Text.

## Zuordnung alt → neu für Projektdateien (FELD_MAPPING)
```js
/* Die Altfassung hatte kein Sichern/Laden und keinen Browser-Speicher; es gibt keine alten
   Projektdateien. Die Zuordnung dient nur der Nachvollziehbarkeit der neuen ids. */
var FELD_MAPPING = {
  datum: 'antragsdatum', we: 'wohneinheiten', 'we-zahl': 'wohneinheiten',
  kosten: 'kosten', 'kosten-zahl': 'kosten', 'wahl-selbst': 'selbstnutzung', eu: 'madeInEu',
  'wahl-alt': 'altanlage', baujahr: 'baujahr', 'baujahr-zahl': 'baujahr',
  einkommen: 'einkommen', 'einkommen-zahl': 'einkommen',
  'jahr-a': 'einkommenJahrA', 'jahr-b': 'einkommenJahrB', kind: 'kind'
};
```

## Entfallene oder zu Ergebnissen gewordene Felder
| Feld (alt) | Was stattdessen | Begründung |
|---|---|---|
| Schieberegler `we`, `kosten`, `baujahr`, `einkommen` | `.ls-range` mit Zahlenfeld (Zahlenfeld maßgeblich) | Doppelung; Baustein 2.1.1, Entscheidung Fabian 2026-10-25 (Kostenvergleich) für Werte, die im Kundengespräch durchgespielt werden |
| Anzeigen `we-anzeige`, `baujahr-anzeige`, `alter-anzeige` | Wert steht im Zahlenfeld; Alter als Hinweis unter dem Baujahr | nur Anzeige des Reglerwerts |
| Button-Gruppen `wahl-selbst`, `wahl-alt` | `.ls-seg` (2 Optionen) bzw. `.ls-select` (6 Optionen) | Regel 6 |
| Ergebnisblock oben („rechnet live mit“) | Ergebnis nach den Eingaben (Bauplan Abschnitt 5), Empfehlungskarte Navy | offene Frage 2 |
| Erklärkästen „Warum das zählt“ je Schritt | Rechenweg im Ergebnis und im Bericht | Abschnitt 7: erst die Antwort, dann die Herleitung |
| Hinweisbalken oben (Merkblatt, Antragstag) | „So geht’s“ (`.ls-help`) und Fuß | Bauplan 1a und 8 |
| Fuß-Link „Zurück zur Übersicht“ | Haus-Icon `.ls-home` | Bauplan 9 |

## Offene Fragen an Fabian
1. **Fördersätze als Eingabe oder nur Datenstand?** CLAUDE.md verlangt, veränderliche Fördersätze nicht fest zu programmieren. Vorschlag (a): eine eingeklappte Karte „Erweitert · Fördersätze“ mit den Konstanten als Zahlenfelder (Höchstbeträge 28 000 / 22 000 / 750 / 15 000 / 8 000 €; Grundförderung 30 %, Klimabonus 16 % und Absenkung 4 Punkte; Einkommensgrenzen 30 / 40 / 50 T€ mit 40 / 30 / 10 %; Familienzuschlag 10 000 €; Obergrenzen 70 / 80 %; Mindestinvestition 300 €), Datenstand `.ls-stand` „Fördersätze Stand 07/2026 (Merkblatt 458) · prüfen“, Standardwerte = heutige Werte. Alternative (b): Konstanten bleiben im Code als eine Tabelle am Anfang, im Tool nur der Datenstand sichtbar. (a) ist mehr Felder, aber eine Änderung der KfW braucht dann keinen Code. Welche Variante?
2. **Ergebnis oben oder unten, live oder „Berechnen“?** Die Altfassung zeigt den Zuschuss ganz oben und rechnet bei jeder Eingabe mit, damit der Kunde beim Schieben sofort sieht, was sich ändert. Der Bauplan setzt das Ergebnis nach die Eingaben. Vorschlag: Bauplan einhalten (Ergebnis unten, Live-Rechnung bleibt, Primärbutton „Bericht drucken / PDF“ wie beim Kostenvergleich). Oder soll die Empfehlungskarte oben stehen, weil das Tool am iPad vor dem Kunden bedient wird?
3. **Bestandsanlage mit sechs Optionen.** Regel 6: 2–4 Optionen `.ls-seg`, viele `.ls-select`. Vorschlag `.ls-select` (Aufklappliste). Alternative: `.ls-seg` mit sechs Einträgen, der auf schmalen Schirmen seitlich scrollt (BACKLOG-Punkt vom 2026-10-25, Kostenvergleich). Einverstanden mit `.ls-select`?
4. **Regler für alle vier Zahlen?** Vorschlag: `.ls-range` für Investitionskosten und Einkommen (werden im Gespräch durchgespielt); Wohneinheiten und Baujahr nur als Zahlenfeld. Oder alle vier mit Regler wie in der Altfassung?
5. **Sichern / Laden.** Die Altfassung hat weder Datei noch Browser-Speicher. Vorschlag: Eingaben im Browser merken (`LS.formularMerken`) und „Neues Projekt“ mit Rückfrage; keine Dateifunktionen (wie Kostenvergleich). Einverstanden?
6. **Bericht für den Kunden.** Vorschlag: Druckdokument nach Berichtsvorlage in Sie-Form mit Eingaben, Zuschuss, Rechenweg, Fristen und dem Hinweis auf den Förderbescheid; Titel „Förderüberschlag Wärmepumpe“. Soll der Bericht so an den Kunden gehen, oder bleibt das Tool reine Gesprächshilfe ohne Druck?
7. **Fördersätze im Firmengehirn.** Zu Fördersätzen, Merkblatt 458 oder IKZ 8/2026 steht nichts in 05/06/07; Quelle ist nur der Code-Kommentar. Vorschlag: Eintrag in 07_offene-punkte.md („Fördersätze foerderung.html gegen Merkblatt 458 prüfen, Stand 07/2026, zwei angekündigte Regeln“) und Datenstand im Tool. Soll ich das eintragen?
8. **Abschnitt in 04_tool-konventionen.md fehlt.** Für foerderung.html gibt es dort keinen Abschnitt (Stand, Erkennungsmerkmal, Datenquellen). Vorschlag: in Schritt 8 anlegen mit Stand alt „f754073, Merkblatt 458 07/2026“ und Stand neu. Einverstanden?
9. **Baujahr-Obergrenze.** Die Altfassung begrenzt das Baujahr auf das aktuelle Kalenderjahr, nicht auf das Antragsjahr; bei einem Antrag 2027 kann 2027 also nicht eingegeben werden. Keine Rechenwirkung in den Referenzfällen. Vorschlag: Obergrenze = Antragsjahr (Feld 1). Einverstanden, oder unverändert lassen?
