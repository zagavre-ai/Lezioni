import json,datetime as dt,sys
GG=['lun','mar','mer','gio','ven','sab','dom'];MM=['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
def fmtS(x): d=dt.date.fromisoformat(x);return f'{GG[d.weekday()]} {d.day} {MM[d.month-1]}'
SEZ=[(1,'Videolezioni registrate da visionare',3,[('tit',''),('arg',''),('ok','done')],[]),(2,'Studio di dispense, slide e materiali didattici',2,[('mat',''),('pag',''),('att',''),('ok','done')],[]),
(3,'Compiti scritti ed esercizi',2,[('tip',''),('arg',''),('lib',''),('sca','date:Scadenza')],[('cons','Consegna:'),('consA','Altro:')]),(4,'Temi, elaborati, relazioni e produzioni scritte',1,[('tip',''),('tit',''),('con','')],[]),
(5,'Preparazione orale e interrogazioni',2,[('arg',''),('pag',''),('tip',''),('dat','date:Data prevista')],[('asp','Aspetti da conoscere o saper esporre:'),('aspA','Altro:'),('dom','Domande guida o indicazioni del docente:')]),
(6,'Attività pratiche, tecniche e applicative',1,[('att',''),('str',''),('mod',''),('sca','date:Scadenza')],[]),(7,'Verifiche e attività programmate',1,[('tip',''),('arg',''),('dat','date:Data'),('not','')],[]),
(8,'Riepilogo delle attività assegnate',0,[],[('st',''),('rec','Da recuperare:')]),(9,'Correzione dei compiti e osservazioni del docente',1,[('cor',''),('esi','')],[]),(10,'Prima della prossima lezione lo studente dovrà',3,[('x','')],[])]
has=lambda v:(len(v)>0) if isinstance(v,list) else (v is True or (isinstance(v,str) and v.strip()!=''))
def testo(r):
    out=[]
    for n,t,rows,f,ex in SEZ:
        parti=[]
        for i in range(rows):
            v=[]
            for k,ty in f:
                if ty=='done': continue
                x=r.get(f'{n}.{i}.{k}')
                if has(x): v.append(', '.join(x) if isinstance(x,list) else (ty[5:]+' '+fmtS(x) if ty.startswith('date') else x))
            if v: parti.append(' · '.join(v)+(' [completata]' if r.get(f'{n}.{i}.ok') else ''))
        for k,l in ex:
            x=r.get(f'{n}.ex.{k}')
            if has(x): parti.append((l+' ' if l else '')+(', '.join(x) if isinstance(x,list) else x))
        if parti: out.append(f'{n}. {t.upper()}: '+' | '.join(parti))
    return '\n'.join(out)
for f in sys.argv[1:]:
    V=json.load(open(f))
    for v in V:
        if v['mat'].upper().startswith('ECNOLOGIE'): v['mat']='Tecnologie dei processi di produzione'
        v['testo']=testo(v['dati'])
    json.dump(V,open(f,'w'),ensure_ascii=False)
print('ok')
