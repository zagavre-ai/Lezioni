# -*- coding: utf-8 -*-
import sys,os,json
sys.path.insert(0,'/tmp/claude-0/l06')
from dati import *
W='/tmp/claude-0/l06';OUT=W+'/out'
rd=lambda f:open(f).read() if os.path.exists(f) else ''
L=[];A=lambda *x:L.append(' '.join(str(i) for i in x))
tl={n:(s,f/30) for n,s,f in json.load(open(f'{OUT}/tl_P1.json'))['timeline']}
c=rd(f'{OUT}/controlli_P1.txt')
A('# RAPPORTO DI REVISIONE · Storia V · Lezione 6 · Il primo dopoguerra (1919-1925) (prof. Giorgio Mazzotti)')
A('Chat «revisione v3» (18/11/2026). Etichette: **misurato** = misura sul file finale; **stima**; **non verificato**.\n')
A('## 0. Punto di partenza')
A('- Lezione rifatta **da zero** nel modello Spagnolo dal video originale del prof (`LEZIONE 6 ... .mp4`, 1092×614, 39 min 37 s), dalle slide (`LEZIONE 6.pdf`, 11 pagine), dal test e dai compiti. Le voci del 15-16/11 erano di un montaggio vecchio e non sono state riusate: **58 voci Kore nuove** (ramo `voci-storia-V-lez06`), tutte ricevute.')
A('- **Mappe:** per la lezione 6 il prof non ha mappe. Le 8 mappe (una per argomento) sono costruite dalle intestazioni e dal testo delle sue card, senza aggiungere contenuti.')
A('- **Una sola Parte**, 55:07. Otto argomenti, uno per slide di testo del prof (l’argomento 7 ha 3 card, gli altri 4).')
A('- Ordine degli argomenti = ordine del parlato. Nell’argomento 2 il prof parla di Jugoslavia, Polonia, Ungheria, Austria: le card sono evidenziate in quest’ordine.')
A('## 1. Misure sul video nuovo'); A(c.split('| pezzo |')[0].strip()); A('')
A('## 2. Confronto con Spagnolo Lez. 1'); A(rd(OUT+'/confronto.md')); A('')
A('## 3. Tabella dei pezzi (presente · minuto · durata misurata)'); A('| pezzo |'+c.split('| pezzo |',1)[1].split('\nfoglio')[0].strip() if '| pezzo |' in c else '(non disponibile)'); A('')
A('## 4. Immagini e carte del prof mostrate')
TT={4:'Carta/immagini del prof',9:'Carta/immagini del prof'}
A('| immagine | argomento | da | a |\n|---|---|---|---|')
for n in PARTI[1]:
    j=json.load(open(f'{W}/pieces/P1_T{n}.mp4.json'));base=tl[f'prof{n}'][0];acc=0
    for k,nn in j['runs']:
        d=nn/10.0
        if k[0]=='img':
            a=base+acc;b=a+d;A(f"| {TT.get(int(k[1]),'p. '+k[1])} (p. {k[1]}) | {n}. {ARG[n-1]['nome']} | {int(a//60)}:{int(a%60):02d} | {int(b//60)}:{int(b%60):02d} |")
        acc+=d
A('Immagini a risoluzione nativa del PDF, ingrandite: morbide (limite del materiale).\n')
A('## 5. Problemi trovati e correzioni')
A('| tipo | com’era | correzione |\n|---|---|---|')
A('| visivo | slide nere/bianche di PowerPoint con webcam 246×138 px | modello Spagnolo: riquadro 4:3, fascia gialla, pannello «PAROLE CHIAVE», card in corso evidenziata dal parlato |')
A('| audio | livello variabile e rumore | catena del kit dall’originale: −16,0 LUFS misurato |')
A('| testo | trascrizione con errori sui nomi («Abrizar», «Balfur», «Pizzucsky», «Rur», «Puc di Monaco», «Goming Ta», «Shankai Shek»…) | ~35 correzioni certe nei sottotitoli |')
A('| audio | pause del prof > 3 s | ridotte a 1,6 s (solo in pausa) |')
A('| struttura | slide in ordine diverso dal parlato | mostrata la slide di ciò di cui si parla |\n')
A('## 6. DA CONFERMARE COL PROF')
A('- ~0:33:00: nel parlato il prof dà alla Cina la rottura dell’alleanza Guomintang-comunisti nel **1927**, la slide dice **1926**: nel quiz ho seguito la slide. Da confermare.')
A('- ~0:27:00: il prof parla di «grandi scioperi industriali del 1925», la slide dice «scioperi dei minatori del 1926»: nel quiz ho seguito la slide.')
A('- «Rif» in Marocco, «Piłsudski» e «Horthy» corretti nei sottotitoli dal contesto; da riascoltare.\n')
A('## 7. Cosa NON ho verificato')
A('- Ascolto umano; pronuncia delle voci Kore (le voci **BEN, MAPN2, MAPN6, MAPN7, MAPN8, GL8** sono segnate «DA CONTROLLARE» dalla master); sincronia delle card controllata a campione; frasi del parlato libero nei sottotitoli da riascoltare.')
A('- Il glossario dura 91 s (la scheda tecnica indica 40–70 s): 8 termini; le mappe durano 30–41 s.')
A('- Testa del prof: sorgente piccola, ingrandita 2,2×.\n')
A('## 8. Come ho verificato')
A('- Trascrizione parola per parola (Parakeet), rilettura integrale; riconoscimento slide mostrata (1 fotogramma/s vs 16 pagine); ffprobe/ebur128/silencedetect/freezedetect/correlazione jingle/sha256 sul file finale.')
open(OUT+'/RAPPORTO_REVISIONE.md','w').write('\n'.join(L)+'\n');print('ok')
