# dispensa A4 orizzontale (stesse slide del video, senza riquadro del prof) con strato di testo invisibile + PDF delle mappe
import sys,json,os,html as H
sys.path.insert(0,'/home/user/work18/lib')
from render import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.utils import ImageReader
PW,PH=landscape(A4)
def cover(out,mappe=False):
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div class=hl style="top:124px"></div>'
    h+='<div class=lab>STORIA · VIDEOLEZIONE</div>'
    if mappe:h+='<div style="position:absolute;left:80px;top:196px"><span class=pill style="font-size:34px;padding:10px 26px">MAPPE</span></div>'
    h+=f'<div class=ttl id=ttl style="top:{300 if mappe else 222}px;font-size:110px;line-height:1.05;width:1700px">L\'Italia repubblicana</div><div class=bar id=bar style="top:{430 if mappe else 350}px"></div>'
    h+='<div class=hl style="top:981px"></div><div class=foot style="left:80px">STORIA</div>'
    return shot(h,out,'',True)
def page(c,png,texts,n=None):
    iw=PW;ih=PW*1080/1920;y=(PH-ih)/2
    c.setFillColorRGB(1,1,1);c.rect(0,0,PW,PH,fill=1,stroke=0)
    c.drawImage(ImageReader(png),0,y,iw,ih)
    t=c.beginText(24,PH-30);t.setTextRenderMode(3);t.setFont('Helvetica',8)
    for x in texts:
        import textwrap
        for ln in textwrap.wrap(x,150):
            try:t.textLine(ln.encode('latin-1','replace').decode('latin-1'))
            except Exception:pass
    c.drawText(t);c.showPage()
def main():
    for w in ('1','2'):
        maps=[]
        c=canvas.Canvas(f'{W}/out/Storia_Lez18_Parte{w}_slide.pdf',pagesize=(PW,PH));c.setTitle(f"Storia · L'Italia repubblicana · dispensa Parte {w}")
        page(c,cover(W+'/st/disp_cover.png'),["Storia","L'Italia repubblicana"])
        S=json.load(open(f'{W}/out/slides_parte{w}.json'))
        for i,s in enumerate(S):
            png=s['png'];txt=[s.get('title',''),s.get('label','')]+list(s.get('cards',[]))
            if s.get('cards') and not s.get('quiz') and not s.get('table') and not s.get('map') and not s.get('mapref'):
                if s.get('img') and s.get('wide'):png=img_slide_wide(s['label'],s['page'],s['img'],s['cards'][0] if s['cards'] else '',f'{W}/st/dp_{w}_{i}.png',None,(),False)
                elif s.get('img'):png=img_slide(s['label'],s['title'],s['page'],s['img'],s['cards'],-1,f'{W}/st/dp_{w}_{i}.png',None,(),False,'.card{opacity:1}')
                else:png=slide_cards(s['label'],s['title'],s['cards'],-1,s['page'],None,(),False,f'{W}/st/dp_{w}_{i}.png','.card{opacity:1}')
            if s.get('map'):
                from maps import MAPS
                txt+=[MAPS[s['map']]['title']]+[b[4] for b in MAPS[s['map']]['boxes']];maps.append((png,dict(s,title=MAPS[s['map']]['title'])))
            page(c,png,txt)
        c.save()
        m=canvas.Canvas(f'{W}/out/Storia_Lez18_Parte{w}_mappe.pdf',pagesize=(PW,PH));m.setTitle("Storia · L'Italia repubblicana · mappe")
        page(m,cover(W+'/st/map_cover.png',True),["MAPPE","Storia","L'Italia repubblicana"])
        for png,s in maps:page(m,png,['Mappa',s.get('title','')])
        m.save();print('ok parte',w,len(maps),'mappe')
if __name__=='__main__':main()
