# -*- coding: utf-8 -*-
# Mappe della Prof.ssa Caputi (lez05), ridisegnate in vettoriale: stessa struttura, stesse parole. Colori BES: pesca centrale, paglierino parole chiave, menta esempi.
def L(*items):
    """items: stringhe semplici (titolo di sezione) o liste (punti elenco)"""
    h=''
    for it in items:
        if isinstance(it,list): h+='<ul style="margin:2px 0 6px 0;padding-left:34px">'+''.join(f'<li>{x}</li>' for x in it)+'</ul>'
        else: h+=f'<div>{it}</div>'
    return h
def nodo(id,c,x,y,w,h,txt,da=None,g=None,ls=False,fs=None,arg=None,cols=None):
    return dict(id=id,c=c,x=x,y=y,w=w,h=h,h2=txt,da=da,g=g,ls=ls,fs=fs,arg=arg,cols=cols)
MAPPE={}
# ---------- MAPPA 1: Fibre vegetali: origine ed estrazione
MAPPE[1]=dict(titolo="Fibre vegetali: origine ed estrazione", nodi=[
 nodo('r','pes',560,130,800,130,'FIBRE VEGETALI: ORIGINE ED ESTRAZIONE',g=0),
 nodo('o','pag',70,330,540,90,'<b>ORIGINE</b>','r',1),
 nodo('s','pag',690,330,540,90,'<b>STRUTTURA DEL FUSTO</b>','r',2),
 nodo('e','pag',1310,330,540,90,'<b>ESTRAZIONE</b>','r',3),
 nodo('o2','men',70,470,540,330,L('Le fibre vegetali possono derivare da:',['Fusto (vasi liberiani)','Foglie','Frutti','Alghe']),'o',1,True),
 nodo('s2','men',690,470,540,420,L(['Corteccia','Legno','Cambio','Floema (vasi liberiani)'],'Le fibre tessili si trovano nel floema e sono unite da sostanze pectiche.'),'s',2,True),
 nodo('e2','men',1310,470,540,330,L('Macerazione',['Chimico-fisica o microbiologica','Scioglie le sostanze pectiche','Separa la fibra dalla parte legnosa']),'e',3,True),
])
VOCI_M1=[ "Mappa concettuale: fibre vegetali, origine ed estrazione.",
 "Primo ramo, origine. Le fibre vegetali possono derivare da fusto, cioè dai vasi liberiani, da foglie, da frutti e da alghe.",
 "Secondo ramo, struttura del fusto. Corteccia, legno, cambio e floema, cioè i vasi liberiani. Le fibre tessili si trovano nel floema e sono unite da sostanze pectiche.",
 "Terzo ramo, estrazione. La macerazione, un processo chimico-fisico o microbiologico, scioglie le sostanze pectiche e separa la fibra dalla parte legnosa."]
# ---------- MAPPA 2: Fibre da fusto (liberiane): lino, canapa, juta, ramiè (si costruisce in 4 argomenti)
_y=290; _h=70
MAPPE[2]=dict(titolo="Fibre da fusto (liberiane)", nodi=[
 nodo('r','pes',560,120,800,110,'FIBRE DA FUSTO (LIBERIANE)',arg=2,g=0),
 nodo('li','pag',40,_y,440,_h,'<b>LINO</b>','r',1,arg=2),
 nodo('li2','men',40,_y+110,440,620,L('Qualità',['Verde → fibre finissime','Gialla → pregiata e resistente','Bruna → più grossa e robusta'],'Lavorazione',['Macerazione','Sgranatura','Scavezzatura','Scotolatura','Pettinatura'],'Morfologia',['Aspetto a canna di bambù','Striature e nodi']),'li',1,True,arg=2),
 nodo('ca','pag',500,_y,440,_h,'<b>CANAPA</b>','r',1,arg=3),
 nodo('ca2','men',500,_y+110,440,430,L(['Cannabis sativa','Elevata tenacità','Antistatica','Poco elastica'],'Lavorazione',['Macerazione','Decanapulazione','Eventuale cotonizzazione con NaOH']),'ca',1,True,arg=3),
 nodo('ju','pag',960,_y,440,_h,'<b>JUTA</b>','r',1,arg=4),
 nodo('ju2','men',960,_y+110,440,500,L(['Crescita rapida','Ricca di lignina','Rigida','Invecchia facilmente'],'Proprietà',['Molto igroscopica','Assorbe fino al 25% di acqua']),'ju',1,True,arg=4),
 nodo('ra','pag',1420,_y,440,_h,'<b>RAMIÈ</b>','r',1,arg=5),
 nodo('ra2','men',1420,_y+110,440,450,L(['Bianco','Fine e lucente','Simile alla seta'],'Lavorazione',['Decorticazione meccanica','Degommatura chimica con soda caustica']),'ra',1,True,arg=5),
])
VOCI_M2={2:["Mappa concettuale: fibre da fusto, cioè liberiane. Cominciamo dal lino.",
 "Lino. Qualità: verde, fibre finissime; gialla, pregiata e resistente; bruna, più grossa e robusta. Lavorazione: macerazione, sgranatura, scavezzatura, scotolatura e pettinatura. Morfologia: aspetto a canna di bambù, con striature e nodi."],
 3:["Canapa. Cannabis sativa. Elevata tenacità, antistatica, poco elastica. Lavorazione: macerazione, decanapulazione ed eventuale cotonizzazione con NaOH, cioè soda caustica."],
 4:["Juta. Crescita rapida, ricca di lignina, rigida, invecchia facilmente. Proprietà: molto igroscopica, assorbe fino al venticinque per cento di acqua."],
 5:["Ramiè. Bianco, fine e lucente, simile alla seta. Lavorazione: decorticazione meccanica e degommatura chimica con soda caustica."]}
# ---------- MAPPA 3: Fibre minori, da foglia, frutto e alghe
MAPPE[3]=dict(titolo="Fibre minori, da foglia, frutto e alghe", nodi=[
 nodo('r','pes',500,120,920,130,'FIBRE MINORI, DA FOGLIA, FRUTTO E ALGHE',g=0),
 nodo('a','pag',40,300,440,90,'<b>FIBRE LIBERIANE MINORI</b>','r',1,fs=30),
 nodo('b','pag',500,300,440,90,'<b>FIBRE DA FOGLIA</b>','r',2,fs=30),
 nodo('c','pag',960,300,440,90,'<b>FIBRE DA FRUTTO</b>','r',3,fs=30),
 nodo('d','pag',1420,300,440,90,'<b>FIBRE ALGINICHE</b>','r',4,fs=30),
 nodo('a2','men',40,430,440,300,L(['Ortica','Ginestra','Gelsomino']),'a',1,True),
 nodo('b2','men',500,430,440,560,L('Canapa di Manila (Abaca)',['Molto tenace',"Resistente all'acqua marina"],'Sisal',['Fibra bianca e rigida'],'Rafia',['Robusta ed elastica']),'b',2,True),
 nodo('c2','men',960,430,440,360,L('Cocco',['Fibre brune','Molto resistenti','Utilizzate per zerbini']),'c',3,True),
 nodo('d2','men',1420,430,440,360,L('Seta marina',['Fibre molto fini','Lucenti','Simili al ramiè superiore']),'d',4,True),
])
VOCI_M3=["Mappa concettuale: fibre minori, da foglia, da frutto e alghe.",
 "Fibre liberiane minori: ortica, ginestra e gelsomino.",
 "Fibre da foglia. Canapa di Manila, detta anche abaca: molto tenace e resistente all'acqua marina. Sisal: fibra bianca e rigida. Rafia: robusta ed elastica.",
 "Fibre da frutto. Cocco: fibre brune, molto resistenti, utilizzate per zerbini.",
 "Fibre alginiche. Seta marina: fibre molto fini, lucenti, simili al ramiè superiore."]
# ---------- MAPPA 4: Saggi e analisi delle fibre vegetali
MAPPE[4]=dict(titolo="Saggi e analisi delle fibre vegetali", nodi=[
 nodo('r','pes',500,380,920,110,'SAGGI E ANALISI DELLE FIBRE VEGETALI',g=0),
 nodo('q','pag',60,110,560,80,'<b>SAGGI QUANTITATIVI</b>','r',1,fs=32),
 nodo('q2','men',60,200,560,150,L('Liquido di Schweitzer',['Scioglie le fibre liberiane','Non scioglie il cotone']),'q',1,True),
 nodo('m','pag',1300,110,560,80,'<b>ANALISI MICROSCOPICA</b>','r',2,fs=32),
 nodo('m2','men',1300,200,560,150,L(['Lino → punte acute','Canapa → punte arrotondate','Sunn → lume largo e ovale']),'m',2,True),
 nodo('c','pag',30,540,380,80,'<b>COMBUSTIONE</b>','r',3,fs=30),
 nodo('c2','men',30,650,380,300,L(['Lino e cotone bruciano rapidamente','Odore di carta bruciata','Ceneri grigie fini']),'c',3,True),
 nodo('re','pag',430,540,700,80,'<b>REATTIVI COLORIMETRICI</b>','r',4,fs=30),
 nodo('re2','men',430,650,700,350,'<div style="column-count:2;column-gap:30px">'+L('Fluoroglucina',['Lino → incolore','Canapa → rosa','Juta → rosso sangue'],'Rosso di rutenio',['Colora di rosso lino, juta e ramiè'],'Cloroioduro di zinco',['Lino → bruno-violaceo','Canapa → viola','Juta → giallo'])+'</div>','re',4,True,fs=30),
 nodo('t','pag',1150,540,700,80,'<b>TEST FISICI</b>','r',5,fs=30),
 nodo('t2','men',1150,650,700,350,'<div style="column-count:2;column-gap:30px">'+L('Galleggiamento',['Lino → galleggia','Canapa → affonda rapidamente'],'Lampada di Wood',['Lino → giallo','Cotone → violetto'],'Ceneri',['Sisal → calcaree','Canapa di Manila → silicee'])+'</div>','t',5,True,fs=30),
])
VOCI_M4=["Mappa concettuale: saggi e analisi delle fibre vegetali.",
 "Saggi quantitativi. Con il liquido di Schweitzer si sciolgono le fibre liberiane, ma non il cotone.",
 "Analisi microscopica. Il lino ha le punte acute, la canapa le punte arrotondate, il sunn un lume largo e ovale.",
 "Combustione. Lino e cotone bruciano rapidamente, con odore di carta bruciata e ceneri grigie e fini.",
 "Reattivi colorimetrici. Fluoroglucina: il lino resta incolore, la canapa diventa rosa, la juta rosso sangue. Rosso di rutenio: colora di rosso lino, juta e ramiè. Cloroioduro di zinco: il lino diventa bruno-violaceo, la canapa viola, la juta gialla.",
 "Test fisici. Galleggiamento: il lino galleggia, la canapa affonda rapidamente. Lampada di Wood: il lino è giallo, il cotone violetto. Ceneri: calcaree per il sisal, silicee per la canapa di Manila."]
