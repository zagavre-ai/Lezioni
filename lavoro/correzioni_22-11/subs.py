# -*- coding: utf-8 -*-
# Sottotitoli .vtt dal video FINALE: parlato del prof (trascrizione del file finale, termini corretti) + voci Kore (testo noto).
import sys, os, re, json
sys.path.insert(0,'/home/work/build')
from anim import digits
CORR=[(r'\b[Gg]orbac[hc]?[eë]?v\b','Gorbačëv'),(r'\b[Gg]orbaciov\b','Gorbačëv'),(r'\b[Gg]orbaciov\b','Gorbačëv'),(r'\b[Bb]re[sz]+nev\b','Brežnev'),(r'\b[Kk]h?omeini\b','Khomeini'),(r'\b[Cc]omeini\b','Khomeini'),
 (r'\b[Tt]ian?anmen\b','Tienanmen'),(r'\b[Tt]ienanmen\b','Tienanmen'),(r'\b[Pp]ahlavi\b','Pahlavi'),(r'\b[Pp]erestroika\b','Perestrojka'),(r'\b[Pp]erestroj?ka\b','Perestrojka'),(r'\b[Gg]lasnost\b','Glasnost'),(r'\b[Kk]ippur\b','Kippur'),
 (r'\bOpec\b','OPEC'),(r'\bOlp\b','OLP'),(r'\b[Ss]alt\b','SALT'),(r'\b[Ff]alkland\b','Falkland'),(r'\b[Pp]inochet\b','Pinochet'),(r'\b[Aa]llende\b','Allende'),(r'\b[Rr]eagan\b','Reagan'),(r'\b[Ts]hatcher\b','Thatcher'),(r'\b[Tt]atcher\b','Thatcher'),(r'\b[Ss]addam\b','Saddam'),(r'\b[Ss]adat\b','Sadat'),(r'\bBegin\b','Begin'),(r'\bCamp [Dd]avid\b','Camp David'),(r'\b[Ss]abra\b','Sabra'),(r'\b[Cc]hatila\b','Chatila'),(r'\b[Hh]amas\b','Hamas'),(r'\b[Dd]eng [Xx]iaoping\b','Deng Xiaoping'),(r'\b[Mm]itterrand\b','Mitterrand'),(r'\b[Pp]laza de [Mm]ayo\b','Plaza de Mayo'),(r'\b[Ww]atergate\b','Watergate'),(r'\b[Hh]elsinki\b','Helsinki'),(r'\b[Bb]retton [Ww]oods\b','Bretton Woods'),(r'\b[Nn]ixon\b','Nixon')]
def fix(t):
    for a,b in CORR: t=re.sub(a,b,t)
    return t
def ts(x):
    h=int(x//3600);m=int(x%3600//60);s=x%60;return f'{h:02d}:{m:02d}:{s:06.3f}'
def blocks(text,t0,t1,maxc=42):
    words=text.split();lines=[];cur=''
    for w in words:
        if len(cur)+len(w)+1<=maxc:cur=(cur+' '+w).strip()
        else:lines.append(cur);cur=w
    if cur:lines.append(cur)
    out=[];i=0
    # blocchi da 2 righe
    grp=[lines[k:k+2] for k in range(0,len(lines),2)];tot=sum(len(' '.join(g)) for g in grp) or 1;t=t0
    for g in grp:
        d=(t1-t0)*len(' '.join(g))/tot;out.append((t,t+d,'\n'.join(g)));t+=d
    return out
def make_vtt(prof_asr,windows,kore,out):
    """prof_asr: segmenti ASR del file finale [{inizio,fine,testo}]; windows: [(a,b)] pezzi del prof nel file finale; kore: [(a,b,testo)]"""
    cues=[]
    for s in prof_asr:
        if any(a-0.6<=(s['inizio']+s['fine'])/2<b+0.6 for a,b in windows) and s['testo'].strip():
            for x in blocks(fix(s['testo'].strip()),s['inizio'],s['fine']): cues.append(x)
    for a,b,t in kore:
        for q in re.split(r'(?<=[\.\!\?])\s+',digits(t)):
            pass
        for x in blocks(digits(t),a,b): cues.append(x)
    cues.sort(key=lambda c:c[0]);fixed=[]
    for i,(a,b,t) in enumerate(cues):
        if i+1<len(cues) and b>cues[i+1][0]-0.02:b=max(a+0.3,cues[i+1][0]-0.02)
        fixed.append((a,b,t))
    with open(out,'w') as f:
        f.write('WEBVTT\n\n')
        for i,(a,b,t) in enumerate(fixed,1):f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{t}\n\n')
    return len(fixed)
