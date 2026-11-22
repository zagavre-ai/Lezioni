# -*- coding: utf-8 -*-
# Piano dei 6 argomenti: tempi nel video ORIGINALE del prof (secondi), card in ordine di parlato, accensioni.
# card = (pagina_slide, indice): vedi contenuti.SLIDES. lit = (tempo_originale, indice_card_in_lista | None)
# immagini del prof dentro l'argomento: (t0, t1, chiave, titolo)
import contenuti as C

TOP = {
 1: dict(titolo="Francia e Gran Bretagna tra le due guerre", t0=169.6, t1=727.0,
         cards=[(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)],
         lit=[(223.1,0),(319.8,1),(362.1,2),(468.6,3),(538.0,4),(619.2,5)], imm=[]),
 2: dict(titolo="Dittature e autoritarismi in Europa ed extra-Europa", t0=729.7, t1=1232.3,
         cards=[(2,1),(2,0),(2,2),(2,3),(4,0),(2,4),(2,5)],
         lit=[(758.7,0),(782.5,1),(836.7,2),(911.9,3),(990.4,4),(1126.2,5),(1173.5,6)], imm=[]),
 3: dict(titolo="L'espansionismo asiatico e la Cina divisa", t0=1232.7, t1=1334.1,
         cards=[(3,0),(3,2),(3,3),(3,1)],
         lit=[(1232.7,0),(1252.8,1),(1277.1,2),(1292.8,3)],
         imm=[(1239.4,1252.0,'asia','Leggere la carta: la «Lunga marcia» (1934-1935) e l’invasione giapponese (1937)')]),
 4: dict(titolo="La guerra civile spagnola (1936-1939)", t0=1334.6, t1=1990.0,
         cards=[(4,1),(4,2),(4,3),(4,4),(4,5)],
         lit=[(1415.4,0),(1508.5,1),(1593.3,2),(1694.4,3),(1802.2,4)],
         imm=[(1924.5,1927.6,'franco','Il generale Franco'),(1927.6,1989.9,'spagna','Leggere la carta: la guerra di Spagna (1936-1939)')]),
 5: dict(titolo="L'aggressività nazista e il fallimento di Locarno", t0=1991.0, t1=2317.9,
         cards=[(5,0),(5,1),(6,0),(5,2)],
         lit=[(1991.0,0),(2018.6,1),(2076.9,2),(2097.9,1),(2113.4,2),(2197.2,3)], imm=[]),
 6: dict(titolo="Verso la Seconda Guerra Mondiale", t0=2318.2, t1=3232.0,
         cards=[(6,1),(6,2),(6,3),(6,4),(6,5)],
         lit=[(2318.2,0),(2447.5,1),(2706.8,2),(2767.9,4),(2865.2,3),(2984.8,4),(3104.5,None)], imm=[]),
}
# Le slide delle pagine 5 e 6: la card «Appeasement» sta nell'argomento 5 (il prof ne parla lì), le altre nell'argomento 6.
SLIDE_TITOLO = {1: "Francia e Gran Bretagna tra le due guerre", 2: "Dittature e autoritarismi in Europa ed extra-Europa",
                3: "L'espansionismo asiatico e la Cina divisa", 4: "La guerra civile spagnola (1936-1939)",
                5: "L'aggressività nazista e il fallimento di Locarno", 6: "Verso la Seconda Guerra Mondiale"}
CHIAVE = C.CHIAVE
