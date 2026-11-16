# prepara la cartella di consegna e la pubblica sul ramo consegna-storia-V-lez18
import sys,os,json,subprocess,shutil,glob,hashlib
N='20';TIT="Gli anni Novanta, il mondo post-bipolare";OUT='/tmp/w20/out';FIN='/tmp/w20/fin';D=f'/tmp/w20/consegna-storia-V-lez{N}'
KT='/home/user/Lezioni/kit/tools/'
os.makedirs(D,exist_ok=True)
def sh(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(str(c)[:150]+r.stderr[-400:])
    return r.stdout
for p in (1,):
    v=f'{FIN}/Storia_Lez{N}_Parte{p}_1080p.mp4'
    sh(['python3',KT+'scheda_da_timeline.py',v,f'{OUT}/timeline_Parte{p}.json',f'{OUT}/quiz_argomenti.json',f'{TIT}',f'{D}/scheda_pubblicazione_Parte{p}.json','Storia'])
    open(f'{D}/testo_youtube_Parte{p}.txt','w').write(sh(['python3',KT+'testo_youtube.py',f'{D}/scheda_pubblicazione_Parte{p}.json','Storia|Storia','Prof. Giorgio Mazzotti',f'Lezione {N} · {TIT}','0',f'{OUT}/timeline_Parte{p}.json']))
    shutil.copy(f'{OUT}/timeline_Parte{p}.json',f'{D}/timeline_Parte{p}.json')
    shutil.copy(f'{OUT}/Storia_Lez{N}_Parte{p}.vtt',D)
    for f in glob.glob(f'{D}/Storia_Lez{N}_Parte{p}_1080p.mp4.parte_*'):os.remove(f)
    base=f'{D}/Storia_Lez{N}_Parte{p}_1080p.mp4.parte_'
    with open(v,'rb') as f:
        i=0;h=hashlib.sha256()
        while True:
            b=f.read(94371840)
            if not b:break
            open(base+'%02d'%i,'wb').write(b);i+=1
    sh(['sha256sum',os.path.basename(v)],cwd=FIN)
    open(f'{D}/Storia_Lez{N}_Parte{p}_1080p.mp4.sha256','w').write(sh(['sha256sum',os.path.basename(v)],cwd=FIN))
for f in ['quiz_argomenti.json',f'Quiz_Storia_Lez{N}.txt',f'Storia_Lez{N}_test_finale_docente.xlsx',f'Storia_Lez{N}_compiti_docente.pdf',f'Storia_Lez{N}_compiti_docente.txt','compiti.json',f'Storia_Lez{N}_dispensa.pdf']:
    shutil.copy(f'{OUT}/{f}',D)
print(sorted(os.listdir(D)))
