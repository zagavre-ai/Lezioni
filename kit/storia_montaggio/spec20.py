# Dati della lezione 20 (Gli anni Novanta, il mondo post-bipolare)
TITOLO="Gli anni Novanta, il mondo post-bipolare"
ARGS=[
 ("Il crollo dell'URSS","fine del bipolarismo · Eltsin · Putin"),
 ("L'egemonia degli Stati Uniti","mondo unipolare · Guerra del Golfo · Clinton"),
 ("Le guerre nella ex Iugoslavia","Tito · pulizia etnica · Kosovo"),
 ("L'Europa negli anni Novanta","riunificazione tedesca · Maastricht · Blair"),
 ("L'Italia nella Seconda Repubblica","Mani pulite · bipolarismo · Berlusconi"),
 ("Medio Oriente, Africa e America Latina","Oslo · Talebani · Ruanda · Mandela"),
 ("I nuovi protagonisti in Asia","Cina · Tigri asiatiche · India"),
 ("La globalizzazione","Internet · No-Global · sfide globali"),
]
def T(c,h,s='',**k):
    d=dict(cue=c,h=h,s=s);d.update(k);return d
AN={
'AN1a':dict(kick="Il crollo dell'URSS",title="Le tappe della fine dell'Unione Sovietica",layout='timeline',items=[
  T('Nel millenovecentonovantuno fallisce','1991','fallisce il colpo di Stato dei comunisti conservatori',lab='1991'),
  T('il ventisei dicembre','26 dicembre','l\'URSS cessa ufficialmente di esistere',lab='26 dicembre'),
  T('La Russia, guidata','Boris Eltsin','dal comunismo al capitalismo',lab='anni Novanta'),
  T('Nel millenovecentonovantanove','Putin','assume la guida e restaura il controllo statale',lab='1999')]),
'AN3a':dict(kick='Le guerre nella ex Iugoslavia',title='La carta dell\'ex Iugoslavia',img='p7',items=[
  T('Sotto Tito','Sotto Tito','una federazione di repubbliche diverse'),
  T('con la morte di Tito','Nazionalismi','dopo la morte di Tito e la fine del comunismo'),
  T('La Bosnia Erzegovina','Bosnia Erzegovina','due entità dopo Dayton (1995)'),
  T('Le repubbliche ottengono','Indipendenze','Montenegro 2006 · Kosovo 2008')]),
}
def R(c,p,e,cue):return dict(concetto=c,parola=p,esempio=e,cue=cue)
MAPS={
'MAP1':dict(titolo="Il crollo dell'URSS",rami=[
  R('Fine del bipolarismo','1991','fine della Guerra fredda','Primo ramo'),
  R('Fine della storia','Fukuyama','trionfo del mercato','Secondo ramo'),
  R('Transizione russa','Eltsin','inflazione, oligarchi','Terzo ramo'),
  R('Cecenia','separatismo','guerra','Quarto ramo'),
  R('Putin','1999','controllo statale','Quinto ramo')]),
'MAP2':dict(titolo="L'egemonia degli Stati Uniti",rami=[
  R('Mondo unipolare','unica superpotenza','poliziotto del mondo','Primo ramo'),
  R('Bush Senior','1989-1993','Guerra del Golfo','Secondo ramo'),
  R('Kuwait','invaso dall\'Iraq','Saddam Hussein','Terzo ramo'),
  R('Clinton','crescita economica','accordi commerciali','Quarto ramo')]),
'MAP3':dict(titolo='Guerre nella ex Iugoslavia',rami=[
  R('Disgregazione','morte di Tito','fine del comunismo','Primo ramo'),
  R('Le guerre','1991-1995','Bosnia','Secondo ramo'),
  R('Pulizia etnica','massacri di civili','Srebrenica','Terzo ramo'),
  R('Accordi di Dayton','1995','pace in Bosnia','Quarto ramo'),
  R('Kosovo','1999','intervento NATO','Quinto ramo')]),
'MAP4':dict(titolo="L'Europa negli anni Novanta",rami=[
  R('Riunificazione tedesca','1990','costi dell\'Est','Primo ramo'),
  R('Maastricht','1992','nasce l\'UE, verso l\'euro','Secondo ramo'),
  R('Francia','alternanza','Mitterrand, Chirac','Terzo ramo'),
  R('Regno Unito','Tony Blair','Terza via','Quarto ramo'),
  R('Allargamento a Est','ex blocco sovietico','nuovi Paesi','Quinto ramo')]),
'MAP5':dict(titolo='La Seconda Repubblica',rami=[
  R('Mani pulite','corruzione','crollo di DC e PSI','Primo ramo'),
  R('Bipolarismo','centro-destra','centro-sinistra','Secondo ramo'),
  R('Berlusconi','Forza Italia','vince nel 1994','Terzo ramo'),
  R('Governi Prodi','debito pubblico','risanamento','Quarto ramo'),
  R('Nuove sfide','instabilità','flussi migratori','Quinto ramo')]),
'MAP6':dict(titolo='Medio Oriente, Africa, America Latina',rami=[
  R('Israele e Palestina','accordi di Oslo','1993','Primo ramo'),
  R('Estremismo islamico','Talebani','Al-Qaeda','Secondo ramo'),
  R('Africa','guerre civili','genocidio in Ruanda','Terzo ramo'),
  R('Sudafrica','fine apartheid','Mandela presidente','Quarto ramo'),
  R('America Latina','ritorno alla democrazia','crisi e disuguaglianze','Quinto ramo')]),
'MAP7':dict(titolo='I nuovi protagonisti in Asia',rami=[
  R('Cina','capitalismo','senza democrazia','Primo ramo'),
  R('Tigri asiatiche','boom industriale','Corea del Sud, Taiwan','Secondo ramo'),
  R('Crisi finanziaria','1997','stop temporaneo','Terzo ramo'),
  R('Giappone','stagnazione','instabilità politica','Quarto ramo'),
  R('India','liberalizzazione','centro del software','Quinto ramo')]),
'MAP8':dict(titolo='La globalizzazione',rami=[
  R('Mercati unificati','multinazionali','merci, capitali, servizi','Primo ramo'),
  R('Rivoluzione informatica','Internet','personal computer','Secondo ramo'),
  R('No-Global','Seattle','1999','Terzo ramo'),
  R('Sfide globali','6 miliardi','flussi migratori','Quarto ramo'),
  R('Allarmi ambientali','inquinamento','biodiversità','Quinto ramo')]),
'MAPF1':dict(titolo='Anni Novanta · il mondo post-bipolare',rami=[
  R('Crollo URSS','1991','fine Guerra fredda','Il crollo'),
  R('USA','unica superpotenza','Guerra del Golfo','Gli Stati Uniti'),
  R('Europa','Iugoslavia','Maastricht','L\'Europa vive'),
  R('Italia','Seconda Repubblica','Mani pulite','L\'Italia entra'),
  R('Resto del mondo','nuovi conflitti','nuovi protagonisti','Nel resto del mondo'),
  R('Globalizzazione','Internet','mercati','E tutto avviene')]),
}
