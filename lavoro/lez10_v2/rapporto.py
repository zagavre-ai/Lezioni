# RAPPORTO_REVISIONE.md della v2 (modello Spagnolo). uso: rapporto.py CARTELLA TAG "Titolo" N VIDEO.mp4 timeline.json n_pagine_pdf durata_docente_originale_s
import sys,os,json,subprocess
W,TAG,TIT,N,V,TLF,NP,DOC=sys.argv[1:9];os.chdir(W)
d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V],capture_output=True,text=True).stdout)
mm=lambda x:'%d:%04.1f'%(x//60,x%60)
cf=open('controllo_finale.log').read().strip().splitlines() if os.path.exists('controllo_finale.log') else []
cj=open('controllo_jingle.log').read().strip().splitlines() if os.path.exists('controllo_jingle.log') else []
sy=open('sincronia.txt').read().strip()
L=f'''# RAPPORTO DI REVISIONE · Inglese AFM triennio · Lezione {N} · {TIT} · v2

Tag `{TAG}` · chat della master E1 · 16/11/2026 · prof.ssa Maria Vittoria Fontanesi.
La v1 (consegnata la mattina del 16/11) non rispettava lo STOP QUALITÀ e il modello grafico Spagnolo Lez. 1 (decisioni di Sara del 16/11): questa v2 la **sostituisce sullo stesso ramo**. Stesse voci Kore, stessi testi, stessi quiz.

**Misurato:** durata {mm(d)} ({d:.1f} s); prof {mm(float(DOC))} **intero, senza nessun taglio** (nella v1 le pause oltre 1 s erano accorciate a 0,6 s).

## Confronto con il modello Spagnolo (punto 000, 1–11)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla della materia 15 s → dissolvenza → copertina | OK · `Sigla_Inglese_15s`; **tutte** le transizioni del video sono dissolvenze morbide di 1 s (nella v1 c'erano cerchi, tendine e zoom) |
| 2 | Copertina: logo, «INGLESE · VIDEOLEZIONE», titolo + barretta, card ARGOMENTI su due colonne | corretto (nella v1 era una scheda blu notte). Sulla copertina c'è la voce Kore di benvenuto, il prof non parla: copertina senza riquadro, come le «slide senza prof» |
| 3 | Slide: fondo bianco, riga «0N · ARGOMENTO», titolo Bricolage 800 + barretta, card, giallo solo sulla riga in corso | corretto (nella v1 fondo grigio chiaro #F4F7FB) |
| 4 | Piè di pagina «INGLESE · Prof.ssa Maria Vittoria Fontanesi» + «Pagina N», mai il numero della lezione | corretto (nella v1 mancava «Pagina N») |
| 5 | Riquadro prof 4:3 410×308 in x 1428 y 146, angoli arrotondati, ombra grigia morbida, testa intera, correzione immagine del kit | corretto (v1: 416×312) · correzione `eq contrast 1,04 saturation 1,03, hqdn3d 1.5:1.5:3:3, cas 0,35` sul riquadro rimpicciolito · testa e spalle intere: controllato sul foglio `controllo_minuti.jpg` |
| 6 | Fascia gialla inclinata, due righe «Maria Vittoria Fontanesi» / «PROF.SSA DI INGLESE», sempre visibile col prof | corretto (nella v1 tre righe con il corso) |
| 7 | Slide senza prof (titoli degli argomenti, glossario, ripasso finale): testo grande, logo, piè di pagina | corretto |
| 8 | Font solo Bricolage Grotesque / Figtree / DM Mono | OK per Bricolage e Figtree; DM Mono non è nel kit (`kit/tools/mappa_font`): le etichette sono in Figtree bold spaziato, come nella v1. Nessun altro font |
| 9 | Finale `Sigla_finale_5s_con_avviso_diritti.mp4` | corretto (nella v1 la vecchia sigla di chiusura, prima dei compiti); ora è l'ultimo pezzo |
| 10 | Struttura: sigla → presentazione con voce → per argomento: titolo, prof con slide sincronizzate, pillola di ripasso (mappa animata con voce Kore), quiz di 5 domande → glossario → riepilogo finale → finale | OK · in più: mappa finale e saluto della prof prima del glossario; schede «Verifica finale» e «Compiti» (servono alla pagina interattiva) prima del finale. Durata {mm(d)}: sopra i 60 minuti perché la registrazione della prof è una sola e il prof non si taglia (precedente: lez05 69 min, una Parte) |
| 11 | PDF A4 orizzontale: slide identiche al video senza riquadro e senza fascia; mappe | `{TAG}_slide.pdf`: {NP} pagine, una per slide, stesso ordine e stessa «Pagina N» del video (fatte dagli stessi file HTML, solo senza riquadro e fascia) · mappe: `Mappe_{TAG}.pdf`. Per Inglese AFM nella release **non ci sono mappe della prof**: le mappe sono quelle della lezione (contenuto preso solo dal materiale della prof) |

## Problemi trovati nella v1 e correzioni
| Minuto (v1) | Tipo | Com'era | Come è ora |
|---|---|---|---|
| tutta la lezione | audio | pause del prof oltre 1 s accorciate (prof tagliato) | prof intero, nessun taglio |
| tutta la lezione | audio | solo guadagno + limitatore | catena del kit: `aresample 48k, highpass 80, arnndn (sh.rnnn del kit), loudnorm −16, alimiter` |
| tutta la lezione | visivo | fondo grigio chiaro, riquadro 416×312, fascia su tre righe, niente «Pagina N» | modello Spagnolo (punti 3–6) |
| inizio | visivo | copertina blu notte | copertina bianca con card ARGOMENTI |
| titoli degli argomenti | visivo | schede blu notte | slide bianche con «0N · Topic N» |
| transizioni | visivo | cerchi, tendine, zoom | dissolvenze di 1 s |
| fine | visivo | vecchia sigla di chiusura prima dei compiti | finale 5 s con avviso dei diritti, in fondo |
| consegna | pagina | mancava il PDF delle slide | `{TAG}_slide.pdf` |

## Controlli fatti (misurati)
''' + '\n'.join('- '+x for x in cf if x.strip()) + '''

Scatto dei quiz (correlazione con il jingle):
''' + '\n'.join('- '+x for x in cj if x.strip()) + f'''

Sincronia slide–prof, 6 righe a caso (che cosa si sente quando la riga si accende):
{sy}

## Cosa NON ho potuto verificare
- Ascolto a orecchio: la verifica dell'audio è con le misure (volume, scatto dei quiz) e con la trascrizione automatica, non con l'ascolto umano.
- OCR delle slide: i testi delle slide sono generati da file di testo controllati (stesso testo dei PDF), non riletti con l'OCR.
- **Verifica finale:** nella release manca l'Excel della prof (`ENG_Amministrazione_Lez{int(N):02d}_Verifica.xlsx`): nel ramo c'è un test `PROPOSTA_DA_VALIDARE`.
- **COMPITI_MANCANTI:** nella release manca il PDF dei compiti della prof.
'''
open('RAPPORTO_REVISIONE.md','w').write(L);print('RAPPORTO_REVISIONE.md',len(L))
