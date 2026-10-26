# Feldliste · auslegung.html (Wärmepumpen-Auslegung)

Stand: 2026-10-25 · Erstellt von: Claude Code (Sitzung Umbau auslegung) · Geprüft von Fabian: ☑ 2026-10-25 („passt“; die Vorschläge zu den offenen Fragen 1 und 4–13 gelten damit als angenommen, 15 Datum bleibt am Ende) · Korrekturen von Fabian am 2026-10-25 eingearbeitet (Postleitzahl → Norm-Außentemperatur, PDF-Dateiname, Aeroblock-Prüfung nach dem Umbau)
Zweck: Vor dem Neubau nach DESIGNREGELN.md 6.1 jedes Feld der Altfassung befragen. Erst nach Freigabe bauen.
Alle Beispielwerte erfunden, keine Kundendaten. Altfassung: `alt/auslegung_2026-10-25.html` (Stand 04: 2026-08-17; Erkennungsmerkmal „getrennte Felder für Norm-Außentemperatur und Bivalenzpunkt, Geoblock wählbar“ stimmt; Vorgabe Norm-Außentemperatur noch −14 °C, offener Punkt 07/5).

## Fragen je Feld
1. Geht der Wert in die Rechnung ein? Wenn nein: Ergebnis oder weg.
2. Hat er einen Standardwert aus dem Firmengehirn? Dann vorbelegen.
3. Ändert ihn der Nutzer bei jedem Durchlauf? Wenn nein: „Erweitert“.
4. Folgt er aus einer anderen Eingabe? Dann berechnen und anzeigen.
5. Gehört er zu einer Gruppe? Dann gemeinsame Karte oder Zeile.

## Was die Altfassung rechnet (bleibt unverändert)

Alle Formeln stehen so im Skript der Altfassung (Funktionen `verbrauchHeizlast`, `wandFaktor`, `gebaeudeHeizlast`, `leistungBeiVL`, `apLeistungKurve`, `calc`, `komponentenErmitteln`). Konstanten: 1 800 Volllaststunden (VBh), 0,2 kW Warmwasser je Person, Heizgrenze 15 °C, Heizstab-Toleranz 15 % (Faktor 1,15), Taktungsgrenze 1,3 × untere Modulationsgrenze. Werte, die nicht im Firmengehirn belegt sind, sind unten mit [UNGEPRÜFT] markiert; sie bleiben beim Umbau unverändert und werden im Rechenweg ausgewiesen.

1. **Verbrauchsansatz** (kW): Öl = Liter × 10 kWh/L × Kesselwirkungsgrad ÷ 1 800 h · Gas = kWh (bei m³: × 10 kWh/m³) × Kesselwirkungsgrad ÷ 1 800 h · vorhandene WP = Strom × JAZ ÷ 1 800 h. Ohne Verbrauch (0) entfällt der Ansatz. [1 800 h, 10 kWh/L, 10 kWh/m³ in 05 als Stellschrauben, UNGEPRÜFT]
2. **Gebäudeansatz** (kW), drei Methoden:
   - Pauschale: Wohnfläche × W/m² ÷ 1 000 (30 / 50 / 70 / 90 / 110 / 140 W/m²) [UNGEPRÜFT]
   - Bauteile: spezifische Last = max(15; Basis Baujahr + Fenster + Wand + Dach) W/m²; Wand = Werkstoff (massiv 14 / leicht 10 / Holz 8) + Dicke (bis 24 cm +4 / 24–36 cm 0 / über 36 cm −3) + Dämmung (ohne +4 / teil −6 / WDVS −16) [UNGEPRÜFT]
   - U-Werte: Transmission = Σ(Fläche × U) × ΔT ÷ 1 000 mit ΔT = 20 °C − Norm-Außentemperatur; Lüftung = 0,5 1/h × Wohnfläche × 2,5 m × 0,34 Wh/(m³·K) × ΔT ÷ 1 000 [UNGEPRÜFT]
3. **Auslegungswert Heizlast** = Mittel aus Verbrauchs- und Gebäudeansatz (50/50; bei Abweichung über 35 % des Mittelwerts 60 % Gebäude / 40 % Verbrauch) + Warmwasser 0,2 kW × Personen (entfällt bei „nur Heizung“). Ohne Verbrauch: Gebäudeansatz + Warmwasser. [Gewichtung UNGEPRÜFT]
4. **Last am Bivalenzpunkt** = Heizlast × (15 − Bivalenzpunkt) ÷ (15 − Norm-Außentemperatur), begrenzt auf 0…1 (lineare Lastlinie, 05 [BESTÄTIGT]).
5. **Baugröße**: erstes Gerät der Liste, dessen Leistung am Bivalenzpunkt × 1,15 (streng: × 1,0) ≥ Last am Bivalenzpunkt. Luft/Wasser: Reihenfolge WEB 7/10 → 9/14 → 10/15 → 13/20 → WWP LA 20/30-A R → 43/60-A R (Aeroblock übersprungen, als Alternative WAB 8 → 11 → 14 gesucht, nur auf Wunsch ausgelegt); Sole/Wasser: WGB 8 → 14. Passt nichts, wird das größte Gerät genommen. Leistung = Interpolation über Außentemperatur (Stützpunkte −15 / −7 / +2 / +7 °C, außerhalb geklemmt) und Vorlauf (35 / 45 / 55 / 65 / 75 °C). Tabelle `geraete` im Skript: A−7/W35 der WEB [BELEGT, 05]; alle anderen Kurvenpunkte „aus Diagrammen abgelesen“ [UNGEPRÜFT, 05 Zeile 31]; Aeroblock-Werte siehe offene Frage 3.
6. **Zwei Betriebspunkte**: am Bivalenzpunkt Gebäudelast, WP-Leistung, Deckung = min(100; Leistung ÷ Last × 100), Heizstab = max(0; Last − Leistung); bei Norm-Außentemperatur Heizlast, WP-Leistung, Heizstab = max(0; Heizlast − Leistung), Stufe = aufgerundet(Heizstab ÷ 3 kW) [3/6/9 kW UNGEPRÜFT].
7. **Status** (Badge): Heizstab am Bivalenzpunkt ≤ 0,05 kW → gedeckt · ≤ 15 % der maximalen Leistung → knapp · sonst nicht gedeckt. **Taktungsrisiko**, wenn Last am Bivalenzpunkt < 1,3 × untere Modulationsgrenze.
8. **Zusatzpositionen** (Liste, ohne Rechnung, aus Eingaben abgeleitet): Solar-Kanister, Öltankentsorgung, Erdwärmesonde + Soleverteiler, Speicher (WAS/WES oder WMS oder nur WES), Hebeanlage, Zirkulationspumpe, Reihenpuffer (Heizlast < 1,3 × Modulationsminimum), 2. Heizkreis, zusätzliche Heizkreisverteiler, Heizflächen-Hinweise aus der Alt-Vorlauf-Bewertung, Kühlung (4 Positionen) oder Kühloption, Schallgutachten.
9. **Alt-Vorlauf-Bewertung** (Text, ohne Rechnung): nicht warm → Heizflächen zu klein; Alt-VL ≤ Ziel-VL → sehr gut; Absenkung ≤ 10 K → gut; ≤ 20 K → prüfen; > 20 K → Anpassung wahrscheinlich.
10. Live-Rechnung bei jeder Eingabe, kein Button „Berechnen“. Rundung: kW auf 1 Nachkommastelle, Prozent und W/m² ganzzahlig.

## Felder

| Nr. | Feld (alt) | id (alt) | Einheit | Standard | Bereich (alt) | Pflicht | Herkunft des Werts | Gruppe (neu) | Standard / Erweitert / Ergebnis / entfällt | Feld (neu) | id (neu) | Begründung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Kundenfälle (Liste), + Neu, Duplizieren, Löschen, Speichern | kunde-select, kunde-neu, kunde-dupl, kunde-del, kunde-save | – | – | – | nein | localStorage des Geräts | Projekt | entfällt (ersetzt) | Projekt sichern (Datei) / Projekt laden (Datei) / Neues Projekt | – | Vorlage: Projektdateien statt Geräteliste (DESIGNREGELN 6); Varianten = Datei unter neuem Namen sichern. Eingaben bleiben im Browser (`LS.formularMerken`). Offene Frage 1 |
| 1 | Kunde / Bauvorhaben (Platzhalter mit Name und Straße) | kunde-name | – | leer | Text | nein | Nutzer | Projekt | Standard | Kunde / Projekt | projekt | Kopf, Bericht, Dateiname (`LS.dateiname`); Platzhalter „BV Muster“, Hinweis „keine Personendaten“ (Repo öffentlich, Organisationsanweisung) |
| 2 | Beheizte Wohnfläche (Regler + Zahl) | flaeche, flaeche-num | m² | 120 | Regler 60–800, Zahl ab 20 | ja | Kunde / Plan | Gebäude | Standard | Beheizte Wohnfläche | wohnflaeche | ein Zahlenfeld statt Regler + Zahl (6.1 „Ein Feld, ein Zweck“); Regler nur für Werte, die im Gespräch durchgespielt werden |
| 3 | Wohneinheiten (Regler + Zahl) | wohneinheiten, wohneinheiten-num | WE | 1 | 1–20 | nein | Kunde | Gebäude | Standard (Angabe, keine Rechenwirkung) | Wohneinheiten | wohneinheiten | nur im Bericht; bleibt als Angabe zum Objekt. Offene Frage 8 |
| 4 | Personen (Warmwasser) (Regler + Zahl) | personen, personen-num | Pers. | 2 | 1–16 | ja (bei Heizung + WW) | Kunde | Gebäude | Standard | Personen (Warmwasser) | personen | Rechenwirkung 0,2 kW/Person; bei „nur Heizung“ ausgegraut wie alt |
| 5 | Berechnungsmethode Gebäudehülle | geb-mode (JS `gebMode`) | – | schnell | schnell / detail / uwert | ja | Nutzer | Gebäude | Standard | Gebäudehülle | huelleMethode | drei Optionen → `.ls-seg` „Pauschale / Bauteile / U-Werte“; blendet die Felder 6–19 ein wie alt |
| 6 | Gebäude- / Dämmstandard | pauschale | W/m² | 90 | 30 / 50 / 70 / 90 / 110 / 140 | ja (bei Pauschale) | Tool-Tabelle [UNGEPRÜFT] | Gebäude | Standard | Dämmstandard (Pauschale) | pauschale | `.ls-select`, Optionstexte wie alt; Richtwert mit ≈ im Hinweis |
| 7 | Baujahr / Gebäudealter | d-baujahr | W/m² | 55 (1977–1994) | 70 / 55 / 45 / 38 / 28 / 22 | ja (bei Bauteile) | Tool-Tabelle [UNGEPRÜFT] | Gebäude | Standard (nur bei Bauteile) | Baujahr | baujahr | `.ls-select` |
| 8 | Fensterverglasung | d-fenster | W/m² | 12 | 22 / 12 / 5 / −2 | ja (bei Bauteile) | Tool-Tabelle [UNGEPRÜFT] | Gebäude | Standard (nur bei Bauteile) | Fenster | fenster | `.ls-select` |
| 9 | Wandaufbau (Werkstoff) | d-wand-mat | – | leicht | massiv / leicht / holz | ja (bei Bauteile) | Tool-Tabelle [UNGEPRÜFT] | Gebäude | Standard (nur bei Bauteile) | Wand · Werkstoff | wandWerkstoff | Zeile „Wand“ mit drei Feldern (Werkstoff, Dicke, Dämmung) unter gemeinsamem Label |
| 10 | Wanddicke | d-wand-dicke | – | mittel | dünn / mittel / dick | ja (bei Bauteile) | Tool-Tabelle [UNGEPRÜFT] | Gebäude | Standard (nur bei Bauteile) | Wand · Dicke | wandDicke | wie 9 |
| 11 | Wanddämmung | d-wand-daemm | – | ohne | ohne / teil / wdvs | ja (bei Bauteile) | Tool-Tabelle [UNGEPRÜFT] | Gebäude | Standard (nur bei Bauteile) | Wand · Dämmung | wandDaemmung | wie 9 |
| 12 | Dachdämmung / oberste Geschossdecke | d-dach | W/m² | 6 | 16 / 6 / −3 | ja (bei Bauteile) | Tool-Tabelle [UNGEPRÜFT] | Gebäude | Standard (nur bei Bauteile) | Dach / oberste Decke | dach | `.ls-select` |
| 13 | Außenwand · Fläche | u-wand-a | m² | 140 | ab 0 | ja (bei U-Werte) | Energieausweis / Bauteilberechnung | Gebäude | Standard (nur bei U-Werte) | Außenwand · Fläche | uWandA | Zeile je Bauteil: Fläche und U-Wert nebeneinander |
| 14 | Außenwand · U-Wert | u-wand-u | W/(m²·K) | 0,8 | 0,1–2,5 | ja (bei U-Werte) | wie 13 | Gebäude | Standard (nur bei U-Werte) | Außenwand · U-Wert | uWandU | Einheit als Suffix „W/(m²·K)“ |
| 15 | Dach/Decke · Fläche | u-dach-a | m² | 90 | ab 0 | ja (bei U-Werte) | wie 13 | Gebäude | Standard (nur bei U-Werte) | Dach / Decke · Fläche | uDachA | |
| 16 | Dach/Decke · U-Wert | u-dach-u | W/(m²·K) | 0,4 | 0,1–2,5 | ja (bei U-Werte) | wie 13 | Gebäude | Standard (nur bei U-Werte) | Dach / Decke · U-Wert | uDachU | |
| 17 | Fenster · Fläche | u-fen-a | m² | 25 | ab 0 | ja (bei U-Werte) | wie 13 | Gebäude | Standard (nur bei U-Werte) | Fenster · Fläche | uFensterA | |
| 18 | Fenster · U-Wert | u-fen-u | W/(m²·K) | 1,3 | 0,6–5 | ja (bei U-Werte) | wie 13 | Gebäude | Standard (nur bei U-Werte) | Fenster · U-Wert | uFensterU | |
| 19 | Boden/Keller · Fläche | u-bod-a | m² | 90 | ab 0 | ja (bei U-Werte) | wie 13 | Gebäude | Standard (nur bei U-Werte) | Boden / Keller · Fläche | uBodenA | |
| 20 | Boden/Keller · U-Wert | u-bod-u | W/(m²·K) | 0,6 | 0,1–2,5 | ja (bei U-Werte) | wie 13 | Gebäude | Standard (nur bei U-Werte) | Boden / Keller · U-Wert | uBodenU | |
| 21 | Bestehende Heizung (drei Karten Öl / Gas / Wärmepumpe) | `.heizart-card` (JS `heizart`) | – | Öl | oel / gas / wp | ja | Bestandsanlage des Kunden | Bestandsanlage | Standard | Wärmeerzeuger | bestand | `.ls-seg` „Öl / Gas / Wärmepumpe“; Emoji entfallen |
| 22 | Ölverbrauch pro Jahr | oel-verbrauch | L/a | 3 000 | 0–12 000 | nein (0 = ohne Verbrauchsansatz) | Rechnungen des Kunden | Bestandsanlage | Standard (nur bei Öl) | Ölverbrauch | oelVerbrauch | Zahlenfeld; Hinweis „leer lassen, wenn unbekannt“ |
| 23 | Kesselwirkungsgrad (Öl) | oel-eta | – | 0,85 | 0,80 / 0,85 / 0,90 | ja (bei Öl) | Kesseltyp [UNGEPRÜFT; 05 nennt 0,85] | Bestandsanlage | Standard (nur bei Öl) | Kesseltyp (Nutzungsgrad) | oelNutzungsgrad | `.ls-select` mit denselben drei Optionen; Prozent im Optionstext |
| 24 | Gasverbrauch pro Jahr | gas-verbrauch | m³/a oder kWh/a | 3 000 | 0–60 000 | nein (0 = ohne Verbrauchsansatz) | Rechnungen des Kunden | Bestandsanlage | Standard (nur bei Gas) | Gasverbrauch | gasVerbrauch | Zahlenfeld; Einheit folgt Feld 25 |
| 25 | Abrechnungseinheit Gas | gas-einheit (JS `gasEinheit`) | – | m³ | m³ / kWh | ja (bei Gas) | Rechnung | Bestandsanlage | Standard (nur bei Gas) | Einheit | gasEinheit | `.ls-seg` „m³ / kWh“ direkt am Verbrauchsfeld; Hinweis „≈ 10 kWh/m³ (Erdgas H)“ |
| 26 | Kesselwirkungsgrad (Gas) | gas-eta | – | 0,90 | 0,85 / 0,90 / 0,96 | ja (bei Gas) | Kesseltyp [UNGEPRÜFT] | Bestandsanlage | Standard (nur bei Gas) | Kesseltyp (Nutzungsgrad) | gasNutzungsgrad | wie 23 |
| 27 | Stromverbrauch Wärmepumpe/Jahr | wp-strom | kWh/a | 4 500 | 0–20 000 | nein (0 = ohne Verbrauchsansatz) | Zwischenzähler | Bestandsanlage | Standard (nur bei WP) | Stromverbrauch Wärmepumpe | wpStrom | Zahlenfeld |
| 28 | Jahresarbeitszahl (JAZ) | wp-jaz | – | 3,5 | 1,5–6 | ja (bei WP) | Ablesung / Schätzung | Bestandsanlage | Standard (nur bei WP) | Jahresarbeitszahl JAZ | wpJaz | Zahlenfeld; Richtwert ≈ 3,0–4,0 im Hinweis |
| 29 | Bisherige Vorlauftemperatur bekannt? | alt-vl-bekannt (JS `altVlBekannt`) | – | nein | nein / ja | nein | Kunde / Heizkurve | Bestandsanlage | Standard | Bisheriger Vorlauf | altVlBekannt | `.ls-seg` „unbekannt / bekannt“; blendet 30–31 ein; Bewertungstext erscheint im Ergebnis |
| 30 | Vorlauf der Altanlage am kältesten Tag | alt-vl-wert | °C | 60 | 30–90 | ja (bei bekannt) | Heizkurve des Kessels | Bestandsanlage | Standard (nur bei bekannt) | Vorlauf Altanlage | altVl | Zahlenfeld |
| 31 | Wurde es damit ausreichend warm? | alt-vl-komfort | – | ja | ja / knapp / nein | ja (bei bekannt) | Kunde | Bestandsanlage | Standard (nur bei bekannt) | Räume wurden warm | altVlKomfort | drei Optionen → `.ls-seg` „ja / knapp / nein“ |
| 32 | Heizflächen (drei Karten) | `.heizflaeche-card` (JS `heizflaeche`) | – | keine Auswahl | hk / fbh / beides | ja (alt: ohne Auswahl rechnet das Tool mit VL 45 °C) | Bestand | Heizflächen | Standard | Heizflächen | heizflaechen | `.ls-seg` „Heizkörper / Fußbodenheizung / Beides“; setzt die Ziel-Vorlauftemperatur (50 / 35 / Heizkörper-Kreis) solange sie nicht von Hand geändert wurde. Offene Frage 9 |
| 33 | Anzahl Heizkörper | hf-hk-anzahl | Stück | 8 | 0–60 | nein | Bestand | Heizflächen | Standard (nur bei Heizkörper; Angabe, keine Rechenwirkung) | Anzahl Heizkörper | hkAnzahl | nur Bericht; bleibt, weil das Angebot die Zahl braucht |
| 34 | Rohrsystem | hk-system (JS `hkSystem`) | – | zweirohr | zweirohr / einrohr | nein | Bestand | Heizflächen | Standard (nur bei Heizkörper/Beides; Hinweis + Bericht) | Rohrsystem | rohrsystem | `.ls-seg` „Zweirohr / Einrohr“; Einrohr-Hinweis als `.ls-note--warn` |
| 35 | RTL-Boxen vorhanden? | rtl (JS `rtl`) | – | nein | nein / ja | nein | Bestand | Heizflächen | Standard (nur bei Heizkörper/Beides; Bericht) | RTL-Boxen | rtl | `.ls-seg` „nein / ja“; blendet 36–37 ein; Hinweis wie alt |
| 36 | Anzahl RTL-Boxen | rtl-anzahl | Stück | 1 | 1–40 | nein | Bestand | Heizflächen | Standard (nur bei RTL ja) | Anzahl | rtlAnzahl | |
| 37 | Hersteller / Typ (RTL) | rtl-hersteller | – | leer | Text | nein | Bestand | Heizflächen | Standard (nur bei RTL ja) | Hersteller / Typ | rtlTyp | Textfeld |
| 38 | Heizkreisverteiler FBH (Liste: Etage, Kreise; + Verteiler hinzufügen, ×) | fbh-verteiler-liste (JS `fbhVerteiler`) | Kreise | 1 Verteiler „Erdgeschoss“, 6 Kreise | 0–40 Kreise je Verteiler | nein | Bestand | Heizflächen | Standard (nur bei FBH) | Heizkreisverteiler | verteiler | Positionsliste `.ls-items` (Name, Kreise, Löschen) + „+ Verteiler hinzufügen“; Anzahl > 1 → Zusatzposition. Vorschlag: eine Liste für FBH und Beides (alt zwei getrennte Listen mit 6 bzw. 4 Kreisen Vorgabe). Offene Frage 10 |
| 39 | Anzahl Heizkörper (Pumpengruppe 1, Beides) | hf-beides-hk | Stück | 4 | 0–60 | nein | Bestand | Heizflächen | Standard (nur bei Beides; Bericht) | Anzahl Heizkörper | hkAnzahl | Vorschlag: dasselbe Feld wie 33 (bei Beides mit Vorgabe 4 wie alt), da nie beide sichtbar sind |
| 40 | Vorlauftemperatur Heizkörper (Pumpengruppe 1) | hf-beides-vlhk | °C | 50 | 45 / 50 / 55 / 60 | ja (bei Beides) | Auslegung 50/40 [BESTÄTIGT] | Heizflächen | Standard (nur bei Beides) | Vorlauf Heizkörper-Kreis | beidesVlHk | führt die Ziel-Vorlauftemperatur nach (wie alt); `.ls-select` oder Zahlenfeld, siehe offene Frage 11 |
| 41 | Vorlauftemperatur FBH (Pumpengruppe 2) | hf-beides-vlfbh | °C | 40 | 30 / 35 / 40 / 45 | nein (Bericht) | Auslegung | Heizflächen | Standard (nur bei Beides; Angabe) | Vorlauf FBH-Kreis (gemischt) | beidesVlFbh | keine Rechenwirkung, steht im Bericht |
| 42 | Heizkreisverteiler FBH (Beides) | beides-verteiler-liste (JS `beidesVerteiler`) | Kreise | 1 Verteiler „Erdgeschoss“, 4 Kreise | wie 38 | nein | Bestand | Heizflächen | Standard (nur bei Beides) | → Feld 38 | verteiler | siehe 38 |
| 43 | Kühlfunktion gewünscht? | kuehlen (JS `kuehlen`) | – | nein | nein / ja | nein | Kundenwunsch | Heizflächen | Standard (nur bei FBH/Beides) | Kühlung über Flächenheizung | kuehlung | `.ls-seg` „nein / ja“; vier Zusatzpositionen bei ja, Option bei nein |
| 44 | Anzahl Räume mit Kühlung | kuehlen-raeume | Räume | 1 | 1–40 | ja (bei Kühlung) | Kundenwunsch | Heizflächen | Standard (nur bei Kühlung ja) | Räume mit Kühlung (Blossom-ic Raumregler) | kuehlRaeume | Zahlenfeld; Schreibweise „Blossom-ic“ wie Firmengehirn |
| 45 | Wärmequelle | waermequelle (JS) | – | luft | luft / sole | ja | Planung | Auslegung | Standard | Wärmequelle | waermequelle | `.ls-seg` „Luft/Wasser / Sole/Wasser“; Sole → Geoblock, Erdsonde als Zusatzposition |
| 46 | Aufgabe der Wärmepumpe | wp-aufgabe (JS `wpAufgabe`) | – | heizung_ww | heizung_ww / nur_heizung | ja | Planung | Auslegung | Standard | Aufgabe | aufgabe | `.ls-seg` „Heizung + Warmwasser / nur Heizung“; nur Heizung: kein WW-Zuschlag, kein WAS, Personen ausgegraut |
| 46a | – (neu) | – | – | leer | 5 Ziffern | nein | Objektadresse; Tabelle `normaussentemperatur.json` (PLZ → Norm-Außentemperatur nach DIN/TS 12831-1, mit Quelle und Stand) | Auslegung | Standard | Postleitzahl des Objekts | plz | **Entscheidung Fabian 2026-10-25:** Die Norm-Außentemperatur wird aus der Postleitzahl automatisch eingetragen. Die PLZ befüllt nur das Feld 47; die Rechnung bleibt unverändert, die Referenzfälle A1–A4 setzen die Norm-Außentemperatur direkt. Keine PLZ oder PLZ nicht in der Tabelle → Vorgabe −12,7 °C mit Hinweis „Region Oranienburg, PLZ nicht gefunden“. Tabelle `normaussentemperatur.json` liegt seit 2026-10-25 im Repo (8 176 PLZ, nur PLZ und Wert, Quelle BWP-Klimakarte nach DIN/TS 12831-1:2020-04, schriftliche Zustimmung des BWP liegt laut Fabian vor). Im Tool mit `.ls-stand` „Norm-Außentemperaturen Stand 2026-10-25 · DIN/TS 12831-1“ |
| 47 | Norm-Außentemperatur | norm-at | °C | −14 (Auswahl) | −10 … −18 (8 feste Werte) | ja | aus der Postleitzahl (Feld 46a); ohne Treffer Region Oranienburg −12,7 °C [BESTÄTIGT, 05] | Auslegung | Standard | Norm-Außentemperatur | normAT | **Zahlenfeld, automatisch aus der PLZ befüllt, von Hand überschreibbar** (Hinweis „aus PLZ 16515 · DIN/TS 12831-1“ bzw. „von Hand“); Vorgabe −12,7 °C statt Auswahl −14 °C (07/5, Entscheidung Fabian 2026-10-25). Rechenlogik unverändert, jeder Wert war schon interpolierbar. Bereich −20 … 0 °C |
| 48 | Bivalenzpunkt | ap | °C | −7 (Auswahl) | −12 … −3 (8 feste Werte) | ja | Betriebsstandard −7 °C [BESTÄTIGT] | Auslegung | Standard | Bivalenzpunkt | bivalenz | Zahlenfeld, Vorgabe −7 °C, Bereich −15 … 0 °C; Hinweis „Werksauslegung Weishaupt −5 °C“ bleibt als [UNGEPRÜFT]-Hinweis (05) |
| 49 | Ziel-Vorlauftemperatur | vl (JS `vlManuell`) | °C | 45; nach Heizflächen 50 / 35 / HK-Kreis | 35 / 40 / 45 / 50 / 55 / 65 / 75 | ja | Heizflächen; Auslegung 50/40 [BESTÄTIGT] | Auslegung | Standard | Systemtemperatur Vorlauf | vorlauf | Vorschlag aus den Heizflächen bleibt (Hinweis „automatisch vorgeschlagen“), Handänderung hebt ihn auf wie alt. Auswahl oder Zahlenfeld: offene Frage 11 |
| 50 | Strenge Auslegung erzwingen | streng | – | aus | an / aus | nein | 100 % WP-Deckung [BESTÄTIGT, 06] | Erweitert | Erweitert | Strenge Auslegung (100 % Wärmepumpe) | streng | `.ls-check` im Block „Erweitert“; Kurzzeile „Heizstab bis 15 % zulässig“ bzw. „streng: 100 % Wärmepumpe“ |
| 51 | Speicherkonzept | speicher-konzept (JS `speicherKonzept`) | – | getrennt | getrennt / wms | ja (bei Heizung + WW) | Platz im Technikraum | Auslegung (Technikraum) | Standard | Speicherkonzept | speicherKonzept | `.ls-seg` „WAS + WES getrennt / WMS kombiniert“; bei nur Heizung Hinweis wie alt |
| 52 | WAS · Trinkwasserspeicher | sp-was | L | 300 | 200 / 300 / 400 / 500 / 600 | ja (getrennt, Heizung + WW) | Weishaupt-Programm [BESTÄTIGT als Funktionsumfang, 04] | Auslegung (Technikraum) | Standard (nur bei getrennt) | WAS Trinkwasserspeicher | was | `.ls-select`; geht in die Zusatzpositionen |
| 53 | WES · Energiespeicher (Puffer) | sp-wes | L | 200 | 70 / 200 / 500 / 660 / 910 | ja (getrennt oder nur Heizung) | wie 52 | Auslegung (Technikraum) | Standard (nur bei getrennt / nur Heizung) | WES Energiespeicher | wes | `.ls-select` |
| 54 | WMS · Modularspeicher | sp-wms | – | 300_120 | 300_120 / 200_80 | ja (bei WMS) | wie 52 | Auslegung (Technikraum) | Standard (nur bei WMS) | WMS Modularspeicher | wms | `.ls-select` |
| 55 | Abwasseranschluss am Aufstellort vorhanden? | abwasser (JS) | – | ja | ja / nein | nein | Vor Ort | Auslegung (Technikraum) | Standard | Abwasseranschluss am Aufstellort | abwasser | `.ls-seg` „ja / nein“; nein → Hebeanlage (nur bei Heizung + WW) |
| 56 | Zirkulationsleitung vorhanden? | zirkulation (JS) | – | nein | nein / ja | nein | Vor Ort | Auslegung (Technikraum) | Standard | Zirkulationsleitung | zirkulation | `.ls-seg`; ja → Zirkulationspumpe |
| 57 | Solarthermie-Anlage vorhanden? | solar (JS) | – | nein | nein / ja | nein | Vor Ort | Auslegung (Technikraum) | Standard | Solarthermie | solar | `.ls-seg`; blendet 58 ein |
| 58 | Solarthermie demontieren? | solar-demontage (JS `solarDemontage`) | – | ja | ja / nein | nein | Absprache mit Kunde | Auslegung (Technikraum) | Standard (nur bei Solar ja) | Solarthermie demontieren | solarDemontage | `.ls-seg`; ja → Kanister |
| 59 | Photovoltaik-Anlage vorhanden? | pv (JS) | – | nein | nein / ja / geplant | nein | Vor Ort / Kunde | Auslegung (Technikraum) | Standard (Hinweis + Bericht, keine Rechenwirkung) | Photovoltaik | pv | `.ls-seg` „nein / vorhanden / geplant“; SG-Ready-Hinweis wie alt (wir bauen keine PV) |
| 60 | Besonderheiten zur Bestandsanlage | bes-bestand | – | leer | Text | nein | Nutzer | Bestandsanlage | Standard (Bericht) | Notiz Bestandsanlage | notizBestand | Textfeld je Karte, erscheint im Bericht unter „Besonderheiten“. Offene Frage 12 |
| 61 | Besonderheiten zu den Heizflächen | bes-heizflaechen | – | leer | Text | nein | Nutzer | Heizflächen | Standard (Bericht) | Notiz Heizflächen | notizHeizflaechen | wie 60 |
| 62 | Besonderheiten zum Gebäude | bes-gebaeude | – | leer | Text | nein | Nutzer | Gebäude | Standard (Bericht) | Notiz Gebäude | notizGebaeude | wie 60 |
| 63 | Besonderheiten zur Auslegung & Aufstellung | bes-auslegung | – | leer | Text | nein | Nutzer | Auslegung | Standard (Bericht) | Notiz Auslegung / Aufstellung | notizAuslegung | wie 60 |
| 65 | – (neu, Erweiterung 2026-10-25) | – | – | einzel | einzel / kaskade | ja | Planung (Mehrfamilienhaus, Gewerbe) | Auslegung | Standard | Aufstellung | aufstellung | `.ls-seg` „Einzelgerät / Kaskade“; Kaskade = n baugleiche Geräte [Entscheidung Fabian 2026-10-25, Erweiterung Schritt 10, Referenzfall A6] |
| 66 | – (neu) | – | – | WWP LA 20/30-A R (Luft) / WGB 14 (Sole) | Geräte der Wärmequelle | ja (bei Kaskade) | Weishaupt-Programm | Auslegung | Standard (nur bei Kaskade) | Gerät der Kaskade | kaskadeGeraet | `.ls-select`, Liste folgt der Wärmequelle |
| 67 | – (neu) | – | Stück | leer = automatisch | 2–8 | nein | Planung | Auslegung | Standard (nur bei Kaskade) | Anzahl Geräte | kaskadeAnzahl | leer: kleinste Anzahl ≥ 2, deren Leistung am Bivalenzpunkt × Faktor die Last deckt; sonst Handwert |
| 64 | „Aeroblock stattdessen auslegen“ / „Zurück zur Evoblock“ (Button im Ergebnis) | aero-toggle (JS `aeroblockAktiv`) | – | aus | an / aus | nein | Nutzerentscheidung vor Ort (bauliche Gründe) | Ergebnis | Standard (Aktion im Ergebnis) | Aeroblock stattdessen auslegen | aeroblockAktiv | bleibt als Zweitbutton in der Alternativ-Karte; Zustand wird gesichert (Datei, Browser) |

Anzeigefelder der Altfassung (`v-…` gab es hier nicht; `save-status` „✓ gesichert“, `vl-auto-hint`, `detail-ergebnis`, `uwert-ergebnis`, `sp-hint`, `pv-hint`, `hk-system-hint`, `rtl-hint`, `kuehlen-hint`, `alt-vl-bewertung`, `bivalenz-info` (leer)) sind Hinweise oder Zwischenergebnisse; sie werden `.ls-hint`, `.ls-note` oder Teil des Rechenwegs. Der Statustext „✓ gesichert“ wird `LS.toast('Gespeichert', 'ok')` nur bei Dateiaktionen; das Browser-Merken läuft still.

## Reihenfolge der Gruppen (neu) – Vorschlag, offene Frage 7
1. Projekt (Kunde / Projekt; Hinweis „keine Personendaten“)
2. Gebäude (Wohnfläche, Wohneinheiten, Personen; Gebäudehülle: Pauschale / Bauteile / U-Werte; Notiz)
3. Bestandsanlage (Öl / Gas / Wärmepumpe mit Verbrauch und Kesseltyp; bisheriger Vorlauf; Notiz)
4. Heizflächen (Heizkörper / Fußbodenheizung / Beides; Rohrsystem, RTL, Verteiler, Kühlung; Notiz)
5. Auslegung (Wärmequelle, Aufgabe, Norm-Außentemperatur, Bivalenzpunkt, Vorlauf; Technikraum: Speicher, Abwasser, Zirkulation, Solar, PV; Notiz)
6. Erweitert (strenge Auslegung) – eingeklappt in der Karte Auslegung, wie beim Kostenvergleich

Alt war die Reihenfolge Bestand → Heizflächen → Gebäude → Auslegung. Vorschlag nach 6.1 („erst das, was den Bedarf bestimmt“): Gebäude vor Bestand; beide Ansätze landen in derselben Kennzahlenzeile.

## Ergebnis (Abschnitt 7 DESIGNREGELN)
- Kennzahlen Heizlast (`.ls-kpis`): Verbrauchsansatz · Gebäudeansatz · Auslegungswert (inkl. Warmwasser); darunter der Plausibilitätssatz (Abweichung, Gewichtung).
- Empfehlungskarte (`.ls-card--navy`, Badge „Vorschlag“): Gerät, Modulation, Phase, Nennwärmeleistung A−7/W35.
- Zwei Betriebspunkte als Kennzahlen (UMBAU-ABLAUF): „Am Bivalenzpunkt −7 °C“: Gebäudelast, WP-Leistung ≈, Deckung %; „Bei Norm-Außentemperatur −12,7 °C“: Heizlast, WP-Leistung ≈, Heizstab ≈ (Stufe). Bei Sole/Wasser statt des zweiten Punkts der Sole-Hinweis wie alt.
- Status als Badge mit den Schwellen der Altfassung: gedeckt (Heizstab am Bivalenzpunkt ≤ 0,05 kW), knapp (≤ 15 % der maximalen Leistung), nicht gedeckt (darüber, „nächstgrößere Baugröße prüfen“).
- Taktungshinweis als `.ls-note--warn` (UMBAU-ABLAUF), Heizstab-Hinweis als `.ls-note--warn`/`--danger`, monovalent als `.ls-note--ok`; Hinweise, die eine Handlung verlangen, stehen vor den Kennzahlen.
- Alternative Aeroblock: eigene Karte mit Leistung, Deckung und Button (Feld 64); bei aktivierter Alternative Badge „Ausweichlösung“.
- Heizflächen-Bewertung (bisheriger Vorlauf) als `.ls-note--ok/warn/danger` mit dem Text der Altfassung.
- Zusatzpositionen als Liste mit Badges „erforderlich / objektabhängig / optional“ (statt farbiger Kreise), Texte wie alt; „Blossom-IC“ → „Blossom-ic“.
- Rechenweg als aufklappbarer Block (`.ls-details`) mit Formel, Eingangswerten, Zwischenergebnissen und Einheit; im Druck sichtbar.
- Bericht nach `vorlagen/bericht-vorlage.html`: Kopf, Objekt/Gebäude, Bestandsanlage, Heizlast, Ergebnis mit beiden Betriebspunkten, Zusatzpositionen, Besonderheiten, Fuß mit dem Haftungstext der Altfassung („Überschlägige Ersteinschätzung … DIN EN 12831 … Fachinformation 83603801“). **PDF-Dateiname (Entscheidung Fabian 2026-10-25):** Der Seitentitel beim Drucken lautet „Wärmepumpenauslegung – Gerät – Kunde/Projekt – Datum“, z. B. „Wärmepumpenauslegung – Weishaupt Evoblock WEB 9-14 – BV Muster – 25.10.2026“ (Schrägstriche durch Bindestrich ersetzt wie alt). Die Altfassung hatte die Reihenfolge Tool – Kundenname – Gerät – Datum; sie wird auf Fabians Wunsch getauscht. Der Kundenname darf in den PDF-Dateinamen, weil das PDF in die Kundenakte geht (DESIGNREGELN 9: nur nicht, wenn das PDF in Claude gelangt). Die Projektdatei (JSON) heißt weiter `auslegung_BV-Muster_JJJJ-MM-TT.json` über `LS.dateiname`.
- Emoji und Sonderzeichen der Altfassung (✓ ◐ ⚠ ↻ ℹ 🛢 🔥 ⚡) entfallen; Icons nur aus `assets/icons/icons.html` oder keine.

## Zuordnung alt → neu für Projektdateien (FELD_MAPPING)
```js
/* Die Altfassung hatte keine Projektdateien, nur localStorage (Kundenfälle `lutzspring_evoblock_kunden_v2`,
   Arbeitsstand `lutzspring_evoblock_work_v2`). Die Zuordnung dient der Nachvollziehbarkeit der neuen ids
   und einer möglichen Übernahme des alten Arbeitsstands beim ersten Start (offene Frage 1). */
var FELD_MAPPING = {
  'kunde-name': 'projekt', 'flaeche-num': 'wohnflaeche', 'wohneinheiten-num': 'wohneinheiten', 'personen-num': 'personen',
  gebMode: 'huelleMethode', pauschale: 'pauschale', 'd-baujahr': 'baujahr', 'd-fenster': 'fenster',
  'd-wand-mat': 'wandWerkstoff', 'd-wand-dicke': 'wandDicke', 'd-wand-daemm': 'wandDaemmung', 'd-dach': 'dach',
  'u-wand-a': 'uWandA', 'u-wand-u': 'uWandU', 'u-dach-a': 'uDachA', 'u-dach-u': 'uDachU',
  'u-fen-a': 'uFensterA', 'u-fen-u': 'uFensterU', 'u-bod-a': 'uBodenA', 'u-bod-u': 'uBodenU',
  heizart: 'bestand', 'oel-verbrauch': 'oelVerbrauch', 'oel-eta': 'oelNutzungsgrad', 'gas-verbrauch': 'gasVerbrauch',
  gasEinheit: 'gasEinheit', 'gas-eta': 'gasNutzungsgrad', 'wp-strom': 'wpStrom', 'wp-jaz': 'wpJaz',
  altVlBekannt: 'altVlBekannt', 'alt-vl-wert': 'altVl', 'alt-vl-komfort': 'altVlKomfort',
  heizflaeche: 'heizflaechen', 'hf-hk-anzahl': 'hkAnzahl', hkSystem: 'rohrsystem', rtl: 'rtl', 'rtl-anzahl': 'rtlAnzahl',
  'rtl-hersteller': 'rtlTyp', fbhVerteiler: 'verteiler', beidesVerteiler: 'verteiler', 'hf-beides-hk': 'hkAnzahl',
  'hf-beides-vlhk': 'beidesVlHk', 'hf-beides-vlfbh': 'beidesVlFbh', kuehlen: 'kuehlung', 'kuehlen-raeume': 'kuehlRaeume',
  waermequelle: 'waermequelle', wpAufgabe: 'aufgabe', 'norm-at': 'normAT', ap: 'bivalenz', vl: 'vorlauf', streng: 'streng',
  speicherKonzept: 'speicherKonzept', 'sp-was': 'was', 'sp-wes': 'wes', 'sp-wms': 'wms',
  abwasser: 'abwasser', zirkulation: 'zirkulation', solar: 'solar', solarDemontage: 'solarDemontage', pv: 'pv',
  'bes-bestand': 'notizBestand', 'bes-heizflaechen': 'notizHeizflaechen', 'bes-gebaeude': 'notizGebaeude',
  'bes-auslegung': 'notizAuslegung', aeroblockAktiv: 'aeroblockAktiv', vlManuell: 'vorlaufManuell'
};
```

## Entfallene oder zu Ergebnissen gewordene Felder
| Feld (alt) | Was stattdessen | Begründung |
|---|---|---|
| Kundenfälle-Liste (Auswahl, + Neu, Duplizieren, Löschen, Speichern) | „Projekt sichern (Datei)“, „Projekt laden (Datei)“, „Neues Projekt“ (mit Rückfrage); Eingaben bleiben im Browser | Vorlage und DESIGNREGELN 6; keine Namensliste mit Personendaten im Gerätespeicher; Varianten = Datei unter neuem Namen |
| Regler Wohnfläche, Wohneinheiten, Personen | je ein Zahlenfeld | Doppelung; Regler nur für Werte, die im Gespräch durchgespielt werden (6) |
| Auswahllisten Norm-Außentemperatur und Bivalenzpunkt | Zahlenfelder mit Vorgabe −12,7 °C / −7 °C | Rechenteil interpoliert jeden Wert; −12,7 war bisher nicht wählbar (07/5) |
| Zwischenergebnis-Zeilen (Bauteilansatz, Transmission/Lüftung) | Rechenweg im Ergebnis | 6.1 „Zwischenrechnung wird Ergebnis“ |
| Emoji-Karten Öl/Gas/WP und Heizkörper/FBH/Beides | `.ls-seg` | keine Emoji, Bausteine des Designsystems |
| Hinweisbanner „Überschlägige Ersteinschätzung …“ oben | Fuß und Berichtsfuß, Badge „Vorschlag“ | 7: Vorschlagscharakter sichtbar, kein Dauerbanner |
| Seitentitel als PDF-Dateiname „Wärmepumpenauslegungstool – Kunde – Gerät – Datum“ | „Wärmepumpenauslegung – Gerät – Kunde/Projekt – Datum“ | Reihenfolge nach Entscheidung Fabian 2026-10-25; geprüft: die Altfassung setzte den Kundennamen vor das Gerät |

## Fachliche Prüfung gegen das Firmengehirn (bleibt im Umbau unverändert, wird hier nur festgehalten)
- Norm-Außentemperatur −12,7 °C, Bivalenzpunkt −7 °C, Heizgrenze 15 °C, Heizstab 15 % / streng 100 % [BESTÄTIGT, 05/06]: im Tool enthalten; nur die Vorgabe −14 °C weicht ab (wird zu −12,7 °C).
- Norm-Außentemperatur aus der Postleitzahl (Entscheidung Fabian 2026-10-25): DIN/TS 12831-1:2020-04 ordnet jede Postleitzahl einem Referenzort zu (8 199 Referenzgebiete, Werte auf eine Nachkommastelle). Die Tabelle ist Teil der lizenzierten Norm; eine frei herunterladbare Liste wurde nicht gefunden (Websuche 2026-10-25: nur die Klimakarte des BWP zum Nachschlagen je PLZ, haustechnikdialog.de). Die Tabelle muss aus einer lizenzierten Quelle des Betriebs stammen (Norm, Heizreport) und mit Quelle und Stand in `normaussentemperatur.json` stehen; ob sie in ein öffentliches Repo darf, ist zu klären (offene Frage 14).
- Heizgrenze ist fest 15 °C (Bestand). 05 nennt 10–12 °C für gedämmten Neubau; dafür gäbe es kein Feld. Erweiterung nach Schritt 10 möglich (offene Frage 5).
- Nennwärmeleistung A−7/W35 der WEB 7,09 / 9,49 / 10,07 / 13,15 kW stimmt mit 05 [BELEGT] überein.
- Aeroblock im Tool: „WAB 8 / 11 / 14“ mit A−7/W35 6,2 / 6,9 / 11,2 kW und Modulation 1,6–8,0 / 1,6–11,0 / 4,1–14,0 kW. 05 [BELEGT, Fachinformation 83601801]: WAB 8-A / 11-A / 14-B mit A−7/W35 4,93 / 5,84 / 8,69 kW, Bereich A2/W35 1,6–6,2 / 1,6–6,9 / 4,1–11,2 kW. Die Tool-Werte 6,2 / 6,9 / 11,2 sind offenbar die Bereichsobergrenzen bei A2/W35, nicht die A−7-Leistung. **Entscheidung Fabian 2026-10-25:** Beim Umbau bleiben die Werte unverändert (Nachweis A1/A2); nach der Freigabe werden die Aeroblock-Daten am Datenblatt (Fachinformation 83601801) geprüft und die laut Hersteller richtigen Werte eingetragen (Erweiterung Schritt 10, siehe unten).
- WWP LA: Modulationsbereiche 6,8–30,6 / 17,1–60,0 kW stimmen mit 05; die Kurvenpunkte sind [UNGEPRÜFT].
- Kältemittel: Ergebnis und Bericht nennen pauschal „R290“ und „Vorlauf bis 75 °C“ für jedes Gerät. Firmengehirn: Kältemittel nur vom Typenschild (05, Lehre 10 in 06). Offene Frage 4.
- „Werksauslegung Bivalenztemperatur −5 °C“, „Zusatzheizung 3/6/9 kW“, „Backup-Heizstäbe 2 × 3,5 kW“ (Sole), „Vorlauf WGB bis 65 °C“ stehen in 05 als [UNGEPRÜFT] oder gar nicht; sie bleiben als Hinweistexte, werden aber mit „laut Datenblatt prüfen“ markiert.
- 1 800 Volllaststunden, Kesselwirkungsgrade, 10 kWh je Liter bzw. m³, 0,2 kW je Person, Gewichtung 50/50 bzw. 60/40, Pauschalen und Bauteilzuschläge, Lüftung n = 0,5: tool-intern [UNGEPRÜFT]; 05 Zeile 38 nennt die Stellschrauben als „am eigenen Kundenstamm zu kalibrieren“. Im Rechenweg mit ≈ ausweisen.
- Partner: „Blossom-IC“ → „Blossom-ic“; „BauGrund Süd“ (Weishaupt-Partner, Erdsonde) steht nicht im Firmengehirn – Text bleibt, aber prüfen (offene Frage 6).

## Erweiterungen nach Freigabe des Umbaus (Schritt 10, je ein Satz nach UMBAU-ABLAUF 10.2)
1. **Aeroblock-Daten prüfen** [Entscheidung Fabian 2026-10-25]: Namen (WAB 8-A / 11-A / 14-B), Leistung A−7/W35 und Modulationsbereiche in der Tabelle `geraete` am Datenblatt Fachinformation 83601801 (Firmengehirn `06_datenblaetter/`) prüfen und die laut Hersteller richtigen Werte eintragen; Quelle als Kommentar im Code; neue Referenzfälle A6/A7 (Aeroblock aktiviert), eigener Commit. Bis dahin rechnet das Tool mit den alten Werten, und das Ergebnis trägt den Hinweis „Aeroblock-Werte werden geprüft“.
3. **Kaskaden-Planung** [Entscheidung Fabian 2026-10-25, gebaut am selben Tag vor der Freigabe des Umbaus, Einzelgerät-Pfad unverändert]: Felder 65–67; Rechnung siehe `tests/referenzwerte.md` A6; Zusatzposition „Kaskadenregelung und hydraulische Einbindung“; Hinweis bei Heizlast über 20 kW. Offen: Kaskadierbarkeit, Höchstzahl, Pufferspeicher und Regelung je Baureihe laut Weishaupt-Planungsunterlagen (07/25).
4. **Kompakter Bericht** [Fabian 2026-10-25]: Der Druck zeigt nur den Bericht (Kopf, Zusammenfassung mit Gebäude, Bestand und Heizlast in kompakten Tabellen, Ergebniskarte Navy mit Kennzahlen, Zusatzpositionen, Rechenweg, Notizen, Fuß); die Ergebniskarte am Bildschirm ist `ls-no-print`.
2. **Norm-Außentemperatur aus der Postleitzahl** [Entscheidung Fabian 2026-10-25]: Feld 46a liest `normaussentemperatur.json` (seit 2026-10-25 im Repo, Zustimmung des BWP liegt vor). Wird im Umbau gebaut, ohne Rechenwirkung; Laden wie `lager.json` über die echte Adresse (`LS.datei.extern`), bei fehlender Datei oder lokalem Aufruf Vorgabe −12,7 °C mit Hinweis. Ob die Tabelle zusätzlich in das Tool eingebettet wird (offline auf dem iPad, ≈ 120 KB), entscheidet Schritt 4.

## Offene Fragen an Fabian
1. **Kundenfälle:** Die Altfassung speichert Fälle mit Namen im Browser des iPads (Kundenfälle-Liste, Duplizieren, Löschen). Vorschlag: ersetzen durch Projektdateien (Sichern/Laden) und stilles Browser-Merken wie beim Kostenvergleich; Varianten als Datei unter neuem Namen. Liegen auf den iPads gespeicherte Fälle, die übernommen werden müssen? Dann würde die Neufassung beim ersten Start den alten Arbeitsstand (`lutzspring_evoblock_work_v2`) einmalig übernehmen; die Kundenfälle-Liste ließe sich als Dateien exportieren.
2. ~~Norm-Außentemperatur −12,7 °C als Zahlenfeld~~ **entschieden 2026-10-25 (Fabian):** Zahlenfeld, automatisch aus der Postleitzahl, Vorgabe −12,7 °C. Die Referenzfälle A1–A4 nutzen −14 / −12 / −16 °C, weil die Altfassung nur feste Werte kennt; für −12,7 °C kommt ein Fall A5 nur „neu“ (wie K4).
3. ~~Aeroblock-Werte~~ **entschieden 2026-10-25 (Fabian):** Umbau mit den alten Werten, danach Prüfung am Datenblatt und Eintrag der laut Hersteller richtigen Werte als Erweiterung Schritt 10 (siehe oben).
4. **Kältemittel im Ergebnis:** „R290“ und „Vorlauf bis 75 °C“ stehen pauschal bei jedem Gerät. Vorschlag: aus Ergebnis und Bericht streichen oder je Gerät aus dem Datenblatt eintragen (Kältemittel nur vom Typenschild). Was gilt?
5. **Heizgrenze:** fest 15 °C lassen (Bestand) oder als Feld unter „Erweitert“ mit Vorgabe 15 °C (Erweiterung Schritt 10, Rechenwirkung, Referenzfall)?
6. **Hinweistexte mit ungeprüften Zahlen:** Werksauslegung −5 °C, Zusatzheizung 3/6/9 kW, Backup 2 × 3,5 kW, WGB bis 65 °C, BauGrund Süd, VDI 4640 35–50 W/m. Beibehalten mit „laut Datenblatt prüfen“ oder weglassen?
7. **Reihenfolge der Karten:** Vorschlag Projekt → Gebäude → Bestandsanlage → Heizflächen → Auslegung (Erweitert darin). Alt: Bestand → Heizflächen → Gebäude → Auslegung. Welche Reihenfolge passt zum Termin vor Ort?
8. **Wohneinheiten:** keine Rechenwirkung, nur Bericht. Behalten (Angabe zum Objekt) oder weg?
9. **Heizflächen ohne Auswahl:** Alt rechnet ohne Wahl mit 45 °C. Vorschlag: Pflichtwahl mit Fehlertext („Heizflächen wählen“) statt stiller 45 °C. Oder Vorgabe „Heizkörper“ (Altbau-Schwerpunkt)?
10. **Verteilerliste:** eine Liste für FBH und Beides (statt zwei getrennte mit 6 bzw. 4 Kreisen Vorgabe)? Rechnung unverändert (nur Anzahl > 1 zählt), Bericht zeigt dieselben Zeilen.
11. **Vorlauftemperaturen als Zahlenfeld oder Auswahl:** Ziel-Vorlauf (35–75), Heizkörper-Kreis (45–60), FBH-Kreis (30–45). Der Rechenteil interpoliert jeden Wert. Vorschlag: Zahlenfelder mit denselben Vorgaben und Bereichen, Hinweis „Heizkörper: 50 °C (Auslegung 50/40)“. Oder Auswahl mit den bisherigen Stufen behalten?
12. **Vier Notizfelder** (Bestand, Heizflächen, Gebäude, Auslegung) behalten, oder eine „Notiz“ am Ende?
13. **Live-Rechnung** wie alt (kein Button „Berechnen“), wie beim Kostenvergleich?
14. ~~Quelle und Ablage der PLZ-Tabelle~~ **erledigt 2026-10-25:** Fabian hat die schriftliche Zustimmung des BWP eingeholt; `normaussentemperatur.json` angelegt (nur PLZ und Norm-Außentemperatur, 8 176 Einträge). Ursprüngliche Frage: Die Norm-Außentemperaturen je Postleitzahl stehen in der lizenzierten DIN/TS 12831-1:2020-04 (8 199 Referenzgebiete); frei herunterladbar ist nichts, nur die BWP-Klimakarte zum Nachschlagen. Woher soll die Tabelle kommen (Norm im Betrieb vorhanden? Export aus Heizreport? Nachschlagen und nur die Region Berlin/Brandenburg eintragen?), und darf eine Normtabelle in das öffentliche Repo? Falls nicht: Ablage auf dem Firmenserver (07/11, VPN) oder nur die PLZ der Region als eigene Liste mit Quellenangabe. Ich trage keine Werte ein, die nicht belegt sind. Befund 2026-10-25 (Klimakarte im Browser geprüft): Die Karte lädt alle 8 176 Postleitzahlgebiete mit Norm-Außentemperatur, Jahresmittel, Klimazone, Ort und Höhe als Attribute; PLZ 16515 Oranienburg = −12,7 °C (stimmt mit 05). Technisch ließe sich die ganze Tabelle auslesen. Das Impressum des BWP verlangt für Vervielfältigung und Verbreitung die schriftliche Zustimmung; die Werte stammen aus der lizenzierten DIN/TS 12831-1. Ohne Zustimmung kommt keine Gesamttabelle in das öffentliche Repo. Vorschlag: schriftliche Anfrage an den BWP (Nutzung in einem internen Werkzeug, Quellenangabe); bis dahin nur einzelne PLZ wie beim Nachschlagen (Probe Region 165xx in der Sitzung geprüft: −12,3 bis −12,8 °C).
15. **PDF-Dateiname, Datum am Ende:** Vorgabe „Wärmepumpenauslegung – Gerät – Kunde/Projekt – Datum“. Das Datum stand auch in der Altfassung am Ende; behalten?
