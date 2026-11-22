import json
N=[]
def A(n,t):N.append({"nome":n,"testo":t})
A("INTRO1_R2","Benvenuti alla videolezione di Storia: l'Italia repubblicana. In questa prima parte vediamo l'Italia che esce dalla guerra distrutta, la nascita della Repubblica con il referendum del due giugno millenovecentoquarantasei e la Costituzione. Alla fine di ogni argomento troverai un ripasso e un quiz di cinque domande.")
A("INTRO2_R2","Benvenuti alla seconda parte della videolezione di Storia sull'Italia repubblicana. Prima di ripartire, ripassiamo insieme la prima parte, argomento per argomento.")
A("SP2_1","Primo argomento: un Paese da ricostruire. L'Italia esce dalla guerra distrutta dai bombardamenti alleati e dalle rappresaglie tedesche. Le fabbriche e le infrastrutture sono devastate, la produzione è ferma e mancano i beni di prima necessità. Crescono la disoccupazione e il mercato nero. Nel Centro-Nord ci sono regolamenti di conti contro gli ex fascisti, nel Sud i contadini occupano le terre dei latifondisti.")
A("SP2_2","Secondo argomento: il panorama politico e la nascita della Repubblica. Guardiamo la mappa. Nel millenovecentoquarantasei le italiane e gli italiani scelgono la Repubblica ed eleggono l'Assemblea costituente. Nel millenovecentoquarantotto votano la Democrazia cristiana, che sconfigge il Fronte popolare democratico.")
A("SP2_3","Terzo argomento: la Costituzione. Fra i membri dell'Assemblea costituente ci sono ventuno donne, le madri costituenti. La Costituzione entra in vigore il primo gennaio del millenovecentoquarantotto. Ora vediamo gli anni del Centrismo, il miracolo economico e la stagione del Centrosinistra.")
M={"M2":["Come nasce la Repubblica italiana? Al centro della mappa, le italiane e gli italiani.",
 "Nel millenovecentoquarantasei.","Nel millenovecentoquarantotto.","Nel millenovecentoquarantasei scelgono la Repubblica.","E eleggono l'Assemblea costituente.",
 "Nel millenovecentoquarantotto votano la Democrazia cristiana.","Che sconfigge il Fronte popolare democratico.","Ecco la mappa completa."],
"M5":["Quali sono i principali avvenimenti dell'età detta del centrismo? Al centro della mappa, la crescita economica dell'età del centrismo.",
 "La crescita si basa sull'appartenenza al blocco occidentale.","Si basa sulla partecipazione alla Cee.","Si basa sul basso costo del lavoro.",
 "La crescita causa cambiamenti nel costume e nei consumi.","Con la diffusione di elettrodomestici, televisori, automobili e scooter.",
 "Causa anche intensi flussi migratori.","Diretti dal Sud al Nord.","E dalle campagne alle città.","Ecco la mappa completa."],
"M6":["Che cosa succede alla Democrazia cristiana? Al centro della mappa, la Democrazia cristiana.","Con Fanfani e Moro.",
 "Raggiunge un'alleanza con il Partito socialista di Nenni.","E forma i governi di centrosinistra, dal millenovecentosessantadue.",
 "Che approvano la nazionalizzazione dell'energia elettrica.","E la riforma della scuola media.","Ecco la mappa completa."]}
for k,v in M.items():
    for i,t in enumerate(v):A(f"{k}_{i+1:02d}",t)
json.dump(N,open('nuovi_testi.json','w'),ensure_ascii=False,indent=1)
old=json.load(open('scambio/storia-V-lez18/testi_voci.json'))
names={x['nome'] for x in old}
old+= [x for x in N if x['nome'] not in names]
json.dump(old,open('scambio/storia-V-lez18/testi_voci.json','w'),ensure_ascii=False,indent=1)
print(len(N),len(old))
