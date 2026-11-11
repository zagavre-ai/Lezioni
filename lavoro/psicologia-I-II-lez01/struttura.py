# Struttura della lezione: argomenti, sottotitoli, unità (frasi) e tabelle aggiunte
import json,re
B=json.load(open('/home/claude/lezioni/psicologia-I-II-lez01/blocks.json'))
ARG=[(0,'Le scienze umane come strumento'),(2,'I temi vicini ai giovani'),(3,'Scienze umane e scienze della natura'),(8,'I fattori del comportamento'),(13,'Le discipline e il percorso di studio')]
SUB=[(0,'Introduzione e scopo del corso'),(2,'Temi vicini ai giovani'),(3,'Scienze umane vs scienze della natura'),(8,'I fattori che influenzano il comportamento'),(13,'Le principali discipline delle scienze umane'),(17,'Il percorso di studio nel primo biennio')]
def R(*x): return [[bool(b),t] for b,t in x]
UNITS=[
 ('p',2,R((1,'Le Scienze umane come strumento'),(0,': non solo una materia teorica, ma una chiave per comprendere le proprie'),(1,' esperienze vissute'),(0,'.'))),
 ('p',2,R((1,'Obiettivo'),(0,': aprire e analizzare i diversi contesti dell\'esistenza umana.'))),
 ('p',2,R((1,'Temi vicini ai giovani'),(0,': analisi delle relazioni quotidiane, della'),(1,' ricerca di sé'),(0,' e dell\'inserimento in una'),(1,' società multiculturale e tecnologica'),(0,'.'))),
 ('p',3,R((1,'Oggetto di studio differente'),(0,':'))),
 ('li',3,R((0,'le Scienze della natura studiano la '),(1,'realtà materiale'),(0,' (es. chimica, biologia)'))),
 ('li',3,R((0,'le Scienze umane studiano l\''),(1,'essere umano'),(0,', le sue azioni e la sua mente.'))),
 ('p',3,R((1,'Obiettivo comune'),(0,': spiegare e comprendere la realtà circostante attraverso il'),(1,' metodo scientifico'),(0,'.'))),
 ('p',3,R((1,'Ricerca delle cause'),(0,': identificare le "leggi" o i fattori che'),(1,' determinano i comportamenti'),(0,' delle persone.'))),
 ('p',4,R((1,'Natura multi-causale'),(0,': le azioni umane non dipendono mai da una sola causa.'))),
 ('p',4,R((1,'Fattori principali analizzati'),(0,':'))),
 ('li',4,R((1,'fattori biologici e di sviluppo'),(0,': la crescita e le tappe evolutive della persona'))),
 ('li',4,R((1,'influenza dell\'ambiente'),(0,': il contesto sociale, le relazioni interpersonali e il ruolo della '),(1,'famiglia e della scuola'))),
 ('li',4,R((1,'dimensione storica'),(0,': come i comportamenti, i valori e le tradizioni cambiano '),(1,'nel corso del tempo'),(0,'.'))),
 ('p',5,R((1,'Psicologia'),(0,': studia il'),(1,' comportamento'),(0,' e i'),(1,' processi mentali'),(0,' dell\'individuo.'))),
 ('p',5,R((1,'Sociologia'),(0,': analizza le'),(1,' strutture sociali'),(0,', le istituzioni e i processi di interazione nei gruppi.'))),
 ('p',5,R((1,'Antropologia'),(0,': studia i'),(1,' popoli'),(0,' e le diverse'),(1,' culture'),(0,' umane nel mondo.'))),
 ('p',5,R((1,'Metodologia della ricerca'),(0,': offre gli'),(1,' strumenti scientifici'),(0,' e le tecniche per svolgere le indagini sul campo.'))),
 ('p',6,R((1,'Articolazione del programma'),(0,': studio approfondito della'),(1,' psicologia'),(0,' (processi cognitivi, memoria, pensiero).'))),
 ('p',6,R((0,'Introduzione alla'),(1,' metodologia della ricerca'),(0,' statistica e dei dati.'))),
 ('p',6,R((0,'Integrazione con percorsi di'),(1,' Educazione civica'),(0,' per riflettere sui temi di attualit\u00e0 della societ\u00e0 civile.'))),
]
# indici dei blocchi: ogni unita e un blocco; ARG/SUB riferiti all'indice dell'unita
def txt(runs): return ''.join(t for _,t in runs)
def units():
    U=[]
    for i,(t,pg,runs) in enumerate(UNITS):
        na=[k for k,(s,_) in enumerate(ARG) if s<=i][-1]; ns=[k for k,(s,_) in enumerate(SUB) if s<=i][-1]
        U.append({'t':t,'runs':runs,'a':na,'s':ns,'b':i,'pg':pg,'txt':txt(runs),'par0':True})
    return U
if __name__=='__main__':
    import json
    U=units();print(len(U))
    json.dump(U,open('/home/claude/lezioni/psicologia-I-II-lez01/units.json','w'),ensure_ascii=False)
