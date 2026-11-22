import sys, json, os
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import struttura as S, tlib, piani
from piani import ARGS, B, END, stati_arg, spec_key
OUT='/tmp/w/sl';os.makedirs(OUT,exist_ok=True)
pagine={};lst=[];stati={}
def pagina(k):
    if k not in pagine: pagine[k]=len(pagine)+3   # 1 copertina, 2 di cosa parliamo
    return pagine[k]
for k,n in enumerate(range(1,9)):
    a=ARGS[n];t0=B[f'a{n}'];t1=B[f'a{n+1}'] if n<8 else END
    st=stati_arg(n,t0,t1);stati[n]=[]
    for t,s in st:
        key=spec_key(n,s)
        if s[0]=='i':
            im=a['immagini'][s[1]];pk=f'i{n}_{s[1]}';p=pagina(pk)
            html=tlib.slide_img(f"{n} · {a['titolo']}",im['titolo'],p,f'/tmp/w/hr/{im["file"]}',im['did'],a['kw'])
        else:
            wk=key.rsplit('_',2)[0];p=pagina(wk)
            html,idx=tlib.slide_cards(f"{n} · {a['titolo']}",a['slide'],p,a['cards'],s[1],a['kw'],ev=s[2] if len(s)>2 else None)
        h=f'{OUT}/{key}.html';open(h,'w').write(html)
        if not any(x['png']==f'{OUT}/{key}.png' for x in lst): lst.append(dict(html=h,png=f'{OUT}/{key}.png'))
        stati[n].append((t,key))
json.dump(dict(stati=stati,pagine=pagine),open('/tmp/w/stati.json','w'))
json.dump(lst,open('/tmp/w/lsl.json','w'))
print(len(lst),'slide uniche; pagine',len(pagine))
