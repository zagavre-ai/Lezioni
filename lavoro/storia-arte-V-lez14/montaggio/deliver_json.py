import sys,json,openpyxl;sys.path.insert(0,'/tmp/w/build')
from contents import *
E1={
'T1':["I realismi moderni si sviluppano tra le due guerre mondiali, in Europa e in Nord America.","In Germania questo movimento si incarna nella Nuova Oggettività (Neue Sachlichkeit).","Racconta senza filtri le drammatiche conseguenze della guerra e l'instabilità della Repubblica di Weimar.","Nel 1937 a Monaco viene organizzata la mostra dell'Arte degenerata.","La Camera della cultura del Reich è guidata da Joseph Goebbels."],
'T2':["Otto Dix si forma a Dresda ed è segnato dall'esperienza al fronte.","Metropolis affianca lo sfarzo di un locale da ballo borghese alla miseria dei reduci di guerra.","Metropolis è un'opera a tecnica mista e tempera su tavola.","L'opera riprende la struttura formale dei trittici sacri del gotico e del Rinascimento tedesco e fiammingo.","Il regime non esalta Dix perché rappresenta i militari in modo inglorioso."],
'T3':["Il 26 aprile 1937 l'aviazione tedesca bombarda la cittadina basca di Guernica.","Il governo repubblicano spagnolo affida a Picasso un'opera per l'Esposizione Internazionale di Parigi.","La tela è quasi monocromatica: bianco, nero e grigio.","Nella composizione si contano otto figure divise in tre gruppi.","Dalla spada spezzata del soldato spunta un piccolo fiore, la speranza."],
'T4':["La rivoluzione del 1910 porta alla nascita del Rinascimento messicano.","La pittura murale ha finalità didattiche ed educative per il popolo.","Diego Rivera realizza grandiosi cicli di affreschi nel Palazzo Nazionale.","Nel 1925 un incidente in autobus causa a Frida Kahlo permanenti sofferenze fisiche.","Una colonna ionica di pietra, spezzata in più punti, sostituisce la colonna vertebrale."],
'T5':["Il presidente Roosevelt lancia il New Deal per contrastare la crisi.","Charles Sheeler dipinge American Landscape nel 1930.","American Landscape raffigura lo stabilimento della Ford sul fiume Rouge, senza alcuna presenza umana.","L'uomo di American Gothic stringe un forcone a tre punte, simbolo del duro lavoro manuale.","Nighthawks è il simbolo dell'incomunicabilità e dell'alienazione nelle grandi metropoli moderne."],
'T6':["La Straight Photography è la fotografia diretta, senza ritocchi né alterazioni.","Walker Evans e Dorothea Lange realizzano reportage sulla povertà rurale.","Migrant Mother è lo scatto di Dorothea Lange del 1936.","Florence Owens Thompson è la donna fotografata a Nipomo, in California.","Evans fotografa l'interno di una povera baracca di legno in Alabama."]}
out={}
for k,qs in QUIZ.items():
    n=int(k[1:]);items=[]
    for (p,ans),e in zip(qs,E1[k]):
        items.append(dict(p=p,a=ans[0],w=ans[1:],e=e,ref=e))
    out['Q%d'%n]=dict(title=f'Quiz {n} · {ARG[n-1]}',items=items)
json.dump(out,open('/tmp/w/build/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
wb=openpyxl.load_workbook('/tmp/w/mat/DOMANDE.LEZIONE.14.xlsx');ws=wb.active
dom=[]
for i,r in enumerate(list(ws.iter_rows(values_only=True))[1:],1):
    if not r[0]:continue
    dom.append(dict(n=i,p=str(r[0]).strip(),a=str(r[1]).strip(),w=[str(x).strip() for x in r[2:5]]))
json.dump(dict(titolo="Verifica finale · Storia dell'arte V · I nuovi realismi",domande=dom),open('/tmp/w/build/verifica_finale.json','w'),ensure_ascii=False,indent=1)
json.dump(dict(titolo="Compiti · Storia dell'arte V · I nuovi realismi",esercizi=[dict(n=i+1,tipo='aperta',testo=t) for i,t in enumerate(COMPITI)]),open('/tmp/w/build/compiti.json','w'),ensure_ascii=False,indent=1)
print(len(dom),'domande verifica',sum(len(v['items']) for v in out.values()),'quiz')
