import json,re,subprocess,unicodedata
S=json.load(open('/home/user/w3/orig/trasc.json'))
def norm(w):
    w=unicodedata.normalize('NFD',w.lower()); w=''.join(c for c in w if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]','',w)
STOP=set('della delle degli dello nella nelle questo questa sono viene vengono molto anche quindi perche come dove cosi ecco essere stato stati loro tutti tutte nuovo nuovi quello quella dalla dalle sulla sulle ogni dopo prima'.split())
def stems(t): return {norm(w)[:5] for w in re.findall(r"[A-Za-zÀ-ÿ0-9]+",t) if len(norm(w))>=5 and norm(w) not in STOP}
ARGS={1:(148,1138),2:(1147,1448),3:(1448,1606),4:(1610,1764),5:(1786,2178),6:(2178,2616),7:(2616,2757),8:(2757,3157),9:(3157,3346),10:(3474,3793),11:(3801,4119)}
PDF='/home/user/w3/orig/sl/SLIDE/LEZIONE 3.pdf'
PAGE={1:2,2:4,3:5,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:17}
def cards(p):
    t=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'-layout',PDF,'-'],capture_output=True,text=True).stdout
    lines=[l.strip() for l in t.splitlines() if l.strip()]
    title=lines[0]; out=[]
    for l in lines[1:]:
        if re.match(r'^[A-ZÀ-Ý][^:]{2,70}:\s',l) and (not out or out[-1].rstrip().endswith('.')):
            out.append(l)
        else:
            if out: out[-1]+=' '+l
    return title,out
if __name__=='__main__':
    import sys
    for a,(t0,t1) in ARGS.items():
        title,cs=cards(PAGE[a]); seg=[(i,s) for i,s in enumerate(S) if s['inizio']>=t0-1 and s['inizio']<t1]
        n=len(cs); sc=[[len(stems(c)&stems(s['testo']))/ (1+0.15*len(stems(c))) for c in cs] for i,s in seg]
        # DP monotono
        import numpy as np
        m=len(seg); NEG=-1e9
        dp=[[NEG]*(n) for _ in range(m)]; bk=[[0]*n for _ in range(m)]
        for i in range(m):
            for k in range(n):
                best=NEG;arg=0
                if k==0: best=0
                for j in range(i):
                    if k>0 and dp[j][k-1]>best: best=dp[j][k-1]; arg=j
                if k==0 and False: pass
                dp[i][k]=best+sc[i][k]; bk[i][k]=arg
        k=n-1; i=max(range(m),key=lambda i:dp[i][k]); chosen=[None]*n
        while k>=0:
            chosen[k]=i; i=bk[i][k]; k-=1
        print(f'=== arg {a} {title} [{t0}-{t1}] {n} card')
        for k,c in enumerate(cs):
            s=seg[chosen[k]][1]; print(f'  c{k+1} t={s["inizio"]:.1f} sc={sc[chosen[k]][k]:.1f} | {c[:45]} || {s["testo"][:80]}')
