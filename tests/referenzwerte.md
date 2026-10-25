# Referenzwerte · Interne Tools der Lutz Spring GmbH

Stand: 2026-10-25 · Nur erfundene Werte, keine Kundendaten (Repo ist öffentlich) [BESTÄTIGT, 2026-10-12].
Zweck: Nachweis, dass ein Umbau nichts an der Rechnung ändert (UMBAU-ABLAUF.md Schritt 3 und 5). Jeder Fall wird in der Altfassung gemessen (Spalte „alt“), dann in der Neufassung (Spalte „neu“). Jede Abweichung ist ein Fehler, bis das Gegenteil belegt ist. PDFs unter `tests/pdf/TOOLNAME_FALL_alt.pdf` und `…_neu.pdf`.

Die Spalte „erwartet (Formel)“ ist aus dem Rechenteil der Altfassung nachgerechnet (Python, gleiche Formeln und Rundung) und dient nur als Plausibilitätsprüfung; maßgeblich ist die Messung in der Altfassung.

Testfälle je Tool: A1–A4 `auslegung.html` · K1–K4 `kostenvergleich.html` · H1–H6 `heizkoerper.html` · B1–B3 `bestandsaufnahme.html`. Die Fälle der noch nicht begonnenen Tools werden beim jeweiligen Umbau (Schritt 2) angelegt.

---

## kostenvergleich.html · K1–K4

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

## auslegung.html · A1–A4
Noch anzulegen beim Umbau des Tools (Schritt 2).

## heizkoerper.html · H1–H6
Noch anzulegen beim Umbau des Tools (Schritt 2). Je Fall: Eingaben, alle Kennzahlen, gewählte Artikel, Bestellnummern, Lagerabgleich-Status.

## bestandsaufnahme.html · B1–B3
Noch anzulegen beim Umbau des Tools (Schritt 2). Je Fall: erfasste Positionen und erzeugte `lager.json` (nur Artikel und Stückzahlen).
