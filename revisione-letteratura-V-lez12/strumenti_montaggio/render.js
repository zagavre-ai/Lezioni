// uso: node render.js cartella_html cartella_png   (renderizza ogni .html a 1920x1080)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [src, dst] = process.argv.slice(2);
  fs.mkdirSync(dst, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const f of fs.readdirSync(src).filter(x => x.endsWith('.html')).sort()) {
    const out = path.join(dst, f.replace('.html', '.png'));
    if (fs.existsSync(out) && fs.statSync(out).mtimeMs > fs.statSync(path.join(src, f)).mtimeMs) continue;
    await p.goto('file://' + path.resolve(src, f)); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: out });
  }
  await b.close();
})();
