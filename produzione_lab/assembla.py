# -*- coding: utf-8 -*-
# Assemblaggio: lista, timeline, sottotitoli, quiz, scheda, dispensa. uso: assembla.py spec WORKDIR FASE
import sys,os,json,re,subprocess,importlib,difflib
sys.path.insert(0,'/home/user/work/build');sys.path.insert(0,'/home/user/Lezioni/kit/tools')
S=importlib.import_module(sys.argv[1]);W=os.path.abspath(sys.argv[2])+'/';FASE=sys.argv[3]
import voci as VO,anchors as AN
def sh(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(' '.join(map(str,c))[:200]+'\n'+r.stderr[-600:])
    return r.stdout
def dur(f):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
ORD={int(k):v for k,v in json.load(open(W+'ordine.json')).items()}
PT=VO.parti(S);P=int(sys.argv[4]) if len(sys.argv)>4 else 1
def lista(P=P):
    L=''.join("file '%sseg/%s.mp4'\n"%(W,n) for n in ORD[P]);open(W+'lista%d.txt'%P,'w').write(L)
    t=0;TL=[]
    for n in ORD[P]:
        d=dur(W+'seg/%s.mp4'%n);TL.append([n,round(t,3),round(d,3)]);t+=d
    json.dump(TL,open(W+'timeline%d.json'%P,'w'));print('durata totale',round(t,1),'s =',round(t/60,1),'min')
    return TL
def vtt_tempo(t):return '%02d:%02d:%06.3f'%(t//3600,t%3600//60,t%60)
def righe(txt,mx=42):
    w=txt.split();L=[];cur=''
    for x in w:
        if len(cur)+len(x)+1>mx and cur:L.append(cur);cur=x
        else:cur=(cur+' '+x).strip()
    if cur:L.append(cur)
    return L
def cue_da_testo(t0,t1,txt,out):
    """spezza il testo in blocchi da max 2 righe x 42 car, tempo proporzionale ai caratteri"""
    txt=re.sub(r'\s+',' ',txt).strip()
    if not txt:return
    fr=re.split(r'(?<=[\.\?\!;:])\s+',txt);bl=[];cur=''
    for f in fr:
        if len(cur)+len(f)+1<=84:cur=(cur+' '+f).strip()
        else:
            if cur:bl.append(cur)
            cur=f
            while len(cur)>84:
                k=cur.rfind(' ',0,84);bl.append(cur[:k]);cur=cur[k+1:]
    if cur:bl.append(cur)
    tot=sum(len(b) for b in bl);t=t0
    for b in bl:
        d=(t1-t0)*len(b)/tot;out.append((t,t+d-0.05,righe(b)[:2] if len(righe(b))<=2 else righe(b)));t+=d
def correggi(txt,vocab):
    out=[]
    for w in re.findall(r"\w+|\W+",txt):
        if w.isalpha() and len(w)>=5 and w.lower() not in vocab:
            m=difflib.get_close_matches(w.lower(),vocab_list,1,0.82)
            if m:w=m[0].capitalize() if w[0].isupper() else m[0]
        out.append(w)
    return ''.join(out)
def vtt(TL,P=1):
    global vocab_list
    pdf=open(W+'pdf.txt').read().lower()
    vocab=set(re.findall(r"[a-zàèéìòù]{4,}",pdf));
    for a in S.ARGS:
        for sl in a['slides']:
            for c in sl['c']+[sl['t']]:vocab|=set(re.findall(r"[a-zàèéìòù]{4,}",c.lower()))
    vocab_list=sorted(vocab)
    base=json.load(open(W+'trascr.json'));ali=json.load(open(W+'ali.json'));tg=json.load(open(W+'tagli.json'))
    cues_v=json.load(open(W+'cues_voci.json'))
    out=[];tot=None
    for i,(n,st,ln) in enumerate(TL):
        if re.match(r'^D\d+$',n):
            k=int(n[1:]);a=[x for x in range(len(S.ARGS)) if S.ARGS[x]['n']==k][0]
            lo=tg[a];hi=tg[a+1] if a+1<len(tg) else 1e9
            for b in base:
                if b['e']<=lo or b['s']>=hi:continue
                iv=[x for x in ali if x['s']>=b['s']-0.3 and x['e']<=b['e']+0.3 and x['e']>lo and x['s']<hi]
                if not iv:continue
                sp=sum(x['e']-x['s'] for x in iv);txt=correggi(b['t'],vocab)
                # tempo reale di inizio/fine del chunk base = primo/ultimo intervallo di parlato; suddivisione per ore di parlato
                fr=re.split(r'(?<=[\.\?\!;:])\s+',re.sub(r'\s+',' ',txt).strip());bl=[];cur=''
                for f in fr:
                    if len(cur)+len(f)+1<=84:cur=(cur+' '+f).strip()
                    else:
                        if cur:bl.append(cur)
                        cur=f
                        while len(cur)>84:
                            q=cur.rfind(' ',0,84);bl.append(cur[:q]);cur=cur[q+1:]
                if cur:bl.append(cur)
                tc=sum(len(x) for x in bl);acc=0
                def reale(x):   # x = secondi di parlato -> tempo sorgente
                    for v in iv:
                        d=v['e']-v['s']
                        if x<=d:return v['s']+x
                        x-=d
                    return iv[-1]['e']
                for q in bl:
                    a0=sp*acc/tc;acc+=len(q);a1=sp*acc/tc
                    s0=reale(a0)-lo+st;s1=reale(a1)-lo+st
                    if s1-s0<0.6:s1=s0+0.6
                    out.append((max(st,s0),min(st+ln,s1),righe(q)))
        elif n in cues_v:
            for t,d,tx in cues_v[n]:cue_da_testo(st+t,st+t+d,tx,out)
    out.sort(key=lambda x:x[0])
    # evita sovrapposizioni
    for k in range(len(out)-1):
        if out[k][1]>out[k+1][0]-0.02:out[k]=(out[k][0],out[k+1][0]-0.02,out[k][2])
    with open(W+'%s_Parte%d.vtt'%(S.FILE,P),'w') as f:
        f.write('WEBVTT\n\n')
        for t0,t1,r in out:
            if t1-t0<=0.2:continue
            if len(r)<=2:f.write('%s --> %s\n%s\n\n'%(vtt_tempo(t0),vtt_tempo(t1),'\n'.join(r)))
            else:
                h=(len(r)+1)//2;tm=t0+(t1-t0)*len(' '.join(r[:h]))/len(' '.join(r))
                f.write('%s --> %s\n%s\n\n'%(vtt_tempo(t0),vtt_tempo(tm),'\n'.join(r[:h])));f.write('%s --> %s\n%s\n\n'%(vtt_tempo(tm+0.02),vtt_tempo(t1),'\n'.join(r[h:])))
    print('vtt cues',len(out))
def quiz_files(TL,P=1):
    Q0=VO.quiz(S);Q={k:v for k,v in Q0.items() if int(k[1:]) in PT[P-1]['args']};json.dump(Q,open(W+'quiz_argomenti%d.json'%P,'w'),ensure_ascii=False,indent=1)
    with open(W+'Quiz_%s_Parte%d.txt'%(S.FILE,P),'w') as f:
        f.write('QUIZ · %s · %s\nPer continuare: almeno l\'80%% di risposte corrette. La prima risposta è quella giusta.\n\n'%(S.TITOLO,S.DOCENTE))
        for k,q in Q.items():
            f.write('== %s ==\n'%q['title'])
            for i,d in enumerate(q['domande'],1):
                f.write('%d. %s\n   A) %s  [GIUSTA]\n'%(i,d['domanda'],d['giusta']))
                for L,s in zip('BCD',d['sbagliate']):f.write('   %s) %s\n'%(L,s))
                f.write('   Spiegazione: %s\n'%d['spiegazione'])
            f.write('\n')
def scheda(TL,video,P=1):
    sh([sys.executable,'/home/user/Lezioni/kit/tools/scheda_da_timeline.py',video,W+'timeline%d.json'%P,W+'quiz_argomenti%d.json'%P,'%s · Parte %d'%(PT[P-1].get('titolo',S.TITOLO) if len(PT)==1 else S.TITOLO,P),W+'scheda_pubblicazione%d.json'%P,S.MATERIA])
    sc=json.load(open(W+'scheda_pubblicazione%d.json'%P));t={n:s for n,s,l in TL}
    if 'FI%d'%P in t:sc['t_verifica']=round(t['FI%d'%P],3);sc['t_compiti']=round(t['CI'],3)
    json.dump(sc,open(W+'scheda_pubblicazione%d.json'%P,'w'),ensure_ascii=False,indent=1)
TLF=lambda:json.load(open(W+'timeline%d.json'%P))
if FASE=='lista':lista()
elif FASE=='vtt':vtt(TLF(),P)
elif FASE=='quiz':quiz_files(TLF(),P)
elif FASE=='scheda':scheda(TLF(),sys.argv[5],P)
