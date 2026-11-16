# Testo delle slide del docente (lezione 20), dal PDF del prof
import re
SLIDES=[
 ("Il crollo dell'URSS e il nuovo ordine mondiale","La fine della Guerra fredda",[
  ("La fine del bipolarismo","il crollo dell'Unione Sovietica (1991) chiude l'era della Guerra fredda e l'equilibrio basato sul contrasto tra USA e URSS."),
  ("La tesi della \"fine della storia\"","il politologo Francis Fukuyama teorizza il trionfo definitivo della democrazia liberale e dell'economia di mercato a livello globale."),
  ("La transizione russa","sotto la presidenza di Boris Elcin, la Russia affronta il passaggio traumatico a un'economia di mercato, caratterizzato da forte inflazione, impoverimento e dalla nascita dei potenti \"oligarchi\"."),
  ("L'ascesa di Putin","nel 1999 Vladimir Putin assume la guida della Russia, restaurando il controllo statale e affrontando duramente la crisi separatista e la guerra in Cecenia.")]),
 ("L'egemonia geopolitica degli Stati Uniti","Un mondo unipolare",[
  ("Un mondo unipolare","gli Stati Uniti rimangono l'unica superpotenza mondiale, assumendo il ruolo di \"poliziotto del mondo\"."),
  ("La presidenza Bush Senior (1989-1993)","nel 1991 gli USA guidano una coalizione internazionale nella Guerra del Golfo per respingere l'invasione del Kuwait da parte dell'Iraq di Saddam Hussein."),
  ("La presidenza Clinton (1993-2001)","caratterizzata da una forte crescita economica interna e da una politica estera volta a promuovere la democrazia e gli accordi commerciali globali.")]),
 ("Le guerre nella ex Iugoslavia","La disgregazione della federazione",[
  ("La disgregazione della federazione","con la morte di Tito e la fine del comunismo, emergono i nazionalismi storici che portano alla frantumazione della Iugoslavia."),
  ("I conflitti e la pulizia etnica","tra il 1991 e il 1995 scoppiano guerre sanguinose; il conflitto in Bosnia Erzegovina vede drammatici episodi di \"pulizia etnica\" e massacri di civili (come a Srebrenica)."),
  ("Il Kosovo e l'intervento NATO","nel 1999 la repressione serba contro la maggioranza albanese in Kosovo provoca l'intervento militare della NATO e i bombardamenti sulla Serbia.")]),
 ("Lo scenario europeo negli anni Novanta","Germania, Unione Europea, Francia e Regno Unito",[
  ("La riunificazione tedesca","nel 1990 la Germania si riunifica dopo la caduta del muro di Berlino, affrontando alti costi economici per integrare le regioni orientali dell'ex RFT."),
  ("L'Unione Europea e il trattato di Maastricht","nel 1992 nasce ufficialmente l'UE, ponendo le basi per la moneta unica (Euro) e per una maggiore integrazione politica ed economica."),
  ("Evoluzione politica in Francia e Regno Unito","in Francia si assiste all'alternanza tra il socialista Mitterrand e il conservatore Chirac. Nel Regno Unito, dopo il lungo periodo conservatore di Margaret Thatcher e John Major, vince il laburista Tony Blair con la linea della \"Terza via\"."),
  ("L'allargamento a Est","l'Unione Europea avvia i processi di integrazione per accogliere i Paesi dell'ex blocco sovietico dell'Europa centrale e orientale.")]),
 ("L'Italia nella \"Seconda Repubblica\"","Da Mani pulite a Berlusconi",[
  ("La fine dei vecchi partiti","all'inizio degli anni Novanta, le inchieste giudiziarie di \"Mani pulite\" contro la corruzione provocano il crollo dei partiti storici (Democrazia Cristiana, PSI)."),
  ("La nascita del bipolarismo","il sistema politico si riorganizza intorno a due grandi coalizioni alternative: il centro-destra e il centro-sinistra."),
  ("L'ascesa di Silvio Berlusconi","nel 1994 l'imprenditore televisivo entra in politica con il nuovo partito Forza Italia, vincendo le elezioni e introducendo uno stile comunicativo inedito."),
  ("Le sfide dei governi","l'Italia affronta una forte instabilità politica, l'esigenza di risanare il debito pubblico (governi Prodi) e l'inizio dei grandi flussi migratori.")]),
 ("Medio Oriente, Africa e America Latina","Conflitti e transizioni",[
  ("Il conflitto israelo-palestinese","nel 1993 gli accordi di Oslo accendono la speranza di pace con la nascita dell'Autorità Nazionale Palestinese, ma il processo fallisce nei primi anni Duemila."),
  ("L'estremismo islamico","si diffonde il fondamentalismo radicale in Medio Oriente; in Afghanistan si afferma il regime teocratico dei Talebani, che offre protezione alla rete terroristica di Al-Qaeda fondata da Osama bin Laden."),
  ("Le crisi in Africa","il continente è devastato da guerre civili e drammi umanitari, tra cui il tragico genocidio in Ruanda del 1994 e l'instabilità in Somalia e in Congo."),
  ("Il Sudafrica e la fine dell'Apartheid","nel 1994 si tengono le prime elezioni libere e Nelson Mandela viene eletto presidente, ponendo fine alla segregazione razziale."),
  ("La transizione in America Latina","si consolida il ritorno alla democrazia in Paesi come Cile, Argentina e Brasile, che tuttavia devono affrontare pesanti crisi economiche e forti disuguaglianze sociali.")]),
 ("I nuovi protagonisti in Asia","Cina, Tigri asiatiche, Giappone, India",[
  ("La Cina e il \"capitalismo senza democrazia\"","dopo la repressione di piazza Tienanmen (1989), Pechino mantiene un rigido controllo politico autoritario, ma avvia una straordinaria apertura all'economia di mercato, diventando una potenza economica mondiale."),
  ("Le \"Tigri asiatiche\"","Paesi come Corea del Sud, Taiwan, Singapore e Hong Kong registrano un boom industriale e tecnologico, interrotto temporaneamente da una grave crisi finanziaria nel 1997."),
  ("Il Giappone in stallo","dopo i successi dei decenni precedenti, il Giappone entra negli anni Novanta in una fase di stagnazione economica e instabilità politica."),
  ("Il boom dell'India","avvia riforme di liberalizzazione economica, diventando un centro mondiale per l'industria del software, pur dovendo convivere con grandi sacche di povertà e con le divisioni del sistema delle caste.")]),
 ("La globalizzazione e le sue sfide","Un mondo interconnesso",[
  ("Un mondo interconnesso","la globalizzazione economica unifica i mercati mondiali attraverso la libera circolazione di merci, capitali e servizi, guidata dalle aziende multinazionali."),
  ("La rivoluzione informatica","la diffusione dei personal computer e la nascita di Internet cambiano radicalmente il modo di comunicare, lavorare e accedere alle informazioni, riducendo le distanze planetarie."),
  ("I movimenti No-Global","nascono forti movimenti di protesta (come i tumulti di Seattle nel 1999) che criticano gli effetti della globalizzazione, accusata di aumentare le disuguaglianze tra Paesi ricchi e poveri."),
  ("Sfide globali e flussi migratori","il mondo deve affrontare la crescita demografica (che supera i 6 miliardi a fine secolo), l'aumento dei flussi migratori e i primi grandi allarmi ambientali legati all'inquinamento e alla perdita di biodiversità.")]),
]
def sents(rest):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ù"«])',rest) if x.strip()]
def groups(n):
    if n<=3:return [list(range(n))]
    if n==4:return [[0,1],[2,3]]
    return [list(range(3)),list(range(3,n))]
