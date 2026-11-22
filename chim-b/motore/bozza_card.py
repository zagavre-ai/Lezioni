# bozza_card.py: dalla trascrizione fa una bozza di frasi (card) con i tempi: unisce i frammenti, toglie gli incespicamenti, corregge i termini con un dizionario.
import json, re, sys
CORR = [  # (regex, sostituzione): errori del riconoscimento vocale -> termini corretti (dal PDF della prof)
 (r'\bcortezza\b','corteccia'),(r'\bcortecc?ia\b','corteccia'),(r'\bdiberiani\b','liberiani'),(r'\bvasi diberiani\b','vasi liberiani'),
 (r'\b[Aa]?[Ii]uta\b','juta'),(r'\b[Ii]uda\b','juta'),(r'\bl\'aiuta\b',"la juta"),(r'\bdell\'aiuta\b','della juta'),(r'\bdell\'iuta\b','della juta'),(r'\bl\'iuta\b','la juta'),(r'\bdell\'aiuto\b','della juta'),(r'\bl\'aiuto\b','la juta'),
 (r'\bramier\b','ramiè'),(r'\bramiere\b','ramiè'),(r'\brami\b','ramiè'),(r'\bremiè\b','ramiè'),
 (r'\bfloro?blucina\b','fluoroglucina'),(r'\bfloroglucina\b','fluoroglucina'),(r'\bflora o glucina\b','fluoroglucina'),
 (r'\bruteino\b','rutenio'),(r'\brutegno\b','rutenio'),(r'\bliquido di s[cw]h?w?e?t?[zs]?er\b','liquido di Schweitzer'),
 (r'\bcupra ammoniacale\b','cuproammoniacale'),(r'\bcupro ammoniacale\b','cuproammoniacale'),(r'\bemilcellulosa\b','emicellulosa'),
 (r'\blianine\b','lignina'),(r'\blinina\b','lignina'),(r'\blegnina\b','lignina'),(r'\bligne cellulosa\b','lignocellulosa'),(r'\bligneocellulosa\b','lignocellulosa'),
 (r'\bscotolatura\b','scotolatura'),(r'\bstrillatura\b','strigliatura'),(r'\bstrelliatura\b','strigliatura'),
 (r'\bcanavatella\b','canavatella'),(r'\bsalmento\b','ingiallimento'),
 (r'\bKen ?off\b','kenaf'),(r'\bKenaf\b','kenaf'),(r'\bmacerazione\b','macerazione'),(r'\bidrossido di sodio\b','idrossido di sodio'),
 (r'\bnao ?H\b','NaOH'),(r'\bNao H\b','NaOH'),(r'\btrielina\b','trielina'),(r'\bsuno\b','sunn'),(r'\bSun\b','sunn'),(r'\bsun\b','sunn'),
 (r'\b[Ii]biscus\b','Hibiscus'),(r'\bibisco\b','ibisco'),(r'\bdelibisco\b','dell\'ibisco'),(r'\bagabe\b','agave'),
 (r'\bcanapoli\b','canapuli'),(r'\bdecalabulazione\b','decanapulazione'),(r'\bmarcite\b','marcite'),
]
FILL = re.compile(r'^(um+|ehm+|yeah\.?|ovviamente ehm|e|quindi|questa ehm\.\.\.)[\.\s]*$', re.I)
def pulisci(t):
    t=re.sub(r'\s+',' ',t).strip()
    for a,b in CORR: t=re.sub(a,b,t)
    return t
def frasi(js, a, b):
    """segmenti con inizio in [a,b): ritorna lista di dict(t0,t1,testo,segs)"""
    S=[(i,x) for i,x in enumerate(json.load(open(js))) if a<=x['inizio']<b]
    out=[];cur=None
    for i,x in S:
        t=pulisci(x['testo'])
        if FILL.match(t) or len(t.split())<=1 and not t.endswith('.'): 
            continue
        if cur is None: cur=dict(t0=x['inizio'],t1=x['fine'],testo=t,segs=[i])
        else: cur['testo']+=' '+t; cur['t1']=x['fine']; cur['segs'].append(i)
        # chiudi la frase se finisce con . ? ! e non è un frammento "..."
        if re.search(r'[\.\?\!]$',t) and not t.endswith('...') and len(cur['testo'].split())>=4:
            out.append(cur);cur=None
    if cur: out.append(cur)
    return out
if __name__=='__main__':
    for f in frasi(sys.argv[1],float(sys.argv[2]),float(sys.argv[3])): print(f"{f['t0']:.1f}-{f['t1']:.1f} {f['segs']} {f['testo']}")
