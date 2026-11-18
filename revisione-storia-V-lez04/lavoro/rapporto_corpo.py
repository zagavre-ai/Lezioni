# -*- coding: utf-8 -*-
# Sezioni 4-9 del rapporto (immagini mostrate, problemi, non verificato, come verificato, da confermare col prof)
import sys, os, json
sys.path.insert(0, '/tmp/claude-0/w')
from dati import *
W = '/tmp/claude-0/w'; OUT = W + '/out'
L = []
def A(*x): L.append(' '.join(str(i) for i in x))
TITLE = {4: 'Carta: i Balcani 1911–1913', 6: 'Foto: l’attentato di Sarajevo', 8: 'Carta: fronte occidentale 1914–1916', 9: 'Carta: fronte orientale e balcanico 1914',
         11: 'Vignetta «Sport… bellico 1914» (l’Italia contesa)', 13: 'Carta: fronte italiano 1915–1916', 14: 'Carta: fronte occidentale/orientale 1916',
         16: 'Carta: fronte mediorientale 1915–1916', 18: 'Carta: fronte italiano 1917 (Caporetto)', 21: 'Carta: l’Europa dopo la guerra (1920)', 23: 'Infografica numeri della Grande Guerra', 24: 'Grafico: perdite militari per Paese'}
A('## 4. Immagini e carte del prof mostrate (tabella immagine · Parte · minuto nel video)')
A('Le immagini sono quelle delle slide del prof (`LEZIONE 4.pdf`); compaiono quando il prof le mostra nel suo video (riconosciute confrontando i fotogrammi con le pagine del PDF) e restano finché le commenta. Risoluzione nativa del PDF (circa 800 px di larghezza): **ingrandite, quindi morbide** (limite del materiale).')
A('| immagine | Parte | argomento | da (min:s) | a (min:s) |\n|---|---|---|---|---|')
for P in (1, 2):
    tl = {n: (s, f / 30) for n, s, f in json.load(open(f'{OUT}/tl_P{P}.json'))['timeline']}
    for pos, n in enumerate(PARTI[P], 1):
        j = json.load(open(f'{W}/pieces/P{P}_T{n}.mp4.json')); base = tl[f'prof{pos + POFF[P]}'][0]; acc = 0
        for k, nn in j['runs']:
            d = nn / 10.0
            if k[0] == 'img':
                a = base + acc; b = a + d
                A(f"| {TITLE.get(int(k[1]), 'pagina ' + k[1])} (p. {k[1]} del PDF) | {P} | {POFF[P] + pos}. {ARG[n - 1]['nome']} | {int(a // 60)}:{int(a % 60):02d} | {int(b // 60)}:{int(b % 60):02d} |")
            acc += d
A('\nLe pagine 6 (foto dell’attentato) e 22–23 del PDF non vengono mostrate dal prof nel suo video: nel video nuovo non compaiono.\n')
A('## 5. Problemi trovati e correzioni (minuto = nel video originale del prof)')
A('| minuto (orig.) | tipo | com’era | correzione |\n|---|---|---|---|')
A('| 0:00–3:36 | visivo | titolo e presentazione su slide nera di PowerPoint, senza elenco degli argomenti | copertina nel modello (logo, «STORIA V · VIDEOLEZIONE», card «ARGOMENTI») col prof nel riquadro 4:3 |')
A('| tutto | visivo | prof in un riquadro 246×138 px nell’angolo, con logo del Centro e slide senza grafica del modello | ritaglio 4:3 centrato sul volto, ingrandito a 412×310 px con correzione immagine del kit, fascia gialla col nome, pannello «PAROLE CHIAVE» |')
A('| tutto | visivo | slide del prof lunghe (5 paragrafi di 3–4 righe) senza evidenziazione | slide rifatte dal testo del PDF, card della frase in corso evidenziata (da parole-guida del parlato, controllo a campione ±1,5 s) |')
A('| 1:00:19–1:04:40 e 1:15:10–1:17:50 | visivo | il prof parla di un argomento mentre la slide mostrata è quella di un altro (es. «guerra totale» a slide delle battaglie; genocidio degli armeni a slide «guerra totale») | il video mostra la slide dell’argomento di cui si parla; durante l’inciso sul genocidio degli armeni compare la slide «La guerra totale» |')
A('| 0:08:34, 0:08:48, 0:18:29, 0:30:33, 1:43:21 | audio | 5 pause del prof > 3 s (3,1–4,1 s) | ridotte a 1,6 s (tagli solo in pausa, mai dentro una frase) |')
A('| tutto | audio | parlato a livello variabile, rumore di fondo | catena del kit: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter` dall’originale |')
A('| sottotitoli | testo | trascrizione automatica con errori sui nomi (es. «Salievo», «Tirpiz», «Asazia e Lorena», «millovecentotto», «la cina» per «la cartina») | corretti ~100 errori certi su nomi e date (elenco in `corr.py`); il parlato non è stato riscritto |')
A('')
A('## 6. DA CONFERMARE COL PROF')
A('- 1:35:28 circa: «l’imperatore **Carlo II**» → l’ultimo imperatore d’Austria-Ungheria è Carlo **I** (IV d’Ungheria). Nel sottotitolo ho lasciato quello che dice il prof.')
A('- 1:43:06 circa: riparazioni «**132 mila miliardi** di marchi oro» → la cifra corretta è 132 **miliardi**. Lasciato come detto.')
A('- 0:59:41 circa: «Vittorio Emanuele **II**» detto/trascritto per il sovrano del 1915 (è Vittorio Emanuele **III**): nel sottotitolo corretto in III.')
A('- 1:35:37 circa: le slide e la mappa danno «armistizio (4 novembre 1918)»; il prof dice «firmato il 3 novembre, in vigore il 4»: coerente, nessuna correzione.')
A('- 1:15:43 circa, Lusitania: il prof dice «oltre 100 cittadini statunitensi», la cifra storica è 128: lasciato come detto.\n')
A('## 7. Cosa NON ho verificato')
A('- **Ascolto umano:** nessun passaggio è stato riascoltato da una persona; le misure di tempi e livelli sono automatiche.')
A('- **Sincronia delle card:** la card in corso è scelta da parole-guida nel parlato; controllata a campione su 6 punti, non su tutta la lezione. Dove il prof parla di argomenti non presenti sulla slide la card resta quella dell’ultimo punto trattato.')
A('- **Voci Kore:** pronuncia di nomi e termini (Tirpitz, Schlieffen, Sarajevo, Versailles…) da ascoltare.')
A('- **Testa del prof:** nell’originale la webcam è 246×138 px: ingrandita ~2,2× resta morbida; quando il prof si china in avanti la testa tocca il bordo alto del riquadro (limite dell’originale, non risolvibile).')
A('- **Sottotitoli:** corretti nomi, date e termini certi; ci sono ancora frasi spezzate del parlato libero del prof («Sclamo pure…», «gli schiamenti») che richiedono un riascolto.')
A('- **Quiz e verifica:** domande dal materiale del prof (slide, mappe); la verifica finale è l’Excel del prof, non modificato.')
A('')
A('## 8. Come ho verificato')
A('- Trascrizione completa con tempi parola per parola (`kit/tools/trascrivi.py`, Parakeet TDT, 1026 segmenti) e rilettura integrale del testo.')
A('- Riconoscimento della slide mostrata dal prof: confronto di 1 fotogramma/s con le 24 pagine del PDF (distanza media su miniature 160×118); verifica a vista su 29 fotogrammi.')
A('- Misure sul video finale: ffprobe (durata, fotogrammi), ffmpeg `ebur128` (LUFS, picco), `silencedetect`, `freezedetect` sul riquadro del prof, correlazione dei jingle Quiz, sha256.')
open(OUT + '/rapporto_corpo.md', 'w').write('\n'.join(L) + '\n')
print('corpo ok')
