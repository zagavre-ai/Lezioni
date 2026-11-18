# -*- coding: utf-8 -*-
CUES = {
 1: [["crollo", "impero zarista", "austro-ungarico", "mappa"], ["nuovi stati", "cecoslovacchia", "polonia", "serbi, croati"], ["cuscinetto", "arginare", "bolscevic", "contenere la germania"], ["finlandia", "ucraina", "georgia", "bielorussia", "1922"]],
 2: [["jugoslavia", "centralismo", "serb", "belgrado", "1929"], ["polonia", "polacc", "pizzucsky", "riga", "piłsudski", "1930", "brest"], ["ungheria", "trianon", "kun", "reggen", "horthy", "sovietica"], ["austria", "province rurali", "repubblica costituzionale", "socialdemocr"]],
 3: [["abdicazione", "kaiser", "repubblica democratica", "socialdemocratici"], ["spartachist", "liebknecht", "rosa luxemburg", "rivolta"], ["costituzione", "weimar", "suffragio", "poteri di emergenza"], ["versailles", "diktat", "imposizione", "estrema destra"]],
 4: [["iperinflazione", "riparazioni", "marchi", "risparmi"], ["kapp", "putsch", "colpo di stato", "monaco", "hitler"], ["ruhr", "francesi e belghe", "occupazione"], ["stresemann", "dawes", "prestiti", "stabilizzazione"]],
 5: [["francia", "blocco nazionale", "cartello", "ricostruzione"], ["regno unito", "lloyd george", "voto alle donne", "sussidi"], ["scioperi", "minatori", "1926", "malcontento"], ["irland", "ira", "stato libero", "guerra civile"]],
 6: [["sèvres", "sevres", "ottomano", "spartizione"], ["mustafa kemal", "greci", "losanna", "riscossa"], ["atatürk", "ataturk", "ankara", "alfabeto latino", "laico", "poligamia"], ["sykes", "picot", "mandat", "arabi", "promesse"]],
 7: [["egitto", "1922"], ["india", "gandhi", "amritsar", "disobbedienza", "sale"], ["francese", "marocco", "indocina", "ho chi minh"]],
 8: [["giappone", "colonie tedesche", "risentimento"], ["cina", "yuan shikai", "signori della guerra", "caos"], ["guomintang", "sun yat-sen", "alleanza", "comunisti"], ["chiang kai-shek", "1926", "rottura", "repressione", "guerra civile"]],
}
ORD = {n: list(range(len(CUES[n]))) for n in CUES}
ORD[2] = [0, 1, 3, 2]
OVERRIDE = {}
