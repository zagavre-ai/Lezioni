const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + __dirname + '/responsabile.html', { waitUntil: 'networkidle' });
  await p.pdf({
    path: 'Direttive_operative_Responsabile.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '16mm', bottom: '18mm', left: '14mm', right: '14mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font-family:sans-serif;font-size:7pt;color:#2060AF;
      padding:0 14mm;display:flex;justify-content:space-between;letter-spacing:.8px;font-weight:700;">
      <span>DIRETTIVE OPERATIVE &middot; PROFILO RESPONSABILE</span>
      <span>Pagina <span class="pageNumber"></span> di <span class="totalPages"></span></span></div>`
  });
  await b.close();
  console.log('pdf creato');
})();
