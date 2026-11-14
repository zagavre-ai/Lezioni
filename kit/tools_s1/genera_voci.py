#!/usr/bin/env python3
"""Genera testi_voci.json e quiz.json dalla specifica; con --invia li carica sul ramo voci-<tag> (un solo invio per lezione)."""
import sys,os,json,subprocess,shutil,importlib.util
spec_path=sys.argv[1];out=sys.argv[2]
sp=importlib.util.spec_from_file_location('spec',spec_path);S=importlib.util.module_from_spec(sp);sp.loader.exec_module(S)
voci=[];quiz={}
J=lambda l:' '.join(l)
for P in S.PARTI:
    n=P['n'];voci.append(('INTRO%d'%n,J(P['intro'])))
    for aid in P['argomenti']:
        A=[a for a in S.ARG if a['id']==aid][0]
        voci.append(('R%d'%aid,J(A['ripasso'])))
        for an in A['an']:voci.append((an['nome'],J(an['voce'])))
        voci.append(('MAP%d'%aid,J(A['mappa']['voce'])))
        quiz['Q%d'%aid]={'title':'Quiz %d · %s'%(aid,A['breve']),'items':[{'p':p,'a':a,'w':w,'e':e} for p,a,w,e in A['quiz']]}
    voci.append(('MAPF%d'%n,J(P['mappa_fin']['voce'])));voci.append(('GL%d'%n,J(P['voce_gl'])))
    voci.append(('RF%d'%n,J(P['voce_rf'])));voci.append(('FIN%d'%n,J(P['voce_fin'])))
os.makedirs(out,exist_ok=True)
json.dump([{'nome':n,'testo':t,'lingua':'it'} for n,t in voci],open(out+'/testi_voci.json','w'),ensure_ascii=False,indent=1)
json.dump(quiz,open(out+'/quiz.json','w'),ensure_ascii=False,indent=1)
print(len(voci),'voci,',sum(len(v['items']) for v in quiz.values()),'domande; parole:',sum(len(t.split()) for n,t in voci),'~minuti di voce:',round(sum(len(t.split()) for n,t in voci)/2.6/60,1))
