import re,html as H
LOGO=open('/home/claude/logo/out/Telesio_logo_blu.svg').read()
LOGO=re.sub(r'<\?xml.*?\?>','',LOGO);LOGO=re.sub(r'<title>.*?</title>','',LOGO)
LOGO=re.sub(r'(<svg[^>]*?)\swidth="[^"]*"',r'\1',LOGO,count=1);LOGO=re.sub(r'(<svg[^>]*?)\sheight="[^"]*"',r'\1',LOGO,1).replace('<svg','<svg class="lg"',1)
def mmss(s):s=int(round(s));return f'{s//60}:{s%60:02d}'
TOP=[345]*6+[350]
rows=[];c=0
def r(a,b,cosa,dice,kind=''):rows.append((a,b,cosa,dice,kind))
r(0,30,'Saluto e presentazione','Saluti, dica la materia e il tema della lezione. Si parte subito dal contenuto: niente «ok, cominciamo».','intro')
r(30,150,'Obiettivi e i 7 argomenti','Nomini i sette argomenti nell\'ordine della slide introduttiva, uno alla volta, e dica che cosa saprà fare lo studente alla fine della lezione.','intro')
r(150,210,'Come funziona la lezione','Frase orientativa: «In ogni argomento trovi un\'animazione, una pillola di ripasso e un esercizio: puoi rispondere con calma, senza limiti di tempo.» Poi <b>3 secondi di silenzio</b>.','intro')
c=210
for i,d in enumerate(TOP,1):
    ap,ch=20,45;sp=round((d-ap-ch)*0.64);es=d-ap-ch-sp
    r(c,c+ap,f'Argomento {i} · apertura',f'Prema <b>F9</b> (nuova slide) e aspetti <b>3 secondi</b>. Poi una frase che dice che cosa si impara in questo argomento.','arg')
    r(c+ap,c+ap+sp,f'Argomento {i} · spiegazione','Regola e tabella: legga le righe <b>nell\'ordine in cui compaiono</b>, dicendo per prima la parola iniziale di ogni riga. A ogni cambio di slide, <b>F9</b>.','arg')
    r(c+ap+sp,c+ap+sp+es,f'Argomento {i} · esempi','Esempi letti ad alta voce, uno alla volta, con la stessa tabella a schermo.','arg')
    r(c+d-ch,c+d,f'Argomento {i} · chiusura e annuncio','Frase finale netta, poi la frase di annuncio (orientativa): «Ora guarda l\'animazione, ripassa la regola con la pillola, poi metti alla prova quello che hai imparato con l\'esercizio.» Poi <b>3 secondi di silenzio</b>.','chiu')
    c+=d
r(c,c+90,'Sintesi finale','Sintesi dei sette argomenti, nella lingua della materia. Non annunci il riepilogo finale (lo aggiunge il montaggio). Poi <b>3–4 secondi fermi</b> e fine registrazione.','intro')
TOT=c+90
tr=''.join(f'<tr class="{k}"><td class="n">{mmss(a)}</td><td class="n">{mmss(b)}</td><td><b>{H.escape(w)}</b></td><td>{s}</td></tr>' for a,b,w,s,k in rows)
summ=''.join(f'<tr><td>Argomento {i}</td><td class="n">{mmss(210+sum(TOP[:i-1]))}</td><td class="n">{mmss(210+sum(TOP[:i]))}</td><td class="n">{mmss(d)}</td></tr>' for i,d in enumerate(TOP,1))
CSS='''@page{size:A4;margin:16mm 15mm 18mm}*{box-sizing:border-box}body{font-family:'Figtree',Arial,sans-serif;color:#0B1530;font-size:10.5pt;line-height:1.45;margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.hd{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:.6pt solid #C9D0DC;padding-bottom:3mm;margin-bottom:8mm}.lg{height:10mm;width:auto}.hl{font:800 7pt Figtree;letter-spacing:.16em;text-transform:uppercase;color:#2060AF}
h1{font:800 24pt/1.08 'Bricolage Grotesque';letter-spacing:-.02em;margin:0}.bar{width:22mm;height:1.4mm;background:#2060AF;border-radius:1mm;margin:3mm 0 5mm}
h2{font:800 14pt 'Bricolage Grotesque';margin:9mm 0 3mm;break-after:avoid}.lead{font-size:12pt;color:#2b3550;margin-bottom:4mm}
table{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:9.4pt}th{background:#0B1530;color:#fff;text-align:left;font:800 7.4pt Figtree;letter-spacing:.08em;text-transform:uppercase;padding:2mm}td{border:.5pt solid #DDE3EE;padding:1.8mm 2mm;vertical-align:top}td.n{white-space:nowrap;font-variant-numeric:tabular-nums;font-weight:700;color:#2060AF;width:14mm}tr{break-inside:avoid}tr.chiu td{background:#FFF8C2}tr.intro td{background:#E9EFF7}
.box{background:#EEF0F4;border-radius:2mm;padding:3mm 4mm;margin:3mm 0;break-inside:avoid}.box b.t{display:block;font:800 7.4pt Figtree;letter-spacing:.14em;text-transform:uppercase;color:#2060AF;margin-bottom:1.2mm}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4mm}ul,ol{margin:1mm 0 2mm;padding-left:5mm}li{margin:1mm 0}.big{font:800 20pt 'Bricolage Grotesque';color:#2060AF}.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin:3mm 0}.kpi div{border:.6pt solid #DDE3EE;border-radius:2mm;padding:2.5mm}.kpi small{display:block;font-weight:700;color:#4A5570;font-size:8pt}
.ft{font-size:7.5pt;color:#4A5570;margin-top:8mm;border-top:.6pt solid #C9D0DC;padding-top:2mm}'''
body=f'''<div class="hd">{LOGO}<span class="hl">Canovaccio per la registrazione</span></div>
<h1>Canovaccio dei tempi per la registrazione delle videolezioni</h1><div class="bar"></div>
<p class="lead">Indicazioni per registrare le nuove lezioni in modo che il montaggio possa aggiungere sigle, titoli, animazioni, pillole di ripasso ed esercizi esattamente nei punti giusti. Come riferimento visivo vale la lezione dimostrativa (link e istruzioni nella mail).</p>
<div class="kpi"><div><span class="big">60:00</span><small>durata della videolezione finita</small></div><div><span class="big">{mmss(TOT)}</span><small>parlato del docente (circa)</small></div><div><span class="big">7</span><small>argomenti, di circa 5:45 l'uno</small></div><div><span class="big">F9</span><small>a ogni cambio di slide</small></div></div>
<div class="box"><b class="t">Come leggere i tempi</b>I minuti indicati sono quelli del <b>cronometro della sua registrazione</b>. Sono indicazioni: non serve rispettarli al secondo, ma è importante che ogni argomento abbia circa la stessa durata e che le pause indicate ci siano. Le frasi suggerite sono <b>solo orientative</b>: le adatti al suo modo di parlare.</div>
<h2>1. Prima di registrare</h2>
<ol><li>Riceverà da me le <b>slide della lezione</b> nella grafica del Centro Studi, create dal suo testo in Word: registri presentando quelle slide.</li><li>Tenga accanto questo canovaccio e un cronometro (va bene quello della registrazione).</li><li>Prima della prima lezione faccia una <b>prova di 1 minuto</b>: registri un minuto con la sua attrezzatura, come se fosse la lezione, e me lo invii. Controllo inquadratura, luce e audio e le rispondo con le eventuali correzioni.</li></ol>
<h2>2. La lezione in sintesi</h2>
<table style="break-inside:avoid"><tr><th>Parte</th><th>Dal minuto</th><th>Al minuto</th><th>Durata</th></tr><tr><td>Introduzione</td><td class="n">0:00</td><td class="n">3:30</td><td class="n">3:30</td></tr>{summ}<tr><td>Sintesi finale</td><td class="n">{mmss(TOT-90)}</td><td class="n">{mmss(TOT)}</td><td class="n">1:30</td></tr></table>
<p>Tra un argomento e l'altro il montaggio inserisce titolo, animazione, pillola ed esercizio: per questo lei non deve fare altro che la pausa di 3 secondi alla fine di ogni argomento.</p>
<h2>3. Il canovaccio minuto per minuto</h2>
<table><tr><th>Dal</th><th>Al</th><th>Parte</th><th>Che cosa fare e dire</th></tr>{tr}</table>
<p style="font-size:8.6pt;color:#4A5570">In azzurro le parti di apertura e chiusura della lezione; in giallo le chiusure di argomento con l'annuncio e la pausa.</p>
<h2>4. Le regole di parlato e di ripresa</h2>
<div class="two"><div class="box"><b class="t">Parlato</b><ul><li><b>F9 a ogni cambio di slide</b>, una sola volta; solo avanti con le slide.</li><li><b>3 secondi di silenzio</b> all'inizio di ogni argomento e dopo ogni annuncio.</li><li>Righe delle tabelle lette <b>nell'ordine in cui compaiono</b>, cominciando dalla prima parola della riga: il montaggio la evidenzia mentre la nomina.</li><li>Niente «ok», «allora», «va bene, cominciamo»; niente intercalari («eh», «hmm»): pause pulite.</li><li>Gli esercizi <b>non si leggono a voce</b>: diventano esercizi interattivi.</li><li>Nelle materie di lingua la spiegazione è <b>bilingue</b>.</li><li>La pillola si annuncia come ripasso, approfondimento e ascolto della pronuncia.</li></ul></div>
<div class="box"><b class="t">Ripresa</b><ul><li>Viso e spalle, occhi nel terzo superiore dell'immagine.</li><li>Luce davanti al viso (finestra di fronte, mai alle spalle).</li><li>Fondale semplice e ordinato.</li><li>Microfono vicino alla bocca, stanza senza eco; niente ventole o rumori.</li><li>Restare fermi 3–4 secondi dopo l'ultimo F9 prima di fermare la registrazione.</li><li>Le impostazioni tecniche (risoluzione, qualità, programma) gliele indico dopo aver ricevuto la scheda della sua strumentazione.</li></ul></div></div>
<h2>5. Che cosa mi consegna</h2>
<ul><li>Il testo della lezione in <b>Word (.docx)</b>: un titolo per ogni argomento, i contenuti nell'ordine in cui li presenta, gli esercizi in una parte a sé con le soluzioni.</li><li>La <b>registrazione originale</b>, senza modifiche, con l'audio.</li><li>La <b>scheda della strumentazione</b> compilata (PDF allegato), una volta sola.</li></ul>
<div class="ft">Centro Studi Telesio · Via Monte Napoleone, 8 – 20121 Milano (MI) · Tel. +39 0240130356 · info@centrostuditelesio.it</div>'''
open('canovaccio.html','w',encoding='utf-8').write(f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Canovaccio registrazione videolezioni</title><style>{CSS}</style></head><body>{body}</body></html>')
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.goto('file:///home/claude/docenti/canovaccio.html');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(800)
    pg.pdf(path='/home/claude/docenti/Canovaccio_tempi_registrazione.pdf',format='A4',print_background=True,display_header_footer=True,header_template='<span></span>',footer_template='<div style="font-size:7pt;width:100%;text-align:right;padding-right:15mm;color:#4A5570">Pagina <span class="pageNumber"></span> di <span class="totalPages"></span></div>',margin=dict(top='16mm',bottom='18mm',left='15mm',right='15mm'));b.close()
print(mmss(TOT))
