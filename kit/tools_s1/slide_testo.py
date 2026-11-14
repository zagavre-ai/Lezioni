import subprocess,re
def struttura(pdf,p):
    t=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'-layout',pdf,'-'],capture_output=True,text=True).stdout
    righe=[r for r in t.split('\n')]
    i=0
    while not righe[i].strip():i+=1
    titolo=righe[i].strip();resto='\n'.join(righe[i+1:])
    parti=[x.strip() for x in re.split(r'\n\s*\n',resto) if x.strip()]
    def pul(x):
        x=re.sub(r'[ \t]+',' ',x);x=re.sub(r'-\s*\n\s*','-',x);return re.sub(r'\s*\n\s*',' ',x).strip()
    cards=[]
    for par in map(pul,parti):
        if ':' in par[:90]:lead,rest=par.split(':',1);lead=lead.strip()+':'
        else:lead,rest='',par
        fr=[f.strip() for f in re.split(r'(?<=[.;])\s+(?=[A-ZÀ-Ù«"(])',rest.strip()) if f.strip()]
        cards.append((lead,fr))
    return titolo,cards
if __name__=='__main__':
    import sys
    for p in (2,3,6,7,9,10):
        t,c=struttura(sys.argv[1],p);print(p,t,[ (l,len(f)) for l,f in c])
