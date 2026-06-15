/* =========================================================
   YouthTICK — basit çok dilli motor (TR varsayılan, EN/DE)
   Metin düğümlerini gezer; Türkçe metni window.YT_I18N
   sözlüğündeki çeviriyle değiştirir. Eksik çeviride TR kalır.
   Çeviriler tüm sayfalarda ortak sözlükten otomatik uygulanır.
   ========================================================= */
(function () {
  var STORE = 'ytlang';
  var SUPPORTED = ['tr', 'en', 'de'];
  var nodes = null; // [{ node, tr }]

  function dictFor(lang) {
    var M = window.YT_I18N || {};
    return M[lang] || {};
  }

  function shouldSkip(parent) {
    if (!parent) return true;
    var tag = parent.nodeName;
    if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'NOSCRIPT') return true;
    if (parent.closest && parent.closest('.lang-switch')) return true;
    return false;
  }

  // Sayfa kaynağı TR; ilk gezinmede orijinal (TR) metni önbelleğe al.
  function collect() {
    nodes = [];
    if (!document.body) return;
    var tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
    var n;
    while ((n = tw.nextNode())) {
      if (!n.nodeValue || !n.nodeValue.trim()) continue;
      if (shouldSkip(n.parentNode)) continue;
      nodes.push({ node: n, tr: n.nodeValue });
    }
  }

  function apply(lang) {
    if (SUPPORTED.indexOf(lang) === -1) lang = 'tr';
    if (!nodes) collect();
    var dict = lang === 'tr' ? null : dictFor(lang);
    for (var i = 0; i < nodes.length; i++) {
      var o = nodes[i];
      if (lang === 'tr') { o.node.nodeValue = o.tr; continue; }
      var raw = o.tr;
      var key = raw.trim();
      var t = dict[key];
      if (t != null) {
        var lead = raw.match(/^\s*/)[0];
        var trail = raw.match(/\s*$/)[0];
        o.node.nodeValue = lead + t + trail;
      } else {
        o.node.nodeValue = o.tr; // çeviri yoksa Türkçe kalsın
      }
    }
    document.documentElement.setAttribute('lang', lang);
    var btns = document.querySelectorAll('.lang-switch [data-lang]');
    for (var b = 0; b < btns.length; b++) {
      btns[b].classList.toggle('active', btns[b].getAttribute('data-lang') === lang);
      btns[b].setAttribute('aria-pressed', btns[b].getAttribute('data-lang') === lang ? 'true' : 'false');
    }
    try { localStorage.setItem(STORE, lang); } catch (e) {}
  }

  function stored() {
    try {
      var l = localStorage.getItem(STORE);
      if (SUPPORTED.indexOf(l) !== -1) return l;
    } catch (e) {}
    return 'tr';
  }

  function init() {
    collect();
    apply(stored());
    var sw = document.querySelector('.lang-switch');
    if (sw) {
      sw.addEventListener('click', function (e) {
        var b = e.target.closest('[data-lang]');
        if (b) apply(b.getAttribute('data-lang'));
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.YTLang = { apply: apply, get: stored };
})();
