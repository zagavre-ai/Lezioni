import sys,json
sys.path.insert(0,'/home/claude/v5')
import po9
nt=po9.nt
EY='[SCHEMA DI RIPASSO]'
S={}
S['S1']=dict(title='Le fibre tessili',cols='30% 20% 50%',fs=30,header=['Gruppo','Tipo','Esempi'],rows=[
 ['Fibre naturali','vegetali','cotone, lino, canapa, juta, ramiè, sisal, cocco e kapok'],
 ['Fibre naturali','animali','lana, cashmere, mohair, angora e seta'],
 ['Fibre chimiche o man-made','artificiali','viscosa, acetato, triacetato, cupro, modal e lyocell'],
 ['Fibre chimiche o man-made','sintetiche','poliestere, poliammide o nylon, acrilica, polipropilenica, elastan e aramide']],
 note=nt('FIBRE IN MISCHIA','Uniscono le caratteristiche positive delle varie fibre e minimizzano gli aspetti negativi.'))
S['S2']=dict(title='Le proprietà delle fibre',cols='25% 35% 40%',fs=28,header=['Proprietà','Che cosa indicano','Esempi'],rows=[
 ['morfologiche','come è fatta una fibra','lunghezza, finezza, colore e lucentezza, mano, densità, sezione'],
 ['chimiche','come si comporta a contatto con le sostanze chimiche','resistenza ad acidi, alcali, solventi o ossidanti'],
 ['fisico-meccaniche','come si comporta quando si applica una forza','igroscopicità, tenacità, allungamento a rottura, elasticità, resilienza'],
 ['fisiologiche','come interagisce con il corpo umano e l\'ambiente','coibenza, resistenza ai raggi ultravioletti e alle intemperie']],note=None)
S['S3']=dict(title='Il mercato delle fibre',cols='38% 62%',fs=30,header=['Dato','Valore'],rows=[
 ['Domanda di fibre tessili','otto volte i livelli del 1950; oltre settanta milioni di tonnellate'],
 ['Fibre naturali','dal 62% del 1970 al 37% attuale'],
 ['Poliestere','quasi l\'80% delle fibre sintetiche'],
 ['Cina','dall\'8,7% a oltre il 60% delle fibre sintetiche'],
 ['Indice di sporcabilità','cotone e lana 100 · acrilica 70% · seta 40%'],
 ['Pulibilità','poliammide ed elastan 100% · cotone, acrilica e modal circa 60%']],note=None)
S['S4']=dict(title='Le fibre animali e la lana',cols='30% 70%',fs=30,header=['Voce','In sintesi'],rows=[
 ['Fibre animali','dal bulbo pilifero (lana, peli) o dalle secrezioni ghiandolari (seta)'],
 ['Razze degli ovini','merino · incrociate · indigene'],
 ['Tosatura','una volta all\'anno in primavera; bistosa due volte all\'anno nei climi caldi'],
 ['Lana saltata · sucida · vergine','pecora lavata prima della tosatura · lana appena recisa · solo da animali vivi'],
 ['Lavaggio e asciugatura','il vello viene battuto, lavato in vasche (si libera la lanolina) e asciugato con aria calda']],note=None)
S['S5']=dict(title='La fibra di lana',cols='28% 72%',fs=30,header=['Voce','Dato'],rows=[
 ['Composizione','80% cheratina · 18% altre proteine · 1,5% lanolina · 0,5% sali minerali'],
 ['Struttura','midollo poroso · cortex · membrana esterna o cuticola con squame'],
 ['Finezza (micron)','extrafine fino a 20 · fine 20-25 · intermedia 25-30 · comune 30-50 · ordinaria 50-100'],
 ['Morbidezza','lane agnelline o lambswool · lane matricine'],
 ['Lunghezza','lunghe → filati pettinati · corte → filati cardati']],note=None)
S['S6']=dict(title='Trattamenti, proprietà e cura della lana',cols='28% 72%',fs=29,header=['Voce','In sintesi'],rows=[
 ['Trattamenti chimici','acido solforico · cloro e aceto · ZIRPRO (zirconio o titanio)'],
 ['Finissaggi meccanici','follatura · garzatura · bruciatura o gasatura · superwash · lintrak'],
 ['Proprietà','ingualcibilità e morbidezza · vestibilità · resistenza al fuoco · idrorepellenza · termoisolanti e igroscopiche'],
 ['Lavaggio','acqua tiepida e costante, detergenti neutri; lavaggio a secco'],
 ['Asciugatura e stiratura','all\'ombra e in piano · calore moderato']],note=None)
S['S7']=dict(title='Le lane speciali',cols='34% 33% 33%',fs=30,header=['Animale','Finezza (micron)','Resa per animale'],rows=[
 ['vigogna','13-16','120 g'],['cashmere','13-15','400-1.000 g'],['yak','15-19','400 g'],['cammello','17-23','2.000-5.000 g'],
 ['alpaca','20-25','300 g ogni 2 anni'],['lama','27-30','4.000 g'],['mohair','15-90','1.600 g'],['coniglio d\'angora','10-30','200-500 g ogni 3 mesi']],
 note=None,tweak=".tr>div{padding:7px 20px}")
S['S8']=dict(title='La seta: origine e produzione',cols='28% 72%',fs=30,header=['Voce','In sintesi'],rows=[
 ['Baco da seta','Bombix mori: si nutre di foglie di gelso'],
 ['La bava','fibroina 75-77% · sericina 22-23%'],
 ['Bachicoltura','circa 25 °C; il bozzolo si forma in 3-4 giorni'],
 ['Sgommatura','seta cruda · seta mezza cotta · seta cotta; seta caricata con sali minerali'],
 ['Resa','da 100 kg di bozzoli appena 20-25 kg di seta grezza']],note=None)
S['S9']=dict(title='La seta: trattamenti, proprietà e cura',cols='28% 72%',fs=29,header=['Voce','In sintesi'],rows=[
 ['Acidi','solforico → crespo di seta · acetico → tintura e «fruscio» · cloridrico e nitrico la distruggono'],
 ['Proprietà','drappeggiabilità · limitata gualcibilità · leggerezza · ignifuga · igienica'],
 ['Lavorazione','scivolosità: materassi non troppo alti, taglio automatico, filo cucirino sottile'],
 ['Cura','niente centrifuga · lontano da calore e luce solare · stiratura a rovescio tra 2 panni umidi'],
 ['Fibre del futuro','seta di ragno (Nephila clavipes): i geni del ragno in una capra']],note=None)
DUR=44.0
for k,v in S.items():
    v['eyebrow']=EY; v.setdefault('tweak','')
    po9.SPEC[k]=v
def times(n,has_note):
    T=[];span=38.0/(n+(1 if has_note else 0));a=1.0
    for i in range(n):
        T.append((round(a,2),round(a+0.3,2),round(a+span,2)));a+=span
    return {'rows':T,'note':(round(a,2),round(a+.3,2),DUR-1) if has_note else None}
# piè di pagina: materia e docente
orig=po9.build_html
def bh(name,sp,tms,cards=False):
    return orig(name,sp,tms,cards).replace('<span>SPAGNOLO</span>','<span>TECNOLOGIE DEI MATERIALI E DEI PROCESSI PRODUTTIVI E ORGANIZZATIVI DELLA MODA · Prof.ssa Piera Caputi</span>')
po9.build_html=bh
if __name__=='__main__':
    ks=sys.argv[1:] or list(S)
    M=json.load(open('/home/claude/lezioni/psicologia-I-II-lez01/voci/wav/meta_S1.json'))
    for k in ks:
        v=S[k];m=M[k];DL=1.0
        P=[p+DL for p in m['phrases']];n=len(v['rows']);hn=bool(v.get('note'))
        dur=round(m['dur']+DL+2.5,2)
        rows=[(round(P[i+1],2),round(P[i+1]+0.3,2),round(P[i+2] if i+2<len(P) else dur-1,2)) for i in range(n)]
        tm={'rows':rows,'note':(round(P[n+1],2),round(P[n+1]+.3,2),dur-1) if hn else None}
        po9.render_po(k,k,tm,dur,'/home/claude/lezioni/psicologia-I-II-lez01/po',scale=float(__import__('os').environ.get('SC','1')))
        __import__('shutil').rmtree('/home/claude/lezioni/psicologia-I-II-lez01/po/'+k,ignore_errors=True)
