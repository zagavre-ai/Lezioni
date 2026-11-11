import sys,json,os,re
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez01')
import dark_psi as dark
D='/home/claude/lezioni/psicologia-I-II-lez01/'
OUT=D+'dk'
os.makedirs(OUT,exist_ok=True)
TT=[(['Le scienze umane','come strumento'],'chiave · esperienze vissute','Le scienze umane come strumento'),
(['I temi vicini','ai giovani'],'relazioni · ricerca di sé · società','I temi vicini ai giovani'),
(['Scienze umane e','scienze della natura'],'oggetto di studio · metodo','Scienze umane e scienze della natura'),
(['I fattori del','comportamento'],'biologici · ambiente · storia','I fattori del comportamento'),
(['Le discipline e','il percorso di studio'],'psicologia · sociologia · antropologia','Le discipline e il percorso di studio')]
TX=json.load(open(D+'voci/testi_voci.json'))
def vdur(k):
    f=D+'voci/wav/meta_S1.json'
    if os.path.exists(f):
        M=json.load(open(f))
        if k in M:return M[k]['dur']
    return len(' '.join(TX[k]))/14.8
def caps(text,dur,a0=0.9):
    ss=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()];tot=sum(len(s) for s in ss);t=a0;out=[];span=dur-a0-.4
    for s in ss: d=span*len(s)/tot;out.append([round(t,2),round(t+d,2),s]);t+=d
    return out
SP={}
for i,(l,e,full) in enumerate(TT):
    SP['T%d'%(i+1)]={'type':'title','num':str(i+1).zfill(2),'total':5,'lines':l,'ex':e,'fs':128 if max(len(x) for x in l)<17 else 104,'dur':3.6,'lineY':720 if len(l)==2 else 600}
    SP['Q%d'%(i+1)]={'type':'quiz','topic':full,'act':'Quiz %d'%(i+1),'pts':'5 domande · per continuare almeno l’80%','dur':4.0}
    v=vdur('R%d'%(i+1));dd=max(13.0,round(v+1.8,2))
    SP['R%d'%(i+1)]={'type':'repaso','kicker':'Ripasso con voce','topic':full,'caps':caps(' '.join(TX['R%d'%(i+1)]),v+0.9),'dur':dd}
json.dump(SP,open(D+'scripts_dark.json','w'),ensure_ascii=False,indent=1)
if __name__=='__main__':
    import shutil
    for k in (sys.argv[1:] or SP):
        if os.path.exists(f'{OUT}/{k}.mp4'):continue
        dark.render(SP[k],f'{OUT}/{k}',1.0);shutil.rmtree(f'{OUT}/{k}',ignore_errors=True);print(k,flush=True)
