import sys,os,json,subprocess
sys.path.insert(0,'/home/claude/w/b')
from scenes import *
import prof
os.makedirs(B+'/sc',exist_ok=True); os.makedirs(B+'/fin',exist_ok=True)
TR=SU+'trans.wav'
def build_scene(name,d,trans=True,force=False):
    out=f'{B}/sc/{name}.mkv'
    mark=out+'.ok'
    VER='v5'
    sig=VER+json.dumps([d['dur'],d.get('prov'),[(os.path.basename(f),round(t,2)) for f,t,k in d['events']]])
    if os.path.exists(mark) and open(mark).read()==sig and not force: return out
    tmp=f'{B}/sc/{name}_v.mp4'
    render_scene(d['html'],d['dur'],tmp)
    ev=([(TR,0.0,'fx')] if trans else [])+d['events']
    mux(tmp,ev,d['dur'],out); os.remove(tmp)
    open(mark,'w').write(sig); return out
def scene_list():
    L=[]  # (nome, funzione)
    L.append(('cover',lambda:dict(html=cover_html(False),dur=vox.info('BENV1_R2')['dur']+1.6,events=[(vox.info('BENV1_R2')['path'],0.6,'voce')],prov=vox.info('BENV1_R2')['prov'])))
    L.append(('dic',dic_scene))
    for a in range(1,6):
        L.append((f'tit{a}',lambda a=a:title_scene(a)))
        for i,(nm,_) in enumerate(AN[a]): L.append((f'an{a}_{i}',lambda nm=nm:appro_scene(nm)))
        if a>=3: L.append((f'map{a-2}',lambda a=a:map_scene(a-2)))
        L.append((f'pil{a}',lambda a=a:pillola_scene(a)))
        L.append((f'sch{a}',lambda a=a:schema_scene(a)))
        L.append((f'quiz{a}',lambda a=a:quiz_scene(a)))
    L.append(('glos',glossario_scene))
    for a in range(1,6): L.append((f'rip{a}',lambda a=a:ripasso_scene(a)))
    L.append(('verif',verifica_scene))
    v=vox.info('FIN1')
    L.append(('fin',lambda:dict(html=scene(glows()+'<div style="position:absolute;left:140px;top:420px;font-size:130px;color:#fff" class="h1" data-in="0.3">Per oggi è tutto</div>','',True),dur=v['dur']+1.4,events=[(v['path'],0.5,'voce')],prov=v['prov'])))
    L.append(('compi',compiti_intro))
    items=[(1,'Analizza le trasformazioni economiche, culturali e sociali degli Stati Uniti durante i "Ruggenti Anni Venti", spiegando il ruolo della produzione fordista, della cultura di massa e dell\'emancipazione femminile rappresentata dal fenomeno delle flappers.'),
     (2,'Descrivi gli aspetti più oscuri e contraddittori della società americana negli anni Venti, soffermandoti sulla svolta isolazionista e liberista, sull\'ondata di xenofobia e razzismo (come nel caso Sacco e Vanzetti) e sulle conseguenze del proibizionismo.'),
     (3,'Spiega quali furono le cause profonde del crollo della Borsa di Wall Street del 1929 (sovrapproduzione e speculazione finanziaria) e illustra gli effetti a catena che portarono alla Grande Depressione negli Stati Uniti e in Europa.'),
     (4,'Esponi i principi economici e le principali riforme del New Deal di Franklin Delano Roosevelt (dai lavori pubblici alle leggi sul lavoro e lo Stato sociale), valutandone l\'impatto comunicativo e il bilancio storico complessivo.')]
    L.append(('compi1',lambda:compiti_scene(1,items[:2]))); L.append(('compi2',lambda:compiti_scene(2,items[2:])))
    return L
if __name__=='__main__':
    sel=sys.argv[1:]
    for name,f in scene_list():
        if sel and name not in sel: continue
        d=f(); import time; t=time.time()
        build_scene(name,d); print(name,round(d['dur'],1),round(time.time()-t),'s',flush=True)
