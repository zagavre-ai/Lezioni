#!/usr/bin/env python3
# Sottotitoli .vtt dal VIDEO FINALE: trascrizione di tutto l'audio finale, termini corretti dal materiale del docente.
# uso: python3 subs.py video_finale.mp4 uscita.vtt
import sys, os, json, re, subprocess
V,OUT=sys.argv[1:3]
base=OUT[:-4]+'_asr'
if not os.path.exists(base+'.json'):
    subprocess.run(['python3','/home/user/Lezioni/kit/tools/trascrivi.py',V,base],check=True,env=dict(os.environ,TELESIO_ASR='/tmp/asr'))
segs=json.load(open(base+'.json'))
FIX=[(r'\bGh?[eE]t+h?afi\b|\bGhettafi\b','Gheddafi'),(r'\bMacon\b|\bMacro\b','Macron'),(r'\bprodi\b|\bPerusconi\b','Prodi'),(r'\bsul suono americano','sul suolo americano'),(r'\bBerusconi\b|\bPerusconi\b','Berlusconi'),(r'\bAl[\s-]?(?:Qa[ie]da|Queda|Qaida|Kaida)\b','Al-Qaeda'),(r'\bBrics?\b|\bBRIC\b|\bBricks\b','BRICS'),(r'\bBRICS\b','BRICS'),(r'\bIsis\b|\bisis\b','ISIS'),
     (r'\bGh?[ae]d+h?afi\b|\bGethafi\b|\bGeddafi\b|\bGaddafi\b','Gheddafi'),(r'\bPolitkovsk\w+','Politkovskaja'),(r'\bErdogan\b','Erdoğan'),
     (r'\bO[sz]ama (?:Bil+aden|Bin Laden|bin laden)\b','Osama bin Laden'),(r'\bBag[h]?dad\b','Baghdad'),(r'\bCapitol hill\b|\bcapitol hill\b','Capitol Hill'),
     (r'\bblack lives matter\b|\bBlack lives matter\b','Black Lives Matter'),(r'\bamerica first\b|\bAmerica first\b','America First'),
     (r'\bnext generation eu\b|\bNext generation EU\b|\bNext Generation Eu\b','Next Generation EU'),(r'\bobamacare\b','Obamacare'),
     (r'\bSaddam\b|\bSadam\b','Saddam'),(r'\bhussein\b','Hussein'),(r'\bBen Ali\b','Ben Ali'),(r'\bmubarak\b','Mubarak'),(r'\bAssad\b|\bassad\b','Assad'),
     (r'\bPutin\b|\bputin\b','Putin'),(r'\bMerkel\b|\bMerke\b','Merkel'),(r'\bMacron\b','Macron'),(r'\bMeloni\b','Meloni'),(r'\bDraghi\b','Draghi'),
     (r'\bBerl?usconi\b|\bBeruscon\w+','Berlusconi'),(r'\bProdi\b','Prodi'),(r'\bRenzi\b','Renzi'),(r'\bGentiloni\b','Gentiloni'),(r'\bXi Jinping\b','Xi Jinping'),
     (r'\bTorre gemelle\b|\btorri gemelle\b|\bTorri gemelle\b','Torri Gemelle'),(r'\bPentagono\b|\bpentagono\b','Pentagono'),
     (r'\bmuti subprime\b|\bmutui sub[- ]?prime\b','mutui subprime'),(r'\bTaliban\w*','talebani'),(r'\bFratelli d.Italia\b','Fratelli d\'Italia'),
     (r'\bMovimento 5 [Ss]telle\b|\bmovimento 5 [Ss]telle\b|\bMovimento cinque [Ss]telle\b','Movimento 5 Stelle')]
def fix(t):
    for a,b in FIX: t=re.sub(a,b,t)
    return t
def ts(s):
    h,r=divmod(s,3600);m,r=divmod(r,60);return '%02d:%02d:%06.3f'%(h,m,r)
cues=[]
for s in segs:
    # parole dai token (un token che inizia con spazio apre una parola)
    W=[]
    for t,tok in s['parole']:
        if tok.startswith(' ') or not W: W.append([t,tok.strip(),t])
        else: W[-1][1]+=tok;W[-1][2]=t
    if not W: continue
    cur=[];
    def flush(end):
        global cur
        if not cur: return
        txt=re.sub(r'\s*(\.\.\.|…)\s*$','',fix(' '.join(w[1] for w in cur)))
        a=cur[0][0];cues.append([a,max(end,a+0.4),txt]);cur=[]
    for i,w in enumerate(W):
        cur.append(w)
        n=len(' '.join(x[1] for x in cur));nxt=W[i+1][0] if i+1<len(W) else s['fine']
        brk=(n>=60 and re.search(r'[.,;:?!]$',w[1])) or n>=80 or (w[0]-cur[0][0]>5.5)
        if brk or i==len(W)-1: flush(min(nxt,w[0]+2.5) if i+1<len(W) else s['fine'])
# aggancio dell'inizio dei blocchi all'attacco reale della voce (stesso criterio del controllo finale)
import numpy as np
SR=8000
x8=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V,'-vn','-ac','1','-ar',str(SR),'-f','s16le','-'],capture_output=True).stdout,np.int16).astype(float)
e=np.convolve(x8**2,np.ones(400)/400,'same');thr=np.percentile(e,60)
for c in cues:
    i0=int(max(0,c[0]-0.8)*SR);seg=e[i0:int((c[0]+0.8)*SR)]
    if len(seg) and seg[:int(0.5*SR)].mean()<thr*0.5:
        on=int(np.argmax(seg>thr));t=i0/SR+on/SR
        if abs(t-c[0])<=0.8: c[0]=t
cues.sort()
# evita sovrapposizioni
for i in range(len(cues)-1):
    if cues[i][1]>cues[i+1][0]-0.02: cues[i][1]=cues[i+1][0]-0.02
def wrap(t):
    if len(t)<=42: return t
    mid=len(t)//2;sp=[m.start() for m in re.finditer(' ',t)];k=min(sp,key=lambda x:abs(x-mid));return t[:k]+'\n'+t[k+1:]
with open(OUT,'w') as f:
    f.write('WEBVTT\n\n')
    for i,(a,b,t) in enumerate(cues,1): f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{wrap(t)}\n\n')
print('cue',len(cues),OUT)
