import sys
sys.path.insert(0,'/tmp/claude-0/w/build')
from maps import *

def fauves():
    N=[]
    def n(*a,**k): N.append(Node(*a,**k)); return a[0]
    n('C',"I Fauves (le belve) 1905-1907",'c',900,215,420,size=40,bold=True)
    n('T','Il termine fu utilizzato per sottolineare, in senso spregiativo, l\'uso "selvaggio" del colore','k',270,235,500)
    n('M1','Movimento pittorico francese','k',230,440,400)
    n('M2',"Fu il primo dei grandi movimenti d'avanguardia dell'arte europea nel periodo di sperimentazione",'d',270,640,500)
    n('CP','Caratteristiche principali','k',900,395,480)
    n('c2','Semplificazione delle forme, l\'immediatezza e il colore.','k',780,545,380)
    n('c3',"Si dipinge in relazione al sentire interiore e non all'impressione",'k',1180,545,380)
    n('c1',"La prospettiva viene ignorata e il senso della profondità è prodotto dalla visione di scorcio su un piano unico e dal contrasto cromatico",'k',790,860,540)
    n('c4','Il colore svincolato dalla realtà','k',1180,700,360)
    n('c4b',"Alberi viola e figure umane rosse, scelti e accostati liberamente secondo esclusivamente l'armonia della composizione.",'e',1180,880,520)
    n('c5','La pittura istintiva e immediata','k',300,880,420)
    n('E','Espressionismo 1905-25','d',1640,215,330,shape='ellipse')
    n('MEs','Maggiori esponenti','lab',1640,320,300,size=34)
    for i,(t,x,y) in enumerate([('André Derain',1520,400),('Henri Matisse',1760,400),('Maurice de Vlaminck',1500,480),('Albert Marquet',1770,480),('Georges Braque',1640,560)]):
        n('N%d'%i,t,'e',x,y,280,shape='ellipse')
    n('RIF','I punti di riferimento','lab',1640,650,380)
    n('Cez','Cézanne','e',1470,730,200,shape='ellipse');n('Gau','Gauguin','e',1650,730,200,shape='ellipse');n('VG','Van Gogh','e',1820,730,200,shape='ellipse')
    n('n1','Per la smaterializzazione e ricomposizione delle forme','q',1490,900,360)
    n('n2','Per i colori impiegati puri, con violenza','q',1760,900,300)
    E=[('C','T',1),('C','M1',1),('M1','M2',1),('C','CP',1),('CP','c1',1),('CP','c2',1),('CP','c3',1),('CP','c4',1),('c4','c4b',1),('CP','c5',1),
       ('C','E',0),('E','MEs',0)]+[('MEs','N%d'%i,1) for i in range(5)]+[('C','RIF',0),('RIF','Cez',1),('RIF','Gau',1),('RIF','VG',1),('Cez','n1',1),('Gau','n2',1),('VG','n2',1)]
    M=Map('Chi sono i Fauves?',N,E,[])
    return M
if __name__=='__main__':
    m=fauves();m.static().convert('RGB').save('/tmp/claude-0/w/build/prev_fauves.png')
    for n in m.nodes.values():print(n.id,[int(x) for x in n.box])

def cubismo():
    N=[];E=[]
    def n(*a,**k): N.append(Node(*a,**k)); return a[0]
    def e(a,b,ah=1): E.append((a,b,ah))
    n('C','Cubismo','c',960,330,260,size=44,bold=True)
    labs={'Le':'È','Lna':'Nasce','Lpr':'Principali protagonisti','Lde':'Deriva da','Lte':'Il termine','Lve':'Vedono','Lfa':'Le fasi del Cubismo sono','Lra':'Raffigura','Lsu':'Si supera','Log':"L'oggetto subisce una",'Lso':'I soggetti','Lc1':'Le caratteristiche sono','Lc2':'Le caratteristiche sono','Lc3':'Le caratteristiche sono'}
    for k,v in labs.items(): n(k,v,'lab',960,500,500,size=34)
    boxes=[('A1','Un movimento di avanguardia','k'),('A2','Nel 1907 a Parigi','d'),('P1','Picasso','e'),('P2','Braque','e'),('P3','Gris','e'),('D1','Le ricerche di Cézanne','e'),('D2','Scultura primitiva','k'),
     ('TM','Nasce nel 1908 in senso dispregiativo','d'),('V','Non solo con gli occhi ma anche con la mente','k'),('FR1','Cubismo formativo','d'),('FR2','Cubismo analitico','d'),('FR3','Cubismo sintetico','d'),
     ('F1',"Forme semplificate, volumi puri, influenza dell'arte primitiva",'k'),('F2','Spezza le forme in piccoli piani, il soggetto diventa quasi indecifrabile, il colore è quasi assente','k'),
     ('F3',"Semplifica la scomposizione, usano piani larghi e colorati, usano il collage polimaterico, l'opera diventa un soggetto autonomo",'k'),('R','Simultaneamente un oggetto da vari punti di vista','k'),
     ('S','Il metodo prospettico tradizionale','k'),('SC','Scomposizione','k'),('RC','Ricomposizione sulla tela','k'),('NI','Non sono innovativi','k')]
    for i,(k,t,c) in enumerate(boxes): n(k,t,c,200+(i%6)*320,250+(i//6)*250,380)
    e('C','Le',0);e('Le','A1');e('C','Lna',0);e('Lna','A2');e('C','Lpr',0);[e('Lpr',p) for p in ('P1','P2','P3')]
    e('C','Lra',0);e('Lra','R');e('C','Lsu',0);e('Lsu','S');e('C','Lde',0);e('Lde','D1');e('Lde','D2');e('C','Lte',0);e('Lte','TM')
    e('C','Log',0);e('Log','SC');e('Log','RC');e('C','Lso',0);e('Lso','NI');e('C','Lve',0);e('Lve','V')
    e('C','Lfa',0);[e('Lfa',f) for f in ('FR1','FR2','FR3')]
    e('FR1','Lc1',0);e('Lc1','F1');e('FR2','Lc2',0);e('Lc2','F2');e('FR3','Lc3',0);e('Lc3','F3')
    return Map("Che cos'è il Cubismo?",N,E,[])
FR_CUB=[("Che cos'è il Cubismo?",[]),("Cubismo. È un movimento di avanguardia.",['C','Le','A1']),("Nasce nel millenovecentosette a Parigi.",['Lna','A2']),
 ("Principali protagonisti: Picasso, Braque, Gris.",['Lpr','P1','P2','P3']),("Raffigura simultaneamente un oggetto da vari punti di vista.",['Lra','R']),
 ("Si supera il metodo prospettico tradizionale.",['Lsu','S']),("Deriva dalle ricerche di Cézanne e dalla scultura primitiva.",['Lde','D1','D2']),
 ("Il termine nasce nel millenovecentootto, in senso dispregiativo.",['Lte','TM']),("L'oggetto subisce una scomposizione e una ricomposizione sulla tela.",['Log','SC','RC']),
 ("I soggetti non sono innovativi.",['Lso','NI']),("Vedono non solo con gli occhi, ma anche con la mente.",['Lve','V']),("Le fasi del Cubismo sono tre.",['Lfa']),
 ("Il Cubismo formativo: le caratteristiche sono forme semplificate, volumi puri, influenza dell'arte primitiva.",['FR1','Lc1','F1']),
 ("Il Cubismo analitico: spezza le forme in piccoli piani, il soggetto diventa quasi indecifrabile, il colore è quasi assente.",['FR2','Lc2','F2']),
 ("Il Cubismo sintetico: semplifica la scomposizione, usa piani larghi e colorati, usa il collage polimaterico, l'opera diventa un soggetto autonomo.",['FR3','Lc3','F3'])]
FR_FAU=[("Chi sono i Fauves?",[]),("I Fauves, le belve, millenovecentocinque, millenovecentosette.",['C']),
 ("Il termine fu utilizzato per sottolineare, in senso spregiativo, l'uso selvaggio del colore.",['T']),
 ("Movimento pittorico francese: fu il primo dei grandi movimenti d'avanguardia dell'arte europea nel periodo di sperimentazione.",['M1','M2']),
 ("Caratteristiche principali.",['CP']),
 ("La prospettiva viene ignorata, e il senso della profondità è prodotto dalla visione di scorcio su un piano unico e dal contrasto cromatico.",['c1']),
 ("Semplificazione delle forme, l'immediatezza e il colore.",['c2']),("Si dipinge in relazione al sentire interiore e non all'impressione.",['c3']),
 ("Il colore è svincolato dalla realtà: alberi viola e figure umane rosse, scelti e accostati liberamente, secondo esclusivamente l'armonia della composizione.",['c4','c4b']),
 ("La pittura è istintiva e immediata.",['c5']),("Espressionismo, millenovecentocinque, millenovecentoventicinque.",['E']),
 ("Maggiori esponenti: André Derain, Henri Matisse, Maurice de Vlaminck, Albert Marquet, Georges Braque.",['MEs','N0','N1','N2','N3','N4']),
 ("I punti di riferimento: Cézanne, per la smaterializzazione e ricomposizione delle forme; Gauguin e Van Gogh, per i colori impiegati puri, con violenza.",['RIF','Cez','n1','Gau','VG','n2'])]

def finale():
    N=[];E=[]
    def n(*a,**k): N.append(Node(*a,**k)); return a[0]
    def e(a,b,ah=1): E.append((a,b,ah))
    n('R','Avanguardie (arte)','c',960,200,380,size=44,bold=True)
    n('LP','Periodo','lab',300,200,200);n('PER',"Primo '900",'d',150,300,260);n('LC',"Cos'è",'lab',500,200,200);n('COS','Movimento artistico-culturale nato in Europa','k',600,300,420)
    br=[('ESP','Espressionismo','k'),('CUB','Cubismo','k'),('FUT','Futurismo','k'),('AST','Astrattismo','k'),('DAD','Dadaismo','k'),('SDP','Scuola di Parigi','k'),('SUR','Surrealismo','k'),('MET','Metafisica','k')]
    for i,(k,t,c) in enumerate(br): n(k,t,c,240+(i%4)*480,450+(i//4)*330,380,bold=True)
    ch=[('E1','Esprime il mondo interiore (paura, angoscia)','k'),('FAU','Fauves','k'),('F1','Colori molto forti','k'),('EN','Munch, Nolde','e'),('EM','Matisse','e'),
        ('CU1','Forme geometriche','k'),('CU2','Picasso, Gris, Braque','e'),('FU1','Movimento e velocità; auto e treni; sport','k'),('FU2','Severini, Boccioni, Russolo','e'),
        ('AS1','Esprime il mondo interiore','k'),('AS2','Colori puri','k'),('AS3','Kandinskij, Mondrian','e'),('DA1',"Esprime la libertà dell'artista",'k'),('DA2','Duchamp, Schwitters, Man Ray','e'),
        ('SP1',"Interesse per l'arte primitiva",'k'),('SP2','Modigliani, Chagall','e'),('SU1',"L'inconscio: sogno e fantasia",'k'),('SU2','Miró, Dalí, Ernst, Magritte','e'),('ME1','Atmosfere irreali; mistero','k'),('ME2','De Chirico','e')]
    for i,(k,t,c) in enumerate(ch): n(k,t,c,200+(i%8)*230,600+(i//8)*150,360)
    e('R','LP',0);e('LP','PER');e('R','LC',0);e('LC','COS')
    for k,_,_ in br: E.append(('R',k,1,'elbow',400))
    e('ESP','E1');e('ESP','FAU');e('FAU','F1');e('E1','EN');e('F1','EM')
    e('CUB','CU1');e('CU1','CU2');e('FUT','FU1');e('FU1','FU2');e('AST','AS1');e('AST','AS2');e('AS1','AS3')
    e('DAD','DA1');e('DA1','DA2');e('SDP','SP1');e('SP1','SP2');e('SUR','SU1');e('SU1','SU2');e('MET','ME1');e('ME1','ME2')
    return Map('Che cosa sono le Avanguardie?',N,E,[])
FR_FIN=[("Che cosa sono le Avanguardie?",[]),("Avanguardie, arte.",['R']),("Il periodo: primo Novecento.",['LP','PER']),("Che cos'è: un movimento artistico-culturale nato in Europa.",['LC','COS']),
 ("L'Espressionismo esprime il mondo interiore: paura, angoscia.",['ESP','E1','EN']),("Tra gli Espressionisti, i Fauves: colori molto forti. Munch, Nolde e Matisse.",['FAU','F1','EM']),
 ("Il Cubismo: forme geometriche. Picasso, Gris, Braque.",['CUB','CU1','CU2']),("Il Futurismo: movimento e velocità; auto e treni; sport. Severini, Boccioni, Russolo.",['FUT','FU1','FU2']),
 ("L'Astrattismo esprime il mondo interiore, con colori puri. Kandinskij, Mondrian.",['AST','AS1','AS2','AS3']),("Il Dadaismo esprime la libertà dell'artista. Duchamp, Schwitters, Man Ray.",['DAD','DA1','DA2']),
 ("La Scuola di Parigi: interesse per l'arte primitiva. Modigliani, Chagall.",['SDP','SP1','SP2']),("Il Surrealismo: l'inconscio, sogno e fantasia. Miró, Dalí, Ernst, Magritte.",['SUR','SU1','SU2']),
 ("La Metafisica: atmosfere irreali, mistero. De Chirico.",['MET','ME1','ME2'])]

# ---------------------------------------------------------------- disposizioni ordinate (a righe)
def _mk(M,i,cx,cy,w=None):
    n=M.nodes[i]
    if n.kind=='lab': n.cx,n.cy=cx,cy
    else:
        M.nodes[i]=Node(i,n.text,n.kind,cx,cy,w or n.w,n.size,n.shape,n.bold)
    return M.nodes[i]
def _h(M,i,w):
    n=M.nodes[i]
    return n.h if n.kind=='lab' else Node(i,n.text,n.kind,0,0,w,n.size,n.shape,n.bold).h

def layout_finale(M):
    colx={'B':(480,770),'C':(830,1300),'D':(1340,1700),'E':(1720,1905)}
    rows=[[('ESP','B'),('E1','C'),('EN','D')],[('FAU','C'),('F1','D'),('EM','E')],[('CUB','B'),('CU1','C'),('CU2','D')],[('FUT','B'),('FU1','C'),('FU2','D')],
          [('AST','B'),('AS1','C'),('AS3','D')],[('AS2','C')],[('DAD','B'),('DA1','C'),('DA2','D')],[('SDP','B'),('SP1' if False else 'SP1','C'),('SP2','D')],
          [('SUR','B'),('SU1','C'),('SU2','D')],[('MET','B'),('ME1','C'),('ME2','D')]]
    y=158;gap=14
    for r in rows:
        hs=[_h(M,i,colx[c][1]-colx[c][0]) for i,c in r];H=max(hs)
        for (i,c),h in zip(r,hs):
            x0,x1=colx[c];_mk(M,i,(x0+x1)/2,y+H/2,x1-x0)
        y+=H+gap
    _mk(M,'R',160,360,280)
    _mk(M,'LP',160,640,200);_mk(M,'PER',160,720,260);_mk(M,'LC',160,810,200);_mk(M,'COS',160,930,300)
    return M

def layout_cubismo(M):
    _mk(M,'C',960,420,200)
    def side(rows,lx,tx,tw,y0,gap=4):
        y=y0
        for lab,tg in rows:
            hs=[_h(M,t,tw) for t in tg];tot=sum(hs)+gap*(len(tg)-1);yy=y
            for t,h in zip(tg,hs):
                _mk(M,t,tx,yy+h/2,tw);yy+=h+gap
            _mk(M,lab,lx,y+tot/2);y+=tot+gap+6
    side([('Le',['A1']),('Lna',['A2'])],1290,1690,420,150)
    # protagonisti in una riga
    yp=372
    for t,cx,w in (('P1',1545,170),('P2',1705,150),('P3',1830,110)): _mk(M,t,cx,yp,w)
    _mk(M,'Lpr',1290,yp)
    side([('Lra',['R']),('Lde',['D1','D2'])],1290,1690,420,432)
    side([('Lte',['TM']),('Log',['SC','RC']),('Lso',['NI']),('Lve',['V']),('Lsu',['S'])],620,230,420,150)
    _mk(M,'Lfa',960,712)
    for k,(fr,lc,f,cx) in enumerate([('FR1','Lc1','F1',330),('FR2','Lc2','F2',960),('FR3','Lc3','F3',1590)]):
        _mk(M,fr,cx,782,300);_mk(M,lc,cx,842);h=_h(M,f,600);_mk(M,f,cx,1036-h/2,600)
    return M
if __name__=='__main__':
    for nm,fn in (('finale',lambda:layout_finale(finale())),('cubismo',lambda:layout_cubismo(cubismo()))):
        m=fn();m.static().convert('RGB').save('/tmp/claude-0/w/build/man_%s.png'%nm)
