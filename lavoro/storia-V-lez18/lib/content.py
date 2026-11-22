# -*- coding: utf-8 -*-
import json,re
W='/home/user/work18'
ARG={
1:dict(nome="Un Paese da ricostruire",lines=["Un Paese","da ricostruire"],ex="mercato nero · reduci · latifondi",fs=128,ly=720,prof="Un Paese da ricostruire (il Secondo Dopoguerra)",an='AN1a',R='R1',P='P1',SC='SC1',Q='Q1'),
2:dict(nome="La nascita della Repubblica",lines=["La nascita","della Repubblica"],ex="De Gasperi · Togliatti · 2 giugno 1946",fs=128,ly=720,prof="Il panorama politico e la nascita della Repubblica",an='AN2a',R='R2',P='P2',SC='SC2',Q='Q2'),
3:dict(nome="La Costituzione",lines=["La Costituzione"],ex="Nilde Iotti · Lina Merlin · 1948",fs=150,ly=600,prof="La Costituzione e il nuovo sistema politico",an='AN3a',R='R3',P='P3',SC='SC3',Q='Q3'),
4:dict(nome="Il Centrismo (1948-1953)",lines=["Il Centrismo","(1948-1953)"],ex="De Gasperi · Piano Marshall · NATO",fs=128,ly=720,prof="Gli anni del Centrismo (1948-1953)",an='AN4a',R='R4',P='P4',SC='SC4',Q='Q4'),
5:dict(nome="Il miracolo economico",lines=["Il miracolo","economico"],ex="Fiat 500 · boom · Nord e Sud",fs=128,ly=720,prof="Il miracolo economico e le sue criticità",an='AN5b',R='R5',P='P5',SC='SC5',Q='Q5'),
6:dict(nome="Il Centrosinistra (1953-1963)",lines=["Il Centrosinistra","(1953-1963)"],ex="Fanfani · Moro · ENEL",fs=128,ly=720,prof="La stagione del Centrosinistra (1953-1963)",an='AN6a',R='R6',P='P6',SC='SC6',Q='Q6'),
}
SCH={1:[("Paese distrutto","fabbriche ferme, mancano i beni di prima necessità"),("Disoccupazione","mercato nero; reduci e sfollati in difficoltà"),("Centro-Nord","regolamenti di conti contro gli ex fascisti"),("Sud","i contadini occupano le terre dei latifondisti")],
2:[("Partiti di massa","Democrazia Cristiana, Partito comunista e Partito socialista"),("Amnistia","Togliatti, ministro della Giustizia, per i reati politici"),("2 giugno 1946","referendum: per la prima volta votano le donne"),("La Repubblica","circa 12 milioni di voti contro 10: nasce la Costituente")],
3:[("Madri costituenti","21 donne: Iotti, Merlin, Mattei"),("Uguaglianza","giuridica e sociale tra i sessi"),("1° gennaio 1948","repubblica democratica fondata sul lavoro"),("Tre poteri","Parlamento, Governo, Magistratura")],
4:[("Elezioni 1948","la Democrazia Cristiana vince contro il Fronte democratico popolare"),("Liberismo","De Gasperi ed Einaudi"),("Riforme","riforma agraria e Cassa per il Mezzogiorno"),("Blocco occidentale","Piano Marshall, Patto Atlantico e Comunità del carbone e dell'acciaio")],
5:[("Boom economico","anni Cinquanta e Sessanta: auto, siderurgia, chimica"),("Nuovi consumi","elettrodomestici, automobili, televisione"),("Vacanze di massa","nascono con il boom"),("Criticità","divario Nord-Sud, migrazioni, speculazione edilizia")],
6:[("Apertura ai socialisti","governi Fanfani e Moro"),("Enel","nazionalizzazione dell'energia elettrica"),("Scuola media","unica e obbligatoria fino a 14 anni"),("Partito comunista","dopo l'Ungheria cerca l'autonomia da Mosca")]}
QUIZ=json.load(open(W+'/scambio/storia-V-lez18/quiz.json'))
def load_cards(n):return json.load(open(f'{W}/cards/arg{n}.json'))
