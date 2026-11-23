# prepara la consegna in /tmp/claude-0/w/prod/rev e la carica sul ramo revisione-storia-arte-V-lez13
import sys,os,json,shutil,subprocess,hashlib
W='/tmp/claude-0/w/prod';R=W+'/rev';V='Storia_arte_Lez13_Parte1_1080p.mp4'
os.makedirs(R,exist_ok=True)
def sh(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise SystemExit(' '.join(c)+'\n'+r.stderr[-800:])
    return r
src=W+'/fin/'+V
# timeline con i nomi del kit
ren={'GLOSSARIO':'GL','RIEPILOGO':'RF','FINALE':'FI'}
T=json.load(open(W+'/fin/timeline_raw.json'));T=[[ren.get(n,n),t,l] for n,t,l in T]
json.dump(T,open(R+'/timeline_Parte1.json','w'),ensure_ascii=False)
sh(['python3','/home/user/Lezioni/kit/tools/scheda_da_timeline.py',src,R+'/timeline_Parte1.json',W+'/consegna/quiz_argomenti.json',"Storia dell'arte V · Lezione 13 · Razionalismo e Metafisica",R+'/scheda_pubblicazione_Parte1.json',"Storia dell'arte V"])
for f in ['quiz_argomenti.json','verifica_finale.json','compiti.json','Storia_arte_Lez13_slide.pdf','Storia_arte_Lez13_mappe.pdf']:shutil.copy(W+'/consegna/'+f,R+'/'+f)
shutil.copy(W+'/fin/Storia_arte_Lez13_Parte1.vtt',R+'/Storia_arte_Lez13_Parte1.vtt')
for f in os.listdir(W+'/fin/cr'):shutil.copy(W+'/fin/cr/'+f,R+'/'+f)
for f in ['controllo_voci.json']:
    if os.path.exists(W+'/consegna/'+f):shutil.copy(W+'/consegna/'+f,R+'/'+f)
h=hashlib.sha256()
with open(src,'rb') as f:
    for b in iter(lambda:f.read(1<<20),b''):h.update(b)
open(R+f'/{V}.sha256','w').write(f'{h.hexdigest()}  {V}\n')
for f in os.listdir(R):
    if f.startswith(V+'.parte_'):os.remove(R+'/'+f)
sh(['split','-b','90M','-d','-a','2',src,R+f'/{V}.parte_'])
print('pronto',sorted(os.listdir(R)))
