import sys,json,os
sys.path.insert(0,'/home/claude/v5')
import po9
D='/home/claude/lezioni/afm-inglese-triennio-lez02/'
EY='[SCHEMA DI RIPASSO]'
def k(en,it): return '%s<small class="itr">%s</small>'%(en,it)
TW=".tr small.itr{display:block;font-size:.66em;font-weight:500;font-style:italic;color:#5B6B86;margin-top:4px;letter-spacing:0;text-transform:none}"
S={}
S['S1']=dict(title='Economic systems',cols='32% 68%',fs=30,header=['Key word · parola chiave','In short'],rows=[
 [k('Economic system','sistema economico'),'what to produce · how to produce · for whom to produce'],
 [k('Free-market economy','economia di libero mercato'),'supply and demand · private companies · little government control'],
 [k('Command / planned economy','economia pianificata'),'the government controls everything · prices set by the government'],
 [k('Mixed economy','economia mista'),'the most common · public sector + private sector']],rowp=[1,2,3,4])
S['S2']=dict(title='The public sector',cols='32% 68%',fs=30,header=['Key word · parola chiave','In short'],rows=[
 [k('Public sector','settore pubblico'),'controlled by the state · paid for with taxes'],
 [k('Privatisation','privatizzazione'),'from the end of the 20th century · a controversial phenomenon'],
 [k('Remunicipalisation','rimunicipalizzazione'),'public ownership comes back at a local level'],
 [k('Advantages','vantaggi'),'essential services · no duplication · stable prices · profits to the government'],
 [k('Disadvantages','svantaggi'),'bureaucracy · politics · no competition · losses paid with taxes']],rowp=[1,2,3,4,5])
S['S3']=dict(title='Economic indicators',cols='30% 70%',fs=28,header=['Key word · parola chiave','In short'],rows=[
 [k('GDP','PIL'),'value of goods and services produced in a nation in a year'],
 [k('GNP','PNL'),'GDP + money earned abroad − money earned by foreigners'],
 [k('Business cycle','ciclo economico'),'expansion → recession → depression → recovery'],
 [k('Inflation','inflazione'),'prices rise · ideal rate around 2% · central banks'],
 [k('Deflation · shrinkflation','deflazione'),'prices fall · smaller products, same price'],
 [k('Unemployment','disoccupazione'),'healthy: 3–5% · retraining · incentives · lower taxes']],rowp=[1,2,3,4,5,6])
S['S4']=dict(title='Focus: green economy',cols='32% 68%',fs=30,header=['Key word · parola chiave','In short'],rows=[
 [k('Natural capital','capitale naturale'),"nature's contribution: water, air, land"],
 [k('Green economy','economia verde'),'well-being in the long run · no environmental risks for the future'],
 [k('Sustainable growth','crescita sostenibile'),'natural capital in economic decision making'],
 [k('Consumers','consumatori'),'they want sustainable products · companies adapt']],rowp=[1,2,3,4])
S['S5']=dict(title='Focus: youth unemployment',cols='32% 68%',fs=30,header=['Key word · parola chiave','In short'],rows=[
 [k('NEET rate','tasso di NEET'),'young people aged 15–24 not in employment, education or training'],
 [k('NEET in 2020','NEET nel 2020'),'22.4% · mostly girls and young women'],
 [k('Gender gap','divario di genere'),'more permanent for girls · family responsibilities']],rowp=[1,2,3])
S['GL1']=dict(eyebrow='[GLOSSARIO]',title='Glossary · Glossario',cols='50% 50%',fs=27,header=['English','Italiano'],rows=[
 ['Economic system · supply and demand','sistema economico · domanda e offerta'],
 ['Command economy · mixed economy','economia pianificata · economia mista'],
 ['Public sector · privatisation','settore pubblico · privatizzazione'],
 ['GDP (Gross Domestic Product) · business cycle','PIL (Prodotto Interno Lordo) · ciclo economico'],
 ['Inflation · deflation · unemployment','inflazione · deflazione · disoccupazione'],
 ['Green economy · NEET rate','economia verde · tasso di NEET']],rowp=[1,1,2,2,3,3])
S['RF1']=dict(eyebrow='[RIPASSO FINALE]',title='Final review · Ripasso finale',cols='32% 68%',fs=29,header=['Topic · argomento','Remember'],rows=[
 [k('Economic systems','sistemi economici'),'free-market · command · mixed economy'],
 [k('The public sector','il settore pubblico'),'controlled by the state · advantages and disadvantages'],
 [k('Economic indicators','indicatori economici'),'GDP · business cycle · inflation · deflation · unemployment'],
 [k('Green economy','economia verde'),'natural capital · sustainable growth'],
 [k('Youth unemployment','disoccupazione giovanile'),'NEET rate · gender gap']],rowp=[1,2,3,4,5])
for kk,v in S.items():
    v.setdefault('eyebrow',EY); v['tweak']=v.get('tweak','')+TW
    po9.SPEC[kk]=v
orig=po9.build_html
def bh(name,sp,tms,cards=False):
    return orig(name,sp,tms,cards).replace('<span>SPAGNOLO</span>','<span>INGLESE · Prof.ssa Maria Vittoria Fontanesi</span>')
po9.build_html=bh
if __name__=='__main__':
    ks=sys.argv[1:] or list(S)
    M=json.load(open(D+'voci/wav/meta.json')) if os.path.exists(D+'voci/wav/meta.json') else {}
    for kk in ks:
        v=S[kk];DL=1.0
        if kk in M: m=M[kk]
        else: m={'dur':40.0,'phrases':[i*40.0/(len(v['rows'])+1) for i in range(len(v['rows'])+1)]}  # prova senza voce
        P=[p+DL for p in m['phrases']];n=len(v['rows'])
        dur=round(m['dur']+DL+2.5,2)
        rp=v['rowp']
        rows=[]
        for i in range(n):
            j=rp[i];a=P[j] if j<len(P) else P[-1]
            nx=[x for x in rp if x>j];e=P[nx[0]] if nx and nx[0]<len(P) else dur-1
            rows.append((round(a,2),round(a+0.3,2),round(e,2)))
        po9.render_po(kk,kk,{'rows':rows,'note':None},dur,D+'po',scale=float(os.environ.get('SC','1')))
        __import__('shutil').rmtree(D+'po/'+kk,ignore_errors=True)
