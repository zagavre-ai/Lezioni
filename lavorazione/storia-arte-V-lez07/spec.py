import json,re
PC=json.load(open('/tmp/claude-0/w/build/pdf_cards.json'))
FIX=[('antiacademica','antiaccademica'),('fauvet','fauve'),('’',"'")]
def fix(t):
    for a,b in FIX:t=t.replace(a,b)
    return t
def cards(p):return [fix(c) for c in PC[str(p)]['cards'] if c.strip()]
def ptitle(p):return fix(PC[str(p)]['titolo'])
# (primo suono del docente, ultimo suono) per argomento; i tagli veri vengono spostati nella pausa piu' vicina
T=[
 dict(n=1,short="Il nuovo volto di Parigi",pdf=2,t=(1.3,408.7),
      kw=["Avanguardia","Avant-garde","Belle Époque","Primitivismo","Parigi 1900"],
      cards=[(0,101.7),(1,154.6),(2,212.4),(3,250.4),(4,267.1)],imgs=[]),
 dict(n=2,short="Matisse e i Fauves",pdf=3,t=(411.5,785.1),
      kw=["Fauves","Salon d'Automne","Louis Vauxcelles","La felicità di vivere","Colore puro"],
      cards=[(0,689.1),(1,704.0),(2,752.6),(4,775.6)],
      imgs=[(472.6,'luxe'),(520.2,'felicita'),(559.0,'luxe'),(584.0,'felicita')]),
 dict(n=3,short="L'evoluzione di Matisse",pdf=6,t=(785.8,1025.5),
      kw=["Manifesto del 1908","La Danza","Shchukin","Odalische","Papiers découpés"],
      cards=[(0,799.9),(1,838.1),(2,933.9),(3,966.6)],imgs=[(880.7,'danza')]),
 dict(n=4,short="Picasso e Braque",pdf=8,t=(1026.3,1349.2),
      kw=["Periodo blu","Periodo rosa","Les Demoiselles d'Avignon","Maschere africane","Georges Braque"],
      cards=[(3,1051.0),(0,1064.2),(1,1239.6),(2,1292.7)],
      imgs=[(1090.5,'vita'),(1138.8,'acrobata'),(1246.9,'demoiselles')]),
 dict(n=5,short="Le fasi del Cubismo",pdf=11,t=(1349.7,1692.5),
      kw=["Protocubismo","Cubismo Analitico","Tavolozza monocroma","Cubismo Sintetico","Papiers collés"],
      cards=[(0,1352.0),(1,1406.6),(2,1414.8),(3,1571.4),(4,1605.4)],
      imgs=[(1430.4,'vollard'),(1501.7,'violino_tavolozza'),(1613.0,'fruttiera')]),
 dict(n=6,short="Cubismo dei Salons, Orfismo e scultura",pdf=13,t=(1693.8,1876.2),
      kw=["Cubismo dei Salons","Orfismo","Scultura cubista","Assemblages","Brâncuși"],
      cards=[(0,1703.6),(1,1753.0),(2,1772.7),(3,1812.7),(4,1863.9)],imgs=[(1821.0,'chitarra')]),
 dict(n=7,short="Rousseau, Chagall e Modigliani",pdf=15,t=(1879.0,2288.7),
      kw=["Montparnasse","Rousseau il Doganiere","Marc Chagall","Modigliani","Pittura naïf"],
      cards=[(0,1933.6),(1,1944.5),(2,1984.5),(3,2122.6)],
      imgs=[(2008.3,'chagall_io'),(2060.8,'chagall_parigi'),(2156.7,'nudo'),(2206.9,'jeanne')]),
]
CAP={'luxe':"Henri Matisse · Lusso, calma e voluttà · 1904",
 'felicita':"Henri Matisse · La felicità di vivere · 1905-06",
 'danza':"Henri Matisse · La danza · 1909-10",
 'vita':"Pablo Picasso · La vita · 1903",
 'acrobata':"Pablo Picasso · Acrobata e giovane equilibrista · 1905",
 'demoiselles':"Pablo Picasso · Les Demoiselles d'Avignon · 1907",
 'vollard':"Pablo Picasso · Ritratto di Ambroise Vollard · 1910",
 'violino_tavolozza':"Georges Braque · Violino e tavolozza · 1909",
 'fruttiera':"Georges Braque · Fruttiera e bicchiere · 1912",
 'chitarra':"Pablo Picasso · Chitarra · 1912-14",
 'chagall_io':"Marc Chagall · Io e il mio villaggio · 1911",
 'chagall_parigi':"Marc Chagall · Parigi attraverso la finestra · 1913",
 'nudo':"Amedeo Modigliani · Nudo disteso · 1917",
 'jeanne':"Amedeo Modigliani · Ritratto di Jeanne Hébuterne · 1919"}
