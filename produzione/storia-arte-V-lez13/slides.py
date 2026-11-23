import subprocess,re
def pages():
    t=subprocess.run(['pdftotext','-layout','/tmp/claude-0/w/mat_SLIDE/LEZIONE 13.pdf','-'],capture_output=True,text=True).stdout.split('\f')
    out={}
    for i,p in enumerate(t[:13],1):
        paras=[];cur=[]
        for l in p.split('\n'):
            if l.strip():cur.append(l.strip())
            elif cur:paras.append(' '.join(cur));cur=[]
        if cur:paras.append(' '.join(cur))
        if paras and len(paras[0])>100 and i>1:
            m=re.match(r'^(.*?)\s+((?:[A-ZÈ\"L][^:]{2,60}):.*)$',paras[0])
            ls=[l.strip() for l in p.split('\n') if l.strip()];paras=[ls[0],' '.join(paras[0].split(' ')[len(ls[0].split(' ')):])]+paras[1:]
        out[i]=[REF(x) for x in paras]
    return out
def card(p):
    m=re.match(r'^(.{3,90}?:)\s+(.*)$',p)
    return (m.group(1),m.group(2)) if m else ('',p)

REFUSI=[("delle Arti","delle arti"),("del Regime","del regime"),("di Regime","di regime"),("nel Primo Dopoguerra","nel primo dopoguerra")]
TROVATI=[]
def REF(t):
    for a,b in REFUSI:
        if a in t:TROVATI.append((a,b,t[:60]));t=t.replace(a,b)
    return t
