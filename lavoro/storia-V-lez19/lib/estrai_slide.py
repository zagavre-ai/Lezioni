import re,subprocess,json,html
x=subprocess.run(['pdftohtml','-xml','-i','-stdout','/home/claude/w19/src_slide/LEZIONE 19.pdf'],capture_output=True,text=True).stdout
pages=[];cur=None
for l in x.splitlines():
    m=re.match(r'<page number="(\d+)"',l)
    if m: cur={'n':int(m.group(1)),'titolo':None,'par':[]};pages.append(cur);last=None;continue
    m=re.match(r'<text top="(\d+)" left="\d+" width="\d+" height="\d+" font="(\d+)">(.*)</text>',l)
    if not m or cur is None: continue
    top=int(m.group(1));font=m.group(2);t=html.unescape(m.group(3))
    t=re.sub(r'</b>\s*<b>',' ',t)
    if font=='1' and cur['titolo'] is None: cur['titolo']=re.sub(r'</?b>','',t).strip();continue
    if cur['n']==1: cur['par'].append(t.strip());continue
    if cur['par'] and last is not None and top-last<=55: cur['par'][-1]+=' '+t.strip()
    else: cur['par'].append(t.strip())
    last=top
for p in pages:
    p['par']=[re.sub(r'\s+',' ',s).replace('</b> <b>',' ').replace(' </b>','</b> ').strip() for s in p['par']]
json.dump(pages,open('/home/claude/w19/slide.json','w'),ensure_ascii=False,indent=1)
for p in pages: print(p['n'],p['titolo'],len(p['par']))
