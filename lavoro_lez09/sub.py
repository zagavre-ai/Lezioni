# Sottotitoli .vtt sul video finale: prof (ASR con termini corretti) + voci Kore (testo noto, numeri in cifre). uso: python3 sub.py PARTE
import sys,os,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spec import SEG,mmss
from cifre import cifre
W='/home/user/Lezioni/w/lav/out'
TESTI={x['nome']:x['testo'] for x in json.load(open('/home/user/Lezioni/w/wt_voci/scambio/storia-V-lez09/testi_voci.json'))}
FIX=[(r'\blegge a? ?cerb[oa]\b','legge Acerbo'),(r'\b(?:a|i)?[yY]ar\b','EIAR'),(r'\bAdisabba\b','Addis Abeba'),(r'\bGentili\b','Gentile'),(r'\briforma gentile\b','riforma Gentile'),(r'\bbalille\b','Balilla'),
 (r'\bbalilla\b','Balilla'),(r'\bo ND\b','OND'),(r'\bovra\b','OVRA'),(r'\bIMS e inail\b','INPS e INAIL'),(r'\bInps\b','INPS'),(r'\bIri\b','IRI'),(r'\bgif\b','GIL'),(r'\bNemmi\b','Nenni'),
 (r'\bTranensi\b','Lateranensi'),(r'\bda Tranensi\b','Lateranensi'),(r'\bMincul ?[Pp]op\b','MinCulPop'),(r'\bminculpop\b','MinCulPop'),(r'\bitleriana\b','hitleriana'),(r'\bAlessa Lassie\b','Hailé Selassié'),
 (r'\bpuribiscitario\b','plebiscitario'),(r'\bfasciolittorio\b','fascio littorio'),(r'\bfascistiazione\b','fascistizzazione'),(r'\bRoma Berlino\b','Roma-Berlino'),(r'\bfascio Littorio\b','fascio littorio'),
 (r'\bspinelli\b','Spinelli'),(r'\brossi\b','Rossi'),(r'\bGistuti\b','Istituti'),(r'\bGran consiglio\b','Gran Consiglio'),(r'\bgrande? consiglio\b','Gran Consiglio')]
def fix(t):
    for a,b in FIX:t=re.sub(a,b,t)
    return t
def ts(s):
    h=int(s//3600);m=int(s%3600//60);x=s%60;return '%02d:%02d:%06.3f'%(h,m,x)
def chunks(text,n=76):
    w=text.split();out=[];cur=''
    for x in w:
        if len(cur)+len(x)+1>n and cur:out.append(cur);cur=x
        else:cur=(cur+' '+x).strip()
    if cur:out.append(cur)
    return out
def wrap(t,n=42):
    c=chunks(t,n);return '\n'.join(c[:2]) if len(c)>1 else t
def cues_voice(t0,t1,text):
    ch=chunks(text);L=sum(len(c) for c in ch);acc=0;out=[]
    for c in ch:
        a=t0+(t1-t0)*acc/L;acc+=len(c);b=t0+(t1-t0)*acc/L;out.append((a,b-0.05,c))
    return out
def main(parte):
    TL=json.load(open(W+f'/timeline_Parte{parte}.json'));C=[];MAN=dict(json.load(open(W+f'/parte{parte}_pezzi.json')))
    for n,s,d in TL:
        if re.fullmatch(r'D\d+',n):
            fn='D0' if n=='D0' else 'A'+n[1:]
            info=json.load(open(W+f'/{fn}.json')) if os.path.exists(W+f'/{fn}.json') else None
            if info is None:continue
            segs=info['segs'];
            def f(t):
                acc=0
                for a,b in segs:
                    if a<=t<=b:return acc+t-a
                    acc+=b-a
                return None
            for sg in SEG:
                if not any(a<=sg['inizio']<=b for a,b in segs):continue
                a=f(sg['inizio']);b=f(min(sg['fine'],segs[-1][1]))
                if a is None:continue
                if b is None:b=a+1
                text=fix(sg['testo'].strip())
                if not text:continue
                for x,y,c in cues_voice(s+a,s+b,text):C.append((x,y,c))
        else:
            evp=MAN.get(n,'')+'.ev.json';ev=os.path.exists(evp) and json.load(open(evp))
            if not ev:continue
            from lezione import ARGT
            for st,vn in ev:
                import subprocess
                wp=None
                for dd in ('/home/user/Lezioni/w/wt_voci/scambio/storia-V-lez09/vox','/home/user/Lezioni/w/vox_old',W+'/vox_prov'):
                    if os.path.exists(f'{dd}/{vn}.wav'):wp=f'{dd}/{vn}.wav';break
                du=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',wp],capture_output=True,text=True).stdout)
                for x,y,c in cues_voice(s+st,s+st+du,cifre(TESTI[vn])):C.append((x,y,c))
    C.sort();out=['WEBVTT\n']
    for i,(x,y,c) in enumerate(C):
        y=min(y,C[i+1][0]-0.02) if i+1<len(C) and y>C[i+1][0] else y
        out.append(f'{ts(x)} --> {ts(max(y,x+0.4))}\n{wrap(c)}\n')
    open(W+f'/Storia_Lez9_Parte{parte}.vtt','w').write('\n'.join(out));print('cue',len(C))
if __name__=='__main__':main(int(sys.argv[1]))
