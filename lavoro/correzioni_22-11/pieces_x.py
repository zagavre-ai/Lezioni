# -*- coding: utf-8 -*-
import sys, os, re, json
sys.path.insert(0,'/home/work/build')
from anim import *
import av, layout
fr=av.fr
from dati import ARG
V={v['nome']:v['testo'] for v in json.load(open('/home/work/new/testi_voci_nuovi.json'))}
OLD={v['nome']:v['testo'] for v in json.load(open('/home/work/voci/scambio/storia-V-lez17/testi_voci.json'))}
IMG=lambda p:f'/home/work/l17/img/p{p:02d}.png'
NAME={a['n']:a['nome'] for a in ARG}
APIMG={1:[(0,3)],2:[],3:[(0,6)],4:[(0,3),('Reagan',8)],5:[],6:[(0,11)],7:[(0,14)],8:[(0,17)]}
OUT='/home/work/build/pieces'
def ap_piece(n,base_page):
    t=V[f'AP{n}'];ss=sents(t);head=re.sub(r'^Approfondimento:\s*','',ss[0]).rstrip('.');body=ss[1:]
    # tempi su tutte le frasi
    d=vdur(f'AP{n}');tot=sum(len(x) for x in ss);lead=0.6;ts=[];x=lead
    for q in ss: ts.append(x);x+=d*len(q)/tot
    total=lead+d+1.5
    def img_for(i):
        cur=None
        for key,p in APIMG[n]:
            if key==0 or (i>=0 and any(key in body[k] for k in range(0,i+1))): cur=p
        return IMG(cur) if cur else None
    N=fr(total);items=[];states=[];kick=f"APPROFONDIMENTO · {NAME[n].upper()}"
    def H(i): return lit_html(head[0].upper()+head[1:],f"{n:02d} · {NAME[n].upper()}",body,i,base_page+i+1,img=img_for(i),chip="APPROFONDIMENTO",tfs=50)
    starts=[ts[0]-0.1]+[x-0.15 for x in ts[1:]]
    items.append((f'AP{n}_h',H(-1)));st=[(f'/home/work/build/lit/AP{n}_h.png',fr(starts[1]))]
    for i in range(len(body)):
        items.append((f'AP{n}_{i}',H(i)))
        end=fr(starts[i+2]) if i+2<len(starts) else N
        st.append((f'/home/work/build/lit/AP{n}_{i}.png',end-sum(f for _,f in st)))
    render(items,'/home/work/build/lit')
    out=f'{OUT}/AP{n}.mp4';nn=av.states_video(st,out)
    return dict(path=out,n=nn,audio=[(lead,'wav',vpath(f'AP{n}'))],pages=len(ss))
SCD={ # (parola chiave, riga a schermo) per ogni voce SCn_k, nell'ordine in cui il prof ne parla
1:[("Deficit americano","Nel 1969 Nixon eredita un forte deficit, causato dalla guerra in Vietnam e dai programmi di assistenza sociale."),("Fine di Bretton Woods","Nell'agosto 1971 Nixon sospende la convertibilità del dollaro in oro: finisce il sistema dei cambi fissi."),("Guerra del Kippur","Nel 1973 Egitto e Siria attaccano Israele, gli Stati Uniti lo sostengono e i paesi arabi reagiscono."),("Shock petrolifero","I paesi arabi dell'OPEC riducono l'offerta e quadruplicano il prezzo del petrolio: arrivano inflazione e recessione, la stagflazione.")],
2:[("Camp David","Nel 1978 Sadat e Begin firmano gli accordi di Camp David; Sadat è isolato e viene assassinato nel 1981."),("Libano","Nel 1975 scoppia la guerra civile in Libano; nel 1982 Israele lo invade per cacciare l'OLP."),("Sabra e Chatila","Nel 1982, durante l'invasione, si verificano tragici massacri nei campi profughi di Sabra e Chatila."),("Intifada","Nel 1987 nei territori occupati scoppia la rivolta popolare palestinese e cresce il peso di Hamas.")],
3:[("Caduta dello Shah","Nel 1979 una rivoluzione popolare travolge il regime dello Shah Reza Pahlavi."),("Repubblica Islamica","Khomeini fonda una teocrazia basata sulla sharia e su un forte sentimento anti-occidentale."),("Crisi degli ostaggi","Nel novembre 1979 gli studenti assaltano l'ambasciata americana e tengono in ostaggio il personale per oltre un anno."),("Guerra Iran-Iraq","Saddam Hussein attacca l'Iran nel 1980: la guerra finisce dopo otto anni, con quasi due milioni di morti.")],
4:[("Apertura alla Cina","Nel 1972 Nixon apre relazioni diplomatiche con la Cina di Mao, per isolare l'URSS."),("Distensione","Nascono i trattati SALT 1 e gli accordi di Helsinki sui confini europei e sui diritti umani."),("Watergate e Carter","Lo scandalo Watergate costringe Nixon alle dimissioni nel 1974; poi arrivano Ford e Carter."),("Svolta di Reagan","Nel 1981 Reagan adotta una linea dura contro l'«impero del male» e rilancia le spese militari, con lo scudo spaziale.")],
5:[("Cile","Eletto Allende nel 1970, nel 1973 un golpe di Pinochet instaura una dittatura feroce."),("Argentina","Tra il 1976 e il 1983 la giunta militare fa sparire migliaia di oppositori: i desaparecidos."),("Madri di Plaza de Mayo","Le Madri di Plaza de Mayo manifestano coraggiosamente per chiedere la verità sui figli scomparsi."),("Ritorno alla democrazia","La crisi economica e la sconfitta nelle Falkland del 1982 portano al ritorno della democrazia.")],
6:[("Difficoltà economiche","Gli shock petroliferi colpiscono le industrie europee con inflazione, disoccupazione e conflitti sindacali."),("Thatcher","Eletta nel 1979, la «Lady di ferro» avvia privatizzazioni, tagli allo stato sociale e lotta ai sindacati."),("Allargamento della CEE","Nel 1973 entrano Regno Unito, Irlanda e Danimarca; poi Grecia, Spagna e Portogallo."),("Parlamento europeo","Nel 1979 si tengono le prime elezioni a suffragio universale del Parlamento europeo.")],
7:[("Era Brežnev","L'URSS vive una lunga stagnazione economica, logorata dall'invasione dell'Afghanistan del 1979."),("Riforme di Gorbačev","Nel 1985 Gorbačev lancia la Perestrojka e la Glasnost e avvia il disarmo con gli Stati Uniti."),("Fine dei satelliti","Nel 1989 crollano i regimi comunisti dell'Est, cade il Muro di Berlino e la Germania si riunifica."),("Fine dell'URSS","Nel dicembre 1991 l'URSS si dissolve, nasce la CSI e Gorbačev si dimette.")],
8:[("Riforme di Deng","Dalla fine degli anni Settanta Deng apre la Cina al capitalismo con le Quattro modernizzazioni; l'economia cresce in modo vertiginoso."),("Nessuna apertura politica","Il Partito Comunista mantiene il controllo assoluto dello Stato, senza riforme democratiche."),("Piazza Tienanmen","Nella primavera del 1989 studenti e cittadini chiedono democrazia; a giugno i carri armati reprimono la protesta nel sangue."),("Condanna internazionale","La repressione provoca una ferma condanna internazionale.")]}
SCV={1:['SC1_1','SC1_2','SC1_3','SC1_4'],2:['SC2_1','SC2_2','SC2_4','SC2_3'],3:['SC3_1','SC3_2','SC3_3','SC3_4'],4:['SC4_1','SC4_2','SC4_3','SC4_4'],5:['SC5_1','SC5_2','SC5_4','SC5_3'],6:['SC6_1','SC6_2','SC6_3','SC6_4'],7:['SC7_1','SC7_2','SC7_3','SC7_4'],8:['SC8_1','SC8_2','SC8_3','SC8_4']}
def ripasso_piece(n,page):
    leads=[k+':' for k,_ in SCD[n]];texts=[t for _,t in SCD[n]]
    st=[];t=0.9;ev=[]
    for v in SCV[n]:
        st.append(t);ev.append((t,'wav',vpath(v)));t+=vdur(v)+0.9
    total=t+0.8;N=fr(total)
    def H(i): return lit_html("Ripasso: "+NAME[n],f"{n:02d} · {NAME[n].upper()}",texts,i,page,leads=leads,chip="PILLOLA DI STORIA",tfs=54,fs=36,allv=True,dark=True)
    items=[(f'RP{n}_s',H(-1))]+[(f'RP{n}_{i}',H(i)) for i in range(len(texts))]
    render(items,'/home/work/build/lit')
    states=[(f'/home/work/build/lit/RP{n}_s.png',fr(st[0]-0.1))]
    for i in range(len(texts)):
        end=fr(st[i+1]-0.1) if i+1<len(texts) else N
        states.append((f'/home/work/build/lit/RP{n}_{i}.png',end-sum(f for _,f in states)))
    out=f'{OUT}/RP{n}.mp4';nn=av.states_video(states,out)
    return dict(path=out,n=nn,audio=ev)
if __name__=='__main__':
    L,_=layout.layout(1)
    print(ap_piece(1,L[1]['ap']),ripasso_piece(1,L[1]['schema']))
