/**
 * ABCD Menu App - Performance Load Test
 * Tests the local Python HTTP server with concurrent users.
 * Usage: node load_test.js
 */

const http = require('http');

const HOST = 'localhost';
const PORT = 8080;
const PAGES = ['/', '/appetizers.html', '/biryani.html', '/curries.html'];

// Test configuration
const ROUNDS = [
  { label: '10 concurrent users,  100 requests',  concurrent: 10,  total: 100  },
  { label: '50 concurrent users,  500 requests',  concurrent: 50,  total: 500  },
  { label: '100 concurrent users, 1000 requests', concurrent: 100, total: 1000 },
];

function fetchPage(path) {
  return new Promise((resolve, reject) => {
    const start = Date.now();
    const req = http.get({ host: HOST, port: PORT, path }, (res) => {
      let size = 0;
      res.on('data', (chunk) => size += chunk.length);
      res.on('end', () => resolve({ status: res.statusCode, ms: Date.now() - start, size }));
    });
    req.on('error', reject);
    req.setTimeout(5000, () => { req.destroy(); reject(new Error('timeout')); });
  });
}

async function runRound({ label, concurrent, total }) {
  console.log(`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
  console.log(`  ${label}`);
  console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);

  const results = { ok: 0, errors: 0, times: [] };
  const startAll = Date.now();
  let sent = 0;

  async function worker() {
    while (sent < total) {
      const i = sent++;
      const page = PAGES[i % PAGES.length];
      try {
        const r = await fetchPage(page);
        if (r.status === 200) { results.ok++; results.times.push(r.ms); }
        else results.errors++;
      } catch { results.errors++; }
    }
  }

  const workers = Array.from({ length: concurrent }, () => worker());
  await Promise.all(workers);

  const wallMs = Date.now() - startAll;
  const sorted = [...results.times].sort((a, b) => a - b);
  const avg = (sorted.reduce((s, v) => s + v, 0) / sorted.length) | 0;
  const p50 = sorted[Math.floor(sorted.length * 0.50)] ?? '-';
  const p90 = sorted[Math.floor(sorted.length * 0.90)] ?? '-';
  const p99 = sorted[Math.floor(sorted.length * 0.99)] ?? '-';
  const rps  = ((results.ok / wallMs) * 1000).toFixed(1);

  console.log(`  ✅  Success      : ${results.ok}`);
  console.log(`  ❌  Errors       : ${results.errors}`);
  console.log(`  ⏱   Total time   : ${wallMs} ms`);
  console.log(`  🚀  Req/sec      : ${rps}`);
  console.log(`  📊  Avg latency  : ${avg} ms`);
  console.log(`  📊  P50 latency  : ${p50} ms`);
  console.log(`  📊  P90 latency  : ${p90} ms`);
  console.log(`  📊  P99 latency  : ${p99} ms`);
}

(async () => {
  console.log('\n🔥 ABCD Restaurant Menu – Load Test');
  console.log(`   Target: http://${HOST}:${PORT}`);
  console.log(`   Pages tested: ${PAGES.join(', ')}`);

  for (const round of ROUNDS) {
    await runRound(round);
  }

  console.log('\n✅ Load test complete.\n');
})();
