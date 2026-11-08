# Schemi di ripasso con voce (S1–S5) · parola chiave inglese con piccola traduzione italiana sotto
import sys,json,os,glob,shutil
sys.path.insert(0,'/home/claude/v5')
import po9
D='/home/claude/lezioni/afm-inglese-triennio-lez01/'
def k(en,it): return f'<b>{en}</b><div style="font-size:.62em;font-weight:500;color:#5A6B85;margin-top:4px">{it}</div>'
EY='[REVIEW · RIPASSO]'
S={}
S['S1']=dict(title='Globalisation',rows=[
 [k('Globalisation','globalizzazione'),'growing integration of the world · interdependence of world economies'],
 [k('Effects','effetti'),'free movement of capital, goods and services · international trade · more multinationals'],
 [k('Key factors','fattori chiave'),'transport · communication · labour in LDCs · free trade (WTO)'],
 [k('Supporters','sostenitori'),'development of poorer countries · higher living standards'],
 [k('Opponents','oppositori'),'more inequality · benefits for rich countries · local businesses cannot compete']])
S['S2']=dict(title='Technological advancement',rows=[
 [k('Industry 4.0','Industria 4.0'),'the Fourth Industrial Revolution'],
 [k('Main features','caratteristiche principali'),'automation · AI · smart factories · more skilled workers'],
 [k('IoT · Digital twin','Internet delle cose · gemello digitale'),'machines with sensors exchange data · virtual copies of processes'],
 [k('AI · Machine learning','intelligenza artificiale · apprendimento automatico'),'machines work without people · find patterns and improve'],
 [k('Edge · Cloud computing','elaborazione locale · nel cloud'),'data on your own device · services over the internet']])
S['S3']=dict(title='Diversity and inclusion',rows=[
 [k('Diversity','diversità'),'different cultures, races and identities side by side'],
 [k('Equal opportunities','pari opportunità'),'gender, age, ethnicity, religion, sexual orientation, ability'],
 [k('Generation Z','generazione Z'),'young job seekers value diversity and inclusion'],
 [k('Recruitment','selezione del personale'),'companies rethink how they hire and value everyone']])
S['S4']=dict(title='World instability',rows=[
 [k('Instability','instabilità'),'since 2019: pandemic, political tensions, new conflicts'],
 [k('Pandemic','pandemia'),'closed plants · labour shortages · delays in supplies'],
 [k('Brexit','uscita del Regno Unito dalla UE'),'new rules · customs complexities · trade uncertainty'],
 [k('War in Ukraine','guerra in Ucraina'),'inflation · higher transport costs and raw material prices'],
 [k('New normal','nuova normalità'),'virtual meetings · remote work · digital workplace']])
S['S5']=dict(title='Environmental concerns',rows=[
 [k('Climate change','cambiamento climatico'),'97% of organisations already negatively influenced'],
 [k('Risk · Regulations','rischi · norme'),'extreme weather events · rules against CO2 emissions'],
 [k('Public pressure','pressione dell’opinione pubblica'),'customers prefer sustainably produced goods'],
 [k('Resources · Demand','risorse · domanda'),'scarce resources cost more · demand changes'],
 [k('Working conditions','condizioni di lavoro'),'harder work, e.g. outdoors in extreme heat']])
for n,v in S.items():
    v.update(eyebrow=EY,cols='34% 66%',fs=30,header=['Key word · parola chiave','In short'],note=None);v.setdefault('tweak','')
    po9.SPEC[n]=v
orig=po9.build_html
po9.build_html=lambda name,sp,tms,cards=False: orig(name,sp,tms,cards).replace('<span>SPAGNOLO</span>','<span>INGLESE · Prof.ssa Maria Vittoria Fontanesi</span>')
if __name__=='__main__':
    M={};[M.update(json.load(open(f))) for f in glob.glob(D+'voci/wav/meta_*.json')]
    for n in (sys.argv[1:] or list(S)):
        if os.path.exists(D+f'po/{n}.mp4'):continue
        v=S[n];m=M[n];DL=1.0
        P=[p+DL for p in m['phrases']];r=len(v['rows']);dur=round(m['dur']+DL+2.5,2)
        rows=[(round(P[i+1],2),round(P[i+1]+0.3,2),round(P[i+2] if i+2<len(P) else dur-1,2)) for i in range(r)]
        po9.render_po(n,n,{'rows':rows,'note':None},dur,D+'po',scale=1.0)
        shutil.rmtree(D+'po/'+n,ignore_errors=True)
