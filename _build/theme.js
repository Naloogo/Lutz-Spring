/* Theme-Schalter: data-theme auf <html>, Wunsch lokal gemerkt. Ohne Schalter folgt das Tool dem System. */
(function () {
  var root = document.documentElement;
  var KEY = 'ls-theme';
  function apply(t) {
    if (t === 'dark' || t === 'light') { root.setAttribute('data-theme', t); }
    else { root.removeAttribute('data-theme'); }
    var b = document.getElementById('themeToggle');
    if (b) { b.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark' ? 'true' : 'false'); }
  }
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  apply(saved);
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest && ev.target.closest('#themeToggle');
    if (!b) return;
    var isDark = root.getAttribute('data-theme') === 'dark' ||
      (!root.getAttribute('data-theme') && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
    var next = isDark ? 'light' : 'dark';
    apply(next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
  });
})();

/* Styleguide-Demos */
document.addEventListener('click', function (ev) {
  var t = ev.target.closest && ev.target.closest('#sgToast, #sgDialog, #sgDlgClose, #sgDel1');
  if (!t) return;
  if (t.id === 'sgToast') LS.toast('Raum „Wohnen“ gespeichert', 'ok');
  if (t.id === 'sgDialog') document.getElementById('sgDlg').showModal();
  if (t.id === 'sgDlgClose') document.getElementById('sgDlg').close();
  if (t.id === 'sgDel1') LS.rueckfrage(t.closest('.ls-item'), 'Raum „Wohnen“ löschen?', 'Löschen', function () { LS.toast('Raum gelöscht (Demo)', 'ok'); });
});
