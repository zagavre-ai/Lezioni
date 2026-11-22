import json
P=json.load(open('/home/claude/w/punti.json'))
txt=[x[1] for x in P]
# split card 24 (lavori + controllo)
i=txt[24].index('Il controllo finanziario')
cards=txt[:24]+[txt[24][:i].strip(),txt[24][i:].strip()]+txt[25:]   # 30 cards: indexes shift +1 after 24
# indices now: 0..23 as before, 24 lavori, 25 controllo, 26 AAA, 27 welfare, 28 comunicazione, 29 bilancio
KW={0:['Boom economico','Prima potenza mondiale'],1:['Catena di montaggio','Vendite a rate'],2:['Grattacieli','Grandi città'],
3:['Sogno americano','American way of life'],4:['Jazz','Radio','Cinema di Hollywood'],5:['Generazione perduta','Vuoto morale'],
6:['Diritto di voto','1920'],7:['Flappers','Donne indipendenti'],8:['Moda','Capelli corti'],9:['Charleston','Nuovi comportamenti'],
10:['Isolazionismo','Liberismo','Dazi protezionistici'],11:['Xenofobia','Leggi anti-immigrazione'],12:['Ku Klux Klan','Paura rossa'],
13:['Sacco e Vanzetti','Condannati nel 1927'],14:['Proibizionismo','Mercato nero','Al Capone'],
15:['Fragilità del boom','Crisi agricola'],16:['Sovrapproduzione','Scorte invendute'],17:['Bolla speculativa','Acquisto a credito'],
18:['Giovedì nero','Martedì nero'],19:['Crollo della Borsa','14 milioni di disoccupati'],20:['Baraccopoli','Siccità nel Midwest'],
21:['Hoover','Contagio globale'],22:['Roosevelt','New Deal'],23:['Keynes','Spesa pubblica'],24:['Grandi lavori pubblici','Tennessee Valley Authority'],
25:['Federal Reserve Bank','Dollaro svalutato'],26:['Agricultural Adjustment Act','National Industrial Recovery Act'],27:['Social Security Act','Welfare'],
28:['Fireside chats','Radio'],29:['Bilancio storico','Seconda guerra mondiale']}
# sotto-slide: (arg, [carte], inizio_orig, [ancore carte])   ancore = quando il prof comincia la frase della carta
SUB=[
(1,[0,1],172.1,[175.1,237.5]),(1,[2,4],269.5,[269.5,293.7]),(1,[3,5],409.5,[409.5,590.6]),
(2,[6],668.5,[675.6]),(2,[7,8],724.1,[724.1,729.2]),(2,[9,15],737.9,[737.9,777.4]),
(3,[10,11],854.2,[854.2,946.8]),(3,[12],1026.0,[1026.0]),(3,[13,14],1057.5,[1057.5,1183.0]),
(4,[16,17],1339.8,[1350.2,1398.7]),(4,[18,19],1448.6,[1448.6,1537.9]),(4,[20,21],1589.3,[1589.3,1620.2]),
(5,[22,23],1726.7,[1726.7,1808.3]),(5,[24,26],1833.3,[1841.5,1961.9]),(5,[25,27],1974.8,[1974.8,2036.9]),(5,[28,29],2079.3,[2079.3,2123.3]),
]
ARG={1:'I ruggenti anni Venti',2:'Le donne e le flappers',3:'Isolazionismo, razzismo e proibizionismo',4:'Il crollo del 1929 e la Grande Depressione',5:'Il New Deal di Roosevelt'}
# confini argomenti nel video originale (inizio, fine)
ARGT={1:(172.1,667.5),2:(668.5,853.6),3:(854.2,1339.0),4:(1339.8,1726.2),5:(1726.7,2179.5)}
# approfondimenti: (nome voce, inserire dopo il tempo originale t (fine frase piu' vicina))
AN={1:[('AN1',237.0),('AN2',500.0)],2:[('AN3',721.5),('AN4',767.6)],3:[('AN5',946.3),('AN6_R2',1263.1)],4:[('AN7',1398.1),('AN8',1508.7)],5:[('AN9',1830.8),('AN10',2078.1)]}
