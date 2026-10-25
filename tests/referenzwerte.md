# Referenzwerte · Interne Tools der Lutz Spring GmbH

Stand: 2026-10-25 · Nur erfundene Werte, keine Kundendaten (Repo ist öffentlich) [BESTÄTIGT, 2026-10-12].
Zweck: Nachweis, dass ein Umbau nichts an der Rechnung ändert (UMBAU-ABLAUF.md Schritt 3 und 5). Jeder Fall wird in der Altfassung gemessen (Spalte „alt“), dann in der Neufassung (Spalte „neu“). Jede Abweichung ist ein Fehler, bis das Gegenteil belegt ist. PDFs unter `tests/pdf/TOOLNAME_FALL_alt.pdf` und `…_neu.pdf`.

Die Spalte „erwartet (Formel)“ ist aus dem Rechenteil der Altfassung nachgerechnet (Python, gleiche Formeln und Rundung) und dient nur als Plausibilitätsprüfung; maßgeblich ist die Messung in der Altfassung.

Testfälle je Tool: A1–A5 `auslegung.html` (angelegt 2026-10-25, A5 nur neu) · K1–K6 `kostenvergleich.html` · H1–H6 `heizkoerper.html` · B1–B3 `bestandsaufnahme.html`. Die Fälle der noch nicht begonnenen Tools werden beim jeweiligen Umbau (Schritt 2) angelegt.

---

## kostenvergleich.html · K1–K6

Altfassung: `alt/kostenvergleich_2026-10-25.html` · Feldliste: `tests/feldliste-kostenvergleich.md`.
Messung „alt“ am 2026-10-25 in der unveränderten Altfassung (lokaler Server, Chromium; Eingaben per Skript gesetzt, Ergebnisse aus der Anzeige abgelesen). PDFs: `tests/pdf/kostenvergleich_K1_alt.pdf` … `K3_alt.pdf` (Druck aus Chrome, A4, ohne Kopf-/Fußzeile).
Rundung der Altfassung: Jahreskosten und Ersparnis auf ganze €, ct/kWh auf 2 Nachkommastellen, effektive JAZ auf 2 Nachkommastellen, Prozent auf ganze Zahl, PV-Mengen auf ganze kWh.

**Befund aus der Messung (K2, K3):** Die Altfassung übernimmt den SCOP nicht exakt. Das JAZ-Feld ist ein Schieberegler mit Schrittweite 0,1; beim Setzen von 3,79 bzw. 5,09 rundet der Browser auf 3,8 bzw. 5,1, und mit diesem gerundeten Wert wird gerechnet (Anzeige „JAZ 3,8“ neben dem Hinweis „SCOP 55 °C für WEB 9/14“). Die Spalte „erwartet (Formel)“ rechnet mit dem exakten Datenblattwert und weicht deshalb um wenige € ab. Entscheidung Fabian 2026-10-25 (06): Neufassung rechnet mit dem exakten SCOP; die Abweichungen bei K2/K3 sind gewollt und entsprechen der Spalte „erwartet (Formel)“. K1 (JAZ manuell) ist identisch.

Messung „neu“ am 2026-10-25 in `kostenvergleich.html` (design.css 2.1.1), gleiche Eingaben, Heizöl als 0,95 €/L (neue Einheit). Alle Werte stimmen mit „erwartet (Formel)“ überein. PDFs: `tests/pdf/kostenvergleich_K1_neu.pdf` … `K3_neu.pdf`.

### K1 · Gas, Standardwerte, JAZ manuell, ohne PV
Eingaben: Jahres-Wärmebedarf 18 000 kWh · Baugröße manuell · JAZ 4,0 · Heizstab-Anteil 0 % · Strompreis 27,0 ct/kWh · Bestandsanlage Gas · Gaspreis 11,0 ct/kWh · Nutzungsgrad 92 % · PV aus.

| Kennzahl | Einheit | erwartet (Formel) | alt (gemessen 2026-10-25) | neu (gemessen) | Status |
|---|---|---|---|---|---|
| Effektive JAZ | – | 4,00 | 4,00 | 4,00 | gleich |
| Wärmepumpe ct/kWh Wärme | ct/kWh | 6,75 | 6,75 | 6,75 | gleich |
| Gas ct/kWh Wärme | ct/kWh | 11,96 | 11,96 | 11,96 | gleich |
| Jahreskosten Wärmepumpe | €/a | 1 215 | 1 215 | 1 215 | gleich |
| Jahreskosten Gas | €/a | 2 152 | 2 152 | 2 152 | gleich |
| Ersparnis pro Jahr | €/a | 937 | 937 | 937 | gleich |
| Günstiger als Gas | % | 44 | 44 | 44 | gleich |

### K2 · Öl, WEB 9/14 bei W55 (SCOP 3,79), Heizstab 3 %, ohne PV
Eingaben: Jahres-Wärmebedarf 24 000 kWh · Baugröße WEB 9/14 · Heizflächen Heizkörper W55 (JAZ übernimmt SCOP, Feld gesperrt) · Heizstab-Anteil 3 % · Strompreis 30,0 ct/kWh · Bestandsanlage Öl · Ölpreis 95 ct/L · Nutzungsgrad 88 % · PV aus.

| Kennzahl | Einheit | erwartet (Formel, SCOP 3,79) | alt (gemessen 2026-10-25, JAZ-Feld 3,8) | neu (gemessen) | Status |
|---|---|---|---|---|---|
| JAZ (übernommen) | – | 3,79 | 3,8 (Reglerschritt 0,1) | 3,79 | gewollt (06: SCOP exakt) |
| Effektive JAZ | – | 3,50 | 3,51 | 3,50 | gewollt, = Formel |
| Wärmepumpe ct/kWh Wärme | ct/kWh | 8,58 | 8,56 | 8,58 | gewollt, = Formel |
| Öl ct/kWh Wärme | ct/kWh | 10,80 | 10,80 | 10,80 | gleich (Eingabe 0,95 €/L) |
| Jahreskosten Wärmepumpe | €/a | 2 059 | 2 054 | 2 059 | gewollt, = Formel |
| Jahreskosten Öl | €/a | 2 591 | 2 591 | 2 591 | gleich |
| Ersparnis pro Jahr | €/a | 532 | 537 | 532 | gewollt, = Formel |
| Günstiger als Öl | % | 21 | 21 | 21 | gleich |

Hinweis zu K2 (Stand 2026-10-25, nach Umbau der Heizflächen-Option): Die Option „Heizkörper · W55“ gibt es in der Neufassung nicht mehr (Auslegung auf 50 °C, Entscheidung Fabian, 06). K2 bleibt als Nachweis der Rechenlogik gültig und ist in der Neufassung über „Baugröße manuell, JAZ 3,79“ reproduzierbar (gemessen 2026-10-25: identische Werte wie in Spalte „neu“). Für die neue Option gilt K4.

### K4 · Öl, WEB 9/14 bei W50 (SCOP interpoliert), Heizstab 3 %, ohne PV
Erweiterung 2026-10-25 (Entscheidung Fabian: Heizkörper-Auslegung auf 50 °C). Der SCOP W50 ist kein Datenblattwert, sondern linear zwischen W35 (4,59) und W55 (3,79) interpoliert und auf 2 Stellen gerundet: 4,59 + (3,79 − 4,59) × 15 ÷ 20 = 3,99 [VORSCHLAG der Methode; offener Punkt 07: Wert bei Weishaupt erfragen]. Kein „alt“-Wert, weil die Altfassung nur W35/W55 kannte.
Eingaben wie K2, aber Heizflächen „Heizkörper · W50“: Jahres-Wärmebedarf 24 000 kWh · WEB 9/14 · Heizstab-Anteil 3 % · Strompreis 30,0 ct/kWh · Öl 0,95 €/L · Nutzungsgrad 88 % · PV aus.

| Kennzahl | Einheit | erwartet (Formel) | alt | neu (gemessen 2026-10-25) | Status |
|---|---|---|---|---|---|
| JAZ (übernommen, W50) | – | 3,99 | – | 3,99 | = Formel |
| Effektive JAZ | – | 3,66 | – | 3,66 | = Formel |
| Wärmepumpe ct/kWh Wärme | ct/kWh | 8,19 | – | 8,19 | = Formel |
| Öl ct/kWh Wärme | ct/kWh | 10,80 | – | 10,80 | = Formel |
| Jahreskosten Wärmepumpe | €/a | 1 966 | – | 1 966 | = Formel |
| Jahreskosten Öl | €/a | 2 591 | – | 2 591 | = Formel |
| Ersparnis pro Jahr | €/a | 625 | – | 625 | = Formel |
| Günstiger als Öl | % | 24 | – | 24 | = Formel |

PDF: `tests/pdf/kostenvergleich_K4_neu.pdf`.

### K5 · Gas, WWP LA 20/30-A R bei W35 (SCOP 5,20), ohne Heizstab, ohne PV
Erweiterung 2026-10-25 (Fabian: weitere Baureihen WAB, WGB, WWP LA). SCOP W35/W55 der WWP LA aus Weishaupt Fachinformation 83603701 (07/2026) [BELEGT]. Kein „alt“-Wert, weil die Altfassung nur WEB kannte. Für WAB und WGB ist nur der SCOP W35 belegt; der W55-Wert wird seit dem Nachtrag K6 aus ηs zurückgerechnet.
Eingaben: Jahres-Wärmebedarf 40 000 kWh · WWP LA 20/30-A R · Flächenheizung W35 · Heizstab-Anteil 0 % · Strompreis 30,0 ct/kWh · Gas 14,0 ct/kWh · Nutzungsgrad 92 % · PV aus.

| Kennzahl | Einheit | erwartet (Formel) | alt | neu (gemessen 2026-10-25) | Status |
|---|---|---|---|---|---|
| JAZ (übernommen, W35) | – | 5,20 | – | 5,20 | = Formel |
| Effektive JAZ | – | 5,20 | – | 5,20 | = Formel |
| Wärmepumpe ct/kWh Wärme | ct/kWh | 5,77 | – | 5,77 | = Formel |
| Gas ct/kWh Wärme | ct/kWh | 15,22 | – | 15,22 | = Formel |
| Jahreskosten Wärmepumpe | €/a | 2 308 | – | 2 308 | = Formel |
| Jahreskosten Gas | €/a | 6 087 | – | 6 087 | = Formel |
| Ersparnis pro Jahr | €/a | 3 779 | – | 3 779 | = Formel |
| Günstiger als Gas | % | 62 | – | 62 | = Formel |

PDF: `tests/pdf/kostenvergleich_K5_neu.pdf`.

### K6 · Gas, WAB 11-A bei W50 (W55 aus ηs zurückgerechnet), ohne Heizstab, ohne PV
Erweiterung 2026-10-25 (Fabian: für WAB und WGB wird ein sinnvoller SCOP gebraucht, notfalls errechnet). Weishaupt veröffentlicht für WAB/WGB keinen SCOP W55; er wird aus der ηs (W55) der Fachinformation zurückgerechnet: SCOP = (ηs + 3) × 2,5 ÷ 100 (Verordnung (EU) 813/2013, CC = 2,5, F = 3 %; an sechs belegten Weishaupt-Paaren geprüft, Abweichung ≤ 0,4 Prozentpunkte). WAB 11-A: ηs 138 % → W55 ≈ 3,53; W50 = 4,70 + (3,53 − 4,70) × 15 ÷ 20 = 3,82 [BERECHNET, Näherung; 07/21].
Eingaben: Jahres-Wärmebedarf 18 000 kWh · WAB 11-A · Heizkörper W50 · Heizstab-Anteil 0 % · Strompreis 30,0 ct/kWh · Gas 14,0 ct/kWh · Nutzungsgrad 92 % · PV aus.

| Kennzahl | Einheit | erwartet (Formel) | alt | neu (gemessen 2026-10-25) | Status |
|---|---|---|---|---|---|
| JAZ (übernommen, W50) | – | 3,82 | – | 3,82 | = Formel |
| Effektive JAZ | – | 3,82 | – | 3,82 | = Formel |
| Wärmepumpe ct/kWh Wärme | ct/kWh | 7,85 | – | 7,85 | = Formel |
| Gas ct/kWh Wärme | ct/kWh | 15,22 | – | 15,22 | = Formel |
| Jahreskosten Wärmepumpe | €/a | 1 414 | – | 1 414 | = Formel |
| Jahreskosten Gas | €/a | 2 739 | – | 2 739 | = Formel |
| Ersparnis pro Jahr | €/a | 1 326 | – | 1 326 | = Formel |
| Günstiger als Gas | % | 48 | – | 48 | = Formel |

PDF: `tests/pdf/kostenvergleich_K6_neu.pdf`.

### K3 · Gas, WEB 7/10 bei W35 (SCOP 5,09), Heizstab 1,5 %, mit PV
Eingaben: Jahres-Wärmebedarf 12 000 kWh · Baugröße WEB 7/10 · Heizflächen Flächenheizung W35 (JAZ übernimmt SCOP) · Heizstab-Anteil 1,5 % · Strompreis 28,0 ct/kWh · Bestandsanlage Gas · Gaspreis 12,4 ct/kWh · Nutzungsgrad 85 % · PV an: 9,5 kWp · 980 kWh/kWp · Deckungsanteil 30 %.

| Kennzahl | Einheit | erwartet (Formel, SCOP 5,09) | alt (gemessen 2026-10-25, JAZ-Feld 5,1) | neu (gemessen) | Status |
|---|---|---|---|---|---|
| JAZ (übernommen) | – | 5,09 | 5,1 (Reglerschritt 0,1) | 5,09 | gewollt (06: SCOP exakt) |
| Effektive JAZ | – | 4,80 | 4,80 | 4,80 | gleich |
| Wärmepumpe ct/kWh Wärme | ct/kWh | 5,84 | 5,83 | 5,84 | gewollt, = Formel |
| Gas ct/kWh Wärme | ct/kWh | 14,59 | 14,59 | 14,59 | gleich |
| Jahreskosten Wärmepumpe | €/a | 701 | 699 | 701 | gewollt, = Formel |
| Jahreskosten Gas | €/a | 1 751 | 1 751 | 1 751 | gleich |
| PV-Ertrag pro Jahr | kWh | 9 310 | 9 310 | 9 310 | gleich |
| Gedeckter WP-Stromanteil | kWh | 751 | 749 | 751 | gewollt, = Formel |
| Zusätzliche Ersparnis durch PV | €/a | 210 | 210 | 210 | gleich |
| Jahreskosten WP + PV | €/a | 490 | 490 | 490 | gleich |
| Ersparnis pro Jahr (WP + PV gegen Gas) | €/a | 1 260 | 1 261 | 1 260 | gewollt, = Formel |
| Günstiger als Gas | % | 72 | 72 | 72 | gleich |

---

## auslegung.html · A1–A5

Altfassung: `alt/auslegung_2026-10-25.html` · Feldliste: `tests/feldliste-auslegung.md`.
Angelegt 2026-10-25 (Schritt 2). Spalte „erwartet (Formel)“ aus dem Rechenteil der Altfassung nachgerechnet (Python, gleiche Stützpunkte, Interpolation und Rundung: kW auf 1 Nachkommastelle, Prozent ganzzahlig). Spalte „alt“ wird in Schritt 3 in der unveränderten Altfassung gemessen, „neu“ in Schritt 5.

Messung „alt“ am 2026-10-25 in der unveränderten Altfassung (`auslegung.html` im Git, byteidentisch mit `alt/auslegung_2026-10-25.html`; die Kopie in `alt/` selbst lädt `theme.css` nicht, weil die Datei im Hauptordner liegt). Ablauf: lokaler Server, Eingaben als Arbeitsstand im Format der Altfassung gesetzt (localStorage, wie nach einem Neuladen), Ergebnisse aus der Anzeige abgelesen (headless Chrome, DOM), PDFs `tests/pdf/auslegung_A1_alt.pdf` … `A4_alt.pdf` (Druckzusammenfassung der Altfassung, A4, je 2 Seiten, ohne Kopf-/Fußzeile des Browsers). Alle Kennzahlen stimmen mit „erwartet (Formel)“ überein. Anzeigeformat der Altfassung: ganze kW ohne „,0“ („10 kW“, „≈ 13 kW“, „1,7–14 kW“); in der Tabelle steht der Wert, das Format in Klammern.

**Befunde aus der Messung (Altfassung):**
1. Kühlfunktion geht beim Neuladen verloren: `standAnwenden` prüft die Sichtbarkeit der Kühlung, bevor die Heizflächen wiederhergestellt sind; dadurch wird „Kühlung ja“ auf „nein“ gesetzt und der Kühlblock bleibt ausgeblendet, bis die Heizfläche erneut angetippt wird. Betrifft auf dem iPad jedes Neuladen der Homescreen-App. Für A2 wurden die Zusatzpositionen deshalb zusätzlich im Browser nach echtem Klick (Fußbodenheizung, „Ja, aktive Kühlung“) gemessen; das PDF `auslegung_A2_alt.pdf` zeigt den Zustand nach Neuladen (Kühloption statt der vier Kühlpositionen). Die Neufassung muss den Zustand vollständig wiederherstellen; das ist eine gewollte Abweichung (Fehlerbehebung), Kennzahlen unverändert.
2. Die Kundenfälle-Liste wird nie aus dem Speicher geladen (`kundenLaden` ist definiert, wird aber nicht aufgerufen); nach einem Neuladen ist die Liste leer, und „Speichern“ überschreibt die gespeicherte Liste. Es gibt daher keine alten Fälle, die zu übernehmen wären (Feldliste, Frage 1). Der Fallname erscheint deshalb auch nicht in den PDFs; der Seitentitel lautet „Wärmepumpenauslegungstool - Gerät - Datum“.
3. Die Kennzahlen „Gebäudeheizlast“, „WP-Leistung bei Norm-Außentemperatur“ und „Heizstab-Anteil“ erscheinen nur bei Luft/Wasser; bei Sole/Wasser (A4) steht stattdessen der Sole-Hinweis.

Messung „neu“ am 2026-10-25 in `auslegung.html` (design.css 2.1.2): gleiche Eingaben als Browser-Speicher der Neufassung gesetzt (Felder per id, Verteilerliste und Aeroblock-Zustand), Ergebnisse aus der Anzeige abgelesen (headless Chrome), PDFs `tests/pdf/auslegung_A1_neu.pdf` … `A5_neu.pdf`. **Alle Kennzahlen aller Fälle sind identisch mit „erwartet (Formel)“ und „alt“** (Vergleich per Skript, 0 Abweichungen). Unterschiede nur in der Darstellung: ganze kW mit „,0“ („10,0 kW“), Status als Badge „gedeckt / knapp / nicht gedeckt“ statt ✓ ◐ ⚠, Hinweise ohne Symbole, „Blossom-ic“ statt „Blossom-IC“, kein „R290“ im Gerätetext. A2: die vier Kühlpositionen erscheinen in der Neufassung auch nach Neuladen (Befund 1 behoben). Die Neufassung druckt Ergebnis und Bericht (Zusammenfassung, Heizlast, Ergebnis, Zusatzpositionen, Rechenweg); die PDFs sind länger als die der Altfassung, weil Karten im Druck nicht umbrechen (BACKLOG).
Die Altfassung kennt für Norm-Außentemperatur und Bivalenzpunkt nur feste Auswahlwerte; A1–A4 nutzen deshalb −14 / −12 / −16 °C. Für die neue Vorgabe −12,7 °C (07/5) kommt in Schritt 5 ein Fall A5 nur „neu“ (wie K4 beim Kostenvergleich), sobald Fabian die Feldliste freigibt.
Gemeinsame Vorgaben, soweit nicht anders genannt: Wärmequelle Luft/Wasser · Aufgabe Heizung + Warmwasser · Speicher getrennt WAS 300 l + WES 200 l · Abwasser ja · Zirkulation nein · Solarthermie nein · PV nein · strenge Auslegung aus · bisheriger Vorlauf unbekannt · Rohrsystem Zweirohr · RTL nein · Kühlung nein · Aeroblock-Alternative nicht aktiviert · Notizen leer.

### A1 · Öl, Pauschale, Heizkörper, Standardwerte
Eingaben: Bestand Öl, 3 000 L/a, Kesseltyp Niedertemperatur (85 %) · Wohnfläche 120 m² · Wohneinheiten 1 · Personen 2 · Gebäudehülle Pauschale „Altbau teilsaniert (90 W/m²)“ · Heizflächen Heizkörper, 8 Stück, Zweirohr · Norm-Außentemperatur −14 °C · Bivalenzpunkt −7 °C · Ziel-Vorlauf 50 °C (automatisch aus Heizkörper).
Rechenweg: Verbrauch 3 000 × 10 × 0,85 ÷ 1 800 = 14,17 kW · Gebäude 120 × 90 ÷ 1 000 = 10,80 kW · Abweichung 26,97 % → 50/50 → 12,48 kW · + 2 × 0,2 kW = 12,88 kW · Lastanteil (15 + 7) ÷ (15 + 14) = 0,7586 → 9,77 kW · WEB 7/10 bei −7/W50: 7,00 × 1,15 = 8,05 < 9,77 → WEB 9/14: (9,4 + 9,3) ÷ 2 = 9,35 × 1,15 = 10,75 ≥ 9,77 · bei −14 °C: 8,55 + (1 ÷ 8) × (9,35 − 8,55) = 8,65 kW.

| Kennzahl | Einheit | erwartet (Formel) | alt (gemessen) | neu (gemessen) | Status |
|---|---|---|---|---|---|
| Ölverbrauchsansatz | kW | 14,2 | 14,2 | 14,2 kW | gleich |
| Gebäudeansatz (Pauschale 90 W/m²) | kW | 10,8 | 10,8 | 10,8 kW | gleich |
| Plausibilität | – | „plausibel (27 % Abweichung)“, Mittel beider Wege | „plausibel (27 % Abweichung)“, Mittel beider Wege | Verbrauch und Gebäudehülle plausibel (27 % Abweichung). Auslegungswert = Mittel beider Wege, plus 0,4 kW Warmwasser für 2 Personen. | gleich |
| Auslegungswert Heizlast (inkl. 0,4 kW Warmwasser) | kW | 12,9 | 12,9 | 12,9 kW | gleich |
| Empfohlenes Gerät | – | Weishaupt Evoblock WEB 9/14 · Modulation 1,7–14,0 kW · 230 V | Weishaupt Evoblock WEB 9/14 · Modulation 1,7–14 kW · 230 V (Anzeige „14“) | Weishaupt Evoblock WEB 9/14 · Modulation 1,7–14,0 kW · 230 V · Luft/Wasser · Badge „Vorschlag“ | gleich |
| Gebäudelast bei −7 °C | kW | 9,8 | 9,8 | 9,8 kW | gleich |
| WP-Leistung A−7/W50 | kW | ≈ 9,4 | ≈ 9,4 | ≈ 9,4 kW | gleich |
| Deckung am Bivalenzpunkt | % | 96 | 96 | 96 % | gleich |
| Status Bivalenzpunkt | – | knapp (geringe Heizstab-Unterstützung) | „◐ Am Bivalenzpunkt −7 °C bereits geringe Heizstab-Unterstützung nötig“ (warn) | „knapp“ · Am Bivalenzpunkt −7 °C bereits geringe Heizstab-Unterstützung nötig. | gleich |
| Nennwärmeleistung A−7/W35 | kW | 9,5 | 9,5 | 9,5 kW | gleich |
| Gebäudeheizlast bei −14 °C | kW | 12,9 | 12,9 | 12,9 kW | gleich |
| WP-Leistung A−14/W50 | kW | ≈ 8,7 | ≈ 8,7 | ≈ 8,7 kW | gleich |
| Heizstab-Anteil bei −14 °C | kW | ≈ 4,2 (Stufe 2) | ≈ 4,2; Hinweis „rechnerisch Stufe 2“ | ≈ 4,2 kW (Stufe 2) | gleich |
| Taktungsrisiko | – | nein | nein | nein | gleich |
| Alternative Aeroblock | – | WAB 14, ≈ 10,9 kW, 100 % Deckung | Weishaupt Aeroblock WAB 14, „Leistung ≈ 10,9 kW, 100 % Deckung“, Button „Aeroblock stattdessen auslegen“ | Alternative: Weishaupt Aeroblock WAB 14 · Würde die Anforderung ebenfalls erfüllen (Leistung ≈ 10,9 kW, 100 % Deckung am Bivalenzpunkt), ist aber teurer. Nur akti… | gleich |
| Zusatzpositionen | – | Öltankentsorgung · WAS 300 l · WES 200 l · Schallgutachten (46 dB(A), optional) | Öltankentsorgung · WAS 300 l · WES 200 l (erforderlich) · Schallgutachten (optional) | Öltankentsorgung inkl. Restölentsorgung [erforderlich] · WAS 300 l · Trinkwasserspeicher [erforderlich] · WES 200 l · Energiespeicher [erforderlich] · Schallgutachten / Schallschutzmaßnahmen [optional] | gleich |

### A2 · Gas in kWh, Bauteil-Konfigurator, Fußbodenheizung, Kühlung, WMS, Aeroblock aktiviert
Eingaben: Bestand Gas, 18 000 kWh/a (Einheit kWh), Kesseltyp Brennwert (96 %) · Wohnfläche 150 m² · Wohneinheiten 1 · Personen 4 · Gebäudehülle Bauteile: Baujahr 1995–2001, Fenster 2-fach modern, Wand massiv / 24–36 cm / Teildämmung, Dach gut gedämmt · Heizflächen Fußbodenheizung, 2 Verteiler (Erdgeschoss 6 Kreise, 1. Obergeschoss 5 Kreise) · Kühlung ja, 3 Räume · Norm-Außentemperatur −12 °C · Bivalenzpunkt −7 °C · Ziel-Vorlauf 35 °C (automatisch) · Speicher WMS 300/120 · Abwasser nein · Zirkulation ja · Solarthermie ja, demontieren · PV geplant · im Ergebnis „Aeroblock stattdessen auslegen“ angetippt.
Rechenweg: Verbrauch 18 000 × 0,96 ÷ 1 800 = 9,60 kW · spezifisch max(15; 45 + 5 + (14 + 0 − 6) + (−3)) = 55 W/m² → 8,25 kW · Abweichung 15,13 % → 50/50 → 8,925 kW · + 4 × 0,2 = 9,725 kW · Lastanteil 22 ÷ 27 = 0,8148 → 7,92 kW · Evoblock: WEB 7/10 bei −7/W35 7,09 × 1,15 = 8,15 ≥ 7,92 · Aeroblock: WAB 8 6,2 × 1,15 = 7,13 < 7,92; WAB 11 6,9 × 1,15 = 7,94 ≥ 7,92 → aktiviert · bei −12 °C: 6,2 + (3 ÷ 8) × 0,7 = 6,46 kW.

| Kennzahl | Einheit | erwartet (Formel) | alt (gemessen) | neu (gemessen) | Status |
|---|---|---|---|---|---|
| Gasverbrauchsansatz | kW | 9,6 | 9,6 | 9,6 kW | gleich |
| Bauteilansatz (Zeile) | – | „≈ 55 W/m² (Basis 45 + Fenster 5 + Wand 8 + Dach −3)“ | „≈ 55 W/m² (Basis 45 + Fenster 5 + Wand 8 + Dach −3)“ | im Rechenweg: Bauteilansatz ≈ 55 W/m² (Basis 45 + Fenster 5 + Wand 8 + Dach −3; mindestens 15) × 150 m² ÷ 1 000 = 8,25 kW | gleich |
| Gebäudeansatz | kW | 8,3 | 8,3 | 8,3 kW | gleich |
| Plausibilität | – | „plausibel (15 % Abweichung)“ | „plausibel (15 % Abweichung)“ | Verbrauch und Gebäudehülle plausibel (15 % Abweichung). Auslegungswert = Mittel beider Wege, plus 0,8 kW Warmwasser für 4 Personen. | gleich |
| Auslegungswert Heizlast (inkl. 0,8 kW Warmwasser) | kW | 9,7 | 9,7 | 9,7 kW | gleich |
| Standardempfehlung (vor Umschalten) | – | Weishaupt Evoblock WEB 7/10 | Weishaupt Evoblock WEB 7/10 („Standardempfehlung wäre …“, Button „Zurück zur Evoblock (WEB 7/10)“) | Weishaupt Evoblock WEB 7/10 (Text in der Alternativ-Karte, Button „Zurück zur Evoblock“) | gleich |
| Ausgelegtes Gerät (Ausweichlösung aktiv) | – | Weishaupt Aeroblock WAB 11 · Modulation 1,6–11,0 kW · 230 V | Weishaupt Aeroblock WAB 11 · Modulation 1,6–11 kW · 230 V, Badge „Ausweichlösung aktiv“ | Weishaupt Aeroblock WAB 11 · Modulation 1,6–11,0 kW · 230 V · Luft/Wasser · Badge „Ausweichlösung“ | gleich |
| Gebäudelast bei −7 °C | kW | 7,9 | 7,9 | 7,9 kW | gleich |
| WP-Leistung A−7/W35 | kW | ≈ 6,9 | ≈ 6,9 | ≈ 6,9 kW | gleich |
| Deckung am Bivalenzpunkt | % | 87 | 87 | 87 % | gleich |
| Status Bivalenzpunkt | – | knapp (geringe Heizstab-Unterstützung) | „◐ … geringe Heizstab-Unterstützung nötig“ (warn) | „knapp“ · Am Bivalenzpunkt −7 °C bereits geringe Heizstab-Unterstützung nötig. | gleich |
| Nennwärmeleistung A−7/W35 | kW | 6,9 | 6,9 | 6,9 kW | gleich |
| Gebäudeheizlast bei −12 °C | kW | 9,7 | 9,7 | 9,7 kW | gleich |
| WP-Leistung A−12/W35 | kW | ≈ 6,5 | ≈ 6,5 | ≈ 6,5 kW | gleich |
| Heizstab-Anteil bei −12 °C | kW | ≈ 3,3 (Stufe 2) | ≈ 3,3; Hinweis „rechnerisch Stufe 2“ | ≈ 3,3 kW (Stufe 2) | gleich |
| Taktungsrisiko | – | nein | nein | nein | gleich |
| Zusatzpositionen | – | Kanister Solarflüssigkeit · WMS 300/120 · Hebeanlage · Zirkulationspumpe · zusätzliche Heizkreisverteiler (1 über Standard, 2 Verteiler / 11 Kreise) · Taupunktfühler · diffusionsdichte Dämmung · Blossom-ic Raumregler (3 Räume) · Umschaltung Heizen/Kühlen · Schallgutachten (49 dB(A)) | nach Klick: Kanister · WMS 300/120 · Hebeanlage · Zirkulationspumpe · zusätzliche Heizkreisverteiler (1 über Standard) · Taupunktfühler · diffusionsdichte Dämmung · Blossom-IC Raumregler (3 Räume) · Umschaltung Heizen/Kühlen (alle erforderlich) · Schallgutachten (optional). Nach Neuladen fehlen die vier Kühlpositionen (Befund 1) | Leerer Kanister für Solarflüssigkeit [erforderlich] · WMS 300/120 · Modularspeicher [erforderlich] · Hebeanlage für Ablauf Sicherheitsgruppe [erforderlich] · Zirkulationspumpe mit Zeit-/Temperatursteuerung [erforderlich] · Zusätzliche Heizkreisverteiler (1 über Standard) [erforderlich] · Taupunktfühler / Kondensatüberwachung [erforderlich] · Diffusionsdichte Dämmung der kälteführenden Leitungen [erforderlich] · Blossom-ic Raumregler (3 Räume) [erforderlich] · Umschaltung Heizen/Kühlen + Kühlstation [erforderlich] · Schallgutachten / Schallschutzmaßnahmen [optional] | gleich, auch nach Neuladen (Befund 1 behoben) |

### A3 · Vorhandene Wärmepumpe, U-Werte direkt, Heizkörper + FBH, nur Heizung, streng, bisheriger Vorlauf bekannt
Eingaben: Bestand Wärmepumpe, 6 000 kWh/a Strom, JAZ 3,0 · Wohnfläche 200 m² · Wohneinheiten 2 · Personen 3 (ohne Wirkung, WW extern) · Gebäudehülle U-Werte: Außenwand 180 m² / 1,2 · Dach 120 m² / 0,6 · Fenster 30 m² / 2,8 · Boden 120 m² / 0,8 · Heizflächen Beides: 6 Heizkörper, Einrohr, RTL ja (2 Stück), Vorlauf Heizkörper-Kreis 50 °C, FBH-Kreis 40 °C, 1 Verteiler (Erdgeschoss 4 Kreise) · bisheriger Vorlauf bekannt: 70 °C, „knapp“ · Aufgabe nur Heizung · WES 500 l · Norm-Außentemperatur −16 °C · Bivalenzpunkt −7 °C · Ziel-Vorlauf 50 °C (aus Heizkörper-Kreis) · strenge Auslegung an.
Rechenweg: Verbrauch 6 000 × 3,0 ÷ 1 800 = 10,00 kW · ΔT = 36 K · Σ(A × U) = 216 + 72 + 84 + 96 = 468 W/K → Transmission 16,85 kW · Lüftung 0,5 × 200 × 2,5 × 0,34 × 36 ÷ 1 000 = 3,06 kW → 19,91 kW · Abweichung 66,26 % > 35 → 0,6 × 19,91 + 0,4 × 10,00 = 15,94 kW · kein Warmwasser · Lastanteil 22 ÷ 31 = 0,7097 → 11,32 kW · streng (× 1,0): WEB 7/10 7,00 · 9/14 9,35 · 10/15 9,95 < 11,32; WEB 13/20 (13,0 + 12,9) ÷ 2 = 12,95 ≥ 11,32 · Aeroblock: WAB 14 10,9 < 11,32 → keine Alternative · bei −16 °C (geklemmt auf −15): 12,35 kW.

| Kennzahl | Einheit | erwartet (Formel) | alt (gemessen) | neu (gemessen) | Status |
|---|---|---|---|---|---|
| WP-Verbrauchsansatz | kW | 10,0 | 10 (Anzeige „10 kW“) | 10,0 kW | gleich |
| U-Wert-Zeile | – | „Transmission ≈ 16,8 kW + Lüftung ≈ 3,1 kW bei ΔT=36 K“ | „Transmission ≈ 16,8 kW + Lüftung ≈ 3,1 kW bei ΔT=36 K“ | im Rechenweg: Transmission Σ(A × U) × ΔT = 468,0 W/K × 36,0 K ÷ 1 000 ≈ 16,8 kW + Lüftung 0,5 1/h × 200 m² × 2,5 m × 0,34 Wh/(m³·K) × 36,0 K ÷ 1 000 ≈ 3,1 kW (Norm-Innentemperatur 20 °C) = 19,91 kW | gleich |
| Gebäudeansatz | kW | 19,9 | 19,9 | 19,9 kW | gleich |
| Plausibilität | – | „Große Abweichung (66 %) … Gebäudeansatz 60 %“ | „Große Abweichung (66 %) … Gebäudeansatz 60 %“ | Große Abweichung zwischen Verbrauch und Gebäudehülle (66 %). Altanlage evtl. über- oder unterdimensioniert oder untypisches Nutzerverhalten; der Gebäudeansatz wird mit 60 % stärker gewichtet. Vor dem Angebot prüfen. | gleich |
| Auslegungswert Heizlast (ohne Warmwasser) | kW | 15,9 | 15,9 | 15,9 kW | gleich |
| Empfohlenes Gerät | – | Weishaupt Evoblock WEB 13/20 · Modulation 3,2–20,0 kW · 400 V | Weishaupt Evoblock WEB 13/20 · Modulation 3,2–20 kW · 400 V | Weishaupt Evoblock WEB 13/20 · Modulation 3,2–20,0 kW · 400 V · Luft/Wasser · Badge „Vorschlag“ | gleich |
| Gebäudelast bei −7 °C | kW | 11,3 | 11,3 | 11,3 kW | gleich |
| WP-Leistung A−7/W50 | kW | ≈ 13,0 | ≈ 13 (Anzeige „≈ 13 kW“) | ≈ 13,0 kW | gleich |
| Deckung am Bivalenzpunkt | % | 100 | 100 | 100 % | gleich |
| Status Bivalenzpunkt | – | gedeckt (ohne Heizstab) | „✓ Die Wärmepumpe deckt den Bivalenzpunkt −7 °C vollständig ohne Heizstab“ (success) | „gedeckt“ · Die Wärmepumpe deckt den Bivalenzpunkt −7 °C vollständig ohne Heizstab. | gleich |
| Nennwärmeleistung A−7/W35 | kW | 13,2 | 13,2 | 13,2 kW | gleich |
| Gebäudeheizlast bei −16 °C | kW | 15,9 | 15,9 | 15,9 kW | gleich |
| WP-Leistung A−16/W50 | kW | ≈ 12,4 | ≈ 12,4 | ≈ 12,4 kW | gleich |
| Heizstab-Anteil bei −16 °C | kW | ≈ 3,6 (Stufe 2) | ≈ 3,6; Hinweis „rechnerisch Stufe 2“ | ≈ 3,6 kW (Stufe 2) | gleich |
| Taktungsrisiko | – | nein | nein | nein | gleich |
| Alternative Aeroblock | – | keine | keine | keine | gleich |
| Heizflächen-Bewertung | – | „Absenkung prüfen“ (70 → 50 °C = 20 K, warn) | „Von 70 °C auf 50 °C sind 20 K Absenkung — das ist deutlich …“ (warn); Zusatzposition „Absenkversuch vor Angebotslegung“ (objektabhängig) | „Heizflächen: Absenkung prüfen. Von 70 °C auf 50 °C sind 20 K Absenkung, das ist deutlich. Vor dem Angebot einen Absenkversuch durchführen oder die Heizflächen r…“ (warn) | gleich |
| Zusatzpositionen | – | WES 500 l · Erweiterungsmodul 2. Heizkreis · Absenkversuch vor Angebotslegung (objektabhängig) · Kühlfunktion optional · Schallgutachten (45 dB(A)) | WES 500 l · Erweiterungsmodul 2. Heizkreis (erforderlich) · Absenkversuch (objektabhängig) · Kühlfunktion optional · Schallgutachten (optional) | WES 500 l · Energiespeicher [erforderlich] · Erweiterungsmodul 2. Heizkreis + gemischte Pumpengruppe [erforderlich] · Absenkversuch vor Angebotslegung [objektabhängig] · Kühlfunktion über Flächenheizung (optional) [optional] · Schallgutachten / Schallschutzmaßnahmen [optional] | gleich |

### A4 · Sole/Wasser, kleiner Neubau ohne Verbrauch, Taktungsrisiko
Eingaben: Bestand Gas mit Verbrauch 0 (Feld geleert), Einheit kWh, Kesseltyp Niedertemperatur (90 %) · Wohnfläche 60 m² · Wohneinheiten 1 · Personen 2 · Gebäudehülle Pauschale „Neubau GEG (30 W/m²)“ · Heizflächen Fußbodenheizung, 1 Verteiler (Erdgeschoss 6 Kreise) · Wärmequelle Sole/Wasser · Speicher getrennt WAS 200 l + WES 70 l · Norm-Außentemperatur −14 °C · Bivalenzpunkt −7 °C · Ziel-Vorlauf 35 °C (automatisch).
Rechenweg: kein Verbrauchsansatz · Gebäude 60 × 30 ÷ 1 000 = 1,80 kW · + 0,4 kW = 2,20 kW · Lastanteil 0,7586 → 1,67 kW · WGB 8 bei −7/W35 8,6 × 1,15 = 9,89 ≥ 1,67 · Taktung: 1,67 < 1,7 × 1,3 = 2,21 → ja; Reihenpuffer: 2,20 < 2,21 → ja.

| Kennzahl | Einheit | erwartet (Formel) | alt (gemessen) | neu (gemessen) | Status |
|---|---|---|---|---|---|
| Gasverbrauchsansatz | – | „—“ (kein Verbrauch) | „—“ (kein Verbrauch) | – | gleich |
| Gebäudeansatz (Pauschale 30 W/m²) | kW | 1,8 | 1,8 | 1,8 kW | gleich |
| Plausibilität | – | „Nur Gebäudeansatz genutzt“ | „Nur Gebäudeansatz genutzt“ | Nur Gebäudeansatz genutzt (kein Verbrauch angegeben), plus 0,4 kW Warmwasser für 2 Personen. | gleich |
| Auslegungswert Heizlast (inkl. 0,4 kW Warmwasser) | kW | 2,2 | 2,2 | 2,2 kW | gleich |
| Empfohlenes Gerät | – | Weishaupt Geoblock WGB 8 · Modulation 1,7–8,6 kW · 400 V | Weishaupt Geoblock WGB 8 · Modulation 1,7–8,6 kW · 400 V | Weishaupt Geoblock WGB 8 · Modulation 1,7–8,6 kW · 400 V · Sole/Wasser · Badge „Vorschlag“ | gleich |
| Gebäudelast bei −7 °C | kW | 1,7 | 1,7 | 1,7 kW | gleich |
| WP-Leistung A−7/W35 | kW | ≈ 8,6 | ≈ 8,6 | ≈ 8,6 kW | gleich |
| Deckung am Bivalenzpunkt | % | 100 | 100 | 100 % | gleich |
| Status Bivalenzpunkt | – | gedeckt (ohne Heizstab) | „✓ … vollständig ohne Heizstab“ (success) | „gedeckt“ · Die Wärmepumpe deckt den Bivalenzpunkt −7 °C vollständig ohne Heizstab. | gleich |
| Sole-Hinweis | – | monovalenter Betrieb, Heizlast 2,2 kW gedeckt | „Monovalenter Betrieb — die Sole/Wasser-Wärmepumpe deckt die volle Heizlast von 2,2 kW …“ (success) | „Monovalenter Betrieb. Die Sole/Wasser-Wärmepumpe deckt die volle Heizlast von 2,2 kW auch an den kältesten Tagen, da die…“ (ok) | gleich |
| Taktungsrisiko | – | ja (1,7 kW nahe 1,7 kW Modulationsminimum) | ja: „↻ Taktungsrisiko im Teillastbetrieb: Last am Bivalenzpunkt (1,7 kW) nahe der unteren Modulationsgrenze (1,7 kW)“ | ja: „Taktungsrisiko im Teillastbetrieb. Last am Bivalenzpunkt (1,7 kW) nahe der unteren Modulationsgrenze (1,7 kW). Ausreichendes Anlagenvolumen bzw. Pufferspeicher vorsehen.“ | gleich |
| Zusatzpositionen | – | Erdwärmesonde · Soleverteiler · WAS 200 l · WES 70 l · zusätzliches Anlagenvolumen (Reihenpuffer) · Kühlfunktion optional · Schallgutachten (39 dB(A)) | Erdwärmesonde · Soleverteiler · WAS 200 l · WES 70 l · zusätzliches Anlagenvolumen (erforderlich) · Kühlfunktion optional · Schallgutachten (optional) | Erdwärmesonde inkl. Bohrung [erforderlich] · Soleverteiler + Solekreis-Zubehör [erforderlich] · WAS 200 l · Trinkwasserspeicher [erforderlich] · WES 70 l · Energiespeicher [erforderlich] · Zusätzliches Anlagenvolumen (Reihenpuffer) [erforderlich] · Kühlfunktion über Flächenheizung (optional) [optional] · Schallgutachten / Schallschutzmaßnahmen [optional] | gleich |

### A5 · wie A1, Norm-Außentemperatur −12,7 °C (nur Neufassung)
Eingaben wie A1, Norm-Außentemperatur −12,7 °C (Vorgabe der Neufassung, Region Oranienburg; in der Altfassung nicht wählbar, Entscheidung Fabian 2026-10-25, 06). Angelegt 2026-10-25 in Schritt 5.
Rechenweg: Heizlast wie A1 = 12,88 kW · Lastanteil (15 + 7) ÷ (15 + 12,7) = 0,7942 → 10,23 kW · WEB 7/10: 8,05 < 10,23 → WEB 9/14: 10,75 ≥ 10,23 · bei −12,7 °C: 8,55 + (2,3 ÷ 8) × 0,8 = 8,78 kW → Heizstab 12,88 − 8,78 = 4,10 kW.

| Kennzahl | Einheit | erwartet (Formel) | alt (gemessen) | neu (gemessen 2026-10-25) | Status |
|---|---|---|---|---|---|
| Ölverbrauchsansatz | kW | 14,2 | – | 14,2 kW | gleich |
| Gebäudeansatz (Pauschale 90 W/m²) | kW | 10,8 | – | 10,8 kW | gleich |
| Auslegungswert Heizlast (inkl. 0,4 kW Warmwasser) | kW | 12,9 | – | 12,9 kW | gleich |
| Empfohlenes Gerät | – | Weishaupt Evoblock WEB 9/14 · Modulation 1,7–14,0 kW · 230 V | – | Weishaupt Evoblock WEB 9/14 · Modulation 1,7–14,0 kW · 230 V · Luft/Wasser | gleich |
| Gebäudelast bei −7 °C | kW | 10,2 | – | 10,2 kW | gleich |
| WP-Leistung A−7/W50 | kW | ≈ 9,4 | – | ≈ 9,4 kW | gleich |
| Deckung am Bivalenzpunkt | % | 91 | – | 91 % | gleich |
| Status Bivalenzpunkt | – | knapp (Heizstab 0,88 kW ≤ 15 % von 14 kW) | – | „knapp“ | gleich |
| Nennwärmeleistung A−7/W35 | kW | 9,5 | – | 9,5 kW | gleich |
| Gebäudeheizlast bei −12,7 °C | kW | 12,9 | – | 12,9 kW | gleich |
| WP-Leistung A−12,7/W50 | kW | ≈ 8,8 | – | ≈ 8,8 kW | gleich |
| Heizstab-Anteil bei −12,7 °C | kW | ≈ 4,1 (Stufe 2) | – | ≈ 4,1 kW (Stufe 2) | gleich |
| Taktungsrisiko | – | nein | – | nein | gleich |
| Alternative Aeroblock | – | WAB 14, ≈ 10,9 kW, 100 % Deckung | – | Alternative: Weishaupt Aeroblock WAB 14 | gleich |
| Zusatzpositionen | – | Öltankentsorgung · WAS 300 l · WES 200 l · Schallgutachten (optional) | – | Öltankentsorgung inkl. Restölentsorgung [erforderlich] · WAS 300 l · Trinkwasserspeicher [erforderlich] · WES 200 l · Energiespeicher [erforderlich] · Schallgutachten / Schallschutzmaßnahmen [optional] | gleich |

## heizkoerper.html · H1–H6
Noch anzulegen beim Umbau des Tools (Schritt 2). Je Fall: Eingaben, alle Kennzahlen, gewählte Artikel, Bestellnummern, Lagerabgleich-Status.

## bestandsaufnahme.html · B1–B3
Noch anzulegen beim Umbau des Tools (Schritt 2). Je Fall: erfasste Positionen und erzeugte `lager.json` (nur Artikel und Stückzahlen).
