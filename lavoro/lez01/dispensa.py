#!/usr/bin/env python3
# Dispensa A4 orizzontale (immagini identiche alle slide del video + strato di testo invisibile) e PDF delle mappe.
import os,sys,re,json,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
import blu,render,piano,voci,mappa_bes as MB
import build,blue_pieces as B
from asm import sh,WK,ST
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfgen import canvas
OUT=WK+'dispensa/';os.makedirs(OUT,exist_ok=True)
def bgframe():
    p=OUT+'bg.png'
    if not os.path.exists(p):sh(['ffmpeg','-v','error','-y','-ss','2','-i',WK+'bg_blu.mp4','-frames:v','1',p])
    return Image.open(p).convert('RGBA')
def su_blu(layer):
    im=bgframe();im.alpha_composite(layer);return im.convert('RGB')
def camstill(t,n):
    p=OUT+f'cam_{n}.png'
    if not os.path.exists(p):sh(['ffmpeg','-v','error','-y','-ss',f'{t:.2f}','-i',WK+'cam.mp4','-frames:v','1',p])
    return p
def pagina_blu_semplice(kicker,titolo_t,righe=None,size=36,pagina=None,mappe=False):
    blu.CUR=pagina
    im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
    d.text((960,300),kicker.upper(),font=fig(34,True),fill=GIALLO,anchor='mm')
    return im
def cover_dispensa(extra=None):
    blu.CUR=None
    im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
    d.text((960,330),"STORIA DELL'ARTE V",font=fig(40,True),fill=GIALLO,anchor='mm')
    d.text((960,520),"Il Neoclassicismo",font=brico(150),fill=(255,255,255),anchor='mm')
    d.rounded_rectangle((900,620,1020,627),3,fill=GIALLO)
    if extra:d.text((960,760),extra,font=brico(84),fill=(255,255,255),anchor='mm')
    return su_blu(im)
def costruisci(parte):
    seq=build.piano_parte(parte);pg,pagine=build.numera(seq)
    pages=[]  # (jpg path, testo invisibile)
    def add(im,testo):
        p=OUT+f'P{parte}_{len(pages)+1:03d}.jpg';im.convert('RGB').save(p,quality=88);pages.append((p,testo))
    add(cover_dispensa(),"Storia dell'arte V. Il Neoclassicismo.")
    for nm in seq:
        if nm in('SIG','FIN','CI','D0','COVER','COVER2'):continue
        blu.CUR=pg.get(nm)
        if nm=='ARG':
            im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((960,170),'GLI ARGOMENTI DELLA LEZIONE',font=fig(34,True),fill=GIALLO,anchor='mm');y=260
            for i,t in enumerate(B.ARGT):
                h=blu.altezza_riga(f'{i+1}. {t}',1400,46);blu.card_blu(im,260,y,1400,f'{i+1}. {t}','off',46);y+=h+24
            add(su_blu(im),'Gli argomenti della lezione. '+' '.join(f'{i+1}. {t}.' for i,t in enumerate(B.ARGT)))
        elif nm=='SP':
            im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((960,150),'RIPASSO DELLA PARTE PRECEDENTE',font=fig(32,True),fill=GIALLO,anchor='mm');y=230
            for i,(t,x) in enumerate(voci.SPS[:3]):
                d.text((120,y),f'{i+1}. {t}',font=brico(40),fill=(255,255,255));y+=58
                h=blu.altezza_riga(x,1680,32);blu.card_blu(im,120,y,1680,x,'off',32);y+=h+26
            add(su_blu(im),'Ripasso della Parte precedente. '+' '.join(f'{t}. {x}' for t,x in voci.SPS[:3]))
        elif re.fullmatch(r'T\d',nm):
            n=int(nm[1]);add(su_blu(blu.scheda_titolo(f'Argomento {n}',B.ARGT[n-1])),f'Argomento {n}. {B.ARGT[n-1]}.')
        elif re.fullmatch(r'D\d',nm):
            a=int(nm[1])
            for i,s in enumerate(piano.SLIDE[a]):
                ch=render.chunks(s);cam=camstill(s['t0']+3,f'{a}_{i}')
                for j,c in enumerate(ch):
                    im=render.slide_dispensa(s,a,B.ARGT[a-1],pagine[(a,i)]+j,c,cam,cont=j>0)
                    txt=s['titolo']+'. '+' '.join(re.sub(r'\*\*','',s['cards'][k][1]) for k in c)+' Parole chiave: '+', '.join(s['kw'])+'. '+' '.join(x[1] for x in s['img'])
                    add(im,txt)
        elif re.fullmatch(r'A\d',nm):
            n=int(nm[1]);art,tit,call=B.APPROF[n]
            im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((1010,170),'APPROFONDIMENTO',font=fig(30,True),fill=GIALLO,anchor='lm')
            for i,l in enumerate(wrap(d,tit,brico(46),830)):d.text((1010,225+i*56),l,font=brico(46),fill=(255,255,255))
            y=420
            for c in call:
                h=blu.altezza_riga(c[1],830,38);blu.card_blu(im,1010,y,830,c[1],'off',38);y+=h+16
            base_=bgframe();a=Image.open(ASSET+art+'.png').convert('RGBA');a=fit(a,(880,800));base_.alpha_composite(a,(80+(880-a.width)//2,170+(800-a.height)//2));base_.alpha_composite(im)
            add(base_,'Approfondimento. '+tit+'. '+' '.join(c[1] for c in call))
        elif re.fullmatch(r'R\d',nm):
            n=int(nm[1]);add(su_blu(blu.scheda_pillola(B.ARGT[n-1],voci.PIL[f'R{n}'],len(voci.PIL[f'R{n}'])-1)),'Pillola di ripasso. '+B.ARGT[n-1]+'. '+' '.join(voci.PIL[f'R{n}']))
        elif re.fullmatch(r'Q\d',nm):
            n=int(nm[1]);im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((960,330),f'QUIZ · ARGOMENTO {n}',font=fig(34,True),fill=GIALLO,anchor='mm');d.text((960,470),'5 domande',font=brico(130),fill=(255,255,255),anchor='mm')
            d.text((960,610),B.ARGT[n-1],font=fig(46),fill=(205,222,250),anchor='mm');d.text((960,720),"Per continuare serve almeno l'80%",font=fig(40,True),fill=(255,255,255),anchor='mm')
            add(su_blu(im),f'Quiz, argomento {n}. 5 domande. Per continuare serve almeno l\'80%.')
        elif nm=='GL':
            im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((960,100),'GLOSSARIO',font=fig(32,True),fill=GIALLO,anchor='mm');y=150
            for t,x in voci.GLOSS:
                h=blu.altezza2(t,x,1700,30);blu.card_blu2(im,110,y,1700,t,x,'off',30);y+=h+8
            add(su_blu(im),'Glossario. '+' '.join(f'{t}: {x}' for t,x in voci.GLOSS))
        elif nm=='RF':
            im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((960,100),'RIPASSO FINALE',font=fig(32,True),fill=GIALLO,anchor='mm');y=150
            for i,(t,x) in enumerate(voci.RFS):
                d.text((110,y),f'{i+1}. {t}',font=brico(36),fill=(255,255,255));y+=46
                h=blu.altezza_riga(x,1700,28);blu.card_blu(im,110,y,1700,x,'off',28);y+=h+14
            add(su_blu(im),'Ripasso finale. '+' '.join(f'{t}. {x}' for t,x in voci.RFS))
        elif nm=='MF':
            m=MB.stato(len(MB.N),True,pagina=pg.get('MF'));add(m,"Mappa: Che cos'è il Neoclassicismo? "+'; '.join((n[5]+': ' if n[5] else '')+n[6] for n in MB.N))
        elif nm=='VER':
            im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((960,330),'VERIFICA FINALE',font=fig(34,True),fill=GIALLO,anchor='mm');d.text((960,470),'10 domande',font=brico(130),fill=(255,255,255),anchor='mm')
            d.text((960,610),'Il Neoclassicismo',font=fig(46),fill=(205,222,250),anchor='mm');d.text((960,720),"Per proseguire serve almeno l'80%",font=fig(40,True),fill=(255,255,255),anchor='mm')
            add(su_blu(im),"Verifica finale. 10 domande. Per proseguire serve almeno l'80%.")
        elif nm=='COMP':
            im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
            d.text((960,90),'COMPITI',font=fig(32,True),fill=GIALLO,anchor='mm');y=130
            for i,t in enumerate(voci.COMPITI):
                h=blu.altezza_riga(t,1700,30);blu.card_blu(im,110,y,1700,f'{i+1}) '+t,'off',30);y+=h+10
            add(su_blu(im),'Compiti. '+' '.join(voci.COMPITI)+' '+voci.CHIUSURA)
    return pages
def pdf(pages,out,titolo):
    pw,ph=landscape(A4);c=canvas.Canvas(out,pagesize=(pw,ph));c.setTitle(titolo);c.setAuthor('Centro Studi Telesio')
    ih=pw*1080/1920;y0=(ph-ih)/2
    for p,t in pages:
        c.setFillColorRGB(1,1,1);c.rect(0,0,pw,ph,fill=1,stroke=0)
        c.drawImage(p,0,y0,width=pw,height=ih)
        to=c.beginText(20,ph-30);to.setTextRenderMode(3);to.setFont('Helvetica',8)
        t=t.replace('’',"'").replace('·','-').replace('→','->').replace('…','...')
        t=t.encode('cp1252','replace').decode('cp1252')
        import textwrap
        for l in textwrap.wrap(t,160)[:200]:to.textLine(l)
        c.drawText(to);c.showPage()
    c.save()
if __name__=='__main__':
    for parte in (1,2):
        pages=costruisci(parte)
        pdf(pages,WK+f'Dispensa_Storia_arte_Lez1_Parte{parte}.pdf',"Storia dell'arte V · Il Neoclassicismo")
        print('parte',parte,len(pages),'pagine')
    # PDF mappe
    m=[(OUT+'MAPPE_cover.jpg',"Storia dell'arte V. Il Neoclassicismo. MAPPE.")]
    cover_dispensa('MAPPE').save(m[0][0],quality=90)
    mm=MB.stato(len(MB.N),True).convert('RGB');mm.save(OUT+'MAPPA.jpg',quality=92)
    m.append((OUT+'MAPPA.jpg',"Mappa: Che cos'è il Neoclassicismo? "+'; '.join((n[5]+': ' if n[5] else '')+n[6] for n in MB.N)))
    pdf(m,WK+'Mappe_Storia_arte_Lez1.pdf',"Storia dell'arte V · Il Neoclassicismo · MAPPE")
    print('mappe ok')
