# Pannelli ingranditi (scheda con testo del libro) per T2 e L'assiuolo. Carattere 44-46 px.
import sys,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
OUT=sys.argv[1];os.makedirs(OUT,exist_ok=True)
SER='/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
if not os.path.exists(SER):
    import subprocess;SER=subprocess.check_output(['fc-match','-f','%{file}','Liberation Serif']).decode()
HL=(253,237,136);INK=(24,24,30);SUPC=(30,120,90)
# regione da ridisegnare (copre scheda + ombra): 60..1405 x 330..960; scheda 80..1385 x 351..939
X0,Y0,X1,Y1=60,330,1405,960
def card():
    im=Image.new('RGB',(X1-X0,Y1-Y0),'white')
    sh=Image.new('RGBA',im.size,(0,0,0,0));d=ImageDraw.Draw(sh)
    d.rounded_rectangle((20,21+6,20+1305,21+588+6),28,fill=(40,60,110,38));sh=sh.filter(ImageFilter.GaussianBlur(10))
    im.paste(sh,(0,0),sh)
    d=ImageDraw.Draw(im);d.rounded_rectangle((20,21,20+1305,21+588),28,fill='white',outline=(230,233,240),width=2)
    return im
def toks(s):
    # ^N^ = apice
    out=[];i=0
    import re
    for m in re.split(r'(\^\d+\^)',s):
        if not m: continue
        if m.startswith('^'): out.append(('sup',m.strip('^')))
        else:
            for w in m.split(' '):
                if w: out.append(('w',w))
            # spazio finale gestito dai token
    return out
def layout(d,text,font,sf,width):
    import re
    words=[]
    for w in text.split(' '):
        if not w: continue
        pcs=[]
        for p in re.split(r'(\^\d+\^)',w):
            if not p: continue
            pcs.append(('s',p.strip('^')) if p.startswith('^') and len(p)>2 else ('t',p))
        words.append(pcs)
    def wl(pcs): return sum(d.textlength(t,font=font) if k=='t' else d.textlength(t,font=sf)+2 for k,t in pcs)
    sp=d.textlength(' ',font=font);lines=[];line=[];lw=0
    for pcs in words:
        ww=wl(pcs)
        if line and lw+sp+ww>width: lines.append(line);line=[];lw=0
        lw+=(sp if line else 0)+ww;line.append(pcs)
    if line: lines.append(line)
    return lines
def draw_lines(d,lines,font,sf,x,y,lh):
    sp=d.textlength(' ',font=font)
    for ln in lines:
        cx=x
        for pcs in ln:
            for k,t in pcs:
                if k=='t': d.text((cx,y),t,font=font,fill=INK);cx+=d.textlength(t,font=font)
                else: d.text((cx+1,y+4),t,font=sf,fill=SUPC);cx+=d.textlength(t,font=sf)+2
            cx+=sp
        y+=lh
def prosa(path,text,fs=46):
    im=card();d=ImageDraw.Draw(im);font=ImageFont.truetype(SER,fs);sf=ImageFont.truetype(SER,int(fs*0.55))
    lines=layout(d,text,font,sf,1305-2*70)
    lh=int(fs*1.45);hh=len(lines)*lh+50
    top=21+(588-hh)//2
    d.rounded_rectangle((36,top,20+1305-16,top+hh),16,fill=HL)
    draw_lines(d,lines,font,sf,20+70,top+25,lh)
    im.save(path);return len(lines)
def strofa(path,rows,nums,hl,fs=44):
    # rows: righe; nums: {indice:numero di riga}
    im=card();d=ImageDraw.Draw(im);font=ImageFont.truetype(SER,fs);sf=ImageFont.truetype(SER,int(fs*0.55));nf=ImageFont.truetype(SER,30)
    lh=int(fs*1.5);hh=len(rows)*lh+40;top=21+(588-hh)//2
    if hl: d.rounded_rectangle((120,top,20+1305-100,top+hh),16,fill=HL)
    for i,r in enumerate(rows):
        y=top+20+i*lh
        if i in nums: d.text((160,y+8),str(nums[i]),font=nf,fill=(70,70,80))
        draw_lines(d,layout(d,r,font,sf,2000),font,sf,260,y,lh)
    im.save(path)
T2=("È dentro noi un fanciullino che non solo ha brividi^1^, come credeva Cebes Tebano^2^ che primo in sé lo scoperse, ma lagrime ancora e tripudi suoi^3^. "
 "Quando la nostra età è tuttavia tenera^4^, egli confonde la sua voce con la nostra, e dei due fanciulli che ruzzano e contendono^5^ tra loro, e, insieme sempre, temono sperano godono piangono, "
 "si sente un palpito solo, uno strillare e un guaire solo. Ma quindi noi cresciamo, ed egli resta piccolo; noi accendiamo negli occhi un nuovo desiderare^6^, "
 "ed egli vi tiene fissa la sua antica serena maraviglia^7^; noi ingrossiamo e arrugginiamo^8^ la voce, ed egli fa sentire tuttavia e sempre il suo tinnulo^9^ squillo come di campanello. [...]")
i=T2.index('Ma quindi')
print('T2 righe',prosa(OUT+'/t2a.png',T2[:i].strip(),48),prosa(OUT+'/t2b.png',T2[i:],48))
S=[["Dov’era la luna? ché il cielo","notava in un’alba di perla^1^,","ed ergersi il mandorlo e il melo","parevano a meglio vederla^2^.","Venivano soffi di lampi^3^","da un nero di nubi laggiù;","veniva una voce dai campi:","chiù^4^..."],
   ["Le stelle lucevano^5^ rare^6^","tra mezzo alla nebbia di latte^7^:","sentivo il cullare del mare^8^,","sentivo un fru fru tra le fratte^9^;","sentivo nel cuore un sussulto,","com’eco d’un grido che fu^10^.","Sonava lontano il singulto^11^:","chiù..."],
   ["Su tutte le lucide vette^12^","tremava^13^ un sospiro di vento:","squassavano le cavallette","finissimi sistri d’argento^14^","(tintinni a invisibili porte","che forse non s’aprono più?^15^...);","e c’era quel pianto di morte^16^...","chiù..."]]
nums=[{4:5},{1:10,6:15},{3:20}]
for i,r in enumerate(S):
    strofa(OUT+'/s%d.png'%(i+1),r,nums[i],False);strofa(OUT+'/s%dh.png'%(i+1),r,nums[i],True)
