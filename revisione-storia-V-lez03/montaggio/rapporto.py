import json, re, sys, random
sys.path.insert(0, '/home/user/w3/build')
import data as D
S = D.S
out = []
def w(*a): out.append(' '.join(str(x) for x in a))
random.seed(5)
w("# RAPPORTO DI REVISIONE · Storia V · «L'Italia di Giolitti» · correzioni 22/11")
w("Chat di produzione · ramo `revisione-storia-V-lez03` · riparto dalla consegna del 20/11 (video e slide rifatti, voci Kore già esistenti riusate). Ogni dato è etichettato **M** (misurato), **S** (a vista) o **NV** (non verificato).\n")
w("## 1. Lavoro fatto (prompt correzioni 22/11)")
w("| # | Punto | Esito |\n|---|---|---|")
rows = [
 ("Mappe del prof", "Le 3 mappe del PDF «MAPPE LEZIONE 3» sono ridisegnate nel modello BES (pesca, celeste, paglierino, menta, lilla, legenda in alto a destra, testo 40–44 px), stesse parole e stesse frecce, costruite ramo per ramo con la voce Kore (una voce per ogni riquadro, riquadro acceso in giallo mentre parla, mappa intera ferma 4 s). Mappa 1 (svolta di Giolitti) dopo l'argomento 2; mappa 2 (sviluppo economico) dopo l'argomento 9; mappa 3 («GIOLITTI») dopo l'argomento 11. Tolte tutte le mappe nostre (mappe finali comprese). Gli altri argomenti chiudono con la pillola. La mappa 3 nel PDF del prof non ha la domanda come titolo: ho scritto «Come Giolitti affronta le pressioni dei nazionalisti e l'avanzata dei socialisti?» con parole del prof (come da risposta della master)."),
 ("Slide del prof", "Slide rifatte con testo delle card a 40 px, interlinea 1,5, al massimo 3 card intere (mai «…»), bordo giallo e pallino quando il prof comincia la frase, riquadro 4:3 del prof (412×309 a x=1428, y=148) con fascia gialla. Le slide sono «a finestra»: a ogni cambio di card o di inserto la pagina cambia (Pagina N). Dove il prof resta a lungo su un punto ho messo gli approfondimenti Kore (2 per argomento al massimo)."),
 ("Introduzione animata", "Copertina e «Di cosa parliamo» senza riquadro del prof; il riquadro compare solo quando il prof comincia a parlare (0,35 s prima della prima parola). Il nome del prof non è né detto né scritto nelle animazioni (compare solo nella fascia gialla)."),
 ("Copertina", "Titolo esatto «L'Italia di Giolitti» con l'elenco degli argomenti; introduzione del prof 148,4 s (sotto i 3 minuti), poi «Di cosa parliamo»."),
 ("Parte 2", "Si apre con lo spiegone: dopo la sigla un ripasso animato con voce Kore della Parte 1, argomento per argomento, con le immagini del prof e la mappa 1 di quella Parte."),
 ("Refusi", "Corretti nelle nostre slide e nella dispensa: «Sciopero del 1904» → «sciopero del 1904» (titolo p. 5 del PDF); «movimenti femministe» → «movimenti femministi» (p. 11). Anomalie lasciate come le dice il prof: la slide p. 4 scrive «Confederazione Generale del Lavoro (Cgil)» ma il prof dice «CGdL» (la sigla storica del 1906 è CGdL; la Cgil nasce nel 1944); «Ina» scritto con la sola iniziale maiuscola (la slide spiega la sigla); il prof dice «Crispy», «Beccaris» ecc. nel parlato ma le slide hanno l'ortografia giusta."),
 ("Audio", "Parlato del prof dall'originale con highpass a 80 Hz e riduzione leggera del rumore (afftdn nr 6), nessun altro filtro: timbro misurato più sotto. Pause oltre 2,5 s accorciate a circa 1 s (solo 2 nel parlato). −16 LUFS misurati sulla Parte. La lezione 3 non è tra le 4 e 6 (audio da rifare)."),
 ("Dispensa e PDF mappe", "Dispensa A4 orizzontale per Parte con le stesse slide del video a tutta larghezza e strato di testo invisibile; copertina con sola materia e titolo; piè di pagina «STORIA V · Pagina N» senza nome del prof. PDF delle mappe a parte con copertina identica più «MAPPE»."),
]
for i, (a, b) in enumerate(rows, 1): w(f"| {i} | {a} | {b} |")
w("")
open('/home/user/w3/rapporto_parte_statica.md', 'w').write('\n'.join(out))
print('ok')
