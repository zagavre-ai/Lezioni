#!/usr/bin/env python3
# Sottotitoli .vtt: voce del docente (trascrizione con i tempi, nomi corretti dal materiale del docente) + voci Kore (frasi del testo).
import os,sys,re,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build,voci
from asm import WK,dur_wav
FILL={'mm','um','uh','yeah','mm-hmm','eh','ah'}
FIX=[(r"\bW[iy]n[ck]?[eg]?l?[ms]ann\b|\bWinkelman+\b|\bWingelman+\b|\bWinckelmann\b","Winckelmann"),(r"\bJohan\b","Johann"),(r"\bKaufm?ann\b|\bKauffmann\b","Kauffmann"),
(r"\bÉtienne Louis\b|\bEtienne Louis\b","Étienne-Louis"),(r"\bBuin\b|\bBoulet\b|\bBoullé\b|\bBoulée\b","Boullée"),(r"\bSou?ff?l[oa]w?n?\b|\bSufflot\b|\bSoufflon\b","Soufflot"),
(r"\bSaint[ -]Genevi[eè]ve\b","Sainte-Geneviève"),(r"\bPier ?Marin[oi]\b|\bPiermanini\b|\bPier Manini\b","Piermarini"),(r"\bK[ae]ndel?s?o?n? Hall\b|\bCandle ?[Ss]tall Hall\b|\bCandle ?[Ss]tall\b|\bKendall Hall\b","Kedleston Hall"),
(r"\bMarble Hole\b","Marble Hall"),(r"\bVallalla\b|\bValhalla\b","Walhalla"),(r"\bOrazz?i\b","Orazi"),(r"\bCuriazz?i\b","Curiazi"),(r"\bAmore Psiche\b|\bAmore psiche\b","Amore e Psiche"),
(r"\bCanoa\b","Canova"),(r"\bMarata\b|\bMaratta\b","Marat"),(r"\bCharlotte Corvette\b","Charlotte Corday"),(r"\bpalla ?corda\b|\bPalla ?corda\b","Pallacorda"),(r"\bVarsill\w*\b","Versailles"),
(r"\bEngre\b|\bHencre\b|\bIngre\b|\bEng\b","Ingres"),(r"\bDavide\b","David"),(r"\bpanthéon\b|\bPanthéon\b|\bPantio\b|\bPanthon\b|\bPanteon\b|\bpantheon\b","Pantheon"),(r"\bneoclassicismo\b","Neoclassicismo"),(r"\bneoclassico\b","neoclassico"),
(r"\bGran tour\b|\bgran tour\b|\bGrand tour\b","Grand Tour"),(r"\bNewton\b","Newton"),(r"\bBrandeburgo\b","Brandeburgo")]
def parole():
    S=json.load(open(WK+'trasc.json'));W=[];cur=None
    for s in S:
        for t,w in s['parole']:
            if w.startswith(' ') or cur is None:
                if cur:W.append(cur)
                cur=[t,w.strip()]
            else:cur[1]+=w
    if cur:W.append(cur)
    # attacca la punteggiatura
    out=[]
    for t,w in W:
        if re.fullmatch(r'[.,;:?!…]+',w) and out:out[-1][1]+=w
        else:out.append([t,w])
    return [(t,w) for t,w in out if re.sub(r'[^\w-]','',w).lower() not in FILL and w!='']
def fix(t):
    for a,b in FIX:t=re.sub(a,b,t)
    return t
def cues_prof(a,b,t0piece,ca):
    W=[(t,w) for t,w in parole() if a<=t<b]
    cues=[];cur=[];
    def chiudi():
        nonlocal cur
        if not cur:return
        txt=fix(' '.join(w for _,w in cur));s=cur[0][0];e=cur[-1][0]+0.5
        cues.append((t0piece+(s-ca),t0piece+(min(e,W_next(cur))-ca),txt));cur=[]
    idx={id(w):i for i,w in enumerate(W)}
    def W_next(c):
        i=W.index(c[-1]);return W[i+1][0] if i+1<len(W) else c[-1][0]+0.6
    for i,(t,w) in enumerate(W):
        cur.append((t,w))
        L=len(' '.join(x for _,x in cur));dur=t-cur[0][0]
        fine=bool(re.search(r'[.?!]$',w));gap=(W[i+1][0]-t) if i+1<len(W) else 9
        if L>=70 or dur>5.5 or (fine and L>25 and gap>0.35) or (re.search(r'[,;:]$',w) and L>55) or gap>1.2:chiudi()
    chiudi()
    return cues
def spezza(txt,maxc=42):
    w=txt.split();lines=[];cur=''
    for x in w:
        if len((cur+' '+x).strip())<=maxc:cur=(cur+' '+x).strip()
        else:lines.append(cur);cur=x
    if cur:lines.append(cur)
    return '\n'.join(lines[:2]) if len(lines)<=2 else '\n'.join([lines[0],' '.join(lines[1:])])
def cues_voce(nome,t0,voce_start,testo):
    p=f'/home/user/Lezioni/scambio_voci/vox/NC_{nome}.wav'
    vd=dur_wav(p) if os.path.exists(p) else None
    if vd is None:
        pv=WK+f'prov/NC_{nome}.wav';vd=dur_wav(pv)
    sent=[s.strip() for s in re.split(r'(?<=[.!?])\s+',testo) if s.strip()]
    tot=sum(len(s) for s in sent);t=t0+voce_start;out=[]
    for s in sent:
        d=vd*len(s)/tot
        # frasi lunghe: spezza in blocchi da ~84 caratteri sulle virgole
        parts=[s]
        if len(s)>84:
            parts=[];cur=''
            for chunk in re.split(r'(?<=[,;:])\s+',s):
                if len(cur)+len(chunk)>84 and cur:parts.append(cur);cur=chunk
                else:cur=(cur+' '+chunk).strip()
            if cur:parts.append(cur)
        ts=t
        for pp in parts:
            dd=d*len(pp)/len(s);out.append((ts,ts+dd,pp));ts+=dd
        t+=d
    return out
TV={'COVER':1.2,'ARG':1.0,'SP':1.2,'GL':1.4,'RF':1.4,'MF':1.0,'COMP':1.2}
def tc(x):
    h=int(x//3600);m=int((x%3600)//60);s=x%60;return f'{h:02d}:{m:02d}:{s:06.3f}'
def main(parte,out):
    tl=json.load(open(WK+f'timeline_raw_P{parte}.json'));cues=[]
    for nm,t0,d in tl:
        if nm in build.PROF_CUT:
            _,a,b,pre=build.PROF_CUT[nm];cues+=cues_prof(a,b,t0,a-pre)
        elif re.fullmatch(r'[AR]\d',nm):
            n=int(nm[1]);tv=1.0 if nm[0]=='A' else 2.4
            txt=voci.VOCI[nm].replace('«','').replace('»','');cues+=cues_voce(nm,t0,tv,txt)
        elif nm in('SIG','FIN','CI'):pass
        elif nm in voci.VOCI:cues+=cues_voce(nm,t0,TV.get(nm,1.0),voci.VOCI[nm].replace('«','').replace('»',''))
    cues=sorted(cues)
    # niente sovrapposizioni
    fixed=[]
    for i,(s,e,t) in enumerate(cues):
        if i+1<len(cues):e=min(e,cues[i+1][0]-0.02)
        if e-s<0.6:e=s+0.6
        fixed.append((s,e,t))
    with open(out,'w') as f:
        f.write('WEBVTT\n\n')
        for i,(s,e,t) in enumerate(fixed):f.write(f'{i+1}\n{tc(s)} --> {tc(e)}\n{spezza(t)}\n\n')
    print(out,len(fixed),'cue')
if __name__=='__main__':main(int(sys.argv[1]),sys.argv[2])
