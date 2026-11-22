import json,sys,itertools,os,html
from PIL import ImageFont
B='/tmp/w/b'
FREG=B+'/fonts/Figtree-SemiBold.ttf'
def font(sz): return ImageFont.truetype(FREG,sz)
# nodes: id, text, color, col(1-4), group
N=[
('c','Giovanni Verga','l1',1,0),
('pad','Considerato il padre del Verismo in Italia','pag',1,1),
('vL','Vita','pag',1,2),
('v1','1840 · nasce a Catania','cel',1,2),
('v2','1865 · a Firenze','cel',1,3),
('v3','1872 · a Milano, centro culturale nazionale','cel',1,4),
('v4','1878 · c’è la svolta verso il Verismo, con Rosso Malpelo','cel',1,5),
('v5','1893 · torna a Catania','cel',1,6),
('v6','1922 · muore a Catania','cel',1,7),
('fL','Formazione','pag',2,8),
('f1','Irregolare','pag',2,8),
('f2','Scrittori francesi','pag',2,8),
('pL','Poetica','pag',2,9),
('p1','Attenzione ai problemi sociali','pag',2,9),
('p2','Impersonalità di chi scrive','pag',2,10),
('p3','«Far parlare» i personaggi','pag',2,11),
('p4','Lingua vicina al parlato: la prosa sembra aderire alla realtà','pag',2,12),
('oL','Opere','pag',2,13),
('o0','Scene umili da contesti quotidiani','pag',2,13),
('w1','1871 · Storia di una Capinera: l’attenzione sulla figura femminile combattuta tra la sua devozione sincera a Dio e la passione per Nino','men',3,14),
('w2','1878 · Rosso Malpelo: sul lavoro minorile','men',3,15),
('w3','1880 · La Lupa: una donna adesca un giovane e lo convince a sposare la figlia solo per poterlo sedurre','men',3,16),
('w4','1880 · Cavalleria rusticana: il dramma dell’amore e della gelosia nella mentalità popolare','men',4,17),
('w5','1881 · I Malavoglia: la lotta per il progresso, i cui problemi sono quelli del pane quotidiano','men',4,18),
('w6','1889 · Mastro-don Gesualdo: la sconfitta di chi aspira alla nobiltà attraverso un matrimonio combinato','men',4,19),
('w7','1882 · La roba: novella sull’ascesa sociale e la tragedia personale di un contadino','men',4,20),
]
# arrows parent->child
AR=[('c','pad'),('c','vL'),('vL','v1'),('vL','v2'),('vL','v3'),('vL','v4'),('vL','v5'),('vL','v6'),('c','fL'),('fL','f1'),('fL','f2'),('c','pL'),('pL','p1'),('pL','p2'),('pL','p3'),('pL','p4'),('c','oL'),('oL','o0'),('o0','w1'),('o0','w2'),('o0','w3'),('o0','w4'),('o0','w5'),('o0','w6'),('o0','w7')]
COL={'l1':('#FFDCC6','#C2410C'),'cel':('#DCEEFB','#1D4ED8'),'pag':('#FFF3BF','#A16207'),'men':('#DDF3E4','#15803D'),'lil':('#EBE3F7','#6D28D9')}
def wrap(t,f,w):
    words=t.split();lines=[];cur=''
    for x in words:
        c=(cur+' '+x).strip()
        if f.getlength(c)>w and cur: lines.append(cur);cur=x
        else: cur=c
    lines.append(cur);return lines
def layout(sz,widths,xs,gap=14,top=100,bot=1032):
    f=font(sz);lh=int(sz*1.35);pad=14
    boxes={}
    cols={i:[] for i in (1,2,3,4)}
    for nid,t,c,col,g in N: cols[col].append(nid)
    txt={n[0]:n for n in N}
    for col in (1,2,3,4):
        y=top
        for nid in cols[col]:
            _,t,c,_,_=txt[nid]
            fs=sz+10 if c=='l1' else sz
            ff=font(fs);lines=wrap(t,ff,widths[col-1]-2*pad-10)
            h=len(lines)*int(fs*1.35)+2*pad+8
            if c=='l1': h=max(h,80)
            boxes[nid]=[xs[col-1],y,widths[col-1],h,lines,fs]
            y+=h+gap
        if y-gap>bot: return None
    return boxes
for sz in (36,34,32,30,28):
    widths=[400,430,480,500];xs=[60];
    for w in widths[:-1]: xs.append(xs[-1]+w+20)
    b=layout(sz,widths,xs)
    if b: print('size',sz);break
else: raise SystemExit('non entra')
json.dump({'sz':sz,'boxes':b},open('/tmp/w/map/layout.json','w'))
print({k:(v[0],v[1],v[2],v[3]) for k,v in list(b.items())[:5]})
print('max y',max(v[1]+v[3] for v in b.values()))
