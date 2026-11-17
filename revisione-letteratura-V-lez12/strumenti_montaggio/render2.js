const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [src, dst] = process.argv.slice(2); fs.mkdirSync(dst, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(src).filter(x => x.endsWith('.html')).sort()) {
    await p.goto('file://' + path.resolve(src, f)); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(dst, f.replace('.html', '.png')) });
  }
  await b.close();
})();
