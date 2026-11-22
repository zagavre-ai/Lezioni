# Prepara la cartella di consegna revisione-storia-V-lez19: video a pezzi da 90 MB con sha256, vtt, timeline/scheda rigenerati sul video finale, PDF, JSON
import os,sys,json,subprocess,shutil,hashlib
W='/home/claude/w19';D=W+'/revisione-storia-V-lez19'
os.makedirs(D,exist_ok=True)
for f in os.listdir(D):
    p=os.path.join(D,f)
    if os.path.isfile(p): os.remove(p)
def sh(c): 
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode: print(r.stderr[-400:])
    return r
for n in (1,2):
    v=f'Storia_Lez19_Parte{n}_1080p.mp4';src=f'{W}/final/{v}'
    shutil.copy(src,f'{D}/{v}')
    h=hashlib.sha256(open(src,'rb').read()).hexdigest();open(f'{D}/{v}.sha256','w').write(f'{h}  {v}\n')
    sh(['split','-b','90M','-d','-a','2',f'{D}/{v}',f'{D}/{v}.parte_']);os.remove(f'{D}/{v}')
    shutil.copy(f'{W}/final/Storia_Lez19_Parte{n}.vtt',f'{D}/Storia_Lez19_Parte{n}.vtt')
    shutil.copy(f'{W}/timeline_tool_P{n}.json',f'{D}/timeline_Parte{n}.json')
    sh(['python3','/home/user/Lezioni/tools/scheda_da_timeline.py',src,f'{W}/timeline_tool_P{n}.json',f'{W}/consegna/quiz_argomenti.json',f'Storia V · L’Italia dal ’68 alla crisi della Prima Repubblica · Parte {n}',f'{D}/scheda_pubblicazione_Parte{n}.json','Storia V'])
    for ext in ('controllo.txt','miniature.jpg'):
        s=f'{src}.{ext}'
        if os.path.exists(s): shutil.copy(s,f'{D}/{v}.{ext}')
for f in os.listdir(W+'/consegna'): shutil.copy(f'{W}/consegna/{f}',f'{D}/{f}')
print(sorted(os.listdir(D)))
