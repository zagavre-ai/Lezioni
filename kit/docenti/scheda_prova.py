# Scheda della prova per materia: è l'unica parte che cambia da una selezione all'altra.
# uso: python3 scheda_prova.py  (modifica il dizionario PROVE e aggiungi la materia nuova)
import re
from playwright.sync_api import sync_playwright
PROVE={'Spagnolo':{
 'libri':['<b>Imparare lo spagnolo</b> (disponibile su Amazon)','<b>¡Así de fácil!</b> (Loescher), con i materiali digitali: le indicazioni di accesso gliele inviamo a parte'],
 'argomenti':'I contenuti iniziali dei due libri, <b>nell\'ordine degli indici</b>, integrati in modo complementare (un argomento può prendere la regola da un libro e gli esempi o gli ascolti dall\'altro). Si parte dalle basi: <b>l\'alfabeto</b>, poi gli argomenti che seguono negli indici, fino a 5–7 argomenti per la lezione.',
 'requisiti':['<b>Alfabeto con la pronuncia scritta</b> accanto a ogni lettera, per esempio: <i>H — hache [àce]</i>, <i>Ñ — eñe [ègne]</i>.',
  '<b>Ascolto e pronuncia</b> (requisito fondamentale): lettere e parole pronunciate da lei, con «Ripeti con me» e una pausa per la ripetizione, poi la spiegazione dei suoni. Lo stesso per ogni argomento che nei libri ha un audio (cuffie, tasto play, QR code).',
  'Spiegazione in <b>italiano e spagnolo</b>; esempi in spagnolo con la traduzione italiana.',
  'Riepilogo finale <b>interamente in spagnolo</b>.',
  'Nessuna conoscenza data per scontata: lo studente parte da zero.']}}
LOGO=open('/home/claude/logo/out/Telesio_logo_blu.svg').read()
LOGO=re.sub(r'<\?xml.*?\?>','',LOGO);LOGO=re.sub(r'<title>.*?</title>','',LOGO)
LOGO=re.sub(r'(<svg[^>]*?)\swidth="[^"]*"',r'\1',LOGO,count=1);LOGO=re.sub(r'(<svg[^>]*?)\sheight="[^"]*"',r'\1',LOGO,count=1).replace('<svg','<svg class="lg"',1)
CSS=open('canovaccio.py').read().split("CSS='''")[1].split("'''")[0]
for M,P in PROVE.items():
    b=f'''<div class="hd">{LOGO}<span class="hl">Scheda della prova · {M}</span></div>
<h1>Scheda della videolezione · {M}</h1><div class="bar"></div>
<p class="lead">Questa scheda dice <b>che cosa</b> deve contenere la sua videolezione di {M}. <b>Come</b> prepararla e registrarla è spiegato nelle Linee guida.</p>
<h2>Libri di riferimento</h2><ul>{''.join('<li>'+x+'</li>' for x in P['libri'])}</ul>
<h2>Argomenti della videolezione</h2><p>{P['argomenti']}</p>
<h2>Requisiti specifici di {M}</h2><ul>{''.join('<li>'+x+'</li>' for x in P['requisiti'])}</ul>
<div class="box"><b class="t">Diritti d'autore</b>Dai libri si prendono argomenti, regole e metodo. Slide, esempi, esercizi, quiz, test e ascolti sono <b>originali</b>, preparati da lei: non si riproducono pagine, immagini, esercizi o audio dei manuali.</div>
<h2>Che cosa ci consegna</h2><ol><li>Il testo della lezione nel modello Word (con esercizi, quiz di argomento, riepilogo e compiti a casa).</li><li>Il test finale nel modello Excel.</li><li>La Scheda di assegnazione dei compiti compilata.</li><li>La scheda della strumentazione (subito).</li><li>Dopo il nostro ok sulla prova tecnica di 1 minuto: la registrazione completa.</li></ol>
'''
    open('scheda_prova.html','w').write(f'<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}</body></html>')
    with sync_playwright() as p:
        br=p.chromium.launch();pg=br.new_page();pg.goto('file:///home/claude/docenti/scheda_prova.html');pg.wait_for_timeout(800)
        pg.pdf(path=f'/home/claude/invio/Scheda_della_prova_{M}.pdf',format='A4',print_background=True,margin=dict(top='16mm',bottom='18mm',left='15mm',right='15mm'));br.close()
print('ok')
