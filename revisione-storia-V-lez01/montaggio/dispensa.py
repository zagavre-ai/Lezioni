import sys,os,json
sys.path.insert(0,'/tmp/w/b')
from plan import *
from kinds2 import *
from kinds import cards_state
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.utils import ImageReader
import io
PW,PH=landscape(A4)
def add_page(c,im,texts,n,cover=False):
    buf=io.BytesIO();im.convert('RGB').save(buf,'JPEG',quality=90);buf.seek(0)
    iw=PW;ih=PW*9/16;y=(PH-ih)/2+4
    c.drawImage(ImageReader(buf),0,y,iw,ih)
    t=c.beginText(10,y+ih-20);t.setTextRenderMode(3);t.setFont('Helvetica',10)
    for tx in texts:
        t.textLine(tx.encode('latin-1','replace').decode('latin-1'))
    c.drawText(t)
    if not cover:
        c.setFont('Helvetica-Bold',8);c.setFillColorRGB(0.13,0.38,0.69);c.drawString(14,9,'STORIA V');c.drawRightString(PW-14,9,f'Pagina {n}')
    c.showPage()
def blue_final(label,title,units,fs=40,gl=False,tsize=70):
    disp=[digits(u) for u in units]
    pages=[];cur=[]
    d=ImageDraw.Draw(Image.new('RGB',(10,10)));tot=0
    # greedy split by height estimate
    f=font(FIG,fs);lh=int(fs*1.45)
    for u in disp:
        h=len(wrap(d,u,f,1780-110))*lh+40+18
        if tot+h>760 and cur: pages.append(cur);cur=[];tot=0
        cur.append(u);tot+=h
    if cur: pages.append(cur)
    out=[]
    for pg in pages:
        im=cards_state(0,label,title,pg,len(pg)-1,fs,1780,gl,len(pg),1.0,tsize=tsize)
        # no highlight in handout: redraw plain
        out.append((im,[title]+pg))
    return out
def build_handout(parts=(1,2),outname='/tmp/w/out/Storia_Lez1_dispensa.pdf'):
    c=canvas.Canvas(outname,pagesize=(PW,PH))
    cov=Image.new('RGB',(W,H),WHITE);d=ImageDraw.Draw(cov);cov.paste(LOGO_B,(56,34),LOGO_B)
    d.text((64,330),'STORIA V',font=font(FIGB,40),fill=BLUE);f=font(BRI,120);y=400
    for l in wrap(d,'Il Novecento, il secolo delle masse',f,1700): d.text((60,y),l,font=f,fill=NAVY);y+=134
    d.rectangle((64,y+14,224,y+26),fill=BLUE)
    add_page(c,cov,['Storia V','Il Novecento, il secolo delle masse'],0,cover=True)
    n=0
    for p in parts:
        for sp in seq_with_pages_local(p):
            k=sp[0];name=spec_name(sp)
            if k=='teach':
                pk=json.load(open(f'{PC}/{name}.picks.json'));info=pk['info'];nn=sp[1]
                for (pg,cards,times) in info:
                    im=white_frame(f'Argomento {nn}',TIT[nn],pg,False,KW[nn]);y=300
                    for cc in cards: y=draw_card(im,60,y,cc,True,plain=True)+26
                    n+=1;add_page(c,im,[TIT[nn]]+cards,n)
            elif k=='an':
                us=split_sentences(TXT[sp[1]]);title=us[0].rstrip('.')
                for im,tx in blue_final('Approfondimento',title,us[1:],42,False,74): n+=1;add_page(c,im,tx,n)
            elif k=='ripasso':
                us=split_sentences(TXT[sp[1]])
                for im,tx in blue_final('Ripasso',sp[3],us[1:],42): n+=1;add_page(c,im,tx,n)
            elif k=='cards' and sp[1]!='FIN1' and sp[1]!='FIN2':
                us=split_sentences(TXT[sp[1]])
                for im,tx in blue_final(sp[3],sp[4],us[1:],42,gl=(len(sp)>5)): n+=1;add_page(c,im,tx,n)
            elif k=='map':
                m=MAPS[sp[2]];L=map_layout(m);im=draw_map(m,L,list(m['order']),None)
                n+=1;add_page(c,im,[m['title']]+[L[x]['text'] for x in m['order']],n)
    c.save();return n
def seq_with_pages_local(p):
    from go import seq_with_pages
    return seq_with_pages(p)
def build_maps(outname='/tmp/w/out/Storia_Lez1_mappe.pdf'):
    c=canvas.Canvas(outname,pagesize=(PW,PH))
    cov=Image.new('RGB',(W,H),WHITE);d=ImageDraw.Draw(cov);cov.paste(LOGO_B,(56,34),LOGO_B)
    d.text((64,250),'MAPPE',font=font(FIGB,56),fill=YEL if False else BLUE);d.text((64,330),'STORIA V',font=font(FIGB,40),fill=BLUE)
    f=font(BRI,120);y=400
    for l in wrap(d,'Il Novecento, il secolo delle masse',f,1700): d.text((60,y),l,font=f,fill=NAVY);y+=134
    d.rectangle((64,y+14,224,y+26),fill=BLUE)
    add_page(c,cov,['MAPPE','Storia V','Il Novecento, il secolo delle masse'],0,cover=True)
    for i,k in enumerate(MAPS,1):
        m=MAPS[k];L=map_layout(m);im=draw_map(m,L,list(m['order']),None)
        add_page(c,im,[m['title']]+[L[x]['text'] for x in m['order']],i)
    c.save()
if __name__=='__main__':
    os.makedirs('/tmp/w/out',exist_ok=True)
    build_maps();print('maps ok')
