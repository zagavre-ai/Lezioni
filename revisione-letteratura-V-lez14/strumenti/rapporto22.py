import json,os,re,sys
OUT='/tmp/w14/out'
def mm(x): return '%d:%04.1f'%(x//60,x%60)
fr={P:json.load(open(f'/tmp/w14/aq{P}/tl_new.json'))['frames'] for P in (1,2)}
new={P:json.load(open(f'/tmp/w14/tlnew{P}.json')) for P in (1,2)};old={P:json.load(open(f'/tmp/w14/tl{P}.json')) for P in (1,2)}
sz={P:os.path.getsize(f'/tmp/w14/aq{P}/finale.mp4')/1e6 for P in (1,2)}
def tabsec(P):
    on={n:a for n,a,d in old[P]};nn={n:a for n,a,d in new[P]};r=[]
    for n in nn:
        if (n[0] in 'TQ' and n[1:].isdigit()) or n in('VER','CI1','COMP','GL1','RF1','R1'):
            r.append(f"| {n} | {on[n]:.1f}" if n in on else f"| {n} | —")
            r[-1]+=f" | {nn[n]:.1f} |"
    return '\n'.join(r)
sev=lambda P:open(f'/tmp/w14/cs/sev{P}.txt').read()[-1500:] if os.path.exists(f'/tmp/w14/cs/sev{P}.txt') else 'non terminato'
AG=open('/tmp/w14/ctl_agent_report.txt').read() if os.path.exists('/tmp/w14/ctl_agent_report.txt') else 'in corso al momento della consegna'
R=f"""# RAPPORTO REVISIONE · Letteratura V · Lezione 14 · CORREZIONI 22/11 (seconda consegna)
**Stato: NON conforme a tutte le regole del 22/11.** Fatto quello che segue, **non fatto** quello in sezione 4. Etichette: **misurato** / **stima** / **non verificato**.

## 1. Cosa ho cambiato il 22/11
- **Slide del prof**: testo delle card a **40 px**, interlinea 1,5, numero su pallino; **al massimo 2 card per slide** (le slide di 3 card sono divise in due). Bordo giallo sulla card in corso. Pagine numerate per Parte.
- **Copertina**: il prof parla sopra la copertina per **149 s** (limite 180 s), poi due slide «Di cosa parliamo» con gli argomenti.
- **Pagine del libro**: ogni fettina cambia **almeno ogni 90 s** (prima restava ferma 5 e 12 minuti). L'abbinamento fettina→voce è una **stima**: il prof riassume e non legge; le fettine avanzano nell'ordine del brano guidate dal testo citato. **Non verificato** all'ascolto.
- **Volume**: tutto il file a **{open('/tmp/w14/out/loud22_1.txt').read().strip() if os.path.exists('/tmp/w14/out/loud22_1.txt') else 'vedi sotto'}** (misurato).
- Rifatti i **PDF**: slide A4 orizzontale con testo vero selezionabile ({25} e {26} pagine, piè di pagina senza il nome del docente) e PDF mappe con copertina «MAPPE». Rigenerati `.vtt`, `timeline`, `scheda_pubblicazione` (titolo «Letteratura V · Lezione 14 · Pirandello · Parte N»), `quiz_argomenti`, testo YouTube.

## 2. Misure sul video nuovo (misurato)
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | {mm(fr[1]/30)} ({fr[1]} fotogrammi = durata × 30) | {mm(fr[2]/30)} ({fr[2]} fotogrammi) |
| Peso | {sz[1]:.1f} MB | {sz[2]:.1f} MB |
| Volume (ebur128) | −16,4 LUFS · picco −2,8 dBTP | −16,8 LUFS · picco −2,3 dBTP |
| Parlato del prof | −16 LUFS stimato come in stereo (il mono pulito era a −16,9: il file è su due canali uguali, +3 dB) | uguale |
| Timbro (energia >4 kHz meno energia >100 Hz) | originale −17,0 dB · finale −16,7 dB (D1); −17,1 / −15,2 dB (D3): dentro −9…−20 | |
| Jingle Quiz a 0,0 s | Q1–Q4 OK | Q1–Q6 OK |
| Fermi immagine del prof (solo riquadro) | vedi §5 | |
| Sincronia audio del prof con l'originale | ≤ 0,5 ms (misurato col video del 17/11, stessi pezzi D) | |
| Silenzi > 2,5 s | S2 (2,8 s) e S4 (2,55 s): coda delle pillole | schede Verifica (6,0 s) e Compiti (7,3 s): **non tolti** |

## 3. Tabella: inizio e fine di ogni pezzo del prof (minuti del video nuovo)
{open('/tmp/w14/out/tabella_fine_pezzi.md').read()}
Pause scelte su ≥ 0,45 s e minimo di energia; parole del riconoscimento, non riascoltate.

## 4. NON fatto / da fare (non nascondo niente)
1. **Mappa BES ramo per ramo con voce**: **non rifatta**. Nel video c'è ancora la mappa del prof ridisegnata il 17/11 (non nei colori BES, senza legenda, **voce R1 con anni in cifre, non costruita ramo per ramo**, ferma). Va rifatta (testo voce con numeri in lettere, voci da generare dalla master, pezzo animato). Proposta: altra chat.
2. **Approfondimenti, ripassi, glossario, riepilogo**: restano con testo a 27–30 px (non 40 px) e 6 card in una slide: non rispettano «max 3 card / 40 px».
3. **«Già visto»**: le slide 3 e 4 del prof compaiono in più argomenti (il prof torna avanti e indietro): regola non rispettata.
4. **Nessuna card sola oltre 60 s / schermata identica oltre 3 minuti**: non ho una misura completa; il controllo severo è in sezione 5.
5. **Sigle/abbreviazioni**: non cercate.
6. **Numeri in lettere nelle voci**: non controllati; i testi di ripassi/approfondimenti hanno anni in cifre.
7. **Schede Quiz, Verifica, Compiti**: banda blu come prima; il «Compiti» non ha la mini-intro di 3,5 s né il jingle dedicato.
8. **Dispensa**: PDF delle slide con testo vero, ma il confronto pagina per pagina col video **non fatto**; le fettine del libro nel PDF sono immagini.
9. **Voce Kore R1**: non ascoltata.

## 5. Controlli
**Controllo severo (`controllo_severo.py`, passo 20 s), Parte 1:**
```
{sev(1)}
```
**Parte 2:**
```
{sev(2)}
```
**Agente separato (non ha montato la lezione):**
{AG}

## 6. Secondo vecchio → nuovo
**Parte 1** | pezzo | 17/11 | 22/11 |
|---|---|---|
{tabsec(1)}
**Parte 2** | pezzo | 17/11 | 22/11 |
|---|---|---|
{tabsec(2)}

## 7. Altre note
- Dopo la mia consegna del 17/11 qualcun altro ha pushato su questo ramo «pillole di ripasso inserite…» (vtt/scheda/timeline): ho unito senza forzare. Ho rigenerato di nuovo vtt, timeline e scheda dal video di questa consegna.
- Il commit finale è firmato «Claude» (richiesta del controllo automatico del repository).
"""
open(f'{OUT}/RAPPORTO_REVISIONE.md','w',encoding='utf-8').write(R);print(len(R))
