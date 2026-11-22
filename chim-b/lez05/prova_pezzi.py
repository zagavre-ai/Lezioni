import sys,os; sys.path.insert(0,'/home/user/lav/eng'); sys.path.insert(0,'/home/user/lav/lez05/spec')
import pezzi, maps, contenuto as C
os.makedirs('lez05/out_p',exist_ok=True)
ctx=pezzi.Ctx('lez05/lav','lez05/vox','lez05/img','lez05/out_p')
a=C.ARG[0]
print('T',pezzi.titolo(ctx,1,a['titolo'],'IMG_A1_fusto'))
print('P',pezzi.approf(ctx,1,a['app'],'IMG_A1_fusto',a['titolo']))
print('R',pezzi.pillola(ctx,1,a['pill'],'Ripasso: '+a['titolo']))
print('QS',pezzi.quiz_scheda(ctx,1))
q=a['quiz'][3]; print('Q',pezzi.quiz_dom(ctx,1,4,q[0],q[1],q[2],q[3],'ORIGINE DELLE FIBRE VEGETALI'))
nodi=maps.MAPPE[1]['nodi']
print('M',pezzi.mappa(ctx,1,[f'M1_{i}' for i in range(4)],maps.VOCI_M1,nodi,'','MAPPA · FIBRE VEGETALI'))
print(ctx.prova and len(ctx.prova),'voci segnaposto')
