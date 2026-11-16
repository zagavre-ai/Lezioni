# Inglese AFM triennio · Lezione 10 · Work today

Tag: `afm-inglese-triennio-lez10` · una sola Parte · durata misurata **65:39** (3939.1 s) · docente 59:04 dopo i tagli delle pause (1,0 s → 0,6 s).
Video 1080p, x264 veryfast CRF 19, AAC 192k; 239.1 MiB; a pezzi da 90 MiB (`.parte_NN`) + `.sha256`.

## Come ricomporre il video
```
cat Inglese_Lez10_Parte1_1080p.mp4.parte_* > Inglese_Lez10_Parte1_1080p.mp4
sha256sum -c Inglese_Lez10_Parte1_1080p.mp4.sha256
```

## Struttura
- sigla, benvenuto (voce Kore, inglese B1), docente con slide sincronizzate e parole chiave tradotte in italiano;
- per ogni argomento: titolo, docente, mappa concettuale animata (voce Kore), scheda Quiz (5 domande, almeno 80%);
- mappa finale, saluto della docente, glossario (24 parole inglese/italiano), ripasso finale, verifica finale, sigla, compiti.
- `t_verifica` = 3915.464 s · `t_compiti` = 3928.664 s (bande blu su quiz, verifica e compiti).

## Argomenti (inizio nel video)
- 4:14 · 1. Today's job market
- 21:18 · 2. Job stability
- 34:38 · 3. Flexibility at work
- 47:18 · 4. Digital communication
- 56:25 · 5. Employability skills

## Controllo di sincronia (righe a caso, cosa si sente quando la riga si accende)

- 48:43.86 · argomento 4, slide 1, riga 3: «Information is transmitted instantaneously: it saves time and money and improves productiv» · si sente (da 1 s prima): «The main characteristic of digital communication is that information is transmitting»
- 31:05.23 · argomento 2, slide 2, riga 4: «Taxes and expenses to pay, and stress due to the constant search for new gigs.» · si sente (da 1 s prima): «another issue is to do with taxes and expenses because they since they»
- 55:33.44 · argomento 4, slide 3, riga 5: «Its name entered the English language: "I'll zoom you later", "Let's have a Zoom".» · si sente (da 1 s prima): «platforms. And its name has even entered the English language as a verb as well as a noun.»
- 61:21.40 · argomento 5, slide 3, riga 5: «Numeracy and IT skills: using data to support your work, IT skills like coding.» · si sente (da 1 s prima): «and developing possible solutions and finally numeracy and IT skills. This is to say using»
- 7:39.63 · argomento 1, slide 1, riga 4: «During recessions unemployment rises and wages are low; when unemployment drops, businesse» · si sente (da 1 s prima): «The job market clearly plays a very important role in the economy and it is all»
- 12:19.90 · argomento 1, slide 2, riga 1: «New in-demand professions: digitalisation and technology lead to a higher demand for IT jo» · si sente (da 1 s prima): «economy. So starting with the first point, we can say that the trend of digitalization»

## File
- `Mappe_afm-inglese-triennio-lez10.pdf`: mappe A4 orizzontale, una per pagina (una per argomento + mappa finale), stessa grafica del video.
- `quiz_argomenti.json`, `Quiz_Inglese_Lez10.txt`: quiz di fine argomento (da approvare).
- `scheda_pubblicazione.json`, `testo_youtube.txt`, sottotitoli `.vtt` della docente (italiano e inglese, come parla lei; corretti a mano dove la trascrizione automatica sbagliava).
