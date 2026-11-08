# Stato della lezione per la master (sostituisce il blocco «PER LA MASTER» incollato da Sara).
# La chat scrive/aggiorna stato/<tag>.json e lo carica nel ramo stato-<tag>; la master legge tutti i rami stato-* da sola.
# uso:
#   python3 tools/stato.py TAG --materia "Storia III" --lezione "Lezione 2 · titolo" --docente "Prof. ..."
#   python3 tools/stato.py TAG --parte 1 --titolo "..." --stato IN_MONTAGGIO|IN_CODIFICA|PRONTA|FERMA \
#          [--video FILE.mp4] [--vtt FILE.vtt] [--scheda scheda_pubblicazione.json] [--timeline timeline.json] [--voci kore|segnaposto] [--quiz_ok si|no] [--fermi_ok si|no] [--sub_ok si|no]
#   python3 tools/stato.py TAG --manca "testo" --serve_master "testo" --domanda_sara "testo" --nota "testo"
#   python3 tools/stato.py TAG --invia      (carica su GitHub; si può aggiungere a qualsiasi chiamata)
# Durata, fotogrammi e peso del video li MISURA da solo (ffprobe): non si scrivono a mano.
import sys,os,json,argparse,subprocess,time,shutil
REPO='/home/claude/lezioni'
a=argparse.ArgumentParser();a.add_argument('tag')
for k in ['materia','lezione','docente','parte','titolo','stato','video','vtt','voci','quiz_ok','fermi_ok','sub_ok','manca','serve_master','domanda_sara','nota','scheda','timeline']:a.add_argument('--'+k)
a.add_argument('--invia',action='store_true');o=a.parse_args()
F=f'{REPO}/stato_locale/{o.tag}.json';os.makedirs(os.path.dirname(F),exist_ok=True)
S=json.load(open(F)) if os.path.exists(F) else {'tag':o.tag,'parti':{},'manca':'','serve_master':[],'domande_sara':[],'note':[]}
for k in ['materia','lezione','docente']:
    if getattr(o,k):S[k]=getattr(o,k)
def misura(v):
    r=subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets:format=duration,size','-of','json',v],capture_output=True,text=True)
    j=json.loads(r.stdout);d=float(j['format']['duration']);fr=int(j['streams'][0]['nb_read_packets'])
    return {'durata_s':round(d,1),'durata':'%d:%04.1f'%(d//60,d%60),'fotogrammi':fr,'fotogrammi_attesi':round(d*30),'peso_MB':round(int(j['format']['size'])/1e6,1)}
if o.parte:
    P=S['parti'].setdefault(str(o.parte),{})
    for k in ['titolo','stato','voci','quiz_ok','fermi_ok','sub_ok']:
        if getattr(o,k):P[k]=getattr(o,k)
    if o.video:P['video']=os.path.basename(o.video);P.update(misura(o.video))
    if o.vtt:P['vtt']=os.path.basename(o.vtt)
    if o.scheda:P['scheda']=json.load(open(o.scheda))   # serve alla master per il testo YouTube (capitoli)
    if o.timeline:P['timeline']=[x for x in json.load(open(o.timeline)) if str(x[0])[:2] in ('GL','RF','FI','T1','T2','T3','T4','T5','T6','T7','T8','T9','Q1')][:40]
    if P.get('stato')=='PRONTA':
        bad=[k for k in ['quiz_ok','fermi_ok','sub_ok'] if P.get(k)!='si']+(['voci'] if P.get('voci')!='kore' else [])+(['peso'] if P.get('peso_MB',0)>419 else [])
        if bad:P['stato']='IN_MONTAGGIO';print('NON PRONTA, manca:',bad)
if o.manca is not None and o.manca:S['manca']=o.manca
for k,l in [('serve_master','serve_master'),('domanda_sara','domande_sara'),('nota','note')]:
    if getattr(o,k):S[l].append({'quando':time.strftime('%d/%m %H:%M'),'testo':getattr(o,k)})
S['aggiornato']=time.strftime('%Y-%m-%d %H:%M:%S');json.dump(S,open(F,'w'),ensure_ascii=False,indent=1)
print(json.dumps(S,ensure_ascii=False,indent=1))
if o.invia:
    br='stato-'+o.tag;wt=f'/tmp/stato_wt_{o.tag}'
    subprocess.run(['git','-C',REPO,'worktree','remove','--force',wt],capture_output=True);shutil.rmtree(wt,ignore_errors=True)
    subprocess.run(['git','-C',REPO,'fetch','-q','origin',f'{br}:refs/remotes/origin/{br}'],capture_output=True)
    ex=subprocess.run(['git','-C',REPO,'rev-parse','--verify','-q',f'origin/{br}'],capture_output=True).returncode==0
    subprocess.run(['git','-C',REPO,'worktree','add','-q','--detach',wt]+([f'origin/{br}'] if ex else []),check=True)
    if not ex:subprocess.run(['git','-C',wt,'checkout','-q','--orphan',br],check=True);subprocess.run(['git','-C',wt,'rm','-rfq','.'],capture_output=True)
    os.makedirs(wt+'/stato',exist_ok=True);shutil.copy(F,wt+f'/stato/{o.tag}.json')
    subprocess.run(['git','-C',wt,'add','-f','stato'],check=True)
    subprocess.run(['git','-C',wt,'commit','-qm',f'stato {o.tag} {S["aggiornato"]}'],capture_output=True)
    r=subprocess.run(['git','-C',wt,'push','-q','origin',f'HEAD:refs/heads/{br}','--force'],capture_output=True,text=True)
    subprocess.run(['git','-C',REPO,'worktree','remove','--force',wt],capture_output=True)
    print('INVIATO alla master' if r.returncode==0 else 'PUSH NON RIUSCITO: '+r.stderr[-300:])
