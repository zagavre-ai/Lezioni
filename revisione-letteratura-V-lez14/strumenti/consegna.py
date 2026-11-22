import json,sys,os,shutil,subprocess,hashlib,re
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import buildd
CD='/tmp/w14/cons/consegna-letteratura-V-lez14';OUT='/tmp/w14/out'
for P in (1,2):
    tl=json.load(open(f'/tmp/w14/tlnew{P}.json'));fr=json.load(open(f'/tmp/w14/aq{P}/tl_new.json'))['frames']
    dur=round(fr/30,2)
    st={n:s for n,s,d in tl}
    S=json.load(open(f'{CD}/scheda_pubblicazione_parte{P}.json'))
    S['titolo']=f'Letteratura V · Lezione 14 · Pirandello · Parte {P}';S['durata_s']=dur
    for a in S['argomenti']:
        n=a['n'];a['titolo']=buildd.ARGS[P][n-1];a['inizio_s']=st[f'T{n}'];a['quiz_s']=st[f'Q{n}']
    for k,v in S['quiz'].items():
        n=int(k[1:]);v['title']=f'Quiz {n} · '+buildd.ARGS[P][n-1]
    if P==2:
        S['t_verifica']=st['VER'];S['t_compiti']=st.get('CI1',st.get('COMP'))
    json.dump(S,open(f'{OUT}/scheda_pubblicazione_parte{P}.json','w'),ensure_ascii=False,indent=1)
    q=json.load(open(f'{CD}/quiz_argomenti_parte{P}.json'))
    for k,v in q.items(): v['title']=f'Quiz {int(k[1:])} · '+buildd.ARGS[P][int(k[1:])-1]
    json.dump(q,open(f'{OUT}/quiz_argomenti_parte{P}.json','w'),ensure_ascii=False,indent=1)
    t=open(f'{CD}/Quiz_Letteratura_Lez14_Parte{P}.txt',encoding='utf-8').read().replace("La visione del mondo e la trappola sociale","La visione del mondo e l'umorismo").replace('I primi grandi romanzi','Il fu Mattia Pascal')
    open(f'{OUT}/Quiz_Letteratura_Lez14_Parte{P}.txt','w',encoding='utf-8').write(t)
    json.dump(tl,open(f'{OUT}/timeline_parte{P}.json','w'))
    # testo YouTube
    r=subprocess.run(['python3','/home/user/Lezioni/kit/tools/testo_youtube.py',f'{OUT}/scheda_pubblicazione_parte{P}.json','Letteratura italiana (V anno)|Letteratura','Prof. Giorgio Mazzotti','Lezione 14 · Pirandello',str(P),f'{OUT}/timeline_parte{P}.json'],capture_output=True,text=True)
    open(f'{OUT}/testo_youtube_parte{P}.txt','w',encoding='utf-8').write(r.stdout);print(P,r.stderr[-200:])
    # video a pezzi + sha
    src=f'/tmp/w14/aq{P}/finale.mp4';name=f'Letteratura_Lez14_Parte{P}_1080p.mp4'
    h=hashlib.sha256();i=0
    with open(src,'rb') as f:
        while True:
            b=f.read(94371840)
            if not b: break
            open(f'{OUT}/{name}.parte_{i:02d}','wb').write(b);h.update(b);i+=1
    open(f'{OUT}/{name}.sha256','w').write(f'{h.hexdigest()}  {name}\n');print(P,'pezzi',i)
