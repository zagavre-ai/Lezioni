# PDF delle slide A4 orizzontale, identiche al video (senza riquadro del prof e senza fascia col nome).
# uso: pdf_slide.py pagine_pdf.json uscita.pdf      (pagine_pdf.json: elenco dei PNG 1920x1080 in ordine)
import sys,json
from PIL import Image
P=json.load(open(sys.argv[1]));W,H=3508,2480   # A4 a 300 dpi
pages=[]
for f in P:
    im=Image.open(f).convert('RGB');w=W-2*90;h=round(w*1080/1920)
    pg=Image.new('RGB',(W,H),'white');pg.paste(im.resize((w,h),Image.LANCZOS),(90,(H-h)//2));pages.append(pg)
pages[0].save(sys.argv[2],save_all=True,append_images=pages[1:],resolution=300)
print(sys.argv[2],len(pages),'pagine')
