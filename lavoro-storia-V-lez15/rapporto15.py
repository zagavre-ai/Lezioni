# -*- coding: utf-8 -*-
import sys,os,json
sys.path.insert(0,'/tmp/claude-0/l15')
from dati import *
W='/tmp/claude-0/l15';OUT=W+'/out'
rd=lambda f:open(f).read() if os.path.exists(f) else ''
L=[];A=lambda *x:L.append(' '.join(str(i) for i in x))
tl={n:(s,f/30) for n,s,f in json.load(open(f'{OUT}/tl_P1.json'))['timeline']}
c=rd(f'{OUT}/controlli_P1.txt')
A('# RAPPORTO DI REVISIONE · Storia V · Lezione 15 · La decolonizzazione (1945-1975) (prof. Giorgio Mazzotti)')
A('Chat «revisione v3» (18/11/2026). Etichette: **misurato** = misura sul file finale; **stima**; **non verificato**.\n')
A('## 0. Punto di partenza')
A('- Nessuna consegna precedente (nessun ramo `consegna-storia-V-lez15`): lezione rifatta **da zero** nel modello Spagnolo dal video originale del prof (`LEZIONE 15 LA DECOLONIZZAZIONE (1945-1975).mp4`, 1092×614, 42 min 20 s), dalle slide (`LEZIONE 15.pdf`, 16 pagine), dal test e dai compiti. Le 25 voci del 16/11 erano di un montaggio vecchio e non sono state riusate: **71 voci Kore nuove** (ramo `voci-storia-V-lez15`), tutte ricevute.')
A('- **Mappe:** la mappa del prof per la lezione 15 **non esiste** (come da indice). Le 10 mappe (una per argomento) sono costruite dalle intestazioni e dal testo delle sue card, senza aggiungere contenuti.')
A('- **Una sola Parte**, 60:04 (la regola dell’8/11 ammette fino a circa 65 min in una Parte). Dieci argomenti, uno per slide di testo del prof.')
A('- Ordine degli argomenti = ordine del parlato; «Le premesse» ecc. seguono le slide. Durante «L’Africa subsahariana» il prof torna alle colonie portoghesi (card di «Apartheid», mostrata) e alla carta del Nord Africa (mostrata con l’etichetta dell’argomento 5).\n')
A('## 1. Misure sul video nuovo'); A(c.split('| pezzo |')[0].strip()); A('')
A('## 2. Confronto con Spagnolo Lez. 1'); A(rd(OUT+'/confronto.md')); A('')
A('## 3. Tabella dei pezzi (presente · minuto · durata misurata)'); A('| pezzo |'+c.split('| pezzo |',1)[1].split('\nfoglio')[0].strip() if '| pezzo |' in c else '(non disponibile)'); A('')
A('## 4. Immagini e carte del prof mostrate')
TT={6:'Carta/immagini: Indocina e Sud-Est asiatico',8:'Carta: Africa del Nord',11:'Carta: l’Africa coloniale e indipendente',13:'Carta: Palestina (piano ONU)',15:'Carta: Canale di Suez'}
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
A('| testo | trascrizione con errori sui nomi («Seylon», «Gana», «Yen Bien plus», «Jaharlal Neru», «Geddafi», «Gamad Hab / Hel nascer»…) | ~30 correzioni certe nei sottotitoli |')
A('| audio | pause del prof > 3 s | ridotte a 1,6 s (solo in pausa) |')
A('| struttura | slide in ordine diverso dal parlato | mostrata la slide di ciò di cui si parla |\n')
A('## 6. DA CONFERMARE COL PROF')
A('- ~0:30:34: «la Somalia passa sotto i francesi» (trascrizione incerta): dopo il 1947 la Somalia italiana fu in amministrazione fiduciaria italiana; da riascoltare.')
A('- ~0:38:10: «dall’altra parte c’è l’Arabia Saudita» a proposito del Sinai/Suez: probabilmente Israele; da riascoltare.')
A('- «Zaire» e altre date dette a voce coincidono con le slide (1951 Libia, 1956 Marocco e Tunisia, 1962 Algeria, 1960 «anno dell’Africa»).\n')
A('## 7. Cosa NON ho verificato')
A('- Ascolto umano; pronuncia delle voci Kore (la voce **MAPN4** «Asia e Indocina» è segnata «DA CONTROLLARE» dalla master: 11 parole diverse dal testo); sincronia delle card controllata a campione; frasi del parlato libero nei sottotitoli da riascoltare.')
A('- Il glossario dura 94 s (la scheda tecnica indica 40–70 s): 8 termini; le mappe durano 24–30 s.')
A('- Testa del prof: sorgente piccola, ingrandita 2,2×.\n')
A('## 8. Come ho verificato')
A('- Trascrizione parola per parola (Parakeet), rilettura integrale; riconoscimento slide mostrata (1 fotogramma/s vs 16 pagine); ffprobe/ebur128/silencedetect/freezedetect/correlazione jingle/sha256 sul file finale.')
open(OUT+'/RAPPORTO_REVISIONE.md','w').write('\n'.join(L)+'\n');print('ok')
