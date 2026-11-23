# Dispensa A4 orizzontale identica al video (una pagina per slide), con strato di testo invisibile; PDF delle mappe a parte.
import sys, os, re, json, glob, subprocess, html as H
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import tlib, mappe, struttura as S
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
pdfmetrics.registerFont(TTFont('Fig','/root/.fonts/Figtree-Regular.ttf'))
OUT='/tmp/w/dsp';os.makedirs(OUT,exist_ok=True)
CAM='/tmp/w/cam_still.png'
def testo_html(h):
    h=re.sub(r'<style.*?</style>','',h,flags=re.S);h=re.sub(r'<(br|/div|/p|/li)[^>]*>','\n',h);h=re.sub(r'<[^>]+>','',h)
    return [x.strip() for x in H.unescape(h).split('\n') if x.strip()]
def fix_footer(h,n):
    h=re.sub(r'<div class="pg"[^>]*>.*?</div>','',h)
    return h.replace('<div class="ft">',f'<div class="pg">Pagina {n}</div><div class="ft">',1)
def pagine_dispensa(parte):
    """lista di (html_path, usa_webcam) nell'ordine del video"""
    pg=[]
    def kh(pre):
        g=[x for x in glob.glob(f'/tmp/w/kh/{pre}_*.html')]
        num=[(int(m.group(1)),x) for x in g for m in [re.fullmatch(rf'{re.escape(pre)}_(\d+)_[0-9a-f]{{10}}\.html',os.path.basename(x))] if m]
        if num:
            top=max(n for n,_ in num);return max([x for n,x in num if n==top],key=os.path.getmtime)
        g=[x for x in g if re.fullmatch(rf'{re.escape(pre)}_[0-9a-f]{{10}}\.html',os.path.basename(x))]
        return max(g,key=os.path.getmtime) if g else None
    J=json.load(open('/tmp/w/stati.json'))['stati']
    args=S.PARTE1 if parte==1 else S.PARTE2
    if parte==1:
        pg.append((glob.glob('/tmp/w/kh/di_cosa_*.html')[0],True))
    else:
        h=kh('spg');pg.append((h,False)) if h else None
    for n in args:
        seen=[];
        for t,k in J[str(n)]:
            if k.startswith('i'):
                if k not in seen: seen.append(k);pg.append((f'/tmp/w/sl/{k}.html',True))
                continue
            if k in seen: continue
            seen.append(k)
            pg.append((f'/tmp/w/sl/{k}.html',True))
        for pre in (f'AP{n}',f'PS{n}'):
            h=kh(pre)
            if h: pg.append((h,False))
    pg.append((kh(f'GL{parte}'),False));pg.append((kh(f'RIEP{parte}'),False))
    if parte==2:
        for k in (1,2,3,4):
            h=kh(f'comp{k}')
            if h: pg.append((h,False))
    return [p for p in pg if p[0]]
def componi(parte):
    from mont import maschera
    import mont
    pagine=pagine_dispensa(parte);titolo='La Germania da Weimar al nazismo'
    L=[];jobs=[]
    cov=f'{OUT}/cov_{parte}.html';open(cov,'w').write(tlib.copertina_semplice(titolo));jobs.append(dict(html=cov,png=f'{OUT}/p{parte}_000.png'))
    testi=[['STORIA · VIDEOLEZIONE',titolo]]
    for i,(hp,cam) in enumerate(pagine,2):
        h=open(hp).read()
        import shutil;pp=f'{OUT}/p{parte}_{i:03d}.png';shutil.copy(hp[:-5]+'.png',pp);jobs.append(dict(html=hp,png=pp));testi.append(testo_html(h))
    json.dump(jobs[:1],open(f'{OUT}/jobs{parte}.json','w'));subprocess.run(['node','/home/user/Lezioni/lavoro/shot.js',f'{OUT}/jobs{parte}.json'],check=True)
    # webcam ferma nel riquadro (stessa del video) dove serve
    cam=Image.open(CAM).convert('RGB');mask=Image.open(maschera()).convert('L')
    for i,(hp,c) in enumerate(pagine,2):
        if c:
            f=f'{OUT}/p{parte}_{i:03d}.png';im=Image.open(f).convert('RGB');im.paste(cam,(1428,148),mask);im.save(f)
    pdf=f'/tmp/w/cons/Storia_Lez10_Parte{parte}_slide.pdf';scrivi(pdf,[j['png'] for j in jobs],testi);return pdf,len(jobs)
def scrivi(pdf,pngs,testi):
    W,Hh=landscape(A4);c=canvas.Canvas(pdf,pagesize=(W,Hh))
    c.setTitle('Storia · La Germania da Weimar al nazismo');c.setAuthor('Centro Studi Telesio')
    for p,tx in zip(pngs,testi):
        w=W;h=W*9/16;y=(Hh-h)/2
        c.drawImage(p,0,y,w,h)
        t=c.beginText(24,Hh-30);t.setFont('Fig',9);t.setTextRenderMode(3)   # testo invisibile, selezionabile
        for r in tx: t.textLine(r)
        c.drawText(t);c.showPage()
    c.save()
def mappe_pdf():
    jobs=[];testi=[]
    cov=f'{OUT}/cov_mappe.html';open(cov,'w').write(tlib.copertina_semplice('La Germania da Weimar al nazismo','MAPPE'));jobs.append(dict(html=cov,png=f'{OUT}/m_000.png'));testi.append(['STORIA · VIDEOLEZIONE','MAPPE','La Germania da Weimar al nazismo'])
    for k in (1,2,3):
        p=f'{OUT}/m_{k}.html';open(p,'w').write(mappe.stato_html(f'M{k}',None,True));jobs.append(dict(html=p,png=p[:-5]+'.png'))
        M=mappe.MAPPE[f'M{k}'];testi.append([M['titolo']]+[b[6] for b in M['boxes']]+[f[2] for f in M['frecce'] if f[2]]+[e[0] for e in M['etichette']])
    json.dump(jobs,open(f'{OUT}/jobs_m.json','w'));subprocess.run(['node','/home/user/Lezioni/lavoro/shot.js',f'{OUT}/jobs_m.json'],check=True)
    pdf='/tmp/w/cons/Storia_Lez10_mappe.pdf';scrivi(pdf,[j['png'] for j in jobs],testi);return pdf
if __name__=='__main__':
    for a in sys.argv[1:]:
        if a=='m': print(mappe_pdf())
        else: print(componi(int(a)))
