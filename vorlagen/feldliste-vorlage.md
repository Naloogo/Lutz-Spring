# Feldliste · TOOLNAME

Stand: JJJJ-MM-TT · Erstellt von: … · Geprüft von Fabian: ☐ (Datum)
Zweck: Vor dem Neubau nach DESIGNREGELN.md 6.1 jedes Feld der Altfassung befragen. Erst nach Freigabe bauen.
Alle Beispielwerte erfunden, keine Kundendaten.

## Fragen je Feld
1. Geht der Wert in die Rechnung ein? Wenn nein: Ergebnis oder weg.
2. Hat er einen Standardwert aus dem Firmengehirn? Dann vorbelegen.
3. Ändert ihn der Nutzer bei jedem Durchlauf? Wenn nein: „Erweitert“.
4. Folgt er aus einer anderen Eingabe? Dann berechnen und anzeigen.
5. Gehört er zu einer Gruppe? Dann gemeinsame Karte oder Zeile.

## Felder

| Nr. | Feld (alt) | id (alt) | Einheit | Standard | Bereich | Pflicht | Herkunft des Werts | Gruppe (neu) | Standard / Erweitert / Ergebnis / entfällt | Feld (neu) | id (neu) | Begründung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Heizlast | heizlast | W | – | 0–50 000 | ja | Heizlastbericht, Raumwert | Bedarf | Standard | Heizlast Φ<sub>HL</sub> | heizlast | unverändert |
| 2 | Reserve | reserve | % | 0 | 0–30 | nein | Einzelfall (kein Standard, 06) | Bedarf | Erweitert | Sicherheitsreserve | reserve | selten geändert |
| 3 | Norm-AT | ta | °C | −12,7 | −20–0 | ja | Region Oranienburg (06) | Temperaturen | Standard | Norm-Außentemperatur | normAT | einheitliche Bezeichnung über alle Tools |
| 4 | … | | | | | | | | | | | |

## Reihenfolge der Gruppen (neu)
1. Projekt / Raum
2. Bedarf (Heizlast, Raumtemperatur)
3. Temperaturen (Norm-Außentemperatur, System VL/RL)
4. Einbau (Bauhöhe, Baulänge, Bauform, Bestand)
5. Erweitert (Reserve, Exponent, Anschlussseite, …)

## Zuordnung alt → neu für Projektdateien (FELD_MAPPING)
```js
var FELD_MAPPING = { ta: 'normAT', tl: 'raumTemp' };
```

## Entfallene oder zu Ergebnissen gewordene Felder
| Feld (alt) | Was stattdessen | Begründung |
|---|---|---|
| Konsolenanzahl | Ergebnis aus Baulänge (Kermi: 2 bis BL 1600, 3 ab 1800) | ableitbar |

## Offene Fragen an Fabian
- …
