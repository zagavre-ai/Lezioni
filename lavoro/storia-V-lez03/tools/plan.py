# piano di montaggio della lezione 3 di Storia V
import json,sys,os,re,hashlib,bisect
sys.path.insert(0,'/tmp/w/tools')
from argom import ARG,ROWS,tfs
from num import to_digits
import slides as SL
import hl
VOX='/tmp/w/voci/scambio/storia-V-lez03/vox/'
VN='/tmp/w/vn/'
SND='/tmp/w/kit/home/claude/v5/snd/'
PNG='/tmp/w/build/png/';os.makedirs(PNG,exist_ok=True)
TX={x['nome']:x['testo'] for x in json.load(open('/tmp/w/vocirepo/scambio/storia-V-lez03/testi_voci.json'))}
SLT=json.load(open('/tmp/w/mat/slides_text.json'))
def fr(t): return round(t*30)
def q(t): return round(t*30)/30
import wave,contextlib
def vdur(n):
    with contextlib.closing(wave.open(VN+n+'.wav')) as w: return w.getnframes()/w.getframerate()
REQ={}   # png path -> funzione html
def S(key,html):
    p=PNG+key+'.png'
    REQ[p]=html;return p
# ---- tempi del prof (tagli su pause, mai a metà frase)
CUT=[0,149.6,1147.2,1447.1,1610.35,1786.5,2173.4,2614.9,2752.7,3153.85,3475.3,3800.8,4118.5]
IMG={1:(1138.0,'img_p3','Il regicidio di Umberto I e Giovanni Giolitti'),3:(1606.5,'img_p6','Filippo Turati, leader dei socialisti moderati'),
     4:(1763.5,'img_p8','Romolo Murri, il democratico-cristiano'),9:(3346.5,'img_p14','I flussi migratori italiani nel primo Novecento'),
     10:(3792.5,'img_p16','La guerra di Libia (1911-1912)')}
KEYS={1:["Adua","Crisi del pane","Bava Beccaris","Ostruzionismo","Regicidio"],2:["Neutralità dello Stato","Camere del lavoro","CGdL"],3:["Riformisti","Massimalisti","Sciopero del 1904"],
 4:["Non expedit","Pio X","Trasformismo"],5:["Legge Orlando","Daneo-Credaro","INA"],6:["Suffragio maschile","Indennità","Patto Gentiloni"],7:["Anna Kuliscioff","Lucciola","Delitto d'onore"],
 8:["Protezionismo","Banca mista","Ansaldo e Fiat"],9:["Triangolo industriale","Latifondo","Salvemini"],10:["Guerra in Libia","Pascoli","Trattato di Losanna"],11:["Salandra","Settimana rossa","Mussolini"]}
AN_T={1:"La crisi di fine secolo, tappa dopo tappa",2:"I protagonisti della crisi",3:"Che cosa cambia con Giolitti?",4:"Le organizzazioni dei lavoratori",5:"Riformisti e massimalisti",6:"Lo sciopero generale del 1904",
 7:"Chiesa e Stato italiano",8:"Che cos'è il trasformismo",9:"Le riforme sociali",10:"La scuola nell'età giolittiana",11:"Il suffragio universale maschile",12:"Il Patto Gentiloni",13:"Chi lotta per i diritti delle donne",
 14:"Le riforme mancate per le donne",15:"Dove si concentra l'industria",16:"Le grandi industrie del decollo",17:"Il Nord e il Sud a confronto",18:"L'emigrazione italiana",19:"La guerra di Libia (1911-1912)",
 20:"Perché Giolitti va in guerra",21:"Gli ultimi anni dell'età giolittiana",22:"Tre protagonisti alla fine di un'epoca"}
MAPS={2:(1,'map_1.png',"La svolta di Giolitti",[(0,0,1366,235),(0,235,1366,385),(0,620,683,491),(683,620,683,491)]),
      9:(2,'map_2.png',"Il decollo industriale",[(0,0,1420,290),(0,290,470,460),(470,290,480,460),(950,290,470,460)]),
      11:(3,'map_3.png',"La caduta di Giolitti",[(0,0,1317,165),(0,165,660,688),(660,165,657,688)])}
PAGE=[0]
def newpage(): PAGE[0]+=1;return PAGE[0]

# ---- allineamento frasi su trascrizione delle voci (cat_trasc)
_CAT=None
def cat():
    global _CAT
    if _CAT is None:
        seg=json.load(open('/tmp/w/cat_trasc.json'));man=json.load(open('/tmp/w/cat_man.json'))
        W=[]
        for s in seg:
            cur='';t0=None
            for t,p in s['parole']:
                if p.startswith(' ') and cur: W.append((t0,cur));cur='';t0=None
                if t0 is None:t0=t
                cur+=p
            if cur:W.append((t0,cur))
        _CAT=(W,man)
    return _CAT
def split_sents(text):
    ss=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()]
    return ss
def sent_starts(name,sents):
    """tempo di inizio (s, nel wav originale) di ogni frase, via conteggio parole"""
    W,man=cat();a,b=man[name]
    ws=[(t-a,w) for t,w in W if a-0.3<=t<=b+0.3]
    n=len(ws);tw=[len(s.split()) for s in sents];T=sum(tw);cum=0;res=[]
    for s,k in zip(sents,tw):
        idx=min(n-1,int(round(cum*n/T)));res.append(max(0,ws[idx][0]-0.05));cum+=k
    return res
def ranges(name,sents):
    st=sent_starts(name,sents);d=vdur(name)
    return [(st[i],(st[i+1]-0.08) if i+1<len(st) else d) for i in range(len(st))]
def merge_short(sents,mn=36):
    out=[]
    for s in sents:
        if out and len(s)<mn: out[-1]=(out[-1][0],out[-1][1]+' '+s)
        else: out.append((len(out),s))
    return out

def A(f,off=0,g=1.0,a=None,b=None): return dict(f=f,off=off,g=g,a=a,b=b)
def voice(n,off=0,g=1.0): return A(VN+n+'.wav',off,g)
def snd(n,off=0,g=0.9): return A(SND+n+'.wav',off,g)

def seg_title(n):
    return dict(id=f't{n:02d}',k='card',mp4=f'/tmp/w/cards/t{n:02d}.mp4',frames=fr(4),aud=[snd('titolo',0)])
def seg_quiz(n):
    return dict(id=f'q{n:02d}',k='card',mp4=f'/tmp/w/cards/q{n:02d}.mp4',frames=fr(5),aud=[snd('quiz',0.5)])
def seg_prof(n):
    a,b=CUT[n],CUT[n+1];t0=q(a);fr_=fr(b-a)
    pg=SLT_page(n)
    arg=ARG[n-1];cards=SLT[str(arg['page'])]['cards']
    pgn=newpage()
    tl=hl.viterbi(cards,a,b)
    nome=arg['breve'] if False else arg['titolo']
    kick=nome
    states=[]
    def txt(i): return S(f'a{n:02d}_s{i}',lambda i=i:SL.head(f"{n:02d} · {kick.upper()}",SLT[str(arg['page'])]['title'] if False else arg['titolo'])+SL.cards_html(cards,i)+SL.prof_panel(KEYS[n])+SL.foot("Storia V",pgn))
    last=None
    for t,c in tl:
        states.append([round(t-a,2),txt(int(c)),'cut'])
    if not states or states[0][0]>0: states.insert(0,[0.0,txt(-1),'cut'])
    else: states[0][0]=0.0
    if n in IMG:
        ti,im,title=IMG[n];pg2=newpage()
        p=S(f'a{n:02d}_img',lambda:SL.immagine(n,arg['titolo'],title,f'/tmp/w/mat/{im}.png',pg2,True,KEYS[n]))
        states=[s for s in states if s[0]<ti-a]+[[round(ti-a,2),p,'x']]
    return dict(id=f'prof{n:02d}',k='prof',t0=t0,frames=fr_,bg=states)
def SLT_page(n): return ARG[n-1]['page']

def an_states(i):
    name=f'AN{i}';text=to_digits(TX[name])
    sents=split_sents(text)
    if i==15: sents=sents[1:]          # tolta la frase «guardiamo sulla carta»: la carta non è nei materiali del prof
    sents0=split_sents(TX[name])
    st=sent_starts(name,sents0);d=vdur(name)
    if i==15: st=st[1:]
    # unisci frasi troppo corte alla precedente
    cards=[];starts=[]
    for s_,t_ in zip(sents,st):
        if cards and len(s_)<36: cards[-1]+=' '+s_
        else: cards.append(s_);starts.append(t_)
    return cards,starts,d
def seg_an(n,i):
    arg=ARG[n-1];cards,starts,d=an_states(i)
    off=0.8;pgn=newpage()
    if i==15: a0,a1=starts[0],None
    dur=off+(d-(starts[0] if i==15 else 0))+1.2
    seq=[];
    def pngk(k): return S(f'an{i:02d}_{k}',lambda k=k:SL.animaz(n,arg['titolo'],AN_T[i],cards,k,pgn))
    if i==19:
        pimg=S('an19_img',lambda:SL.immagine(n,arg['titolo'],AN_T[19],'/tmp/w/mat/img_p16.png',pgn,False))
        seq=[[pimg,fr(dur)]]
    else:
        t0s=starts[0] if i==15 else 0
        ts=[off+(t-t0s) for t in starts];ts[0]=min(ts[0],0.6)
        ts.append(dur)
        seq=[[pngk(0),fr(ts[0])]]
        for k in range(len(cards)): seq.append([pngk(k+1),fr(ts[k+1])-fr(ts[k])])
        tot=sum(f for _,f in seq);seq[-1][1]+=fr(dur)-tot
    a=A(VN+f'AN{i}.wav',off if i!=15 else off-0, 1.0, a=(starts[0] if i==15 else None))
    return dict(id=f'an{i:02d}',k='seq',seq=seq,frames=sum(f for _,f in seq),aud=[a])
def seg_gloss(parte,name):
    text=to_digits(TX[name]);ss=split_sents(text)[1:]
    st=sent_starts(name,split_sents(TX[name]))[1:]
    items=[tuple(s.split(':',1)) for s in ss];items=[(a.strip(),b.strip().rstrip('.')) for a,b in items]
    d=vdur(name);off=0.8;pgn=newpage()
    ts=[off+t for t in st]+[off+d+1.5]
    seq=[[S(f'gl{parte}_s',lambda:SL.glossario(parte,items,-1,pgn)),fr(ts[0])]]
    for k in range(len(items)): seq.append([S(f'gl{parte}_{k}',lambda k=k:SL.glossario(parte,items,k,pgn)),fr(ts[k+1])-fr(ts[k])])
    return dict(id=f'gloss{parte}',k='seq',seq=seq,frames=sum(f for _,f in seq),aud=[voice(name,off)])

