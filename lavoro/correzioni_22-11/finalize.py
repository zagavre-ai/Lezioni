# -*- coding: utf-8 -*-
# Prepara la cartella di consegna /home/work/consegna: video a pezzi + sha256, vtt, timeline, scheda, pdf, quiz, controlli.
import sys, os, json, re, shutil, subprocess, hashlib, glob
sys.path.insert(0,'/home/work/build')
import events, subs
C='/home/work/consegna';os.makedirs(C,exist_ok=True)
TIT="Le fasi conclusive della guerra fredda (1969-1991)"
def sh(c,**k): return subprocess.run(c,check=True,**k)
for P in (1,2,3):
    v=f'/home/work/build/out/Storia_Lez17_Parte{P}_1080p.mp4';name=os.path.basename(v)
    # sottotitoli sul video finale
    e,w=events.events(P);asr=json.load(open(f'/home/work/build/asrfin/P{P}.json'))
    n=subs.make_vtt(asr,w,e,f'{C}/Storia_Lez17_Parte{P}.vtt')
    # timeline (nomi del kit) e scheda
    t=json.load(open(f'/home/work/build/out_timeline_P{P}.json'));out=[]
    for nm,s,f in t:
        m=re.match(r'(titolo|prof|quiz)(\d+)$',nm)
        k=({'titolo':'T','prof':'D','quiz':'Q'}[m.group(1)]+m.group(2)) if m else {'glossario':'GL','riepilogo':'RF','siglafinale':'FI'}.get(nm,nm)
        out.append([k,round(s,3),round(f/30,3)])
    json.dump(out,open(f'{C}/timeline_Parte{P}.json','w'),ensure_ascii=False)
    sh(['python3','/home/user/Lezioni/kit/tools/scheda_da_timeline.py',v,f'{C}/timeline_Parte{P}.json','/home/work/build/quiz_argomenti_ok.json',f'{TIT} · Parte {P}',f'{C}/scheda_pubblicazione_Parte{P}.json','Storia V'],stdout=subprocess.DEVNULL)
    # video a pezzi da 90 MB + sha256 del file intero
    h=hashlib.sha256();
    with open(v,'rb') as f:
        for b in iter(lambda:f.read(1<<24),b''):h.update(b)
    open(f'{C}/{name}.sha256','w').write(f'{h.hexdigest()}  {name}\n')
    for old in glob.glob(f'{C}/{name}.parte_*'):os.remove(old)
    sh(['split','-b','90M','-d','-a','2',v,f'{C}/{name}.parte_'])
    for fn in glob.glob(f'/home/work/build/cr/*Parte{P}_1080p*'):shutil.copy(fn,C)
    shutil.copy(f'/home/work/build/docs/Storia_Lez17_Parte{P}_dispensa.pdf',C)
    if os.path.exists(f'/home/work/build/docs/Storia_Lez17_Parte{P}_mappe.pdf') and P in (1,3): shutil.copy(f'/home/work/build/docs/Storia_Lez17_Parte{P}_mappe.pdf',C)
    print(P,n,'cue')
for fn in ['compiti.json','verifica_finale.json','Quiz_Storia_Lez17.txt']: shutil.copy('/home/work/build/'+fn,C)
shutil.copy('/home/work/prev/video/Verifica_finale_Storia_Lez17.xlsx',C+'/Verifica_finale_Storia.xlsx')
print('ok')
