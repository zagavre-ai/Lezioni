# -*- coding: utf-8 -*-
import re,json,sys
from num2words import num2words
def parlato(s):
    s=s.replace('−','meno ').replace('%',' per cento').replace('EN 13402','E N tredici quattrocentodue').replace('CAD','cad').replace('CAM','cam').replace('TNT','T N T').replace('v.v.','gradi di vestibilità').replace('U.A.','unità antropometriche')
    s=re.sub(r'(\d+)\s*-\s*(\d+)',r'\1 e \2',s)
    s=re.sub(r'\d+',lambda m:num2words(int(m.group()),lang='it'),s)
    s=s.replace('·',',').replace('  ',' ')
    return s.strip()
def parti(S):
    P=getattr(S,'PARTI',None)
    if P:return P
    return [dict(args=[a['n'] for a in S.ARGS],glossario=S.GLOSSARIO,mappa_finale=S.MAPPA_FINALE,intro=S.INTRO,fin=S.FIN,titolo=S.TITOLO)]
ORD=['Primo','Secondo','Terzo','Quarto','Quinto','Sesto','Settimo','Ottavo','Nono','Decimo','Undicesimo','Dodicesimo']
def costruisci(S):
    V=[]
    def add(n,t):V.append(dict(nome=n,testo=parlato(t),lingua='it'))
    PT=parti(S);A={a['n']:a for a in S.ARGS}
    for p,pt in enumerate(PT,1):
        add('INTRO%d'%p,pt['intro'])
        if p>1:
            add('RPR%d_0'%p,'Prima di continuare, ripassiamo la parte precedente.')
            for k,n in enumerate(PT[p-2]['args'],1):add('RPR%d_%d'%(p,n),'%s: %s'%(ORD[k-1],A[n]['titolo'][0].lower()+A[n]['titolo'][1:]+'.'))
        for n in pt['args']:
            a=A[n]
            add('AN%d_0'%n,'Approfondiamo: %s.'%a['an']['t'])
            for k,(b,s,f) in enumerate(a['an']['items'],1):add('AN%d_%d'%(n,k),'%s: %s'%(s,f))
            m=a['mappa'];add('MP%d_0'%n,'La mappa: %s.'%m['titolo'])
            for k,(c,pp,e) in enumerate(m['rami'],1):add('MP%d_%d'%(n,k),'%s: parola chiave, %s. Per esempio, %s.'%(c,pp,e))
            add('R%d'%n,'Ripassiamo: '+a['ripasso'])
        add('GL%d_0'%p,'Ripassiamo le parole chiave%s.'%(' di questa parte' if len(PT)>1 else ' della lezione'))
        for k,(t,d) in enumerate(pt['glossario'],1):add('GL%d_%d'%(p,k),'%s: %s.'%(t,d))
        mf=pt['mappa_finale'];MP='MPF' if len(PT)==1 else 'MPF%d'%p;add(MP+'_0','La mappa di %s: %s.'%('tutta la lezione' if len(PT)==1 else 'questa parte',mf['titolo']))
        for k,(c,pp,e) in enumerate(mf['rami'],1):add('%s_%d'%(MP,k),'%s: %s, %s.'%(c,pp,e))
        add('RF%d_0'%p,'Prima di salutarci, ricapitoliamo insieme gli argomenti %s.'%('della lezione' if len(PT)==1 else 'di questa parte'))
        for k,n in enumerate(pt['args'],1):add('RF%d_%d'%(p,n),'%s: %s'%(ORD[k-1],A[n]['titolo'][0].lower()+A[n]['titolo'][1:]+'.'))
        add('FIN%d'%p,pt['fin'])
    add('COMP1',S.COMPITI)
    return V
def quiz(S):
    Q={}
    for a in S.ARGS:
        Q['Q%d'%a['n']]=dict(title='Quiz %d · %s'%(a['n'],a['titolo']),domande=[dict(domanda=d,giusta=g,sbagliate=s,spiegazione=sp) for d,g,s,sp in a['quiz']])
    return Q
if __name__=='__main__':
    import importlib;S=importlib.import_module(sys.argv[1]);V=costruisci(S)
    json.dump(V,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
    json.dump(quiz(S),open(sys.argv[3],'w'),ensure_ascii=False,indent=1)
    print(len(V),'voci;',sum(len(v['testo']) for v in V),'caratteri; ~%d s'%(sum(len(v['testo']) for v in V)/14.5))
