# BACKLOG · Gestaltung und Funktion der Tools

Sammelstelle für alles, was beim Benutzen stört oder fehlt. Gelöst wird es im Designsystem (design.css + Styleguide), nie in einem einzelnen Tool. Erledigtes nach CHANGELOG.md.

| Datum | Wer | Was stört / fehlt | Wo (Tool, Stelle) | Beispiel oder Screenshot | Status |
|---|---|---|---|---|---|
| 2026-10-25 | Fabian | Kachelbilder für foerderung.html und bad-angebot.html fehlen (Platzhalter aktiv) | index.html | – | erledigt 2026-10-25: beide Bilder waren in der alten index.html eingebettet, jetzt `bilder/foerderung.jpg` und `bilder/bad.jpg` |
| 2026-10-25 | Fabian | Kachel „Angebotserstellung Bad“ auf der alten Startseite führt ins Leere, Tool noch nicht gebaut | index.html | – | Zwischenstand 2026-10-25: Kachel ohne Link mit Badge „in Vorbereitung“; Link wieder setzen, sobald bad-angebot.html gebaut ist |
| 2026-10-25 | Claude Code (Umbau kostenvergleich) | Kopf im Druck: Titelspalte zu schmal, „Kostenvergleich“ wird mit Trennstrich umbrochen, Untertitel in 7 Zeilen | kostenvergleich.html, Druck (design.css `.ls-header` @media print) | tests/pdf/kostenvergleich_K2_neu.pdf, Seite 1 | offen |
| 2026-10-25 | Claude Code (Umbau kostenvergleich) | Fuß rutscht auf eine eigene dritte Seite, wenn die Berichtskarte die zweite Seite füllt (`.ls-card` bricht nicht innerhalb) | kostenvergleich.html, Druck | tests/pdf/kostenvergleich_K3_neu.pdf, Seite 3 | offen |
| 2026-10-25 | Fabian | Textbutton „Dunkel / Hell“ im Kopf zu klobig | Kopfbalken aller Tools | – | erledigt in 2.1.1: `.ls-theme-toggle` (Symbolknopf) |
