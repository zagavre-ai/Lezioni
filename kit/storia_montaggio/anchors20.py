# Ancore (frase del docente, cerca dopo t) -> (card, frase). Il primo elemento e' lo stato all'inizio dell'argomento.
START=[('Il crollo',229),('Vediamo i vincitori',1300),('Contemporaneamente',1650),('Nel resto del continente europeo',2100),('Ora è molto importante',2600),('adesso proviamo',2900),('per concludere vediamo',3090),('è il caso appunto',3210)]
GROUPS={1:[[0,1],[2,3]],2:[[0,1,2]],3:[[0,1,2]],4:[[0,2],[1,3]],5:[[0,1],[2,3]],6:[[0,1,2],[3,4]],7:[[0,1],[3,2]],8:[[0,1],[2,3]]}
ANC={ # k: [(frase, dopo, card, sent)]  ; il primo evento (card iniziale) parte dall'inizio dell'argomento
1:[(None,0,0,0),('la fine della storia',286,1,0),('Partiamo proprio',470,2,0),('federazione russa è composta',800,3,0)],
2:[(None,0,0,0),('Accava dopo Reagan',1340,1,0),('vince poi De Clinton',1540,2,0)],
3:[(None,0,0,0),('Inizia la guerra',1740,1,0),('allora interviene la Nato',1930,2,0)],
4:[(None,0,0,0),('Nel Regno Unito',2170,2,0),('trattato di Maastricht',2230,1,0),("l'ingresso nell'Unione Europea",2400,3,0)],
5:[(None,0,None,0),('la seconda repubblica',2640,1,0),('I vecchi partiti non esistono',2655,0,0),('Silvio Berlusconi',2700,2,0),('sfide',2760,3,0)],
6:[(None,0,0,0),('fondamentalismo',2950,1,0),('In Africa',2960,2,0),('fine del regime',2985,3,0),("L'America Latina",2995,4,0),('figlio rinnegato',3030,1,0)],
7:[(None,0,0,0),('Accanto alla Cina',3130,1,0),("Anche l'India",3155,3,0),('Il Giappone ha attraversato',3190,2,0)],
8:[(None,0,0,0),('Internet',3235,1,0),('movimento No Global',3260,2,0),('Il 2000 si è aperto',3300,3,0)],
}
