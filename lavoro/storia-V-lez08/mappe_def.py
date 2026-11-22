# Le 3 mappe del prof: stesse parole, stessa struttura, stesse frecce. Nodi: (testo, cx, cy, w, h, colore, size)
M1=dict(titolo='Quali sono le condizioni dell\'Italia nel dopoguerra?',
 nodi={'n0':('L\'Italia nel dopoguerra',960,240,760,90,'pesca',50),'n1':('difficile situazione economica',420,440,620,100,'pagl',40),'n2':('tensioni politiche',1380,440,560,100,'pagl',44),
       'n3':('la mobilitazione contadina e operaia',780,655,620,120,'pagl',38),'n4':('l\'insoddisfazione dei nazionalisti per la «vittoria mutilata»',1480,655,740,120,'pagl',38),
       'n5':('occupazione delle fabbriche (1920)',780,875,620,110,'celeste',40),'n6':('occupazione di Fiume (1919)',1480,875,740,110,'celeste',40)},
 archi=[('n0','n1','vive una'),('n0','n2','è attraversata da'),('n2','n3','con'),('n2','n4','con'),('n3','n5','che culmina nella'),('n4','n6','che porta alla')],
 voce='MAP1',testo='Quali sono le condizioni dell\'Italia nel dopoguerra? L\'Italia vive una difficile situazione economica ed è attraversata da tensioni politiche. Le tensioni sono due: la mobilitazione contadina e operaia, che culmina nell\'occupazione delle fabbriche del millenovecentoventi, e l\'insoddisfazione dei nazionalisti per la vittoria mutilata, che porta all\'occupazione di Fiume del millenovecentodiciannove.',
 anc=[('n0','Ital',3.5),('n1','econom',None),('n2','politi',None),('n3','mobil',None),('n5','fabbr',None),('n4','nazion',None),('n6','Fiume',None)])
M2=dict(titolo='Come nasce e si sviluppa il movimento fascista?',
 nodi={'n0':('Benito Mussolini',960,260,640,100,'pesca',50),'n1':('Fasci di combattimento (1919)',500,500,700,120,'celeste',42),'n2':('squadrismo',500,760,520,110,'pagl',44),
       'n3':('blocchi nazionali (1921)',1420,500,700,120,'celeste',42),'n4':('il Partito nazionale fascista (1921)',1420,760,700,130,'celeste',42)},
 archi=[('n0','n1','fonda i'),('n0','n3','partecipa ai'),('n1','n2','che praticano lo'),('n3','n4','e fonda')],
 voce='MAP2',testo='Come nasce e si sviluppa il movimento fascista? Benito Mussolini fonda i Fasci di combattimento nel millenovecentodiciannove, che praticano lo squadrismo. Partecipa poi ai blocchi nazionali del millenovecentoventuno e fonda il Partito nazionale fascista.',
 anc=[('n0','Mussol',None),('n1','combat',None),('n2','squadr',None),('n3','blocc',None),('n4','Parti',None)])
M3=dict(titolo='Come Mussolini conquista il potere?',
 nodi={'n0':('Benito Mussolini',960,235,640,90,'pesca',50),'n1':('la marcia su Roma (1922)',960,385,640,90,'celeste',44),'n2':('l\'incarico di governo',960,535,600,90,'pagl',44),
       'n3':('liberali',480,705,420,110,'pagl',44),'n4':('una riforma elettorale',480,880,560,100,'lilla',44),
       'n5':('dispone l\'assassinio di Matteotti (1924)',1440,705,640,110,'celeste',40),'n6':('rivendica pubblicamente l\'accaduto (1925)',1440,880,640,110,'lilla',40)},
 archi=[('n0','n1','decide'),('n1','n2','e ottiene'),('n2','n3','insieme ai'),('n3','n4','e introduce'),('n2','n5','dopo il quale'),('n5','n6','e')],
 voce='MAP3_R2',testo='Come Mussolini conquista il potere? Benito Mussolini decide la marcia su Roma, del millenovecentoventidue, e ottiene l\'incarico di governo. Insieme ai liberali introduce una riforma elettorale. Dopo l\'incarico di governo, dispone l\'assassinio di Matteotti, nel millenovecentoventiquattro, e rivendica pubblicamente l\'accaduto nel millenovecentoventicinque.',
 anc=[('n0','Benito',None),('n1','marcia',None),('n2','incarico',None),('n3','liberali',None),('n4','riforma',None),('n5','assass',None),('n6','rivendica',None)])
