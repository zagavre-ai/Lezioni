# Storia V (Mazzotti) · indice dei materiali nella release `mazzotti-storia-V`

Ogni zip è indipendente: scarica SOLO gli zip che contengono la tua lezione (`gh release download mazzotti-storia-V -p "<nome zip>"`), poi `unzip` solo i file che servono.

| Lez | Video (zip · file · MB) | Slide (zip) | Mappe (zip) |
|---|---|---|---|
| 1 | release `storia-V-lez01` · LEZIONE.1.IL.NOVECENTO.IL.SECOLO.DELLE.MASSE.mp4 · 1615 | 002 | 002 |
| 2 | release `storia-V-lez02` · LEZIONE.2.IL.MONDO.AGLI.INIZI.DEL.XX.SECOLE.E.L.IMPERIALISMO.mp4 · 1335 | 007 | 007 |
| 3 | file singolo `LEZIONE.3.L.ITALIA.DI.GIOLITTI.mp4` · 1311 | **manca** | 004 |
| 4 | file singolo `LEZIONE.4.LA.PRIMA.GUERRA.MONDIALE.mp4` · 1990 | 011 | **manca** |
| 5 | 007 · LEZIONE 5 LA RIVOLUZIONE RUSSA.mp4 · 1090 | **manca** | 003 |
| 6 | 001 · LEZIONE 6 IL PRIMO DOPOGUERRA (1919-1925).mp4 · 757 | 006 | **manca** |
| 7 | 003 · LEZIONE 7 GLI STATI UNITI DAL BOOM ECONOMICO AL NEW DEAL.mp4 · 694 | 002 | **manca** |
| 8 | file singolo `LEZIONE.8.IL.DOPOGUERRA.ITALIANO.E.IL.FASCISMO.1919-1925.mp4` · 1707 | **manca** | **manca** |
| 9 | 003 · LEZIONE 9 L_ITALIA DEL REGIME FASCISTA.mp4 · 1276 | 010 | **manca** |
| 10 | file singolo `LEZIONE.10.LA.GERMANIA.DA.WEIMAR.AL.NAZISMO.mp4` · 1843 | 007 | **manca** |
| 11 | 002 · LEZIONE 11 L_URSS DI STALIN (1924-1939).mp4 · 480 | 011 | 004 |
| 12 | 006 · LEZIONE 12 L_EUROPA E IL MONDO NEGLI ANNI TRENTA.mp4 · 1032 | **manca** | 010 |
| 13 | 4 file singoli `Storia.V.Lez.13-1…-4.mp4` · 962+968+933+1044 | **manca** | 006 |
| 14 | 009 · LEZIONE 14 LA GUERRA FREDDA (1945-1961).mp4 · 1373 | 007 | 004 |
| 15 | 010 · LEZIONE 15 LA DECOLONIZZAZIONE (1945-1975).mp4 · 809 | 003 | **manca** |
| 16 | 002 · LEZIONE 16 GLI ANNI SESSANTA TRA CRISI E PROGRESSI.mp4 · 774 | 004 | 006 |
| 17 | file singolo `LEZIONE.17.LE.FASI.CONCLUSIVE.DELLA.GUERRA.FREDDA.1969-1991.mp4` · 1953 | **manca** | 006 |
| 18 | 011 · LEZIONE 18 L_ITALIA REPUBBLICANA.mp4 · 1362 | 011 | 011 |
| 19 | 005 · LEZIONE 19 L_ITALIA DAL _68 ALLA CRISI DELLA PRIMA REPUBBLICA.mp4 · 1528 | 003 | **manca** |
| 20 | 004 · LEZIONE 20 GLI ANNI NOVANTA IL MONDO POST-BIPOLARE.mp4 · 1079 | 010 | 010 |
| 21 | 001 · LEZIONE 21 IL MONDO DAL 2001 AD OGGI.mp4 · 1065 | **manca** | 003 |

**Test finali (Excel del prof), lezioni 1–21:** zip `STORIA.V-20261114T194325Z-1-001.zip` (caricato il 14/11), file «DOMANDE LEZIONE N.xlsx».
**Compiti del prof (lezioni 1–21):** zip `STORIA.V.-20261114T220649Z-1-001.zip` (caricato il 14/11 sera), file «LEZIONE N.pdf» (domande aperte). Vanno nella scheda «Compiti» e in `compiti.json`.
**Video caricati il 14/11 come file singoli:** `LEZIONE.3.L.ITALIA.DI.GIOLITTI.mp4`, `Storia.V.Lez.13-1/-2/-3.mp4` (lezione 13 in 3 file), `LEZIONE.17.LE.FASI.CONCLUSIVE.DELLA.GUERRA.FREDDA.1969-1991.mp4`, `LEZIONE.21.IL.MONDO.DAL.2001.AD.OGGI.mp4`. Ancora mancanti: 4, 8, 10.
**Download:** con l'API REST (gh release download non funziona nelle sessioni): `gh api -H "Accept: application/octet-stream" repos/zagavre-ai/Lezioni/releases/assets/<id>`.

Il numero dello zip è l'ultima parte del nome: `…-1-001.zip` = 001. Lo zip 008 contiene gli Excel delle verifiche del prof (test finale di ogni lezione): SERVONO, da caricare. Video ancora mancanti: lezioni 3, 4, 8, 10, 13, 17.
Le lezioni 1 e 2 sono già avviate con le release `storia-V-lez01` e `storia-V-lez02`.
Test finali e compiti: arrivano dalla direzione il 13/11; nel video restano le schede «Verifica finale» e «Compiti».

## Controllo del 17/11 sera (master, lettura remota di tutti gli zip)
- **Video: ci sono tutti e 21.** La 13 è in 4 file (13-1 … 13-4), non 3.
- **Test finali (DOMANDE LEZIONE 1–21.xlsx) e compiti (LEZIONE 1–21.pdf): completi.**
- **Slide del prof mancanti:** lezioni 3, 5, 8, 12, 13, 17, 21 → senza PDF le slide si ricostruiscono dai fotogrammi del video (come la 17).
- **Mappe del prof mancanti:** lezioni 4, 6, 7, 8, 9, 10, 15, 19.
- Lo zip **008** dell'esportazione del 11/11 non è mai stato caricato: probabilmente contiene proprio queste slide e mappe.

## Aggiornamento 17/11 21:35 (Sara): slide e mappe complete
- `SLIDE-20261117T202354Z-1-001.zip`: **slide del prof di TUTTE le lezioni 1–21** («LEZIONE N.pdf», 8–28 pagine). Usare queste (sostituiscono la tabella sopra: le slide non mancano più per nessuna lezione).
- `MAPPE-20261117T202853Z-1-001.zip`: **mappe del prof 1–21 tranne la 15** («MAPPE LEZIONE N.pdf», 3–6 pagine).
- Ancora mancante: **solo la mappa della lezione 15.**
