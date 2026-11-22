import json,re
def parole(path):
    """ricostruisce parole intere (t_inizio, t_fine, testo) dai token"""
    segs=json.load(open(path)); W=[]
    for si,s in enumerate(segs):
        cur=None
        for t,tok in s['parole']:
            if tok.startswith(' ') or cur is None:
                if cur: W.append(cur)
                cur=[t,t,tok.strip(),si]
            else:
                cur[2]+=tok; cur[1]=t
        if cur: W.append(cur)
    # fine parola = inizio della successiva (limitata)
    for i,w in enumerate(W):
        nxt=W[i+1][0] if i+1<len(W) else w[1]+0.4
        w[1]=min(max(w[1]+0.2,w[0]+0.1), nxt) if nxt>w[0] else w[1]+0.2
    return W

FIX={'brille':'briglie','brille.':'briglie.','jacard':'jacquard','ja':'jacquard','dessitura':'tessitura','subio':'subbio','armeture':'armature','repsito':'reps','crepe':'crêpe','crepe.':'crêpe.',
 'saglia':'saia','nevitta':'navetta','poa':'pois','feli':'fili','orbito':'ordito','orgiti':'orditi','narvature':'nervature','batabia':'batavia','brifrontura':'bifrontura','brifontura':'bifrontura','frontture':'fronture',
 'rettilini':'rettilinee','cantro':'cantre','ottagonale':'ortogonale','katena':'catena','coupet':'coupé','sccoccamento':'scoccamento','scocamenti':'scoccamenti','cimos':'cimose','reduzione':'riduzione','finisso':'finissaggio','annnerito':'annerito','annarimento':'annerimento','stilizzi':'stilisti','sfola':'spola','intrec':'intrecci'}
def frasi(path):
    W=parole(path); out=[]; cur=[]
    for w in W:
        cur.append(w)
        if re.search(r'[.?!]$',w[2]) and len(cur)>=1:
            out.append(cur); cur=[]
    if cur: out.append(cur)
    # unisci frammenti (<5 parole) alla frase vicina
    res=[]
    for f in out:
        if res and (len(f)<5 or len(res[-1])<5):
            res[-1]=res[-1]+f
        else: res.append(f)
    R=[]
    for f in res:
        txt=' '.join(FIX.get(w[2].lower(),FIX.get(w[2].lower().strip('.,?!'),w[2])) if False else FIX.get(w[2].lower(),w[2]) for w in f)
        R.append({'t0':round(f[0][0],2),'t1':round(f[-1][1],2),'testo':txt,'n':len(f)})
    return R
