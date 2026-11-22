# Assemblaggio di una Parte: costruisce i pezzi Kore (con cache), poi dissolvenze + codifica finale.
import sys,os,json,subprocess,hashlib,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lezione import *
VER=json.load(open('/home/user/Lezioni/w/verifica.json'));COMP=json.load(open('/home/user/Lezioni/w/compiti.json'))
def std(src,out):
    if os.path.exists(out):return
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vf','scale=1920:1080,fps=30,format=yuv420p','-af','aresample=48000,aformat=channel_layouts=stereo','-c:v','libx264','-preset','veryfast','-crf','16','-c:a','pcm_s16le','-ar','48000',out],check=True)
def sig(states,extra=''):
    return 'v2'+hashlib.md5(''.join(s['html'] for s in states).encode()).hexdigest()+json.dumps([(s.get('voce'),voce(s['voce'])[1]) for s in states if s.get('voce')])+extra
def kpiece(name,states,**kw):
    out=W+f'/{name}.mkv';sg=sig(states,json.dumps(kw,default=str))
    if os.path.exists(out) and os.path.exists(out+'.sig') and open(out+'.sig').read()==sg:return out
    piece(name,states,out,None,**kw);open(out+'.sig','w').write(sg);return out
def verifica_states():
    S=[dict(html=dark('VERIFICA DI SBARRAMENTO','Verifica finale',f'{len(VER["domande"])} domande · per continuare serve almeno l’{VER["soglia_percento"]}%',sz=84),hold=4.3)]
    for q in VER['domande']:
        opts=[q['a']]+q['w'];ov=''.join(f'<div style="margin:8px 0;font:600 34px/1.35 Fig">{"ABCD"[i]} · {G.esc(o)}</div>' for i,o in enumerate(opts))
        inner=f'<div class="card" style="position:absolute;left:80px;top:300px;width:1760px"><span class=n>{q["n"]}</span>{G.esc(q["p"])}<div style="margin-top:14px">{ov}</div></div>'
        S.append(dict(html=hdoc(inner,'VERIFICA FINALE',f'Domanda {q["n"]} di {len(VER["domande"])}',240,'',False),hold=9.0))
    return S
def compiti_states():
    S=[dict(html=dark('COMPITI','Compiti','',sz=110),hold=2.6)]
    for e in COMP['esercizi']:
        inner=f'<div class="card" style="position:absolute;left:80px;top:300px;width:1760px"><span class=n>{e["n"]}</span>{G.esc(e["testo"])}</div>'
        S.append(dict(html=hdoc(inner,'COMPITI',f'Esercizio {e["n"]}',240,'',False),hold=10.0))
    return S
def cache_lines(parte):
    PG=plan_pagine(parte);P=[]   # (nome, funzione che ritorna path mkv)
    def add(n,f):P.append((n,f))
    kit=KIT
    add('SIGLA',lambda:(std(kit+'/sigle/Sigla_Storia_15s.mp4',W+'/SIGLA.mkv'),W+'/SIGLA.mkv')[1])
    if parte==1:
        add('COVERV',lambda:kpiece(f'COVERV_{parte}',cover_states('INTRO1_R2',1,PG['COVERV']),trans=True))
        add('D0',lambda:W+'/D0.mkv')
        add('DP',lambda:kpiece(f'DP_{parte}',dp_states('DP1',1,PG['DP']),trans=True))
        args=[1,2,3,4,5];qs={1:'Q1',2:'Q2',3:'Q3',4:'Q4',5:'Q5'};maps={2:['M1a','M1b']}
    else:
        add('SPIEGONE',lambda:kpiece(f'SPIEGONE_{parte}',spiegone_states(PG['SPIEGONE'] if parte==2 else 0),trans=True))
        add('COVERV',lambda:kpiece(f'COVERV_{parte}',cover_states('INTRO2_R2',2,PG['COVERV']),trans=True))
        add('DP',lambda:kpiece(f'DP_{parte}',dp_states('DP2',2,PG['DP']),trans=True))
        args=[6,7,8,9,10];qs={6:'Q6',7:'Q7',8:'Q8',9:'Q9',10:'Q10'};maps={6:['M2'],8:['M3'],10:['M4']}
    for n in args:
        add(f'T{n}',lambda n=n:kpiece(f'T{n}',t_states(n,ARGT[n]),trans=False,anim=True,lead=0.2,tail=0.5,jingle=(KIT+'/suoni/titolo.wav',0.2)))
        add(f'A{n}',lambda n=n:W+f'/A{n}.mkv')
        add(f'AP{n}',lambda n=n:kpiece(f'AP{n}',ap_states(n,PG[f'AP{n}']),trans=True))
        for mk in maps.get(n,[]):add(f'MAP_{mk}',lambda mk=mk:kpiece(f'MAP_{mk}',map_states(mk,PG[f'MAP_{mk}']),trans=True))
        add(f'PI{n}',lambda n=n:kpiece(f'PI{n}',pips_states(n,PG[f'PS{n}']),trans=False,anim=False,jingle=(KIT+'/suoni/repaso.wav',0.2),lead=1.3))
        add(f'{qs[n]}',lambda n=n:kpiece(qs[n],quiz_states(qs[n]),trans=False,anim=True,lead=0.3,tail=0.4,jingle=(KIT+'/suoni/quiz.wav',0.5)))
    if parte==2:
        add('A11',lambda:W+'/A11.mkv')
    add('GL',lambda:kpiece(f'GL_{parte}',gl_states(f'GL{parte}',None,PG['GL']),trans=True))
    add('RF',lambda:kpiece(f'RF_{parte}',rf_states(f'RF{parte}',parte,PG['RF']),trans=True))
    add('FIN',lambda:kpiece(f'FIN_{parte}',fin_states(f'FIN{parte}'),trans=True,anim=True))
    if parte==2:add('VERIFICA',lambda:kpiece(f'VERIFICA_{parte}',verifica_states(),trans=False,anim=False,lead=0.3,tail=0.6,jingle=(KIT+'/suoni/quiz.wav',0.5)))
    add('FINALE',lambda:(std(kit+'/sigle/Sigla_finale_5s_con_avviso_diritti.mp4',W+'/FINALE.mkv'),W+'/FINALE.mkv')[1])
    if parte==2:add('COMPITI',lambda:kpiece(f'COMPITI_{parte}',compiti_states(),trans=False,lead=0.3,tail=0.6,jingle=(KIT+'/suoni/titolo.wav',0.2)))
    return P
def spiegone_states(pag0=1):
    S=[dict(html=dark('RIPASSO','Che cosa abbiamo visto nella prima parte','',sz=70),voce='SP2_0')]
    IM='file:///home/user/Lezioni/w/imgs/'
    for k,(vn,n) in enumerate([('SP2_1',1),('SP2_2',2),('SP2_3',3),('SP2_4',4),('SP2_5',5)]):
        t=cifre(TESTI[vn]);sents=[x for x in re.split(r'(?<=\\.)\\s+',t)]
        w,_=voce(vn);dv=dur(w);tot=sum(len(x) for x in sents);acc=0
        for i,x in enumerate(sents):
            body=''
            if n==2 and i>=len(sents)-1:  # mappa
                pass
            vis=range(max(0,i-1),i+1)
            cards=''.join(f'<div class="card {"on" if j==i else "dim"}" style="font-size:36px"><span class=n>{j+1}</span>{G.esc(sents[j])}</div>' for j in vis)
            img=''
            if n==3:img=f'<img class="img" src="{IM}i-006.jpg" style="left:80px;top:640px;height:340px">'
            if n==4:img=f'<img class="img" src="{IM}i-010.jpg" style="left:1500px;top:300px;height:600px">'
            inner=f'<div style="position:absolute;left:80px;top:300px;width:{1300 if n==4 else 1760}px;display:flex;flex-direction:column;gap:22px">{cards}</div>{img}'
            h=hdoc(inner,'RIPASSO · PRIMA PARTE',ARGT[n],260,pag0+n-1,False)
            if n==2 and i==len(sents)-1:h=map_html(MAPPE['M1a'],[x[0] for x in MAPPE['M1a']['nodi']],None,{(a,b) for a,b,_ in MAPPE['M1a']['archi']},pag=pag0+n-1)
            st=dict(html=h)
            if i==0:st['voce']=vn
            else:st['rel']=dv*acc/tot
            S.append(st)
            if n==2 and i==len(sents)-1:
                m=MAPPE['M1b'];S.append(dict(html=map_html(m,[y[0] for y in m['nodi']],None,{(p,q) for p,q,_ in m['archi']},pag=pag0+n-1),rel=dv*acc/tot+(dv-dv*acc/tot)*0.5))
            acc+=len(x)
    return S
if __name__=='__main__':
    parte=int(sys.argv[1]);P=cache_lines(parte);paths=[]
    for n,f in P:
        try:p=f()
        except Exception as e:print('ERRORE',n,repr(e));raise
        paths.append((n,p));print(n,'ok',flush=True)
    json.dump(paths,open(W+f'/parte{parte}_pezzi.json','w'))
