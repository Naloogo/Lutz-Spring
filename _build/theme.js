/* Theme-Schalter kommt aus ls.js (LS.theme.start). Hier nur die Styleguide-Demos. */
/* Styleguide-Demos */
document.addEventListener('click', function (ev) {
  var t = ev.target.closest && ev.target.closest('#sgToast, #sgDialog, #sgDlgClose, #sgDel1');
  if (!t) return;
  if (t.id === 'sgToast') LS.toast('Raum „Wohnen“ gespeichert', 'ok');
  if (t.id === 'sgDialog') document.getElementById('sgDlg').showModal();
  if (t.id === 'sgDlgClose') document.getElementById('sgDlg').close();
  if (t.id === 'sgDel1') LS.rueckfrage(t.closest('.ls-item'), 'Raum „Wohnen“ löschen?', 'Löschen', function () { LS.toast('Raum gelöscht (Demo)', 'ok'); });
});
