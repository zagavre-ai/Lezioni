import sys;sys.path.insert(0,'/tmp/w/tools')
from plan import *
import plan
KMAP={1:[1,1,2,3,4],2:[1,1,2,3,4],3:[1,2,3]}
def char_starts(sents,d,lead=0.2,tail=0.4):
    tot=sum(len(s) for s in sents);c=0;res=[]
    for s in sents:
        res.append(lead+c/tot*(d-lead-tail));c+=len(s)
    return res
def seg_map(n):
    mi,img,mt,zones=MAPS[n];arg=ARG[n-1];name=f'MAPA{mi}'
    from PIL import Image
    sz=Image.open('/tmp/w/mat/'+img).size
    sents=split_sents(TX[name]);d=vdur(name);off=0.8;pgn=newpage()
    st=[off+t for t in char_starts(sents,d)];ks=KMAP[mi]
    dur=off+d+1.5
    def pk(k): return S(f'map{mi}_{k}',lambda k=k:SL.mappa(n,'/tmp/w/mat/'+img,sz,zones,k,pgn,arg['titolo']))
    seq=[[pk(0),fr(st[0])]]
    for i in range(len(sents)):
        end=st[i+1] if i+1<len(sents) else dur
        seq.append([pk(ks[i]) if False else pk(ks[i]),fr(end)-fr(st[i])])
    tot=sum(f for _,f in seq);seq[-1][1]+=fr(dur)-tot
    return dict(id=f'map{mi}',k='seq',seq=seq,frames=sum(f for _,f in seq),aud=[voice(name,off)])
def seg_pill(n):
    arg=ARG[n-1];name=f'PIL{n}';d=vdur(name)
    sents=split_sents(TX[name]);voff=3.5
    st=[voff+t for t in char_starts(sents,d,0.05,0.1)]
    dur=max(14.0,voff+d+1.5);dur=q(dur)
    caps=[]
    for i,s_ in enumerate(sents):
        a=st[i]-0.1;b=(st[i+1]-0.05) if i+1<len(sents) else voff+d+0.6
        caps.append([round(a,2),round(b,2),s_])
    spec={"type":"repaso","kicker":"Pillola di storia","big":"RIPASSO","topic":arg['breve'],"tfs":tfs(arg['breve'],1500,84,52),"caps":caps,"dur":dur}
    os.makedirs('/tmp/w/build/specs',exist_ok=True);json.dump(spec,open(f'/tmp/w/build/specs/p{n:02d}.json','w'),ensure_ascii=False)
    return dict(id=f'p{n:02d}',k='card',mp4=f'/tmp/w/cards/p{n:02d}.mp4',frames=fr(dur),aud=[snd('repaso',0),voice(name,voff)])
def seg_schema(n):
    arg=ARG[n-1];name=f'R{n}';rows=ROWS[n]
    RS=[x.strip() for x in re.split(r'(?<=[.;])\s+',TX[name]) if x.strip()];sents=RS[1:]
    assert len(sents)==len(rows),(n,len(sents),len(rows))
    rg=ranges(name,RS)[1:]
    pgn=newpage();off=0.6;t=off;PAUSE=2.4
    aud=[];ts=[]
    for (a,b) in rg:
        ts.append(t);aud.append(A(VN+name+'.wav',t,1.0,a,b));t+=(b-a)+PAUSE
    dur=t+3.0-PAUSE+0.6
    kicker=arg['titolo']
    def pk(k,hi=True): return S(f's{n:02d}_{k}{"h" if hi else ""}',lambda k=k,hi=hi:SL.schema(n,arg['breve'],arg['breve'],rows,k,pgn,hi))
    seq=[[pk(0,False),fr(ts[0])]]
    for k in range(len(rows)):
        end=ts[k+1] if k+1<len(rows) else t-PAUSE+0.5
        seq.append([pk(k+1),fr(end)-fr(ts[k])])
    seq.append([pk(len(rows),False),fr(dur)-sum(f for _,f in seq)])
    return dict(id=f's{n:02d}',k='seq',seq=seq,frames=sum(f for _,f in seq),aud=aud)
RIP=[("La crisi di fine secolo","Adua, i morti di Milano e il regicidio portano alla svolta liberale"),("La nuova linea di Giolitti","Dal 1903 lo Stato è un mediatore neutrale: niente forza contro gli scioperi"),("I socialisti","Dialogo con i riformisti di Turati; lo sciopero del 1904 si esaurisce da solo"),("I cattolici","Pio X permette il voto; Giolitti governa con il trasformismo"),("Le riforme","Tutela dei lavoratori e lotta all'analfabetismo")]
def seg_rip2():
    name='RIP2';sents0=split_sents(TX[name]);d=vdur(name)
    rg=ranges(name,sents0);off=1.0;pgn=newpage()
    # frasi: 0 intro, 1..5 argomenti, 6 chiusura
    ts=[off+a for a,b in rg]
    def pk(k,hi=True): return S(f'rip2_{k}{"h" if hi else ""}',lambda k=k,hi=hi:SL.schema(0,"Ripasso della Parte 1","Ripasso della Parte 1",RIP,k,pgn,hi,label="RIPASSO DELLA PARTE 1",kicker="STORIA V · RIPASSO DELLA PARTE 1"))
    dur=off+d+1.5
    seq=[[pk(0,False),fr(ts[1])]]
    for k in range(5):
        end=ts[k+2] if k+2<len(ts) else dur
        seq.append([pk(k+1),fr(end)-fr(ts[k+1])])
    tot=sum(f for _,f in seq);seq[-1][1]+=fr(dur)-tot
    return dict(id='rip2',k='seq',seq=seq,frames=sum(f for _,f in seq),aud=[voice(name,off)])
def seg_final(p,rf,fin,card):
    d=vdur(rf)+0.6+vdur(fin)+1.7
    return dict(id=f'riep{p}',k='card',mp4=f'/tmp/w/cards/{card}.mp4',frames=fr(round(d,1)),aud=[voice(rf,0.4),voice(fin,0.4+vdur(rf)+0.6)])
def seg_sigla(): return dict(id='sigla',k='mp4',mp4='/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4',frames=fr(15),aud=[A('/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4',0,1.0)])
def seg_fine(): return dict(id='fine',k='mp4',mp4='/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4',frames=fr(5),aud=[A('/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4',0,1.0),snd('finale',0)])
def seg_cover(prof):
    pgn=1
    args=[a['titolo'] for a in ARG]
    key='cover_prof' if prof else 'cover_ben'
    p=S(key,lambda:SL.cover("L'Italia di Giolitti",args,prof,1,notice=not prof))
    return p
