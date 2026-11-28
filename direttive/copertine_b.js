const { chromium } = require('playwright');
const fs = require('fs');

const DOCS = [
  { file: 'copb_docente.html', parola: 'Docente',
    claim: 'Come gestire la mia docenza' },
  { file: 'copb_responsabile.html', parola: 'Responsabile',
    claim: 'Come seguire i miei studenti' },
];

(async () => {
  const modello = fs.readFileSync('copertina_b.html', 'utf8');
  const b = await chromium.launch();
  for (const d of DOCS) {
    fs.writeFileSync(d.file, modello
      .replace('__PAROLA__', d.parola)
      
      .replace('__CLAIM__', d.claim));
    const p = await b.newPage();
    await p.goto('file://' + __dirname + '/' + d.file, { waitUntil: 'networkidle' });
    await p.pdf({ path: d.file.replace('.html', '.pdf'), format: 'A4',
      printBackground: true, margin: { top:0, bottom:0, left:0, right:0 } });
    await p.close();
    console.log('copertina B:', d.file.replace('.html', '.pdf'));
  }
  await b.close();
})();
