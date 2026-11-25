import sys,os,json,re,subprocess,shutil
sys.path.insert(0,'/tmp/w/b')
from plan import *
from go import seq_with_pages
OUTD=os.environ.get('OUTD','/tmp/w/out');os.makedirs(OUTD,exist_ok=True)
def tlname(n,p):
    m={f'P{p}_SIGLA':'SIGLA',f'P{p}_GL':'GL',f'P{p}_RF':'RF',f'P{p}_FIN':'FIN',f'P{p}_VER':'VER',f'P{p}_SFIN':'SFIN',f'P{p}_CINTRO':'CINTRO',f'P{p}_COMP':'COMP',f'P{p}_RIP2':'RIP2'}
    if n in m: return m[n]
    if n.startswith('AN_'): return n[3:]
    if n.startswith('MAP_'): return 'MAP'+n[4:]
    if n.startswith('R_'): return 'R'+n[2:]
    return n
FIX=[(r'\b[Bb]elle [EÈéÉ]?po\w*','Belle Époque'),(r'\bpastorizzazione\b','pastorizzazione'),(r'\bpasteur\b','Pasteur'),(r'\bnovecento\b','Novecento'),(r'\bottocento\b','Ottocento')]
def fixtxt(t):
    for a,b in FIX: t=re.sub(a,b,t)
    return t
def wrap2(t,w=42):
    ws=t.split();ls=[];cur=''
    for x in ws:
        if len((cur+' '+x).strip())<=w: cur=(cur+' '+x).strip()
        else: ls.append(cur);cur=x
    if cur: ls.append(cur)
    return '\n'.join(ls)
def chunks(text,t0,t1,maxc=80):
    ws=text.split();out=[];cur=[]
    for w in ws:
        if len(' '.join(cur+[w]))>maxc and cur: out.append(cur);cur=[w]
        else: cur.append(w)
    if cur: out.append(cur)
    tot=sum(len(' '.join(c)) for c in out) or 1;t=t0;res=[]
    for c in out:
        d=(t1-t0)*len(' '.join(c))/tot;res.append((t,t+d,' '.join(c)));t+=d
    return res
def teacher_cues(a,b,off):
    cues=[];cur=[];st=None
    def flush(en):
        nonlocal cur,st
        if cur:
            txt=fixtxt(''.join(x for _,x in cur).strip())
            if txt: cues.append((off+st-a,off+en-a,txt))
        cur=[];st=None
    from common import SEG
    for s in SEG:
        for t,tok in s['parole']:
            if t<a or t>=b: continue
            if st is None: 
                if not tok.strip(): continue
                st=t
            cur.append((t,tok))
            txt=''.join(x for _,x in cur)
            end_p=re.fullmatch(r'\s*[.?!]+\s*',tok) or (tok.strip() in(',',';') and len(txt)>40)
            if end_p or len(txt)>78 or t-st>5.5: flush(t+0.25)
        # segment end
        if cur and s['fine']<b: flush(min(s['fine'],cur[-1][0]+0.6))
    flush(b-0.1)
    # merge too-short and clamp overlaps
    out=[]
    for a_,b_,t in cues:
        if out and a_<out[-1][1]: a_=out[-1][1]
        if b_-a_<0.3: b_=a_+0.3
        out.append((a_,b_,t))
    return out
def vt(t): 
    h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
def assemble(p):
    seq=seq_with_pages(p);pcs=[];t=0.0;TL=[];cues=[]
    for sp in seq:
        n=spec_name(sp);f=f'{PC}/{n}.done'
        if not os.path.exists(f):
            if os.environ.get('SKIPMISSING'): print('SKIP',n);continue
            raise SystemExit('manca '+n)
        r=json.load(open(f));r['start']=t;pcs.append(r);TL.append([tlname(n,p),round(t,3),round(r['dur'],3)])
        if sp[0] in('teach','d0'):
            a,b=r['src'];cues+=teacher_cues(a,b,t)
        for (s,e,tx) in r.get('cues',[]):
            if sp[0]=='map' or True:
                for (cs,ce,ct) in chunks(digits(tx),t+s,t+e): cues.append((cs,ce,ct))
        t+=r['dur']
    nm=f'Storia_Lez1_Parte{p}'
    lst=f'{OUTD}/{nm}.vlist.txt';open(lst,'w').write(''.join(f"file '{r['v']}'\n" for r in pcs))
    alst=f'{OUTD}/{nm}.alist.txt';open(alst,'w').write(''.join(f"file '{r['a']}'\n" for r in pcs))
    vo=f'{OUTD}/{nm}.v.mp4';ao=f'{OUTD}/{nm}.a.wav'
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',vo])
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',alst,'-c','copy',ao])
    L=lufs(ao);g=-16.0-L
    print('part',p,'LUFS',L,'gain',g)
    final=f'{OUTD}/{nm}_1080p.mp4'
    sh(['ffmpeg','-v','error','-y','-i',vo,'-i',ao,'-map','0:v','-map','1:a','-af',f'volume={g:.2f}dB,alimiter=limit=0.80:level=0','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',final])
    json.dump(TL,open(f'{OUTD}/timeline_Parte{p}.json','w'))
    cues.sort()
    with open(f'{OUTD}/{nm}.vtt','w') as fv:
        fv.write('WEBVTT\n\n')
        last=0
        for s,e,tx in cues:
            s=max(s,last);e=max(e,s+0.3);last=e
            fv.write(f'{vt(s)} --> {vt(e)}\n{wrap2(tx)}\n\n')
    return final,TL
if __name__=='__main__':
    for p in [int(x) for x in sys.argv[1:]]: print(assemble(p)[0])
