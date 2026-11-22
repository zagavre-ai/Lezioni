# piano della lezione 8 · L'Espressionismo
from lib import *
TITOLO="L'Espressionismo"
ARG={1:"L'Impero tedesco e la metropoli moderna",2:"Le Secessioni e la svolta espressionista",3:"I precursori: Ensor e Munch",
     4:"Die Brücke e Kirchner",5:"Der Blaue Reiter: Marc, Kandinskij e Klee",6:"L'Espressionismo austriaco"}
LAB={1:"1 · L'Impero tedesco e la metropoli",2:"2 · Le Secessioni e la svolta espressionista",3:"3 · I precursori: Ensor e Munch",
     4:"4 · Die Brücke e Kirchner",5:"5 · Der Blaue Reiter",6:"6 · L'Espressionismo austriaco"}
def S(page,t0,t1,act,keys,arg,part=None): return dict(kind='cards',page=page,t0=t0,t1=t1,act=act,keys=keys,arg=arg,part=part)
def A(img,t0,t1,cap,keys,arg,focus=(0.5,0.5),start=(0.5,0.5),zmax=0.25): return dict(kind='art',img=img,t0=t0,t1=t1,cap=cap,keys=keys,arg=arg,focus=focus,start=start,zmax=zmax)
# pezzi del prof: (id, argomento, inizio prima frase, fine ultima frase, scene)
PROF=[
 dict(id='P0_intro',arg=0,s0=1.03,e1=119.14,scenes=[dict(kind='cover',t0=1.03,t1=119.5)]),
 dict(id='T1',arg=1,s0=120.33,e1=999.97,scenes=[
  S(2,120.33,290.0,[(134,0),(163,1),(232,2)],["Impero tedesco","Bismarck","67 milioni di abitanti","Berlino"],1),
  S(3,290.0,439.5,[(290,1),(317,0),(405,2)],["Metropoli","Angoscia individuale","Alienazione"],1),
  S(5,439.5,507.0,[(450,0),(466,1),(480,2)],["Sigmund Freud","Georg Simmel","Nevrosi"],1),
  S(6,507.0,552.0,[(507,2),(530,1)],["Designer","Produzione in serie","Arte e industria"],1),
  S(71,552.0,563.5,[(552,1),(559,0)],["Deutscher Werkbund","Monaco, 1907"],1),
  S(72,563.5,582.0,[(564,0)],["Karl Schmidt","Friedrich Naumann","Hermann Muthesius"],1),
  S(3,582.0,651.5,[(597,0),(619,1),(632,2)],["Metropoli","Disagio","Espressionisti"],1),
  S(4,651.5,912.0,[(674,0),(782,1),(802,2)],["Agorafobia","Spazio personale","Folla"],1),
  S(5,912.0,999.97,[(939,0),(955,1),(973,2)],["Sigmund Freud","Georg Simmel (1903)","Iperstimolazione"],1)]),
 dict(id='T2',arg=2,s0=1001.06,e1=1684.47,scenes=[
  S(8,1001.06,1352.0,[(1013,0),(1030,1),(1234,2)],["Vienna","Secessione","Interiorità","Conformismo borghese"],2),
  A('manifesto_bruecke',1352.0,1524.0,"<i>Manifesto per una mostra della Brücke</i> · Ernst Ludwig Kirchner, 1905",["Die Brücke","Dresda"],2,focus=(0.5,0.4)),
  A('almanacco',1524.0,1636.0,"<i>Illustrazione per l'Almanacco del Cavaliere Azzurro</i> · Franz Marc e Vasilij Kandinskij, 1912",["Der Blaue Reiter","Monaco"],2),
  S(8,1636.0,1684.47,[(1640,1)],["Vienna","Secessione","Introspezione"],2)]),
 dict(id='T3',arg=3,s0=1685.09,e1=2344.58,scenes=[
  S(10,1685.09,1789.0,[(1694,0),(1754,1),(1780,2)],["James Ensor","Edvard Munch","Pittura dell'anima"],3),
  A('bambina_malata',1789.0,1933.0,"<i>La bambina malata</i> · Edvard Munch, 1885-86",["Edvard Munch","Malattia","Lutto"],3,focus=(0.38,0.4)),
  A('urlo',1933.0,2086.0,"<i>L'urlo</i> · Edvard Munch, 1893",["Angoscia","Fiordo","Cielo rosso sangue"],3,focus=(0.45,0.6)),
  A('pubertà',2086.0,2344.58,"<i>Pubertà</i> · Edvard Munch, 1894-95",["Adolescenza","Ombra inquietante"],3,focus=(0.62,0.28))]),
 dict(id='T4',arg=4,s0=2344.82,e1=2729.19,scenes=[
  S(13,2344.82,2428.0,[(2374,0),(2395,1),(2416,2)],["Die Brücke (Il Ponte)","Der Blaue Reiter","Due anime diverse"],4),
  A('potsdamer',2428.0,2606.0,"<i>Potsdamer Platz</i> · Ernst Ludwig Kirchner, 1914",["Nevrosi urbana","Berlino"],4,focus=(0.5,0.75)),
  A('strada_berlino',2606.0,2656.0,"<i>Strada a Berlino</i> · Ernst Ludwig Kirchner, 1913",["Alienazione","Metropoli"],4),
  A('cinque_donne',2656.0,2729.19,"<i>Cinque donne per la strada</i> · Ernst Ludwig Kirchner, 1913",["Mercificazione","Disagio sociale"],4)]),
 dict(id='T5',arg=5,s0=2732.2,e1=3283.53,scenes=[
  A('grandi_cavalli',2732.2,2855.0,"<i>Grandi cavalli azzurri</i> · Franz Marc, 1911",["Franz Marc","Cavalli azzurri"],5,focus=(0.3,0.6)),
  A('piccoli_cavalli',2855.0,2920.0,"<i>Piccoli cavalli gialli</i> · Franz Marc, 1912",["Cavalli gialli"],5),
  A('grid_kandinskij',2920.0,2957.0,"<i>Le opere di Vasilij Kandinskij</i> · Impressione III, Improvvisazione 28, Studio per Composizione II, Composizione VII",["Vasilij Kandinskij","Astrattismo"],5,zmax=0.04),
  A('impressione3',2957.0,3020.0,"<i>Impressione III (Concerto)</i> · Vasilij Kandinskij, 1911",["Musica e colore","Arnold Schönberg"],5),
  A('improvvisazione28',3020.0,3066.0,"<i>Improvvisazione 28</i> · Vasilij Kandinskij",["Improvvisazioni","Emozioni interne"],5),
  A('studio_comp2',3066.0,3095.0,"<i>Studio per Composizione II</i> · Vasilij Kandinskij, 1910",["Prima opera astratta?"],5),
  A('composizione7',3095.0,3150.0,"<i>Composizione VII</i> · Vasilij Kandinskij, 1913",["Astrattismo","Sinfonia visiva"],5),
  A('senecio',3150.0,3226.0,"<i>Senecio</i> · Paul Klee, 1922",["Paul Klee","Sensibilità infantile"],5),
  A('macchina',3226.0,3283.53,"<i>Macchina per cinguettare</i> · Paul Klee, 1922",["Acquerello","Effetto tragicomico"],5)]),
 dict(id='T6',arg=6,s0=3285.38,e1=3669.54,scenes=[
  S(18,3285.38,3392.0,[(3296,0),(3368,1),(3379,2)],["Vienna","Oskar Kokoschka","Egon Schiele"],6),
  A('sposa_vento',3392.0,3470.0,"<i>La sposa del vento</i> · Oskar Kokoschka, 1913-14",["Alma Mahler","Tormento interiore"],6,focus=(0.45,0.55)),
  A('schiele',3470.0,3543.0,"<i>Autoritratto nudo, smorfie</i> · Egon Schiele, 1910",["Egon Schiele","Linea tagliente"],6,focus=(0.5,0.3)),
  A('abbraccio',3543.0,3669.54,"<i>L'abbraccio</i> · Egon Schiele, 1917",["Erotismo","Carnalità"],6,focus=(0.55,0.5))]),
]
# approfondimenti, pillole, quiz: nomi delle voci (testi_voci.json)
VOCI={1:('A1_APPROF','A1_PILLOLA'),2:('A2_APPROF','A2_PILLOLA'),3:('A3_APPROF','A3_PILLOLA'),4:('A4_APPROF','A4_PILLOLA'),5:('A5_APPROF','A5_PILLOLA'),6:('A6_APPROF','A6_PILLOLA')}
PARTE={1:[1,2,3,4],2:[5,6]}
def taglio(piece):
    """punti di taglio (inizio, fine) nel video originale: nelle pause, 0,15 s prima della frase che segue"""
    s0=piece['s0']; e1=piece['e1']
    ai=max(k for k,f in enumerate(FR) if f['i']<=s0+0.05)
    bi=min([k for k,f in enumerate(FR) if f['f']>=e1-0.05] or [len(FR)-1])
    a=FR[ai]['i']; b=FR[bi]['f']
    prev_end=FR[ai-1]['f'] if ai>0 else 0.0
    nxt=FR[bi+1]['i'] if bi+1<len(FR) else b+1
    return max(a-0.15,prev_end+0.05,0.0), min(b+0.35,nxt-0.15), FR[ai]['testo'], FR[bi]['testo']
