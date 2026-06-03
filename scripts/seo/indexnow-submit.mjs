#!/usr/bin/env node

import fs from 'node:fs';

const HOST = 'youthtick.org';
const BASE = `https://${HOST}`;
const INDEXNOW_ENDPOINT = 'https://api.indexnow.org/indexnow';
const KEY = process.env.INDEXNOW_KEY || 'youthtick-indexnow-20260526';
const KEY_LOCATION = process.env.INDEXNOW_KEY_LOCATION || `${BASE}/youthtick-indexnow-20260526.txt`;

// Article blog slugs — TR and DE versions exist as real files
const articleSlugs = {
  50: 'youthtick-yalova-genclik-erasmus-ve-uluslararasi-firsatlar-rehberi',
  51: 'youthtick-yalova-erasmus-basvuru-rehberi-2026',
  52: 'youthtick-yalova-universite-ogrencileri-icin-erasmus-firsatlari',
  53: 'youthtick-yalova-genclik-topluluklari-ve-gonulluluk-rehberi',
  54: 'youthtick-yalova-dil-okulu-ve-yurtdisi-egitim-alternatifleri',
  55: 'youthtick-yalova-genc-girisimcilik-ekosistemi-rehberi',
  56: 'youthtick-yalova-tekmer-osb-ve-teknopark-firsatlari',
  57: 'youthtick-yalova-stk-ve-genclik-kuruluslari-rehberi'
};

function buildUrls() {
  const urls = [
    // Canonical root pages
    `${BASE}/`,
    `${BASE}/blog.html`,
    `${BASE}/sitemap.xml`,
    `${BASE}/rss.xml`,
    // Main site pages
    `${BASE}/events.html`,
    `${BASE}/focus.html`,
    `${BASE}/impact.html`,
    `${BASE}/opportunities.html`,
    `${BASE}/team.html`,
    `${BASE}/partnership.html`,
    `${BASE}/privacy.html`,
    // Yalova landing pages (canonical .html URLs, no /tr/ or /de/ duplicates)
    `${BASE}/yalova-burs.html`,
    `${BASE}/yalova-dil-okulu.html`,
    `${BASE}/yalova-egitim.html`,
    `${BASE}/yalova-erasmus.html`,
    `${BASE}/yalova-erasmus-istatistik.html`,
    `${BASE}/yalova-esc-gonullu.html`,
    `${BASE}/yalova-genclik-toplulugu.html`,
    `${BASE}/yalova-girisimcilik.html`,
    `${BASE}/yalova-gsb.html`,
    `${BASE}/yalova-kariyer.html`,
    `${BASE}/yalova-konut.html`,
    `${BASE}/yalova-kultur-sanat.html`,
    `${BASE}/yalova-ogrenci-yasami.html`,
    `${BASE}/yalova-sivil-toplum.html`,
    `${BASE}/yalova-sks.html`,
    `${BASE}/yalova-spor.html`,
    `${BASE}/yalova-staj.html`,
    `${BASE}/yalova-t3.html`,
    `${BASE}/yalova-teknofest.html`,
    `${BASE}/yalova-teknopark.html`,
    `${BASE}/yalova-universite.html`,
    `${BASE}/yalova-ytso.html`
  ];

  // Blog articles — canonical URLs use /tr/blog/:slug (Turkish) and /de/blog/:slug (German)
  // as those are real files. Also include /blog/:slug if it exists.
  for (const [id, slug] of Object.entries(articleSlugs)) {
    urls.push(`${BASE}/tr/blog/${id}-${slug}`);
    urls.push(`${BASE}/de/blog/${id}-${slug}`);
  }

  return [...new Set(urls)];
}

async function checkUrl(url) {
  try {
    const res = await fetch(url, { method: 'GET', redirect: 'follow' });
    return {
      url,
      ok: res.ok,
      status: res.status,
      finalUrl: res.url
    };
  } catch (err) {
    return {
      url,
      ok: false,
      status: 0,
      error: err instanceof Error ? err.message : String(err)
    };
  }
}

async function main() {
  const urls = buildUrls();
  const checks = [];
  for (const url of urls) {
    checks.push(await checkUrl(url));
  }

  const bad = checks.filter(x => !x.ok);
  if (bad.length) {
    console.warn(`Warning: ${bad.length} URL(s) failed reachability check`);
    bad.forEach(b => console.warn(`  ${b.status} ${b.url}`));
  }

  const submitUrls = checks.filter(x => x.ok).map(x => x.url);
  if (!submitUrls.length) {
    throw new Error('No reachable URL to submit');
  }

  const payload = {
    host: HOST,
    key: KEY,
    keyLocation: KEY_LOCATION,
    urlList: submitUrls
  };

  const submit = await fetch(INDEXNOW_ENDPOINT, {
    method: 'POST',
    headers: { 'content-type': 'application/json; charset=utf-8' },
    body: JSON.stringify(payload)
  });

  const body = await submit.text();
  const report = {
    at: new Date().toISOString(),
    endpoint: INDEXNOW_ENDPOINT,
    submitStatus: submit.status,
    submitOk: submit.ok,
    submitBody: body,
    keyLocation: KEY_LOCATION,
    urlCount: submitUrls.length,
    attemptedUrlCount: urls.length,
    checks
  };

  fs.writeFileSync('reports/indexnow-submit-report.json', JSON.stringify(report, null, 2));

  console.log(`IndexNow status: ${submit.status}`);
  console.log(`Submitted URLs: ${submitUrls.length} / attempted ${urls.length}`);
  console.log('Report: reports/indexnow-submit-report.json');

  if (!submit.ok && submit.status !== 202) {
    process.exitCode = 1;
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
