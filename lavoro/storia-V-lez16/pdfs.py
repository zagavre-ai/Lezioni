import json,sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
D='/home/user/w/dispensa';F='/home/user/Lezioni/kit/caratteri/'
pdfmetrics.registerFont(TTFont('Fig',F+'Figtree-Regular.ttf'))
PW,PH=landscape(A4)
def make(out,names,title):
    c=canvas.Canvas(out,pagesize=(PW,PH));c.setTitle(title);c.setAuthor('Centro Studi Telesio');c.setSubject('Storia V')
    s=PW/1920
    for n in names:
        c.drawImage(f'{D}/{n}.png',0,0,PW,PH)
        for t in json.load(open(f'{D}/{n}.json')):
            fs=max(4,t['h']*s*0.8);tx=c.beginText(t['x']*s,PH-(t['y']+t['h']*0.8)*s);tx.setFont('Fig',fs);tx.setTextRenderMode(3);tx.textOut(t['t']);c.drawText(tx)
        c.showPage()
    c.save()
P=json.load(open(D+'/pages.json'))
make('/home/user/w/final/Storia_Lez16_dispensa_A4.pdf',[f'p{n:03d}' for n in P],'Storia V · Gli anni Sessanta tra crisi e progressi')
make('/home/user/w/final/Storia_Lez16_mappe.pdf',['mappe_cover','mappa1','mappa2','mappa3'],'MAPPE · Storia V · Gli anni Sessanta tra crisi e progressi')
print('ok')
