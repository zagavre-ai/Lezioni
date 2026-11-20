# -*- coding: utf-8 -*-
import json,re
RAW=json.load(open('/tmp/L18/slides18.json'))
PG={1:2,2:3,3:6,4:7,5:9,6:10}
def q(s):return re.sub(r'"([^"]+)"',r'«\1»',s)
KW={1:["Economia distrutta","Mercato nero","Violenza"],2:["Partiti di massa","Amnistia","Referendum"],3:["Madri costituenti","Costituzione","Tre poteri"],4:["Elezioni 1948","Liberismo","Politica estera"],5:["Boom","Nuovi consumi","Criticità"],6:["Centrosinistra","Riforme","Il PCI"]}
def C(n,i):
    r=RAW[str(PG[n])]['cards'][i];return (q(r[0]),q(r[1]),KW[n][i])
TITLES={n:q(RAW[str(PG[n])]['title']) for n in PG}
NOMI={1:"Un Paese da ricostruire",2:"La nascita della Repubblica",3:"La Costituzione",4:"Il Centrismo (1948-1953)",5:"Il miracolo economico",6:"Il Centrosinistra (1953-1963)"}
SCH={1:[("Paese distrutto","fabbriche ferme, mancano i beni di prima necessità"),("Disoccupazione","mercato nero; reduci e sfollati in difficoltà"),("Centro-Nord","regolamenti di conti contro gli ex fascisti"),("Sud","i contadini occupano le terre dei latifondisti")],
2:[("Partiti di massa","DC, PCI e PSI"),("Amnistia","Togliatti, ministro della Giustizia, per i reati politici"),("2 giugno 1946","referendum: per la prima volta votano le donne"),("La Repubblica","circa 12 milioni di voti contro 10: nasce la Costituente")],
3:[("Madri costituenti","21 donne: Iotti, Merlin, Mattei"),("Uguaglianza","giuridica e sociale tra i sessi"),("1° gennaio 1948","repubblica democratica fondata sul lavoro"),("Tre poteri","Parlamento, Governo, Magistratura")],
4:[("Elezioni 1948","la DC vince contro il Fronte democratico popolare"),("Liberismo","De Gasperi ed Einaudi"),("Riforme","riforma agraria e Cassa per il Mezzogiorno"),("Blocco occidentale","Piano Marshall, Patto Atlantico, CECA")],
5:[("Boom economico","anni Cinquanta e Sessanta: auto, siderurgia, chimica"),("Nuovi consumi","elettrodomestici, automobili, televisione"),("Vacanze di massa","nascono con il boom"),("Criticità","divario Nord-Sud, migrazioni, speculazione edilizia")],
6:[("Apertura ai socialisti","governi Fanfani e Moro"),("ENEL","nazionalizzazione dell'energia elettrica"),("Scuola media","unica e obbligatoria fino a 14 anni"),("PCI","dopo l'Ungheria cerca l'autonomia da Mosca")]}
TERMS1=[("Mercato nero","commercio di beni a prezzi altissimi, fuori dal controllo dello Stato"),("Amnistia","il perdono dei reati politici commessi durante la guerra"),("Referendum istituzionale","il voto per scegliere tra Repubblica e Monarchia"),("Assemblea Costituente","l'assemblea eletta per scrivere la Costituzione"),("Separazione dei poteri","legislativo, esecutivo e giudiziario affidati a organi diversi")]
TERMS2=[("Centrismo","governi della DC con i partiti di centro"),("Piano Marshall","gli aiuti economici americani per la ricostruzione"),("Patto Atlantico","l'alleanza militare del blocco occidentale, la NATO"),("Boom economico","la crescita industriale eccezionale del 1958-1963"),("Nazionalizzazione","il passaggio di un settore sotto il controllo dello Stato")]
AN1={1:'AN1a',2:'AN2a',3:'AN3a',4:'AN4a',5:'AN5b',6:'AN6a'}
ANMAP={4:'confine'}
