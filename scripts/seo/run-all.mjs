#!/usr/bin/env node

import { execSync } from 'node:child_process';

function run(cmd) {
  console.log(`\n$ ${cmd}`);
  execSync(cmd, { stdio: 'inherit' });
}

run('node scripts/seo/ping-sitemaps.mjs');
run('node scripts/seo/indexnow-submit.mjs');

console.log('\nSEO automation run completed.');
