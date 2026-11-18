# -*- coding: utf-8 -*-
CUES = {
 1: [["indebol", "primato", "potenze europee", "seconda guerra"], ["superpotenze", "stati uniti", "unione sovietica", "ideolog", "strategic"], ["consapevolezza", "indipendentist", "leader", "studiato"], ["autodeterminazione", "carta", "nazioni unite", "onu", "1945"]],
 2: [["bandung", "29 stati", "afroasiatic", "1955", "razzismo"], ["non allineati", "allineati", "blocchi", "schierar"], ["dieci principi", "principi", "diritti umani", "sovranità", "uguaglianza"], ["pressioni", "aiuti", "sfera di influenza", "finanziar", "militari"]],
 3: [["gandhi", "nehru", "ritiro", "1947", "britannic"], ["spartizione", "indù", "musulman", "pakistan", "unione indiana"], ["milioni", "profughi", "violenze", "spostamento", "religios"], ["kashmir", "conteso"]],
 4: [["ceylon", "sri lanka", "malesia", "pacific"], ["indonesia", "olanda", "olandes", "1949"], ["indocina", "vietminh", "dien bien phu", "francia"], ["ginevra", "vietnam", "nord", "sud", "divisione"]],
 5: [["libia", "gheddafi", "1951", "italian"], ["marocco", "tunisia", "1956"], ["algeria", "fln", "territorio nazionale", "guerra d'algeria"], ["1962", "repubblica algerina", "accordi", "evian"]],
 6: [["corno", "etiopia", "eritrea", "somalia"], ["ghana", "nkrumah", "kenya", "mau mau", "britannic"], ["colonie francesi", "francesi", "africa occidentale", "1960"], ["congo", "belgio", "katanga", "lumumba"]],
 7: [["apartheid", "segregazione", "sudafrica", "1948"], ["anc", "mandela", "african national", "1962"], ["rhodesia", "unilaterale"], ["portoghes", "angola", "mozambico", "1975", "lisbona"]],
 8: [["mandati", "società delle nazioni", "libano", "siria", "transgiordania"], ["palestin", "risoluzione", "181", "1947", "stato ebraico", "stato arabo"], ["israele", "ben gurion", "1948", "proclama"], ["guerra arabo", "profughi", "vittoria", "confini"]],
 9: [["nasser", "rivoluzione", "1952", "nazionalismo arabo"], ["canale", "suez", "nazionaliz", "assuan", "diga"], ["attaccano", "francia, regno unito", "israele", "crisi"], ["superpotenze", "ritiro", "stati uniti", "unione sovietica", "successo"]],
 10: [["terzo mondo", "sauvy", "povertà"], ["neocolonialismo", "multinazionali", "materie prime"], ["fondo monetario", "fmi", "finanziaria", "dipendenza"], ["nuovo ordine", "anni settanta", "riforma", "onu"]],
}
ORD = {n: [0, 1, 2, 3] for n in range(1, 11)}
ORD[4] = [1, 0, 2, 3]
ORD[6] = [1, 2, 3, 0]
OVERRIDE = {6: [(1305.0, 1390.0, 7, 3)]}
