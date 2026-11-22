# dopo l'assemblaggio di una Parte: timeline, scheda, vtt, controlli, pezzi da 90 MB + sha256, cartella di consegna
import sys, os, json, subprocess, shutil, hashlib, glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan import *
OUT='/tmp/w/out'; K='/home/user/Lezioni/kit/tools'
def run(c): r=subprocess.run(c,capture_output=True,text=True); print(r.stdout[-1500:]); print(r.stderr[-800:]) if r.returncode else None; return r
def fin(parte):
    vid=f'{OUT}/Storia_arte_V_Lez8_Parte{parte}_1080p.mp4'; tp=json.load(open(f'{OUT}/timeline_pezzi_P{parte}.json'))
    tl=[]; 
    for x in tp:
        n=x['pezzo']; d=x['fine']-x['inizio']
        if n.startswith('titolo'): n='T'+n[6:]
        elif n.startswith('quiz'): n='Q'+n[4:]
        elif n.startswith('T') and n[1:].isdigit(): n='D'+n[1:]
        elif n=='P0_intro': n='D0'
        tl.append([n,x['inizio'],round(d,2)])
    json.dump(tl,open(f'{OUT}/timeline_Parte{parte}.json','w'),ensure_ascii=False)
    tit=f"Storia dell'arte V · Lezione 8 · {TITOLO} · Parte {parte}"
    run(['python3',f'{K}/scheda_da_timeline.py',vid,f'{OUT}/timeline_Parte{parte}.json',f'{OUT}/quiz_argomenti.json',tit,f'{OUT}/scheda_pubblicazione_Parte{parte}.json',"Storia dell'arte V"])
    import subs8; print('cue',subs8.vtt(parte,f'{OUT}/Storia_arte_V_Lez8_Parte{parte}_1080p.vtt'))
    # pezzi da 90 MB + sha256
    d=f'{OUT}/consegna'; os.makedirs(d,exist_ok=True)
    for f in glob.glob(f'{d}/Storia_arte_V_Lez8_Parte{parte}_1080p.mp4.parte_*'): os.remove(f)
    subprocess.run(f'split -b 90M -d -a 2 {vid} {d}/{os.path.basename(vid)}.parte_',shell=True,check=True)
    h=hashlib.sha256(open(vid,'rb').read() if os.path.getsize(vid)<1<<30 else b'').hexdigest()
    open(f'{d}/{os.path.basename(vid)}.sha256','w').write(f'{h}  {os.path.basename(vid)}\n')
    print('sha',h)
if __name__=='__main__': fin(int(sys.argv[1]))
