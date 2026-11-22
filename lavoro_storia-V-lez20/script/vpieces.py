import sys;sys.path.insert(0,'/tmp/w/b')
from states import *
from voicelib import *
from pieces import *
SUF=lambda k:f'{k}'
def subs_from(S,ts,lead,D):
    out=[]
    for i,(x,t) in enumerate(zip(S,ts)):
        t1=(ts[i+1]-0.05) if i+1<len(ts) else D
        out.append((lead+t,lead+t1,x))
    return out
def tpiece(arg,part,reg_unused=None):
    n=f'T{arg}'
    png=want(titolo_arg(arg),f'T{arg}')
    return Piece(n,[(0,png)],lead=0,tail=0.5,trans=False,mixes=[(KIT+'/suoni/titolo.wav',0.3,0.0)],fixed_total=4.0,part=part)
def qpiece(arg,part):
    png=want(quiz_scheda(arg),f'Q{arg}')
    return Piece(f'Q{arg}',[(0,png)],lead=0,tail=0.5,trans=False,mixes=[(KIT+'/suoni/quiz.wav',0.5,0.0)],fixed_total=5.0,part=part)
def reveal_piece(name,eyebrow,title,voice,srcsent=None,part=1,tpx=70,lpx=46,sub=None,skip_first=False,extra_wav=None):
    """una voce, una frase alla volta (card gialla). Prima frase = titolo se e' domanda."""
    txt=srcsent or TV[voice];S,ts=sentence_times(voice,txt);S=[digits(x) for x in S]
    wav=prep_voice(voice);D=dur(wav)+0.5
    states=[]
    lead=0.8
    first_is_q=S[0].endswith('?')
    for i,(s,t) in enumerate(zip(S,ts)):
        if first_is_q and i==0:
            png=want(dark_html(eyebrow,S[0],tpx=tpx),f'{name}_t');states.append((0 if i==0 else lead+t,png));continue
        if skip_first and i==0:
            png=want(dark_html(eyebrow,title,tpx=tpx),f'{name}_t');states.append((0,png));continue
        ttl=S[0] if first_is_q else title
        png=want(dark_html(eyebrow,ttl,lines=[s],active=0,tpx=tpx if first_is_q else tpx,lpx=lpx,top=(400 if len(ttl)<45 else 480)),f'{name}_{i}')
        states.append((lead+t if i>0 else 0,png))
    states[0]=(0,states[0][1])
    p=Piece(name,states,audio=wav,D=D,part=part);p.subtitle=subs_from(S,ts,lead,D-0.5);return p
def pill_piece(arg,part,extra=None):
    """pillola di ripasso: jingle repaso, voce PI, righe PSk_n che si accendono"""
    A=ARGS[arg-1]
    ps=[f'PS{arg}_{i}' for i in range(1,8) if os.path.exists(f'/tmp/w/vox/PS{arg}_{i}.wav') or (extra and f'PS{arg}_{i}' in extra)]
    names=[f'PI{arg}']+ps
    srcs={}
    if extra:
        for k,v in extra.items(): srcs[k]=v
    wav,starts,D=concat_voices(f'pill{arg}',names,gap=0.5,srcs=srcs)
    lines=[digits(TV.get(n) or (extra or {}).get(n+'_t')) for n in ps]
    lead=1.0;states=[]
    for k in range(len(ps)+1):
        t=0 if k==0 else lead+starts[k]-0.05
        png=want(dark_html('RIPASSO',A['nome'],lines=lines[:k] if k else [],active=(k-1 if k else None),tpx=66,lpx=38,top=300),f'pill{arg}_{k}') if k else want(dark_html('RIPASSO',A['nome'],tpx=66),f'pill{arg}_0')
        states.append((t,png))
    p=Piece(f'PI{arg}',states,audio=wav,D=D+0.6,lead=lead,trans=False,mixes=[(KIT+'/suoni/repaso.wav',0.1,0.0)],part=part)
    tx=[digits(TV[n]) if n in TV else digits((extra or {}).get(n+'_t','')) for n in names]
    p.subtitle=[(lead+starts[i],lead+(starts[i+1]-0.1 if i+1<len(starts) else D),tx[i]) for i in range(len(names))]
    return p
def map_prof_piece(k,part):
    m=MAPPE_PROF[k];names=m['voci']
    wav,starts,D=concat_voices(f'mapp{k}',names,gap=0.4)
    lead=0.8;states=[];shown=set();allids=set(m['nodes'])
    # step 0: titolo + primo gruppo acceso
    steps=m['steps']
    ends=[starts[i+1]-0.4 if i+1<len(starts) else D for i in range(len(starts))]
    for i,st in enumerate(steps):
        shown|=set(st)
        png=want(map_html(m['titolo'],m['nodes'],m['edges'],set(shown),set(st)),f'mapp{k}_{i}')
        states.append((0 if i==0 else lead+starts[i]-0.1,png))
    # fine: mappa intera ferma 4 s
    fin=want(map_html(m['titolo'],m['nodes'],m['edges'],allids,set()),f'mapp{k}_fin')
    states.append((lead+D+0.1,fin))
    p=Piece(f'MAP{k}',states,audio=wav,D=D+4.2,part=part);p.subtitle=[(lead+starts[i],lead+(starts[i+1]-0.1 if i+1<len(starts) else D),digits(TV[n])) for i,n in enumerate(names)];return p,m['arg']
def map_own_piece(k,part,name=None):
    m=MAPPE_OWN[k];voce=m['voce'];wav=prep_voice(voce);D=dur(wav)
    S,ts=sentence_times(voce,TV[voce])
    n=len(m['rami']);lead=0.8
    ids=lambda j:{'c'}|{f'r{i}' for i in range(j)}
    states=[]
    st0=want(own_map_html(m['titolo'],m['centro'],m['rami'],{'c'},{'c'}),f'mapo{k}_c')
    states.append((0,st0))
    for j in range(n):
        a=ts[j+1] if j+1<len(ts) else ts[-1]
        png=want(own_map_html(m['titolo'],m['centro'],m['rami'],ids(j+1),{f'r{j}'}),f'mapo{k}_{j}')
        states.append((lead+a-0.05,png))
    fin=want(own_map_html(m['titolo'],m['centro'],m['rami'],ids(n),set()),f'mapo{k}_fin')
    states.append((lead+D+0.1,fin))
    return Piece(name or f'MAPO{k}',states,audio=wav,D=D+4.2,part=part)
def reveal_img_piece(name,eyebrow,title,voice,img,part=1,txt=None):
    from PIL import Image
    p=f'{B}/img/{img}.png';iw,ih=Image.open(p).size
    txt=txt or TV[voice];S,ts=sentence_times(voice,txt);S=[digits(x) for x in S]
    wav=prep_voice(voice);D=dur(wav)+0.5;lead=0.8;states=[]
    for i,(s,t) in enumerate(zip(S,ts)):
        png=want(dark_img_html(eyebrow,title,s,p,iw,ih),f'{name}_{i}');states.append((0 if i==0 else lead+t,png))
    p=Piece(name,states,audio=wav,D=D,part=part);p.subtitle=subs_from(S,ts,lead,D-0.5);return p
def spiegone_piece(arg,part,mapfin,img):
    """ripasso animato di un argomento: prima meta' con immagine del prof, seconda con la mappa di quell'argomento"""
    from PIL import Image
    voice=f'R{arg}';A=ARGS[arg-1];S,ts=sentence_times(voice,TV[voice]);S=[digits(x) for x in S]
    wav=prep_voice(voice);D=dur(wav)+0.6;lead=0.8;states=[];half=max(2,len(S)-2)
    p=f'{B}/img/{img}.png' if img else None
    for i,(s,t) in enumerate(zip(S,ts)):
        tt=0 if i==0 else lead+t
        if i<half or not mapfin:
            if p: iw,ih=Image.open(p).size; png=want(dark_img_html(f'RIPASSO · ARGOMENTO {arg}',A['nome'],s,p,iw,ih),f'sp{arg}_{i}')
            else: png=want(dark_html(f'RIPASSO · ARGOMENTO {arg}',A['nome'],lines=[s],active=0,tpx=64,lpx=44,top=330),f'sp{arg}_{i}')
        else: png=mapfin
        states.append((tt,png))
    p=Piece(f'SP{arg}',states,audio=wav,D=D,part=part);p.subtitle=subs_from(S,ts,lead,D-0.6);return p
