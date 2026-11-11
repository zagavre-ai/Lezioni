import sys,json,os,shutil
sys.path.insert(0,'/home/claude/v5')
import po9
D='/home/claude/lezioni/psicologia-I-II-lez01/'
EY='[SCHEMA DI RIPASSO]'
S={}
S['S1']=dict(title='Le scienze umane come strumento',cols='27% 73%',fs=35,header=['Voce','In sintesi'],rows=[
 ['Strumento','non solo teoria: una chiave per comprendere le esperienze vissute'],
 ['Decodificare','interpretare e leggere ciò che abbiamo vissuto e ciò che ci viene raccontato'],
 ['Obiettivo','aprire e analizzare i contesti dell\'esistenza: famiglia, amicizia, sport, nuove tecnologie'],
 ['Chiave di lettura','la transizione verso l\'età adulta e la ricerca di sé'],
 ['Crescita','fattori genetici e ambientali, interni ed esterni: un percorso plurimo']])
S['S2']=dict(title='I temi vicini ai giovani',cols='27% 73%',fs=35,header=['Voce','In sintesi'],rows=[
 ['Temi vicini ai giovani','relazioni quotidiane · ricerca di sé · società multiculturale e tecnologica'],
 ['Società di oggi','multiculturale, con attriti e incomprensioni, e ipertecnologica'],
 ['Eventi collettivi','la pandemia: scuola, comunicazione e sfera psicologica'],
 ['Dialogo','tra noi e il mondo, e tra generazioni'],
 ['Metodo scientifico','casi da analizzare, dati da ricavare, esperimenti per confermarli']])
S['S3']=dict(title='Scienze umane e scienze della natura',cols='27% 73%',fs=35,header=['Voce','In sintesi'],rows=[
 ['Scienze della natura','realtà materiale: leggi universali, costanti e ripetibili'],
 ['Scienze umane','l\'essere umano: soggetto relazionale, psicologico e culturale'],
 ['Causa ed effetto','acqua a 100 gradi: legge rigida · comportamenti: fattori interni ed esterni'],
 ['Prospettive','l\'essere umano è un prisma: tanti punti di vista'],
 ['Obiettivo comune','spiegare e comprendere con il metodo scientifico, cercando le cause']])
S['S4']=dict(title='I fattori del comportamento',cols='27% 73%',fs=35,header=['Voce','In sintesi'],rows=[
 ['Natura multi-causale','mai una sola causa; i comportamenti cambiano nel tempo'],
 ['Biologici e di sviluppo','la crescita e le tappe evolutive della persona'],
 ['Ambiente','contesto sociale, relazioni interpersonali, famiglia e scuola'],
 ['Dimensione storica','comportamenti, valori e tradizioni cambiano nel tempo'],
 ['Insuccesso scolastico','valutazione multidisciplinare: metodo di studio, ambiente, docenti, contesto']])
S['S5']=dict(title='Le discipline e il percorso di studio',cols='27% 73%',fs=35,header=['Disciplina','In sintesi'],rows=[
 ['Psicologia','comportamento e processi mentali: percezione, memoria, pensiero, emozioni'],
 ['Sociologia','strutture sociali, istituzioni e processi di interazione nei gruppi'],
 ['Antropologia','popoli e culture umane: aiuta a comprendere l\'altro'],
 ['Metodologia della ricerca','strumenti scientifici e tecniche per le indagini sul campo'],
 ['Primo biennio','psicologia, metodologia statistica e dati, educazione civica']])
for k,v in S.items():
    v['eyebrow']=EY;v.setdefault('tweak','.tr>div{padding:17px 24px}');v['note']=None;po9.SPEC[k]=v
orig=po9.build_html
def bh(name,sp,tms,cards=False):
    return orig(name,sp,tms,cards).replace('<span>SPAGNOLO</span>','<span>PSICOLOGIA · Prof. Giorgio Mazzotti</span>')
po9.build_html=bh
if __name__=='__main__':
    M=json.load(open(D+'voci/wav/meta_S1.json'))
    for k in (sys.argv[1:] or S):
        if os.path.exists(D+'po/%s.mp4'%k):continue
        v=S[k];m=M[k];DL=1.0
        P=[p+DL for p in m['phrases']];n=len(v['rows'])
        dur=round(m['dur']+DL+2.5,2)
        rows=[(round(P[i],2),round(P[i]+0.3,2),round(P[i+1] if i+1<len(P) else dur-1,2)) for i in range(n)]
        po9.render_po(k,k,{'rows':rows,'note':None},dur,D+'po',scale=1.0)
        shutil.rmtree(D+'po/'+k,ignore_errors=True)
