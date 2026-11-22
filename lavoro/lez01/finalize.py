#!/usr/bin/env python3
# Dopo il montaggio: file di consegna della Parte N (video a pezzi con sha256, vtt, timeline, scheda, controlli).
import os,sys,json,shutil,subprocess,re,glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from asm import WK,sh
import sub
KIT='/home/user/Lezioni/kit/tools/'
CONS=WK+'consegna/';os.makedirs(CONS,exist_ok=True)
def main(parte):
    raw=WK+f'Storia_arte_Lez1_Parte{parte}_1080p.mp4'
    nome=f'StoriaArte_Lez1_Parte{parte}_1080p.mp4'
    dst=CONS+nome
    shutil.copy(raw,dst)
    tl=json.load(open(WK+f'timeline_raw_P{parte}.json'))
    json.dump(tl,open(CONS+f'timeline_Parte{parte}.json','w'),indent=0)
    sub.main(parte,CONS+f'StoriaArte_Lez1_Parte{parte}.vtt')
    qz=WK+'dati/quiz_argomenti.json'
    sh(['python3',KIT+'scheda_da_timeline.py',dst,CONS+f'timeline_Parte{parte}.json',qz,f"Storia dell'arte V · Lezione 1 · Il Neoclassicismo · Parte {parte}",CONS+f'scheda_pubblicazione_Parte{parte}.json',"Storia dell'Arte V"])
    sj=json.load(open(CONS+f'scheda_pubblicazione_Parte{parte}.json'))
    for n,t,d in tl:
        if n=='VER':sj['t_verifica_s']=t
        if n=='CI':sj['t_compiti_s']=t
        if n=='GL':sj['t_glossario_s']=t
    json.dump(sj,open(CONS+f'scheda_pubblicazione_Parte{parte}.json','w'),ensure_ascii=False,indent=1)
    for f in ('quiz_argomenti.json','verifica_finale.json','compiti.json'):shutil.copy(WK+'dati/'+f,CONS+f)
    for f in glob.glob(CONS+nome+'.parte_*'):os.remove(f)
    sh(['split','-b','90M','-d','-a','2',dst,CONS+nome+'.parte_'])
    h=sh(['sha256sum',dst]).stdout.split()[0];open(CONS+nome+'.sha256','w').write(f'{h}  {nome}\n')
    print('consegna',nome,os.path.getsize(dst)//1000000,'MB',h[:12])
if __name__=='__main__':main(int(sys.argv[1]))
