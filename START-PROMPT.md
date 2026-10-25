# Start-Prompt für eine Claude-Code-Sitzung (je Tool)

Sitzung in der Claude-App unter „Code“ mit dem Ordner `lutz-spring-tools` starten (oder im Terminal: `cd "/Users/Arbeit/Lutz Spring/lutz-spring-tools"` und `claude`). Zuerst `/add-dir ../Firmengehirn` eingeben, dann den folgenden Text unverändert einfügen:

```
Lies CLAUDE.md, DESIGNREGELN.md, UMBAU-ABLAUF.md und die Tabelle „Tools (Umbau auf 2.1)“
in CHANGELOG.md. Das Firmengehirn liegt im Nachbarordner ../Firmengehirn (lesen, nie
kopieren). Zeige mir alle Tools des Repos als Liste mit Stand (offen, in Arbeit,
umgebaut, Neubau) und frage mich, welches Tool ich jetzt umbauen möchte. Baue nichts,
bevor ich geantwortet habe.

Nach meiner Antwort gehst du nach UMBAU-ABLAUF.md vor und beachtest die Sonderfälle:
Die Startseite hat keine Rechenlogik, dort entfallen Feldliste und Referenzwerte;
stattdessen bleiben alle Kacheln und Links erhalten, und die eingebetteten Bilder werden
als JPEG nach bilder/ ausgelagert. bad-angebot.html ist ein Neubau nach Schritt-Tabelle.
Für alle anderen Tools: Schritt 1 (Altfassung festhalten, Sicherung nach alt/) und
Schritt 2 (Feldliste nach vorlagen/feldliste-vorlage.md als tests/feldliste-TOOLNAME.md);
fehlt tests/referenzwerte.md oder die Testfälle des Tools, lege sie mit erfundenen Werten
an. Dann hältst du an und zeigst mir Feldliste, Testfälle und offene Fragen zur Freigabe.
Erst nach meinem „passt“ geht es mit Schritt 3 weiter, Schritt für Schritt, jeweils mit
„Wofür“ und „Wie“. Commit und Push mache ich selbst in GitHub Desktop; sag mir nach jedem
Schritt, welche Dateien sich geändert haben und welche Commit-Nachricht passt.
```

## Danach, in derselben Sitzung
- Freigabe: „passt“ oder Korrekturen zur Feldliste.
- Weiter: „weiter mit Schritt 3“ usw.; nach jedem Schritt in GitHub Desktop prüfen, Commit, Push.
- Erweiterungen erst nach Schritt 9 (Schritt 10): „Umbau ist freigegeben. Jetzt Erweiterung: …“
- Störendes an der Gestaltung nicht im Tool lösen, sondern in BACKLOG.md eintragen.
