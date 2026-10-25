# Umbau-Ablauf: ein Tool auf das Designsystem umstellen

Version 2.1 · Stand 2026-10-25 · gilt je Tool, in der Reihenfolge, die Fabian festlegt [BESTÄTIGT, 2026-10-25]
Grundlage: aktueller Stand im Git und `tests/referenzwerte.md`. Regeln: `DESIGNREGELN.md`. Referenz: `styleguide.html`.

Jeder Schritt hat ein „Wofür“ (warum er nötig ist) und ein „Wie“ (was genau zu tun ist), damit auch jemand ohne Vorwissen ihn ausführen kann. Ein Tool gilt erst als umgebaut, wenn Schritt 9 erledigt ist.

---

## Schritt 1 · Altfassung festhalten

**Wofür:** Der Neubau darf nichts verlieren und nichts verändern, was rechnet. Dafür braucht es ein Bild davon, was das Tool heute kann.

**Wie:**
1. Die Datei im Hauptordner öffnen (`heizkoerper.html` usw.). Stand und Erkennungsmerkmal mit `04_tool-konventionen.md` abgleichen; weicht die Live-Datei ab, zuerst klären, welche Fassung gilt.
2. Im Kopf der Datei notieren (oder in `CHANGELOG.md`): Zweck, Datenquellen (eingebettete Tabellen, `lager.json`, Datenblätter), Dateifunktionen (Sichern/Laden, GAEB), Druckausgabe.
3. Den Rechenteil des Skripts markieren: alle Funktionen, die aus Eingaben Ergebnisse machen. Dieser Teil wird unverändert übernommen.

## Schritt 2 · Feldliste erstellen (Regel 6.1)

**Wofür:** Beim Neubau wird das Formular nicht kopiert, sondern aufgeräumt. Die Feldliste ist die Entscheidung darüber, vorher und schriftlich, damit nichts aus Versehen entfällt.

**Wie:**
1. `vorlagen/feldliste-vorlage.md` kopieren nach `tests/feldliste-TOOLNAME.md`.
2. Jedes Feld der Altfassung eintragen: Name, Einheit, Standardwert, zulässiger Bereich, Pflicht ja/nein, Herkunft des Werts, Gruppe, Standard oder „Erweitert“, neuer Name (falls umbenannt), Begründung.
3. Felder ohne Rechenwirkung werden Ergebnis oder entfallen; selten geänderte Felder gehen nach „Erweitert“; Ableitbares wird berechnet statt abgefragt.
4. Die fertige Liste zeigt Fabian; erst nach seinem „passt“ wird gebaut.

## Schritt 3 · Referenzwerte mit der Altfassung messen

**Wofür:** Nur so lässt sich nachher beweisen, dass die Rechnung gleich geblieben ist.

**Wie:**
1. Die Testfälle des Tools aus `tests/referenzwerte.md` nehmen (A1–A4, K1–K3, H1–H6, B1–B3; nur erfundene Werte).
2. Jeden Fall in die Altfassung eingeben, Ergebnisse (alle Kennzahlen, gewählte Artikel, Bestellnummern) in die Tabelle „alt“ eintragen.
3. Je Fall ein PDF der Altfassung unter `tests/pdf/TOOLNAME_FALL_alt.pdf` ablegen.

## Schritt 4 · Neubau aus der Vorlage

**Wofür:** Die Vorlage enthält Bauplan, Marker, Kopf mit Logo, Hilfe, Dateifunktionen und Rückfragen schon richtig; so sehen alle Tools gleich aus.

**Wie:**
1. `vorlagen/tool-vorlage.html` in den Hauptordner kopieren und auf den festen Dateinamen umbenennen (klein, ohne Umlaute; `heizkoerper.html` mit „r“).
2. `TOOLNAME`, Titel, Untertitel, `apple-mobile-web-app-title`, `PROJEKT_KEY` und den Fußtext (Norm/Quelle) setzen.
3. Formular nach der Feldliste aufbauen: Karten, `.ls-fields`, Einheit als Suffix, Hinweise, „Erweitert“. Vokabular aus DESIGNREGELN.md Abschnitt 8.
4. Rechenteil aus Schritt 1 unverändert einfügen; nur die Verbindung zu den Feldern (ids) anpassen. Zahlen über `LS.lesen`, `LS.fmt`, `LS.einheit`.
5. Ergebnis nach Abschnitt 7 aufbauen: Kennzahlen, Auswahltabelle (`.ls-table--cards`), Status-Badges, Rechenweg.
6. Bericht nach `vorlagen/bericht-vorlage.html`; Bestelltabellen, Notizen, Fuß.
7. `FELD_MAPPING` füllen (alte → neue Feldnamen) und das Laden einer alten Projektdatei prüfen.
8. `python3 _build/inline.py TOOLNAME.html` ausführen (fügt `design.css` und `ls.js` ein).
9. Bei Rekonstruktion mit KI: den Prompt-Baustein aus DESIGNREGELN.md Abschnitt 12 verwenden, Altfassung und Feldliste anhängen; die Antwort muss die Tabelle „alt → neu“ enthalten.

## Schritt 5 · Referenzwerte mit der Neufassung messen

**Wofür:** Der Nachweis, dass nichts anders rechnet.

**Wie:**
1. Dieselben Fälle in die Neufassung eingeben, Ergebnisse in die Spalte „neu“ eintragen.
2. Jede Abweichung ist ein Fehler, bis das Gegenteil belegt ist (z. B. eine Korrektur, die Fabian in `06_entscheidungen.md` bestätigt hat, wie der Faktor ≈ 0,40).
3. PDFs der Neufassung unter `tests/pdf/TOOLNAME_FALL_neu.pdf`; alt und neu nebeneinander prüfen: gleiche Werte, gleiche Artikel, gleicher Aufbau nach Berichtsvorlage.

## Schritt 6 · Prüfung auf iPad und Mac

**Wofür:** Die Tools werden vor Ort auf dem iPad bedient; dort entscheidet sich, ob der Umbau taugt.

**Wie:**
1. Mac/Safari: Hell und Dunkel (Systemeinstellung und Schalter), Tastaturbedienung, kein seitliches Scrollen.
2. iPad/Safari hoch und quer: Felder 44 px, Zifferntastatur mit Komma, „Erweitert“ auf- und zuklappen, Auswahltabelle als Karten, Scrollen zum Ergebnis nach „Berechnen“, Toast sichtbar über dem Haus-Icon.
3. Homescreen-App: Symbol (Logo A auf Navy), Statusleiste überlappt nichts, Haus-Icon erreichbar.
4. Dateien: Projekt sichern → Teilen-Blatt → Dateien; Projekt laden in Safari; alte Projektdatei lädt mit Zuordnung.
5. Druck → PDF: nur Kopf, Ergebnis, Bericht, Fuß; Navy-Kopf und Badges sichtbar; keine zerschnittenen Karten; kein Formular.
6. Handy (400 px): einspaltig, Kopf gestapelt, nichts abgeschnitten.

## Schritt 7 · Datenschutz und Inhalt

**Wofür:** Das Repo ist öffentlich.

**Wie:**
1. Keine Kundennamen, Adressen oder echten Bauvorhaben in Beispielen, Platzhaltern, Screenshots oder Testdateien („BV Muster“).
2. Keine Preise, Konditionen oder Kalkulationssätze im Code; Listenpreise der Website sind öffentlich und erlaubt.
3. `noindex` im Kopf, `.gitignore` für DATANORM/DATPREIS unverändert.

## Schritt 8 · Dokumentieren

**Wofür:** Der nächste, der das Tool anfasst, muss sehen, was sich geändert hat.

**Wie:**
1. `CHANGELOG.md`: Datum, Tool, Fassung, Änderungen in Stichworten, Verweis auf Feldliste und Referenzwerte.
2. `04_tool-konventionen.md` im Firmengehirn: Stand und Erkennungsmerkmal des Tools aktualisieren.
3. Hat sich eine fachliche Festlegung geändert, Eintrag in `06_entscheidungen.md` (nur durch Fabian bestätigt).

## Schritt 9 · Freigabe und Veröffentlichung

**Wofür:** Die Live-Adresse ist das, was die Kollegen benutzen; dort darf nur Geprüftes liegen.

**Wie:**
1. Fabian prüft Feldliste, Referenzwerte und PDF-Vergleich und gibt frei.
2. Altfassung nicht löschen, sondern unter `alt/TOOLNAME_JJJJ-MM-TT.html` ablegen, bis das nächste Tool umgebaut ist (danach kann sie weg; Altlasten laut 04).
3. Commit mit Nachricht „TOOLNAME: Umbau auf design.css 2.1 (Referenzwerte geprüft)“, Push, Live-Adresse im iPad-Safari neu laden; Homescreen-App bei Adressänderung neu anlegen.

---

## Reihenfolge der Tools

Legt Fabian fest [BESTÄTIGT, 2026-10-25]. Vorschlag für die Wahl des ersten Tools: eines mit wenigen Feldern und vorhandenen Referenzwerten, damit der Ablauf einmal vollständig durchlaufen und bei Bedarf angepasst wird, bevor das umfangreichste Tool (heizkoerper.html) folgt.

| Tool | Datei | Besonderheiten beim Umbau |
|---|---|---|
| Startseite | `index.html` | Kacheln aus `vorlagen/index-vorlage.html`; Bilder `bilder/*.jpg` |
| Kostenvergleich | `kostenvergleich.html` | Umschalter Gas/Öl als `.ls-seg`; Empfehlungskarte Navy; Diagramm mit festen Reihenfarben; Energiepreise mit Datenstand |
| Förderrechner | `foerderung.html` | Fördersätze als Eingabe mit Standardwert und `.ls-stand`; keine Zusagen zur Förderhöhe im Text |
| WP-Auslegung | `auslegung.html` | Norm-Außentemperatur auf −12,7 °C (offener Punkt 07/5); zwei Betriebspunkte als Kennzahlen; Taktungshinweis als `.ls-note--warn` |
| Heizkörper-Auslegung | `heizkoerper.html` | Räume als `.ls-items`; Treffer als `.ls-table--cards`; Kennzeichen Bestand/aus Lager als Badges; Lagerabgleich-Status als `.ls-status`; Bestellübersicht nach Berichtsvorlage; GAEB |
| Bestandsaufnahme | `bestandsaufnahme.html` | Stepper je Artikel; Plan-Maße im 5er-Raster; `lager.json` sichern |
| Bad-Angebot | `bad-angebot.html` | **Neubau**, kein Umbau: Schritte 1–3 entfallen, stattdessen Feldliste aus dem Entwurf im Testrepo ableiten. Positionen als `.ls-items`; Angebotsdokument nach Berichtsvorlage mit Summenzeile; GAEB X83 nach TOOLS-WISSEN.md; Sie-Form im Dokument |
