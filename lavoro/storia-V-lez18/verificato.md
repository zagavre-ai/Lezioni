**Verificato con misure (script e controlli nel ramo di lavoro; quattro controlli separati di un agente che non ha montato la lezione):**
- Fotogrammi = durata × 30, 1920×1080, peso < 400 MB, −16 LUFS ±1, picco ≤ −1 dBTP, nessuna pausa > 2,5 s (le schede quiz e compiti hanno un sottofondo morbido), timbro del prof dentro −9…−20 dB (6 campioni per Parte; l'originale è già a −19…−22 dB, la pulizia aggiunge un leggero schiarimento).
- `controllo_severo.py` della master: esito OK su entrambe le Parti (nessuna slide o schermata identica oltre 3 min, nessuna card sola oltre 60 s, nessuna card con «…», copertina intera, intro sulla copertina 112 s).
- `controllo_finale.py` del kit: fotogrammi, peso, scatto quiz a 0,0 s, nessun fermo del prof.
- Tagli del prof: tutti in pausa (livello nel taglio sotto −42 dB) e a frase intera (tabella al §2); card: 208 card confrontate con la trascrizione e con il video a 5 fotogrammi/s (card accesa entro ±1,5 s dall'inizio della frase salvo poche eccezioni elencate sotto).
- Sigle rispiegate a schermo (quiz, schemi, glossario, approfondimenti, titoli, mappe); numeri in cifre a schermo; nome del prof solo nella fascia gialla; piè di pagina senza nome; dispensa = video (stesso ordine e numeri di pagina) con strato di testo invisibile; PDF mappe con copertina «MAPPE»; verifica finale = Excel del prof; compiti = quelli del prof.

**NON verificato / difetti noti (da guardare):**
- **Voci Kore:** non ho potuto ascoltare nulla; le voci nuove erano provvisorie fino al loro arrivo (vedi stato delle voci in testa). Pronuncia dei nomi stranieri e latini, trascrizione e bordi vanno controllati a ogni voce.
- Sincronia labbra/voce: l'audio del prof è tagliato con gli stessi campioni del video; misurato uno scarto costante di circa −0,03 s (entro 0,04 s); non controllato a vista su tutti i pezzi.
- `trans.wav` e dissolvenza a ogni cambio di pezzo: messi dal programma a ogni giunzione, controllati solo a campione.
- Immagini: solo quelle del PDF del prof (carta del confine orientale 792×470, foto INA-Casa 255×392, De Gasperi 469×398, Fanfani–Moro 717×632), ingrandite 2–3× con nitidezza: restano di qualità limitata; la carta è piccola sullo schermo.
- Card: poche card (circa 10 su 208) si accendono fino a 4 s dopo l'inizio della frase che riassumono (frasi lunghe unite da due pezzi) e restano alcuni tratti > 5 s in cui il prof parla di altro (commenti fuori tema, aperture lunghe) senza una card accesa.
- Sottotitoli: i pezzi del prof non coperti dalle card sono riconoscimento automatico con dizionario dei nomi: restano errori di parole; **da rileggere prima della pubblicazione**. Circa il 20% dei cue coperti dalle card parte da 1 a 6 s lontano dalla parola esatta.
- Fine di P5b / inizio di P6a: «…chiedono certe riforme sociali. Come.» e la risposta «La scuola media unica?» sono separate da mappa, pillola e quiz dell'argomento 5 (il prof le dice di seguito, la pausa tra le due frasi è troppo breve per tagliare): **decide Sara**.
- L'approfondimento dell'argomento 6 (AN6a) dura circa 38 s (voce da 40 s in su dopo il rifacimento).
- AAC a bitrate variabile (media 150–180 kb/s) invece di 192k fisso.
- Quiz e compiti: senza voce, con sottofondo musicale morbido e un solo jingle iniziale.
