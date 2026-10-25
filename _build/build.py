#!/usr/bin/env python3
"""Baut styleguide.html aus _build/styleguide-body.html + design.css + ls.js. Aufruf im Repo-Hauptordner: python3 _build/build.py"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
b = root / "_build"
css = (root / "assets/css/design.css").read_text(encoding="utf-8")
extra = (b / "styleguide-extra.css").read_text(encoding="utf-8")
body = (b / "styleguide-body.html").read_text(encoding="utf-8")
js = (root / "assets/js/ls.js").read_text(encoding="utf-8") + "\n" + (b / "theme.js").read_text(encoding="utf-8")

head_meta = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#1a2b4a">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>Styleguide · Lutz Spring GmbH</title>"""

repo = f"""<!DOCTYPE html>
<html lang="de">
<head>
{head_meta}
<link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">
<!-- design.css:start -->
<style>
{css}
</style>
<!-- design.css:end -->
<style>
{extra}</style>
</head>
<body>
{body}
<script>
{js}</script>
</body>
</html>
"""
(root / "styleguide.html").write_text(repo, encoding="utf-8")

artifact = f"""<title>Styleguide Lutz Spring</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
{css}
{extra}</style>
{body}
<script>
{js}</script>
"""
art = pathlib.Path("/home/claude/styleguide-lutz-spring.html")
if art.parent.exists(): art.write_text(artifact, encoding="utf-8")  # nur in Claudes Cloud-Umgebung (Artefakt)
print("ok", len(repo), len(artifact))
