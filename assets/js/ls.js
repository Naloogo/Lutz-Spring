/* ============================================================
   ls.js · Lutz Spring GmbH · gemeinsame Hilfsfunktionen der Tools
   Version 2.1 · Stand 2026-10-25
   Wird beim Veröffentlichen von _build/inline.py in jedes Tool eingefügt
   (Marker ls.js:start / ls.js:end im HTML).
   Globales Objekt: LS
   ============================================================ */
(function (w, d) {
  'use strict';
  var LS = {};

  /* ---------- Zahlen ---------- */
  /* Liest deutsche Eingaben: "1.234,5", "12.450", "−12,7", "≈ 7,2", "640 W". Gibt null bei Unsinn. */
  LS.zahl = function (v) {
    if (v == null) return null;
    v = String(v).replace(/[≈\s  ]/g, '').replace(/−/g, '-').replace(/[^0-9.,\-]/g, '');
    if (v.indexOf(',') > -1) v = v.replace(/\./g, '').replace(',', '.');
    else if (/^-?\d{1,3}(\.\d{3})+$/.test(v)) v = v.replace(/\./g, '');
    var n = parseFloat(v);
    return isNaN(n) ? null : n;
  };
  /* Liest ein Feld per id. */
  LS.lesen = function (id) { var el = d.getElementById(id); return el ? LS.zahl(el.value) : null; };
  /* Schreibt deutsch mit festen Nachkommastellen, echtes Minus, schmales Leerzeichen als Tausender. */
  LS.fmt = function (n, stellen) {
    if (n == null || isNaN(n)) return '–';
    var s = Number(n).toLocaleString('de-DE', { minimumFractionDigits: stellen || 0, maximumFractionDigits: stellen || 0 });
    return s.replace(/\./g, ' ').replace('-', '−');
  };
  /* Zahl mit Einheit: LS.einheit(1472,'W') → "1 472 W" ; LS.einheit(7.2,'kW',1,true) → "≈ 7,2 kW" */
  LS.einheit = function (n, einheit, stellen, richtwert) {
    return (richtwert ? '≈ ' : '') + LS.fmt(n, stellen) + (einheit ? ' ' + einheit : '');
  };
  LS.datum = function (dt) { return (dt || new Date()).toLocaleDateString('de-DE'); };
  LS.datumISO = function (dt) { dt = dt || new Date(); return dt.getFullYear() + '-' + String(dt.getMonth() + 1).padStart(2, '0') + '-' + String(dt.getDate()).padStart(2, '0'); };

  /* ---------- Speicher im Browser (Eingaben bleiben erhalten) ---------- */
  LS.speicher = {
    lesen: function (key, fallback) { try { var v = localStorage.getItem(key); return v == null ? fallback : JSON.parse(v); } catch (e) { return fallback; } },
    schreiben: function (key, wert) { try { localStorage.setItem(key, JSON.stringify(wert)); return true; } catch (e) { return false; } },
    loeschen: function (key) { try { localStorage.removeItem(key); } catch (e) {} }
  };
  /* Alle Felder eines Formulars merken und wiederherstellen (per id). */
  LS.formularMerken = function (formId, key) {
    var f = d.getElementById(formId); if (!f) return;
    var felder = f.querySelectorAll('input[id], select[id], textarea[id]');
    var gespeichert = LS.speicher.lesen(key, {});
    felder.forEach(function (el) {
      if (gespeichert.hasOwnProperty(el.id)) {
        if (el.type === 'checkbox' || el.type === 'radio') el.checked = !!gespeichert[el.id]; else el.value = gespeichert[el.id];
      }
    });
    f.addEventListener('input', function () {
      var o = {};
      felder.forEach(function (el) { o[el.id] = (el.type === 'checkbox' || el.type === 'radio') ? el.checked : el.value; });
      LS.speicher.schreiben(key, o);
    });
  };

  /* ---------- Theme ---------- */
  LS.theme = {
    KEY: 'ls-theme',
    setzen: function (t) {
      var r = d.documentElement;
      if (t === 'dark' || t === 'light') r.setAttribute('data-theme', t); else r.removeAttribute('data-theme');
      var b = d.getElementById('themeToggle');
      if (b) b.setAttribute('aria-pressed', r.getAttribute('data-theme') === 'dark' ? 'true' : 'false');
    },
    istDunkel: function () {
      var r = d.documentElement;
      return r.getAttribute('data-theme') === 'dark' || (!r.getAttribute('data-theme') && w.matchMedia && w.matchMedia('(prefers-color-scheme: dark)').matches);
    },
    start: function () {
      var s = null; try { s = localStorage.getItem(LS.theme.KEY); } catch (e) {}
      LS.theme.setzen(s);
      d.addEventListener('click', function (ev) {
        var b = ev.target.closest && ev.target.closest('#themeToggle'); if (!b) return;
        var n = LS.theme.istDunkel() ? 'light' : 'dark';
        LS.theme.setzen(n); try { localStorage.setItem(LS.theme.KEY, n); } catch (e) {}
      });
    }
  };

  /* ---------- Rückmeldungen ---------- */
  LS.toast = function (text, art, ms) {
    var box = d.querySelector('.ls-toasts');
    if (!box) { box = d.createElement('div'); box.className = 'ls-toasts'; box.setAttribute('aria-live', 'polite'); d.body.appendChild(box); }
    var t = d.createElement('div'); t.className = 'ls-toast' + (art ? ' ls-toast--' + art : ''); t.textContent = text;
    box.appendChild(t);
    setTimeout(function () { t.remove(); }, ms || 2600);
  };
  /* Inline-Rückfrage: ersetzt den Auslöser-Button vorübergehend durch „Frage · Ja · Abbrechen“. */
  LS.rueckfrage = function (anker, frage, jaText, onJa) {
    var box = d.createElement('div'); box.className = 'ls-confirm'; box.setAttribute('role', 'alertdialog');
    box.innerHTML = '<b></b><button type="button" class="ls-btn ls-btn--danger ls-btn--sm"></button><button type="button" class="ls-btn ls-btn--secondary ls-btn--sm">Abbrechen</button>';
    box.firstChild.textContent = frage; box.children[1].textContent = jaText || 'Löschen';
    anker.insertAdjacentElement('afterend', box); anker.hidden = true; box.children[1].focus();
    box.children[1].addEventListener('click', function () { box.remove(); anker.hidden = false; onJa(); });
    box.children[2].addEventListener('click', function () { box.remove(); anker.hidden = false; anker.focus(); });
  };
  /* Nach „Berechnen“: auf Touchgeräten zum Ergebnis scrollen und Fokus setzen. */
  LS.zumErgebnis = function (id) {
    var el = d.getElementById(id); if (!el) return;
    var touch = w.matchMedia && w.matchMedia('(pointer: coarse)').matches;
    if (touch) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '-1');
    el.focus({ preventScroll: true });
  };

  /* ---------- Fehler an Feldern ---------- */
  LS.fehler = function (id, text) {
    var inp = d.getElementById(id), err = d.getElementById(id + 'Err');
    if (!inp) return;
    if (text) { inp.setAttribute('aria-invalid', 'true'); if (err) { err.textContent = text; err.hidden = false; inp.setAttribute('aria-describedby', err.id); } }
    else { inp.removeAttribute('aria-invalid'); if (err) { err.hidden = true; err.textContent = ''; } }
  };
  /* Prüft eine Zahl gegen Bereich; gibt Fehlertext oder null. */
  LS.pruefen = function (n, min, max, beispiel) {
    if (n == null) return 'Bitte eine Zahl eintragen' + (beispiel != null ? ', z. B. ' + beispiel : '') + '.';
    if (min != null && n < min) return 'Wert muss mindestens ' + LS.fmt(min, 1).replace(',0', '') + ' sein.';
    if (max != null && n > max) return 'Wert darf höchstens ' + LS.fmt(max, 1).replace(',0', '') + ' sein.';
    return null;
  };

  /* ---------- Dateien (JSON-Projekte) ---------- */
  /* Sichern: lädt eine .json herunter. Auf dem iPad erscheint das Teilen-Blatt → „In Dateien sichern“. */
  LS.datei = {
    sichern: function (name, daten) {
      var blob = new Blob([JSON.stringify(daten, null, 2)], { type: 'application/json' });
      var a = d.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name; d.body.appendChild(a); a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
    },
    /* Laden über <input type="file">; ruft onDaten(objekt) oder onFehler(text). */
    laden: function (inputEl, onDaten, onFehler) {
      inputEl.addEventListener('change', function () {
        var f = inputEl.files && inputEl.files[0]; if (!f) return;
        var r = new FileReader();
        r.onload = function () { try { onDaten(JSON.parse(r.result)); } catch (e) { onFehler && onFehler('Datei konnte nicht gelesen werden. Es wird eine .json aus „Projekt sichern (Datei)“ erwartet.'); } };
        r.onerror = function () { onFehler && onFehler('Datei konnte nicht gelesen werden.'); };
        r.readAsText(f); inputEl.value = '';
      });
    },
    /* Feldnamen alter Projektdateien zuordnen: mapping = { altesFeld: 'neuesFeld', … }, je Objekt in liste. */
    migrieren: function (daten, mapping, listeKey) {
      var liste = listeKey ? (daten[listeKey] || []) : [daten];
      liste.forEach(function (o) { Object.keys(mapping).forEach(function (alt) { if (o.hasOwnProperty(alt) && !o.hasOwnProperty(mapping[alt])) { o[mapping[alt]] = o[alt]; delete o[alt]; } }); });
      return daten;
    },
    /* Externe JSON (z. B. lager.json) laden; funktioniert nur über eine echte Adresse (GitHub Pages), nicht lokal. */
    extern: function (url, onDaten, onFehler) {
      if (!w.fetch || location.protocol === 'file:') { onFehler && onFehler('lokal'); return; }
      fetch(url, { cache: 'no-store' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(onDaten).catch(function (e) { onFehler && onFehler(String(e)); });
    }
  };
  /* Dateiname ohne Personendaten: "Heizkoerper-Auslegung_BV-Muster_2026-10-25.json" */
  LS.dateiname = function (tool, projekt, endung) {
    var p = (projekt || 'BV-Muster').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ß/g, 'ss').replace(/[^A-Za-z0-9-]+/g, '-').replace(/^-|-$/g, '');
    return tool + '_' + p + '_' + LS.datumISO() + '.' + (endung || 'json');
  };

  /* ---------- Drucken ---------- */
  LS.drucken = function () { w.print(); };

  /* ---------- Start ---------- */
  LS.start = function () {
    LS.theme.start();
    var dat = d.getElementById('metaDatum'); if (dat && !dat.textContent.trim().replace('–', '')) dat.textContent = LS.datum();
    d.querySelectorAll('[data-print]').forEach(function (b) { b.addEventListener('click', LS.drucken); });
    /* Kachelbild fehlt → Platzhalter statt kaputtem Bildsymbol */
    d.querySelectorAll('img.ls-tile__img').forEach(function (img) {
      img.addEventListener('error', function () { var ph = d.createElement('div'); ph.className = 'ls-tile__img ls-tile__img--placeholder'; ph.textContent = 'Bild folgt'; img.replaceWith(ph); });
    });
    d.querySelectorAll('.ls-stepper').forEach(function (st) {
      var inp = st.querySelector('input'), minus = st.children[0], plus = st.children[2];
      function set(v) { var min = inp.min !== '' ? +inp.min : 0; v = Math.max(min, v); inp.value = v; inp.dispatchEvent(new Event('input', { bubbles: true })); minus.disabled = v <= min; }
      minus.addEventListener('click', function () { set((+inp.value || 0) - 1); });
      plus.addEventListener('click', function () { set((+inp.value || 0) + 1); });
      inp.addEventListener('change', function () { set(+inp.value || 0); });
      set(+inp.value || 0);
    });
  };
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', LS.start); else LS.start();
  w.LS = LS;
})(window, document);
