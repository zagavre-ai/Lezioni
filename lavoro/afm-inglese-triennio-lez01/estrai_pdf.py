# PDF della docente → pdf_lines.json (righe con grassetti, dimensione e rientro) · uso: python3 estrai_pdf.py lezione.pdf
import pdfplumber,json,sys
src=sys.argv[1] if len(sys.argv)>1 else 'lez1.pdf'
out=[]
with pdfplumber.open(src) as pdf:
    for p in pdf.pages:
        ch=[c for c in p.chars if c['text']!='\x00']
        ws=p.extract_words(keep_blank_chars=True,use_text_flow=True,extra_attrs=['fontname','size'])
        lines={}
        for c in sorted(ch,key=lambda c:(round(c['top']),c['x0'])):
            k=None
            for t in lines:
                if abs(t-c['top'])<3: k=t;break
            if k is None: k=c['top'];lines[k]=[]
            lines[k].append(c)
        L=[]
        for t in sorted(lines):
            cs=sorted(lines[t],key=lambda c:c['x0']);runs=[];prev=None
            for c in cs:
                b='Bold' in c['fontname'] or 'Black' in c['fontname']
                if prev is not None and c['x0']-prev['x1']>c['size']*0.18: s=' '+c['text']
                else: s=c['text']
                if runs and runs[-1][0]==b: runs[-1][1]+=s
                else: runs.append([b,s])
                prev=c
            L.append({'x':round(cs[0]['x0']),'top':round(t),'size':round(max(c['size'] for c in cs),1),'runs':runs})
        out.append(L)
json.dump(out,open('pdf_lines.json','w'),ensure_ascii=False)
print(len(out),'pagine')
