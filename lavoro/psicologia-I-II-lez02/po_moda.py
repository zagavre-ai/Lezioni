# Schemi di ripasso con voce (Psicologia): le righe compaiono e si evidenziano a tempo di voce
import sys,json,os
sys.path.insert(0,'/home/claude/v5')
import po9
EY='[SCHEMA DI RIPASSO]'
S={}
def sch(k,title,rows,cols='32% 68%',fs=31,header=('Voce','In sintesi')):
    S[k]=dict(title=title,cols=cols,fs=fs,header=list(header),rows=[list(r) for r in rows],note=None)
sch('S1',"Che cos'è la mente",[
 ['Psicologia','letteralmente «scienza dell\'anima», dai termini greci psyché e lógos'],
 ['Definizione scientifica','la disciplina che studia il comportamento e i processi mentali dell\'essere umano'],
 ['Attività mentali','ricordare, ragionare, immaginare: memoria, ragionamento, immaginazione'],
 ['Mente e corpo','le attività mentali si distinguono dalle funzioni biologiche del corpo, come respirazione e digestione']])
sch('S2','Le origini: il punto di vista dei filosofi',[
 ['Antica Grecia','Platone e Aristotele (V-IV secolo a.C.) si interrogano sulla psiche e sul suo rapporto con il corpo'],
 ['Non ancora scientifica','mancava un metodo codificato e condiviso: la psicologia scientifica nasce tra Ottocento e Novecento'],
 ['Cartesio (1641)','il dualismo: una netta differenza tra mente e corpo'],
 ['Mente unica','un\'unità indivisibile che non perde nulla se al corpo viene tolto un arto: volere, sentire e comprendere sono sue espressioni'],
 ['Mente e mondo','la mente è il tramite del rapporto con l\'ambiente: se una malattia ne altera le capacità, la relazione è compromessa']],fs=28)
sch('S3','Le funzioni del cervello e i processi mentali',[
 ['Substrato biologico','il cervello è lo strumento biologico della mente: ogni area presiede a una specifica attività mentale'],
 ['Phineas Gage (1848)','un operaio edile sopravvive a una barra di ferro che gli trapassa il cranio'],
 ['Conseguenza','la lesione cambia radicalmente carattere e personalità'],
 ['Importanza scientifica','lega aree cerebrali e dimensioni affettive, emotive e sociali del comportamento']])
sch('S4','Dalla fisiologia alla psicologia scientifica',[
 ['I fisiologi','pongono le basi della psicologia come scienza autonoma: dall\'aspetto biologico (hardware) a quello mentale (software)'],
 ['Gustav Fechner','legge psicofisica: relazione matematica tra l\'intensità dello stimolo e la sensazione percepita'],
 ['Franciscus Donders','metodo dei tempi di reazione: misura la durata delle operazioni mentali']])
sch('S5','Wilhelm Wundt e lo strutturalismo',[
 ['Wilhelm Wundt (1879)','a Lipsia inaugura il primo laboratorio di psicologia: la disciplina diventa una scienza autonoma'],
 ['Strutturalismo (Titchener)','la mente è una struttura formata da un aggregato di elementi più semplici'],
 ['Scopo','scomporre l\'esperienza cosciente per individuare le connessioni tra le singole parti']])
sch('S6','Funzionalismo e Gestalt',[
 ['Funzionalismo (James, 1890)','si contrappone allo strutturalismo'],
 ['Che cosa studia','a che cosa servono i processi mentali: la vita mentale è una «corrente del pensiero» per adattarsi all\'ambiente'],
 ['Gestalt (Wertheimer, 1912)','la mente organizza le informazioni in modo globale e strutturato'],
 ['Il tutto','è diverso dalla somma delle singole parti']],cols='36% 64%',fs=29)
sch('S7','Comportamentismo e cognitivismo',[
 ['Comportamentismo (Watson, 1913)','la psicologia studia solo ciò che è visibile e osservabile: il comportamento'],
 ['La mente','resta fuori dalla ricerca: conta la risposta agli stimoli dell\'ambiente'],
 ['Cognitivismo','nasce nella seconda metà del Novecento, in opposizione al comportamentismo'],
 ['La mente come un computer','riceve input dal mondo esterno, li elabora e restituisce output: comportamenti o risposte']],cols='36% 64%',fs=29)
sch('S8','Jean Piaget e lo sviluppo della mente',[
 ['Epistemologia genetica','Piaget studia le origini e lo sviluppo delle capacità cognitive nel corso della vita'],
 ['1 · Senso-motorio','primi due anni: attività basate su sensi e movimento'],
 ['2 · Pre-operatorio','dai 2 ai 6 anni circa: linguaggio e uso dei simboli'],
 ['3 · Operatorio-concreto','ragionamento logico applicato solo ad azioni e oggetti concreti'],
 ['4 · Operatorio-astratto','adolescenza, 11-15 anni: ipotesi e ragionamenti logici e astratti']],cols='34% 66%',fs=29)
sch('S9','La psicologia oggi',[
 ['Psicologia cognitiva','processi mentali come memoria e attenzione'],
 ['Psicologia dello sviluppo','cambiamenti psichici nel corso della vita'],
 ['Psicologia clinica','studio e trattamento dei disturbi del comportamento'],
 ['Psicologia sociale','il modo in cui la mente agisce nelle interazioni sociali'],
 ['Ambiti pratici','socio-sanitario, scuola, azienda (selezione del personale), marketing, psicologia dello sport']],cols='34% 66%',fs=29)
sch('S10',"La psicologia dell'emergenza",[
 ['Definizione','branca nata in ambito militare: interviene in situazioni straordinarie e traumatiche, come catastrofi naturali, guerre e pandemie'],
 ['Esempi recenti','pandemia da Covid-19 · guerra in Europa nel 2022'],
 ['Funzioni','descrive i fenomeni causati dalle emergenze; elabora interventi per vittime dirette e soccorritori'],
 ['Prevenzione','analizza la percezione del rischio delle comunità']],fs=29)
for k,v in S.items():
    v['eyebrow']=EY;v.setdefault('tweak','');po9.SPEC[k]=v
orig=po9.build_html
def bh(name,sp,tms,cards=False):
    return orig(name,sp,tms,cards).replace('<span>SPAGNOLO</span>','<span>PSICOLOGIA · Prof. Giorgio Mazzotti</span>')
po9.build_html=bh
D='/home/claude/lezioni/psicologia-I-II-lez02/'
if __name__=='__main__':
    ks=sys.argv[1:] or list(S)
    M=json.load(open(D+'voci/wav/meta_S1.json'))
    for k in ks:
        v=S[k];m=M[k];DL=1.0
        P=[p+DL for p in m['phrases']];n=len(v['rows'])
        off=len(P)-n   # frasi in più all'inizio (annuncio dello schema)
        assert off in (0,1),(k,len(P),n)
        dur=round(m['dur']+DL+2.5,2)
        rows=[(round(P[off+i],2),round(P[off+i]+0.3,2),round(P[off+i+1] if off+i+1<len(P) else dur-1,2)) for i in range(n)]
        po9.render_po(k,k,{'rows':rows,'note':None},dur,D+'po',scale=float(os.environ.get('SC','1')))
        __import__('shutil').rmtree(D+'po/'+k,ignore_errors=True)
