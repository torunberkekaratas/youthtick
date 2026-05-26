#!/usr/bin/env node

import fs from 'node:fs';

const sitemapUrl = 'https://www.youthtick.org/sitemap.xml';

const endpoints = {
  google: `https://www.google.com/ping?sitemap=${encodeURIComponent(sitemapUrl)}`,
  bing: `https://www.bing.com/ping?sitemap=${encodeURIComponent(sitemapUrl)}`,
  yandex: `https://webmaster.yandex.com/ping?sitemap=${encodeURIComponent(sitemapUrl)}`
};

async function hit(name, url) {
  try {
    const res = await fetch(url, { method: 'GET', redirect: 'follow' });
    const text = await res.text();
    return { name, url, status: res.status, ok: res.ok, bodyPreview: text.slice(0, 400) };
  } catch (err) {
    return { name, url, status: 0, ok: false, error: err instanceof Error ? err.message : String(err) };
  }
}

const results = [];
for (const [name, url] of Object.entries(endpoints)) {
  results.push(await hit(name, url));
}

const report = { at: new Date().toISOString(), sitemapUrl, results };
fs.writeFileSync('reports/sitemap-ping-report.json', JSON.stringify(report, null, 2));

for (const r of results) {
  console.log(`${r.name}: ${r.status}`);
}
console.log('Report: reports/sitemap-ping-report.json');
