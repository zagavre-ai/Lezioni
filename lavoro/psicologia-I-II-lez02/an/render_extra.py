import sys,json,os
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez02/an')
import render_an as R
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/psicologia-I-II-lez02/'
GL=[("Psicologia","letteralmente scienza dell'anima; studia il comportamento e i processi mentali dell'essere umano"),
("Attività mentali","operazioni come ricordare, ragionare e immaginare"),
("Dualismo","per Cartesio, la netta differenza tra mente e corpo"),
("Substrato biologico","il cervello, strumento biologico della mente"),
("Legge psicofisica","la relazione matematica tra l'intensità di uno stimolo fisico e quella della sensazione percepita"),
("Tempi di reazione","il metodo per misurare la durata delle operazioni mentali"),
("Strutturalismo","la mente come struttura formata da un aggregato di elementi più semplici"),
("Funzionalismo","lo studio di a che cosa servono i processi mentali"),
("Gestalt","la mente organizza le informazioni in modo globale; il tutto è diverso dalla somma delle parti"),
("Comportamentismo","la psicologia studia solo ciò che è osservabile, il comportamento"),
("Cognitivismo","la mente come elaboratore attivo di informazioni"),
("Epistemologia genetica","lo studio delle origini e dello sviluppo delle capacità cognitive"),
("Psicologia dell'emergenza","la branca che interviene nelle situazioni straordinarie e traumatiche")]
RF=[["La mente e le origini",["Psicologia: scienza dell'anima, studia il comportamento e i processi mentali","Platone e Aristotele · Cartesio (1641): il dualismo tra mente e corpo"],[1,2]],
["Il cervello",["Strumento biologico della mente","Il caso di Phineas Gage (1848): lesione, emozioni e personalità"],[3]],
["Dalla fisiologia alla psicologia",["I fisiologi: dall'hardware al software","Fechner: legge psicofisica · Donders: tempi di reazione"],[4]],
["Wundt e lo strutturalismo",["1879: a Lipsia il primo laboratorio di psicologia","Strutturalismo: la mente si scompone in elementi semplici"],[5]],
["Funzionalismo e Gestalt",["Funzionalismo: a che cosa servono i processi mentali","Gestalt: la mente come un tutto organizzato"],[6]],
["Comportamentismo e cognitivismo",["Comportamentismo: solo il comportamento osservabile","Cognitivismo: la mente come un computer"],[7]],
["Jean Piaget",["Epistemologia genetica","Quattro stadi dello sviluppo della mente"],[8]],
["La psicologia oggi",["Molte aree di ricerca e di applicazione","Fino alla psicologia dell'emergenza"],[9]]]
REP=[('Fìnias Ghèig','Phineas Gage'),('Fèkner','Fechner'),('Dònders','Donders'),('Vilhelm Vunt','Wilhelm Wundt'),('Vunt','Wundt'),('Ghestàlt','Gestalt'),('Piagè','Piaget'),('Gùstav','Gustav'),('Èdward Tìcena','Edward Titchener'),('Uìlliam Gèims','William James'),('Vertàimer','Wertheimer'),('Gion Uòtson','John Watson'),('Còvid diciannove','Covid-19'),('milleseicentoquarantuno','1641'),('milleottocentoquarantotto','1848'),('milleottocentosettantanove','1879')]
def cap(s):
    for a,b in REP:s=s.replace(a,b)
    return s
TIT={'GL1':'Le parole chiave','RF1':'Ripasso finale'};EY={'GL1':'Glossario','RF1':'Ripasso finale'};SRC={'GL1':'GLX','RF1':'RFX'}
def spec(k):
    m=json.load(open(D+'voci/wav/meta_S1.json'))[SRC[k]];P=[p+0.8 for p in m['phrases']]
    sp={'id':k,'title':TIT[k],'ey':EY[k],'P':P,'caps':[cap(p) for p in m['text']],'dur':round(m['dur']+0.8+2.5,2)}
    if k=='GL1':sp['gl']=[[a,b] for a,b in GL]
    if k=='RF1':sp['rf']=RF
    return sp
if __name__=='__main__':
    for k in sys.argv[1:]:
        sp=spec(k)
        if os.environ.get('SHOT'):
            ts=[float(x) for x in os.environ['SHOT'].split(',')]
            with sync_playwright() as p:
                b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
                errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
                pg.goto('file://'+D+'an/anim.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300);pg.evaluate("a=>init(a)",sp)
                for f in ts:
                    t=sp['P'][int(f)]+1.2 if f>=0 else sp['dur']-1;pg.evaluate("t=>draw(t)",t);pg.screenshot(path=D+f'fr/{k}_{int(f)}.png')
                print(k,sp['dur'],errs)
        else:R.render(sp,D+'an/'+k);print(k,sp['dur'],flush=True)
