# -*- coding: utf-8 -*-
import sys,os,json
sys.path.insert(0,'/tmp/claude-0/l17')
from dati import *
W='/tmp/claude-0/l17';OUT=W+'/out'
rd=lambda f:open(f).read() if os.path.exists(f) else ''
L=[];A=lambda *x:L.append(' '.join(str(i) for i in x))
A('# RAPPORTO DI REVISIONE · Storia V · Lezione 17 · Le fasi conclusive della Guerra fredda (1969-1991) (prof. Giorgio Mazzotti)')
A('Chat «revisione v3» (19/11/2026). Etichette: **misurato** = misura sul file finale; **stima**; **non verificato**.\n')
A('## 0. Punto di partenza')
A('- Esisteva una consegna del 14/11 con le regole vecchie (`consegna-storia-V-lez17`, 3 Parti da circa 51 min). Rifatta **da zero** nel modello Spagnolo dal video originale del prof (`LEZIONE.17.LE.FASI.CONCLUSIVE.DELLA.GUERRA.FREDDA.1969-1991.mp4`, 1092×614, 102 min 10 s), dalle slide (`LEZIONE 17.pdf`, 17 pagine), dalle sue mappe, dal test e dai compiti. Le voci del 14/11 (ramo `voci-storia-V-lez17`, nomi AN*) erano di un montaggio vecchio e non sono state riusate: **59 voci Kore nuove**, tutte ricevute.')
A('- **Mappe:** il prof ha 3 mappe (Kippur, neoliberismo, Gorbačev): messe dopo gli argomenti 1, 6 e 7. Per gli altri 5 argomenti le mappe sono costruite dalle intestazioni e dal testo delle sue card, senza aggiungere contenuti.')
A('- **Tre Parti** divise alla fine di un argomento: Parte 1 = argomenti 1–3, Parte 2 = argomenti 4–5, Parte 3 = argomenti 6–8. Argomento 1 = slide p. 2, ecc.: un argomento per ogni slide di testo del prof.')
A('- Webcam del prof: riquadro 4:3 (412×310 a x 1428, y 148, angoli arrotondati, ombra, hqdn3d 1.5:1.5:3:3, eq, cas 0,35), come da decisione di Sara del 18/11; la sorgente è piccola (246×138 px) e resta morbida: è il limite del materiale.\n')
for P in sorted(PARTI):
    c=rd(f'{OUT}/controlli_P{P}.txt')
    tl={n:(s,f/30) for n,s,f in json.load(open(f'{OUT}/tl_P{P}.json'))['timeline']}
    A(f'## 1.{P} Misure sul video · Parte {P}'); A(c.split('| pezzo |')[0].strip()); A('')
    A(f'## 3.{P} Tabella dei pezzi · Parte {P} (presente · minuto · durata misurata)'); A('| pezzo |'+c.split('| pezzo |',1)[1].split('\nfoglio')[0].strip() if '| pezzo |' in c else '(non disponibile)'); A('')
A('## 2. Confronto con Spagnolo Lez. 1'); A(rd(OUT+'/confronto.md')); A('')
A('## 4. Immagini e carte del prof mostrate')
A('| immagine | argomento | Parte | da | a |\n|---|---|---|---|---|')
for P in sorted(PARTI):
    tl={n:(s,f/30) for n,s,f in json.load(open(f'{OUT}/tl_P{P}.json'))['timeline']}
    for pos,n in enumerate(PARTI[P],1):
        j=json.load(open(f'{W}/pieces/P{P}_T{n}.mp4.json'));base=tl[f'prof{pos+POFF[P]}'][0];acc=0
        for k,nn in j['runs']:
            d=nn/10.0
            if k[0]=='img':
                a=base+acc;b=a+d;A(f"| p. {k[1]} | {n}. {ARG[n-1]['nome']} | {P} | {int(a//60)}:{int(a%60):02d} | {int(b//60)}:{int(b%60):02d} |")
            acc+=d
A('Immagini a risoluzione nativa del PDF, ingrandite: morbide (limite del materiale).\n')
A('## 5. Problemi trovati e correzioni')
A('| tipo | com’era | correzione |\n|---|---|---|')
A('| visivo | slide nere/bianche di PowerPoint con webcam piccola | modello Spagnolo: riquadro 4:3, fascia gialla, pannello «PAROLE CHIAVE», card in corso evidenziata dal parlato |')
A('| audio | livello variabile e rumore | catena del kit dall’originale: −16,0 LUFS misurato |')
A('| testo | trascrizione con errori sui nomi («Briesnev», «Gorbachev», «Comeini», «Tien Amen», «Pinocchio», «Bete Woods»…) | ~25 correzioni certe nei sottotitoli |')
A('| audio | pause del prof > 3 s | ridotte a 1,6 s (solo in pausa) |')
A('| struttura | l’argomento 5 (America Latina) è detto dopo Reagan, torna indietro («torniamo un attimo indietro») | seguito l’ordine del parlato |')
A('| mappe | in tre argomenti la mappa è del prof | per gli altri cinque costruite dalle slide, senza inventare contenuti |\n')
A('## 6. DA CONFERMARE COL PROF')
A('- Fonte 6:14 (circa 0:04 dell’argomento 1): la trascrizione riporta «…come molti ricorderanno Vittorio Emanuele II solo per il fascismo»; probabile errore di riconoscimento in una digressione. Da riascoltare; nei sottotitoli la frase resta com’è stata riconosciuta.')
A('- Date dette a voce coincidono con le slide (1971 Bretton Woods, 1973 Kippur, 1978 Camp David, 1979 Iran, 1989 Muro). Dove il prof dice «Reagan 1981-1989» la mappa del prof scrive 1981-1988: nella voce della mappa ho seguito la mappa.\n')
A('- **Parte 2, misurato:** un fermo del riquadro del prof di 1,1 s (a 26:28) dentro «America Latina»: è una pausa naturale del prof nella sorgente (tra «Come dire, ehm» e «la giunta di Pinochet», fonte 4019,5 s), non un difetto di montaggio; lasciato com’è (pausa < 3 s).\n')
A('## 7. Cosa NON ho verificato')
A('- Ascolto umano; pronuncia delle voci Kore (la voce **SC4_3** è segnata «DA CONTROLLARE» dalla master); sincronia delle card controllata a campione; frasi del parlato libero nei sottotitoli da riascoltare.')
A('- Il glossario dura circa 60–90 s a Parte (scheda tecnica 40–70 s).')
A('- Testa del prof: sorgente piccola, ingrandita 2,2×.\n')
A('## 8. Come ho verificato')
A('- Trascrizione parola per parola (Parakeet), rilettura; riconoscimento slide mostrata (1 fotogramma/s vs 17 pagine); ffprobe/ebur128/silencedetect/freezedetect/correlazione jingle/sha256 sul file finale di ogni Parte.')
open(OUT+'/RAPPORTO_REVISIONE.md','w').write('\n'.join(L)+'\n');print('ok')
