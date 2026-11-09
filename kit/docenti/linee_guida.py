import re
LOGO=open('/home/claude/logo/out/Telesio_logo_blu.svg').read()
LOGO=re.sub(r'<\?xml.*?\?>','',LOGO);LOGO=re.sub(r'<title>.*?</title>','',LOGO)
LOGO=re.sub(r'(<svg[^>]*?)\swidth="[^"]*"',r'\1',LOGO,count=1);LOGO=re.sub(r'(<svg[^>]*?)\sheight="[^"]*"',r'\1',LOGO,1).replace('<svg','<svg class="lg"',1)
CSS=open('canovaccio.py').read().split("CSS='''")[1].split("'''")[0]
CSS+='''.warn{background:#FFF8C2;border-left:1.4mm solid #FFE600;border-radius:1.5mm;padding:3mm 4mm;margin:3mm 0;break-inside:avoid}
.ck li{list-style:none;margin-left:-5mm}.ck li:before{content:"☐  ";color:#2060AF;font-weight:800}
.step{display:grid;grid-template-columns:9mm 1fr;gap:3mm;margin:2.5mm 0;break-inside:avoid}.step span{font:800 15pt 'Bricolage Grotesque';color:#2060AF}
code{font-family:'DM Mono',monospace;font-size:9pt;background:#EEF0F4;padding:0 1mm;border-radius:1mm}h2{break-before:auto}'''
def mm(s):return f'{s//60}:{s%60:02d}'
TOP=[345]*6+[350];c=210;summ=''
for i,d in enumerate(TOP,1):summ+=f'<tr><td>Argomento {i}</td><td class="n">{mm(c)}</td><td class="n">{mm(c+d)}</td><td class="n">{mm(d)}</td></tr>';c+=d
TOT=c+90
body=f'''<div class="hd">{LOGO}<span class="hl">Linee guida per la videolezione</span></div>
<h1>Linee guida per la realizzazione della videolezione</h1><div class="bar"></div>
<p class="lead">Tutto quello che serve per preparare, registrare e consegnare una videolezione del Centro Studi Telesio: il testo, le slide, l'attrezzatura, i tempi, il tasto F9 e la consegna. Le chiediamo di seguire queste indicazioni punto per punto.</p>
<div class="warn"><b>Non è un video di prova.</b> La videolezione che registrerà è una lezione vera e completa. Se il lavoro sarà approvato e lei entrerà a far parte del nostro corpo docente, il video sarà <b>pubblicato sulla piattaforma</b> del Centro Studi e <b>retribuito</b>. Per questo deve rispettare tutte le indicazioni di questo documento.</div>
<div class="kpi"><div><span class="big">{mm(TOT)}</span><small>il suo parlato (circa)</small></div><div><span class="big">60:00</span><small>la videolezione finita, con titoli, ripassi ed esercizi</small></div><div><span class="big">5–7</span><small>argomenti per lezione</small></div><div><span class="big">F9</span><small>a ogni cambio di scena</small></div></div>

<h2>1. Come si lavora, passo per passo</h2>
<div class="step"><span>1</span><div><b>Lei scrive il testo della lezione</b> sul modello Word allegato (<i>Testo_della_lezione_modello.docx</i>) e me lo invia.</div></div>
<div class="step"><span>1b</span><div><b>Lei prepara il test finale</b> nel modello Excel e <b>compila la Scheda di assegnazione dei compiti</b> (<i>Scheda_assegnazione_compiti.pdf</i>, PDF compilabile) con i compiti che assegna agli studenti al termine di questa lezione: istruzioni ai punti 2 e 7.</div></div>
<div class="step"><span>2</span><div><b>Noi controlliamo l'organizzazione</b>: argomenti, esempi, esercizi con le soluzioni, audio. Se manca qualcosa glielo diciamo.</div></div>
<div class="step"><span>3</span><div><b>Noi prepariamo le slide</b> dal suo testo, nella grafica del Centro Studi: un PDF diviso in <b>scene</b>, ognuna con il suo numero in alto a destra (SCENA 1, SCENA 2…). Il contenuto è solo il suo: non aggiungiamo niente, cambia solo la veste grafica.</div></div>
<div class="step"><span>4</span><div><b>Lei registra una prova tecnica di 1 minuto</b> e ce la invia. Solo questa è una prova: controlliamo inquadratura, luce, audio e il tasto F9, e le diamo l'ok.</div></div>
<div class="step"><span>5</span><div><b>Lei registra la lezione completa</b> con le slide davanti a sé, ma <b>senza mostrarle</b> nel video: le inseriamo noi in montaggio, sincronizzate con la sua voce grazie al tasto F9.</div></div>
<div class="step"><span>6</span><div><b>Noi montiamo la videolezione</b> (sigla, titoli, slide, ripassi, esercizi interattivi, sottotitoli) e la sottoponiamo alla Direzione per l'approvazione.</div></div>

<h2 style="break-before:page">2. Il testo della lezione (modello Word)</h2>
<p>Compili il modello sostituendo i testi in grigio; i titoli restano. Per ogni argomento:</p>
<table><tr><th>Sezione</th><th>Che cosa scrivere</th></tr>
<tr><td><b>Regola</b></td><td>Spiegazione chiara, completa e graduale, <b>in italiano e nella lingua della materia</b>. Si parte dalle basi, senza dare per scontate conoscenze pregresse. Le tabelle si scrivono come tabelle, nell'ordine in cui le leggerà.</td></tr>
<tr><td><b>Esempi</b></td><td>Esempi pratici nella lingua della materia, ognuno con la <b>traduzione italiana</b> sulla stessa riga: <i>esempio — traduzione</i>.</td></tr>
<tr><td><b>Spiegazione degli esempi</b></td><td>Perché ogni esempio applica la regola, in modo dettagliato.</td></tr>
<tr><td><b>Ascolto e pronuncia</b></td><td>Dove il libro prevede un ascolto (cuffie, tasto play, QR code), lei prepara un'attività di ascolto <b>originale, con la sua voce</b>: che cosa pronuncia (lettere, parole, frasi, dialoghi) e che cosa ripete lo studente. Le tracce audio dei libri non si usano nella videolezione per la piattaforma. È uno degli elementi fondamentali della valutazione.</td></tr>
<tr><td><b>Esercizio con soluzione</b></td><td>Esercizi preparati da lei, con le soluzioni.</td></tr><tr><td><b>Quiz dell'argomento</b></td><td>5 domande a scelta multipla (1 risposta corretta e 3 sbagliate ma plausibili): diventano il quiz interattivo che ferma il video alla fine dell'argomento.</td></tr></table>
<p><b>Test finale:</b> almeno 15 domande su tutta la lezione, nel file <i>Modello_test_finale.xlsx</i> (istruzioni nel secondo foglio). Lo studente lo deve superare con l'80% per proseguire.</p>
<p>In fondo al modello: <b>Riepilogo finale</b>, interamente nella lingua della materia, e <b>Compiti a casa</b> con le soluzioni, abbastanza articolati da consolidare davvero la lezione (esercizi grammaticali, completamento di frasi e testi, costruzione di frasi, traduzioni nei due sensi, correzione degli errori, ripasso degli argomenti precedenti).</p>
<div class="box"><b class="t">Libri di testo e diritti d'autore</b><ul><li>Si può prendere spunto da argomenti, regole e metodo dei libri, e usare brevi citazioni o singoli esempi.</li><li><b>Non si possono riprodurre</b> pagine, esercizi o altri contenuti dei manuali nelle slide o nel video.</li><li>Gli esercizi vanno scritti da lei: stessa tipologia e stessa difficoltà del libro, ma con frasi ed esempi suoi.</li><li>Nessun logo o marchio di terzi visibile.</li></ul></div>

<h2>3. Attrezzatura e impostazioni</h2>
<p>Si registra con <b>OBS Studio</b>, gratuito (obsproject.com), aggiornato all'ultima versione. Nel video c'è <b>solo lei, a tutto schermo</b>: nessuna slide, nessuna condivisione dello schermo.</p>
<table><tr><th>Dove</th><th>Impostazione</th></tr>
<tr><td>Impostazioni → Video</td><td>Risoluzione di base e di uscita <b>1920×1080</b>; <b>30 fps</b>.</td></tr>
<tr><td>Impostazioni → Uscita</td><td>Qualità di registrazione <b>«Qualità indistinguibile»</b> (oppure 15.000–20.000 kbps). Formato di registrazione <b>MP4 ibrido</b>: è quello che salva i segni del tasto F9.</td></tr>
<tr><td>Impostazioni → Scorciatoie</td><td>Alla voce <b>«Aggiungi marcatore di capitolo»</b> assegni il tasto <b>F9</b>.</td></tr>
<tr><td>Fonte webcam</td><td>«Dispositivo di cattura video», proprietà: risoluzione <b>1920×1080</b>. Poi clic destro → Trasforma → <b>Adatta allo schermo</b>. Niente zoom digitale.</td></tr>
<tr><td>Microfono</td><td>Nel mixer audio, mentre parla, la barra resta nel verde-giallo e <b>non arriva mai al rosso</b>. Non usi filtri «noise gate» bruschi.</td></tr></table>
<p style="font-size:9pt;color:#4A5570">Se usa un Mac e la tastiera ha i tasti funzione speciali, F9 si preme insieme al tasto <b>fn</b>. Nella prova di 1 minuto controlliamo che i segni arrivino nel file.</p>

<h2>4. Inquadratura, luce, audio</h2>
<div class="two"><div class="box"><b class="t">Inquadratura</b><ul><li><b>Viso e spalle</b>, centrati; occhi nel <b>terzo superiore</b> dell'immagine, un po' di spazio sopra la testa.</li><li>Webcam all'<b>altezza degli occhi</b>; guardi in camera, come se parlasse a uno studente.</li><li>Non troppo lontana: nel montaggio il riquadro è piccolo, il viso deve riempirlo.</li><li>Abbigliamento in tinta unita: niente bianco puro, nero totale o righe fitte.</li></ul></div>
<div class="box"><b class="t">Luce e fondale</b><ul><li>Luce <b>davanti al viso</b> (finestra di fronte o lampada morbida un po' più alta degli occhi). Mai alle spalle o solo di lato.</li><li>Fondale semplice e ordinato, senza finestre luminose né oggetti in movimento.</li><li>Se può, si allontani dal muro di almeno 1,5 m.</li></ul></div>
<div class="box"><b class="t">Audio</b><ul><li>Microfono a 20–30 cm dalla bocca (cuffie con microfono o microfono USB vanno benissimo).</li><li>Stanza silenziosa e senza eco; niente ventole, condizionatori o finestre aperte sul traffico.</li><li>Telefono silenzioso, notifiche del computer spente.</li></ul></div>
<div class="box"><b class="t">Le slide</b><ul><li>Le tenga davanti a sé (secondo schermo, tablet o stampate) come traccia.</li><li><b>Non le mostri</b> e non condivida lo schermo.</li><li>Le <b>pagine gialle</b> sono indicazioni solo per lei («STOP · ESERCIZIO», «RIPASSO FINALE»): non vanno nel video.</li></ul></div></div>

<h2>5. I tempi</h2>
<p>Il suo parlato dura circa <b>{mm(TOT)} minuti</b>; con sigla, titoli, ripassi ed esercizi interattivi la videolezione finita arriva a 50–60 minuti. Con 7 argomenti i tempi sono questi; con meno argomenti ognuno dura un po' di più, ma il totale resta circa uguale. Non serve rispettarli al secondo: conta che gli argomenti abbiano durate simili e che le pause ci siano.</p>
<table style="break-inside:avoid"><tr><th>Parte</th><th>Dal minuto</th><th>Al minuto</th><th>Durata</th></tr><tr><td>Introduzione: saluto, tema, gli argomenti uno per uno, che cosa saprà fare lo studente</td><td class="n">0:00</td><td class="n">3:30</td><td class="n">3:30</td></tr>{summ}<tr><td>Riepilogo finale, nella lingua della materia</td><td class="n">{mm(TOT-90)}</td><td class="n">{mm(TOT)}</td><td class="n">1:30</td></tr></table>
<p>Dentro ogni argomento: apertura (una frase su che cosa si impara), regola, esempi con traduzione, spiegazione degli esempi, eventuale ascolto, chiusura.</p>

<h2>6. Durante la registrazione: il tasto F9 e le pause</h2>
<div class="box"><b class="t">Il tasto F9</b><ul><li>Prema <b>F9 una sola volta ogni volta che passa alla scena successiva</b>, nel momento esatto in cui inizia a parlarne. Serve a far comparire la slide giusta mentre parla.</li><li>Si va <b>solo avanti</b>, mai indietro. F9 non si usa per nient'altro.</li><li>Anche le pagine gialle contano come scene: F9 quando ci arriva.</li><li>Il numero di F9 deve essere uguale al numero di scene meno uno. Se i conti non tornano, il montaggio si ferma.</li></ul></div>
<table><tr><th>Momento</th><th>Che cosa fare</th></tr>
<tr><td><b>Inizio</b></td><td>Avvii la registrazione, resti in silenzio <b>3–4 secondi</b>, poi parta dal contenuto: saluto, materia, tema. Niente «ok, cominciamo».</td></tr>
<tr><td><b>Inizio di ogni argomento</b></td><td>F9 e <b>3 secondi di silenzio</b> (lì il montaggio mette il titolo). Poi riparta dal contenuto.</td></tr>
<tr><td><b>Tabelle</b></td><td>Legga le righe <b>nell'ordine in cui compaiono</b>, dicendo per prima la parola iniziale della riga: il montaggio la evidenzia mentre la nomina.</td></tr>
<tr><td><b>Ascolto e pronuncia</b></td><td>Pronunci lei, con voce chiara e lenta, lettere, parole o frasi; dica «Ripeti con me» e lasci <b>3 secondi di silenzio</b> per la ripetizione dello studente; poi spieghi i suoni. Non faccia ascoltare le tracce dei libri.</td></tr>
<tr><td><b>Pagina gialla «STOP · ESERCIZIO»</b></td><td>F9, una frase di chiusura netta e la frase d'annuncio, ad esempio: <i>«Ora metti alla prova quello che hai imparato con l'esercizio.»</i> Poi <b>3 secondi di silenzio</b>. Non legga domande né soluzioni: l'esercizio interattivo lo inseriamo noi.</td></tr>
<tr><td><b>Pagina gialla «RIPASSO FINALE»</b></td><td>F9 e riepilogo della lezione <b>nella lingua della materia</b>, parlando liberamente.</td></tr>
<tr><td><b>Fine</b></td><td>F9 sull'ultima scena, saluti, poi resti <b>ferma 3–4 secondi</b> prima di fermare la registrazione.</td></tr></table>
<div class="box"><b class="t">Come parlare</b><ul><li>Niente «ok», «allora», «va bene», «eh», «hmm»: al loro posto, pause pulite.</li><li>Parli guardando la camera, con calma, come in classe: non legga in modo meccanico.</li><li><b>Non dica mai il numero della lezione</b>, né all'inizio né durante.</li><li>Se sbaglia una frase, faccia una breve pausa e la ripeta da capo: non serve ricominciare la registrazione.</li><li>Registri tutta la lezione in una volta sola, in un unico file.</li></ul></div>

<h2>7. La Scheda di assegnazione dei compiti</h2>
<p>Si apre con Adobe Acrobat Reader (gratuito) o, su Mac, con Anteprima: si clicca negli spazi bianchi per scrivere e nelle caselle per spuntare. Si compila così:</p>
<table><tr><th>Parte</th><th>Che cosa scrivere</th></tr>
<tr><td><b>Intestazione</b></td><td>Materia, nome e cognome, data di oggi. «Prossima diretta» si lascia vuota.</td></tr>
<tr><td><b>1 · Videolezioni da guardare</b></td><td>Nella prima riga: materia e titolo di questa lezione. La colonna «Lezione» si lascia vuota.</td></tr>
<tr><td><b>2 · Studio della dispensa e delle slide</b></td><td>Spunti le attività che assegna.</td></tr>
<tr><td><b>3 · Esercizi e preparazione alla diretta</b></td><td>Spunti le attività che assegna.</td></tr>
<tr><td><b>Indicazioni del docente</b></td><td>L'elenco preciso dei compiti a casa: quali esercizi (gli stessi della sezione «Compiti a casa» del Word), che cosa ripassare, come e quando consegnare.</td></tr></table>
<p>La salvi con il nome <code>Cognome_Materia_Compiti.pdf</code> e la invii insieme al testo Word.</p>
<h2>8. Come valutiamo la videolezione</h2>
<table><tr><th>Criterio</th><th>Che cosa guardiamo</th></tr>
<tr><td><b>Completezza</b></td><td>Tutti gli argomenti assegnati, nell'ordine degli indici dei libri, senza salti; si parte dalle basi.</td></tr>
<tr><td><b>Chiarezza</b></td><td>Spiegazione graduale e approfondita, in italiano e nella lingua della materia, comprensibile da chi parte da zero.</td></tr>
<tr><td><b>Esempi</b></td><td>Esempi originali con traduzione e spiegazione della regola applicata.</td></tr>
<tr><td><b>Ascolto e pronuncia</b></td><td>Presenza e qualità delle attività di ascolto, pronuncia e ripetizione: <b>requisito fondamentale</b>.</td></tr>
<tr><td><b>Esercizi, quiz e test</b></td><td>Originali, coerenti con gli argomenti, con soluzioni corrette; capacità di preparare esercizi digitali e test interattivi.</td></tr>
<tr><td><b>Compiti</b></td><td>Compiti articolati e vari, non pochi esercizi: grammatica, completamento, traduzioni, costruzione di frasi, correzione degli errori, ripasso.</td></tr>
<tr><td><b>Riepilogo</b></td><td>Riepilogo finale interamente nella lingua della materia.</td></tr>
<tr><td><b>Rispetto delle linee guida</b></td><td>Inquadratura, luce, audio, tempi, F9, pause; diritti d'autore dei manuali.</td></tr></table>
<div class="box"><b class="t">Se inizierà a collaborare con noi</b>Tutti i libri assegnati andranno sviluppati <b>integralmente, dall'inizio alla fine</b>: grammatica, lessico, comunicazione, dialoghi, comprensione scritta e orale, esercizi e ogni altro contenuto dei testi, con lo stesso metodo di questa videolezione.</div>
<h2>9. Consegna</h2>
<ul><li>Il <b>file originale</b> di OBS (.mp4), senza tagli, modifiche o compressioni, con l'audio dentro.</li><li>Lo invii con un <b>link</b> (WeTransfer o Google Drive), non con WhatsApp né come allegato, che riducono la qualità.</li><li>Nome del file: <code>Cognome_Materia_Videolezione.mp4</code>.</li><li>Insieme al video: il testo Word definitivo, il test finale in Excel, la Scheda di assegnazione dei compiti e, se non l'ha già mandata, la scheda della strumentazione compilata.</li></ul>

<h2 style="break-before:page">10. Controllo di 2 minuti prima di premere «Registra»</h2>
<ul class="ck"><li>OBS: 1920×1080, 30 fps, «Qualità indistinguibile», MP4 ibrido.</li><li>F9 assegnato ad «Aggiungi marcatore di capitolo».</li><li>Solo la webcam a tutto schermo, nessuna slide visibile.</li><li>Viso e spalle centrati, occhi nel terzo superiore, webcam all'altezza degli occhi.</li><li>Luce davanti, niente finestre alle spalle.</li><li>Microfono vicino, barra audio mai nel rosso; telefono e notifiche silenziosi.</li><li>Slide in PDF aperte davanti a me, alla SCENA 1.</li><li>Testo Word a portata di mano per gli esempi e gli ascolti.</li></ul>
<div class="ft">Centro Studi Telesio · Via Monte Napoleone, 8 – 20121 Milano (MI) · Tel. +39 0240130356 · info@centrostuditelesio.it</div>'''
open('linee_guida.html','w',encoding='utf-8').write(f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Linee guida videolezione</title><style>{CSS}</style></head><body>{body}</body></html>')
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.goto('file:///home/claude/docenti/linee_guida.html');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(800)
    pg.pdf(path='/home/claude/invio/Linee_guida_videolezione_Telesio.pdf',format='A4',print_background=True,display_header_footer=True,header_template='<span></span>',footer_template='<div style="font-size:7pt;width:100%;text-align:right;padding-right:15mm;color:#4A5570">Pagina <span class="pageNumber"></span> di <span class="totalPages"></span></div>',margin=dict(top='16mm',bottom='18mm',left='15mm',right='15mm'));b.close()
print(mm(TOT))
