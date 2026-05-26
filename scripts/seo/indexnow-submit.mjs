#!/usr/bin/env node

import fs from 'node:fs';

const HOST = 'www.youthtick.org';
const BASE = `https://${HOST}`;
const INDEXNOW_ENDPOINT = 'https://api.indexnow.org/indexnow';
const KEY = process.env.INDEXNOW_KEY || 'youthtick-indexnow-20260526';
const KEY_LOCATION = process.env.INDEXNOW_KEY_LOCATION || `${BASE}/youthtick-indexnow-20260526.txt`;

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
    `${BASE}/`,
    `${BASE}/tr/`,
    `${BASE}/de/`,
    `${BASE}/blog.html`,
    `${BASE}/tr/blog.html`,
    `${BASE}/de/blog.html`,
    `${BASE}/sitemap.xml`,
    `${BASE}/rss.xml`
  ];

  const langs = ['', '/tr', '/de'];
  for (const [id, slug] of Object.entries(articleSlugs)) {
    for (const prefix of langs) {
      urls.push(`${BASE}${prefix}/article.html?id=${id}&slug=${slug}`);
    }
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
    console.warn(`Warning: ${bad.length} URL failed reachability check`);
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
