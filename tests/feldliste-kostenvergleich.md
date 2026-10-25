# Feldliste · kostenvergleich.html (Kostenvergleich Wärmepumpe / Gas & Öl)

Stand: 2026-10-25 · Erstellt von: Claude Code (Sitzung Umbau kostenvergleich) · Geprüft von Fabian: ☑ 2026-10-25 („passt“), Ergänzungen vom selben Tag siehe unten
Zweck: Vor dem Neubau nach DESIGNREGELN.md 6.1 jedes Feld der Altfassung befragen. Erst nach Freigabe bauen.
Alle Beispielwerte erfunden, keine Kundendaten. Altfassung: `alt/kostenvergleich_2026-10-25.html`.

## Fragen je Feld
1. Geht der Wert in die Rechnung ein? Wenn nein: Ergebnis oder weg.
2. Hat er einen Standardwert aus dem Firmengehirn? Dann vorbelegen.
3. Ändert ihn der Nutzer bei jedem Durchlauf? Wenn nein: „Erweitert“.
4. Folgt er aus einer anderen Eingabe? Dann berechnen und anzeigen.
5. Gehört er zu einer Gruppe? Dann gemeinsame Karte oder Zeile.

## Was die Altfassung rechnet (bleibt unverändert)
- Effektive JAZ = 1 ÷ ((1 − h) ÷ JAZ + h ÷ 1), h = Heizstab-Anteil; bei h = 0 gilt JAZ.
- Wärmepumpe: ct/kWh Wärme = Strompreis ÷ effektive JAZ. Gas: Gaspreis ÷ Nutzungsgrad. Öl: (Ölpreis ÷ 10 kWh/L) ÷ Nutzungsgrad.
- Jahreskosten = Jahres-Wärmebedarf × ct/kWh ÷ 100.
- PV (optional): WP-Strombedarf = Wärmebedarf ÷ effektive JAZ; PV-Ertrag = kWp × Jahresertrag; gedeckt = min(WP-Strombedarf × Deckungsanteil, PV-Ertrag); Ersparnis = gedeckt × Strompreis ÷ 100; Kosten WP+PV = max(Kosten WP − Ersparnis, 0).
- Ersparnis = Kosten Vergleichssystem − Kosten WP (bzw. WP+PV); Prozent = Ersparnis ÷ Kosten Vergleichssystem × 100.
- SCOP-Tabelle (EN 14825, Weishaupt Fachinformation 83603801, April 2026): WEB 7/10 5,09/4,02 · 9/14 4,59/3,79 · 10/15 4,96/3,99 · 13/20 4,89/4,01 (W35/W55); Nennwärmeleistung A−7/W35 7,09 · 9,49 · 10,07 · 13,15 kW. Deckt sich mit 05_fachwissen.md [BELEGT].
- Die Altfassung rechnet live bei jeder Eingabe; es gibt keinen Button „Berechnen“.

## Felder

| Nr. | Feld (alt) | id (alt) | Einheit | Standard | Bereich (alt) | Pflicht | Herkunft des Werts | Gruppe (neu) | Standard / Erweitert / Ergebnis / entfällt | Feld (neu) | id (neu) | Begründung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | – (neu) | – | – | leer | – | nein | Nutzer; ohne Personendaten („BV Muster“, Ort + Gewerk) | Projekt | Standard | Kunde / Projekt | projekt | Bauplan Abschnitt 5: steht im Kopf und im PDF; keine Rechenwirkung |
| 1 | Jahres-Wärmebedarf (Schieberegler) | demand | kWh/a | 18 000 | 3 000–60 000, Schritt 500 | ja | Heizlastberechnung oder Verbrauchsabrechnung | Wärmebedarf | entfällt (Doppelung) | – | – | Schieberegler und Zahlenfeld zeigen denselben Wert; ein Feld reicht (6.1 „Ein Feld, ein Zweck“) |
| 2 | Jahres-Wärmebedarf (Zahlenfeld) | demand-num | kWh/a | 18 000 | 1 000–200 000 | ja | wie 1 | Wärmebedarf | Standard | Jahres-Wärmebedarf (Heizung + Warmwasser) | waermebedarf | Zahlenfeld `inputmode="decimal"`, Einheit als Suffix; Bereich 1 000–200 000 wie Zahlenfeld alt; Hinweis „aus Heizlastberechnung oder Verbrauchsabrechnung“ |
| 3 | Baugröße | webModel | – | „manuell“ | manuell, WEB 7/10, 9/14, 10/15, 13/20 | nein | Weishaupt-Baureihe; Modulationsbereich im Optionstext (1,7–10,0 kW usw.) stammt aus der Altfassung | Wärmepumpe | Standard | Baugröße Weishaupt WEB | baugroesse | `.ls-select`; „manuell“ bleibt erste Option; Optionstexte unverändert |
| 4 | Systemtemperatur (bestimmt SCOP) | webSystemTemp | – | W35 | W35 (Flächenheizung), W55 (Heizkörper) | nein (nur bei gewählter Baugröße) | Heizflächen des Kunden | Wärmepumpe | Standard | Heizflächen (SCOP-Punkt) | heizflaechen | zwei Optionen → `.ls-seg` „Flächenheizung · W35 / Heizkörper · W50“; erscheint nur, wenn eine Baugröße gewählt ist (wie alt). **Änderung 2026-10-25 (Fabian):** Heizkörper auf W50 statt W55, weil wir immer auf 50 °C auslegen; SCOP W50 linear zwischen W35 und W55 interpoliert (≈, kein Datenblattwert) |
| 5 | JAZ (Jahresarbeitszahl) | jaz | – | 4,0 | 2,5–5,5, Schritt 0,1 | ja | manuell; bei gewählter Baugröße SCOP aus Tabelle (Feld gesperrt) | Wärmepumpe | Standard | Jahresarbeitszahl JAZ | jaz | bleibt Eingabe (Rechenwirkung bei „manuell“); bei Baugröße gesperrt, Hinweis nennt Quelle und Nennwärmeleistung wie alt |
| 6 | Strompreis | strom | ct/kWh | 27,0 | 15–45, Schritt 0,5 | ja | Energiepreis, veränderlich | Energiepreise | Standard | Strompreis Wärmepumpe | strompreis | veränderlicher Wert → Eingabe mit Standardwert und `.ls-stand` (Datenstand, siehe offene Frage 1) |
| 7 | Heizstab-Anteil an Jahresarbeit | heizstab | % | 0 | 0–15, Schritt 0,5 | nein | Schätzung, typ. 1–3 % bei monoenergetischer Auslegung (Hinweistext alt) | Wärmepumpe („Erweitert“ in der Karte) | Erweitert | Heizstab-Anteil an der Jahreswärme | heizstabAnteil | selten geändert, Standard 0 % (SCOP unterstellt monovalenten Betrieb); Kurzzeile „Heizstab 0 %“ bleibt lesbar |
| 8 | Vergleichssystem (zwei Karten Gas/Öl) | – (div `#compare-toggle`, JS-Variable `compareSystem`) | – | Gas | Gas, Öl | ja | Bestandsanlage des Kunden | Vergleichssystem | Standard | Bestandsanlage | vergleich | zwei Optionen → `.ls-seg` „Gasheizung / Ölheizung“ (UMBAU-ABLAUF: Umschalter als `.ls-seg`); Entscheidung 06 (2026-07-26): Umschalter statt Dreifachvergleich bleibt |
| 9 | Gaspreis | gas | ct/kWh | 11,0 | 5–20, Schritt 0,2 | ja (bei Gas) | Energiepreis, veränderlich | Energiepreise | Standard | Energiepreis Bestandsanlage (Gas: ct/kWh) | energiepreis | Vorschlag: ein Feld, dessen Beschriftung, Einheit und Standardwert mit dem Umschalter wechseln (Gas 11,0 ct/kWh ↔ Öl 95 ct/L); siehe offene Frage 2 |
| 10 | Nutzungsgrad Kessel (Gas) | etagas | % | 92 | 75–98 | ja (bei Gas) | Kessel des Kunden | Vergleichssystem | Standard | Nutzungsgrad Kessel | nutzungsgrad | Vorschlag: ein Feld, Standardwert wechselt mit dem Umschalter (Gas 92 % ↔ Öl 88 %); bleibt sichtbar, weil der Wert je Kunde (Kesselalter) gesetzt wird; siehe offene Frage 2 |
| 11 | Ölpreis | oel | ct/L | 95 | 40–150 | ja (bei Öl) | Energiepreis, veränderlich | Energiepreise | Standard | → Feld 9 (Öl: ct/L) | energiepreis | zusammengelegt mit 9; Umrechnung 10 kWh/L bleibt im Rechenteil und steht als Hinweis am Feld |
| 12 | Nutzungsgrad Kessel (Öl) | etaoel | % | 88 | 70–96 | ja (bei Öl) | Kessel des Kunden | Vergleichssystem | Standard | → Feld 10 | nutzungsgrad | zusammengelegt mit 10 |
| 13 | PV-Anlage berücksichtigen | pvEnabled | – | aus | an/aus | nein | Kunde hat PV oder plant sie | Photovoltaik | Standard (Schalter) | Photovoltaik berücksichtigen | pvAktiv | `.ls-switch` (wirkt sofort: blendet die PV-Felder ein, wie alt); Hinweis: wir bauen keine PV, der Block beschreibt nur die Anlage des Kunden |
| 14 | PV-Anlagengröße | pvkwp | kWp | 8,0 | 1–25, Schritt 0,5 | ja (bei PV) | Anlage des Kunden | Photovoltaik | Standard (nur bei PV an) | PV-Leistung | pvLeistung | Zahlenfeld mit Suffix kWp |
| 15 | Spezifischer Jahresertrag | pvertrag | kWh/kWp | 950 | 800–1 100, Schritt 10 | ja (bei PV) | Richtwert Region | Photovoltaik | Standard (nur bei PV an) | Spezifischer Jahresertrag | pvErtrag | bleibt in der PV-Karte (nur sichtbar, wenn PV an); Richtwert mit ≈ im Hinweis |
| 16 | PV-Deckungsanteil des WP-Stromverbrauchs | pvdeckung | % | 25 | 0–60 | ja (bei PV) | Schätzung; Hinweistext alt: ohne Speicher ≈ 15–30 %, mit Speicher/SG-Ready ≈ 35–50 % | Photovoltaik | Standard (nur bei PV an) | PV-Deckungsanteil am WP-Strom | pvDeckung | Hinweistext gekürzt übernehmen, Richtwerte mit ≈ |

Anzeigefelder der Altfassung (`v-demand`, `v-strom`, `v-jaz`, `v-heizstab`, `v-gas`, `v-etagas`, `v-oel`, `v-etaoel`, `v-pvkwp`, `v-pvertrag`, `v-pvdeckung`) zeigten nur den Schiebereglerwert mit Einheit; sie entfallen, weil die Einheit jetzt als Suffix am Feld steht.

## Reihenfolge der Gruppen (neu)
1. Projekt (Kunde / Projekt; Hinweis „keine Personendaten“)
2. Wärmebedarf (Jahres-Wärmebedarf)
3. Wärmepumpe (Baugröße WEB, Heizflächen W35/W55, JAZ)
4. Bestandsanlage (Umschalter Gas / Öl, Energiepreis, Nutzungsgrad Kessel)
5. Energiepreise: Strompreis steht bei der Wärmepumpe, Gas-/Ölpreis bei der Bestandsanlage; beide tragen den Datenstand (`.ls-stand`)
6. Photovoltaik (Schalter; bei „an“: PV-Leistung, Jahresertrag, Deckungsanteil)
7. Erweitert (Heizstab-Anteil) – seit 2026-10-25 als eingeklappter Block in der Karte Wärmepumpe (Fabian: gehört fachlich dorthin)

## Ergebnis (Abschnitt 7 DESIGNREGELN)
- Kennzahlen (`.ls-kpis`): Jahreskosten Wärmepumpe · Jahreskosten Bestandsanlage (Gas/Öl) · bei PV zusätzlich Jahreskosten WP + PV · effektive JAZ · ct/kWh Wärme WP · ct/kWh Wärme Bestandsanlage.
- Diagramm (`.ls-chart`, Inline-SVG): Balken Wärmepumpe Navy `--ls-chart-wp`, Bestandsanlage Grau `--ls-chart-alt`, WP + PV Ocker `--ls-chart-pv`; Werte am Balken. Die Altfassung färbte Gas orange und Öl rot (Zustandsfarben); das widerspricht der Diagrammregel und entfällt.
- Empfehlungskarte (`.ls-card--navy`): Ersparnis pro Jahr ≈ … € und ≈ … % günstiger, mit Hinweis „Richtwert, keine Zusage“ (Organisationsanweisung: keine Zusagen zu Einsparung). Badge „Vorschlag“.
- PV-Zwischenwerte (PV-Ertrag, gedeckter WP-Strom, Ersparnis durch PV) als Kennzahlen in der PV-Karte, wie alt.
- Rechenweg als aufklappbarer Block mit Formel, Eingangswerten, Zwischenergebnissen und Einheit (bisher nur die Formelzeile im Fuß).
- Emoji der Altfassung (⚡ 🔥 🛢 ☀ 💰) entfallen; Icons nur aus `assets/icons/icons.html` oder keine.

## Zuordnung alt → neu für Projektdateien (FELD_MAPPING)
```js
/* Die Altfassung hatte kein Sichern/Laden; es gibt keine alten Projektdateien.
   Die Zuordnung dient nur der Nachvollziehbarkeit der neuen ids. */
var FELD_MAPPING = {
  'demand-num': 'waermebedarf', webModel: 'baugroesse', webSystemTemp: 'heizflaechen',
  strom: 'strompreis', heizstab: 'heizstabAnteil', gas: 'energiepreis', oel: 'energiepreis',
  etagas: 'nutzungsgrad', etaoel: 'nutzungsgrad', pvEnabled: 'pvAktiv', pvkwp: 'pvLeistung',
  pvertrag: 'pvErtrag', pvdeckung: 'pvDeckung'
};
```

## Entfallene oder zu Ergebnissen gewordene Felder
| Feld (alt) | Was stattdessen | Begründung |
|---|---|---|
| Schieberegler `demand` | Zahlenfeld `waermebedarf` | Doppelung; `design.css` hat keinen Schieberegler, Zahlen werden als `type="text" inputmode="decimal"` eingegeben (DESIGNREGELN 6) |
| Schieberegler für Strom, JAZ, Heizstab, Gas, Öl, Nutzungsgrade, PV | Zahlenfelder mit Einheit als Suffix | wie oben; die alten Bereiche (min/max) werden als Prüfbereich mit Fehlertext übernommen, damit kein Wert außerhalb des bisher Möglichen eingegeben wird |
| Anzeigefelder `v-*` | Einheit als Suffix am Feld | nur Anzeige des Reglerwerts |
| Karten Gas/Öl (`.heizart-card`) | `.ls-seg` Bestandsanlage | zwei Optionen |
| Button „Drucken / als PDF speichern“ | Toolbar „Bericht drucken / PDF“ | Vokabular Abschnitt 8 |
| Fuß-Formelzeile | Rechenweg-Block im Ergebnis, Fuß nach Vorlage | Abschnitt 7 und 5.8 |

## Offene Fragen an Fabian
1. **Datenstand der Energiepreise.** Strom 27,0 ct/kWh, Gas 11,0 ct/kWh, Öl 95 ct/L stammen aus der Altfassung ohne Datum. Welcher Stand soll am `.ls-stand` stehen („Energiepreise Stand MM/JJJJ · prüfen“)? Bis zur Antwort: „Standardwerte der Altfassung, Stand prüfen“. Sollen die Standardwerte geändert werden, ist das eine Erweiterung (Schritt 10), nicht Teil des Umbaus.
2. **Ein Feld für Energiepreis und eins für Nutzungsgrad statt je zwei.** Vorschlag: Beim Umschalten Gas ↔ Öl wechseln Beschriftung, Einheit und Standardwert (11,0 ct/kWh ↔ 95 ct/L; 92 % ↔ 88 %). Nachteil: Wer bei Gas einen eigenen Wert eingetippt hat und auf Öl wechselt, bekommt den Öl-Standard, nicht seinen Gaswert zurück. Die Altfassung merkt sich beide. Alternative: zwei Felder wie bisher, nur das passende sichtbar. Welche Variante?
3. **Live rechnen oder „Berechnen“-Button.** Die Altfassung rechnet bei jeder Eingabe sofort, was im Kundengespräch beim Durchspielen hilft. Vorschlag: Live-Rechnung bleibt; der eine Primärbutton der Toolbar ist „Bericht drucken / PDF“, daneben „Zurücksetzen“. Auf dem iPad wird nach dem Ändern eines Feldes nicht automatisch zum Ergebnis gescrollt. Einverstanden?
4. **Projekt sichern / laden (Datei).** Die Altfassung hat es nicht; das Ergebnis geht als PDF in die Akte. Vorschlag: nur Eingaben im Browser merken (`LS.formularMerken`, wie alle Tools) und „Neues Projekt“ mit Rückfrage; Dateifunktionen weglassen. Einverstanden, oder sollen Sichern/Laden aus der Vorlage mitkommen?
5. **Negative Ersparnis.** Ist die Wärmepumpe teurer, zeigt die Altfassung „≈ −200 €“ und „≈ −10 % günstiger“. Vorschlag für die Anzeige (Rechnung bleibt gleich): bei negativem Wert „Mehrkosten pro Jahr ≈ 200 €“ und „≈ 10 % teurer als Gas“, Karte ohne Empfehlungscharakter. Einverstanden?
6. **Nutzungsgrad Kessel: 05_fachwissen.md nennt als Stellschraube 0,85 [UNGEPRÜFT]**, das Tool 92 % (Gas) und 88 % (Öl). Der Umbau übernimmt die Tool-Werte unverändert (Referenzwerte). Soll der Widerspruch in 07_offene-punkte.md vermerkt werden?
7. **Hinweistext PV.** Die Altfassung nennt SG-Ready und „Weishaupt Energie-Management“ im Hinweis. Kürzen auf „ohne Speicher ≈ 15–30 %, mit Speicher oder SG-Ready ≈ 35–50 %“? Die Richtwerte sind [UNGEPRÜFT]; Quelle fehlt.
8. **SCOP-Rundung der Altfassung (Befund aus Schritt 3).** Der JAZ-Schieberegler hat Schrittweite 0,1; die übernommenen SCOP-Werte 3,79 / 5,09 werden dadurch zu 3,8 / 5,1 gerundet und so gerechnet (K2: Jahreskosten WP 2 054 € statt 2 059 €). Im Neubau gibt es keinen Regler mehr. Zwei Wege: (a) Rundung auf 0,1 im Rechenteil nachbilden, damit alt = neu; (b) exakten SCOP aus der Tabelle rechnen (Datenblatt, [BELEGT]), dann weichen K2/K3 um wenige € von „alt“ ab, Abweichung begründet, Eintrag in 06. Vorschlag: (b), weil der Datenblattwert die dokumentierte Quelle ist und die Rundung nur ein Nebeneffekt des Reglers war. Entscheidung Fabian.

## Entscheidungen von Fabian nach der Freigabe (2026-10-25, in 06 eingetragen)
- Frage 8: **SCOP exakt** aus der Tabelle rechnen (b). K2/K3 weichen damit gewollt von „alt“ ab.
- **Regler plus Zahlenfeld** (`.ls-range`, neu in design.css 2.1.1) für JAZ, Strompreis, Energiepreis Bestandsanlage, Nutzungsgrad, Heizstab-Anteil, PV-Werte und Wärmebedarf. Das Zahlenfeld ist maßgeblich; der Regler ist Komfort fürs Durchspielen.
- **Preisbereiche und Standardwerte:** Strom 10–50 ct/kWh, Standard 30 ct/kWh [BESTÄTIGT]; Gas 5–50 ct/kWh, Standard 14 ct/kWh [BESTÄTIGT, bewusst am oberen Rand des Marktes, damit der Kunde die Ersparnis bei einem Preisanstieg sieht]; Heizöl 0,40–2,50 €/L, Standard 1,80 €/L [BESTÄTIGT]. Einheit Heizöl jetzt €/L (alt ct/L; im Rechenteil × 10 statt ÷ 10). Datenstand 10/2026 am Feld. Quellen für Strom/Gas: Vergleichsportale Brandenburg, Oktober 2026 (Haushaltsstrom ≈ 29–35 ct/kWh, Wärmepumpentarif ≈ 22 ct/kWh; Gas Brandenburg ≈ 12 ct/kWh, Grundversorgung ≈ 12,5–13,6 ct/kWh). Keine Firmenkalkulation.
- Fragen 2–5 und 7: Vorschläge angenommen. Frage 1 damit beantwortet (Stand 10/2026). Frage 6: Widerspruch zu 05 bleibt als Hinweis bestehen, Tool-Werte 92 %/88 % werden übernommen.
- **Nachtrag 2026-10-25 (Fabian):** „Erweitert“ (Heizstab-Anteil) steht in der Karte Wärmepumpe, nicht als eigene Karte. Heizkörper-Option bezieht den SCOP auf W50 (unsere Auslegung), interpoliert zwischen den Datenblattpunkten W35 und W55; neuer Referenzfall K4. Der genaue W50-Wert ist bei Weishaupt zu erfragen (07).
