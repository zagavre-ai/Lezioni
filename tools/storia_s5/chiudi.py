# uso: chiudi.py N consegna_dir video.mp4 timeline.json [--mappe]
import sys,os,json,re,subprocess,shutil,zipfile,glob,openpyxl
from PIL import Image
N=int(sys.argv[1]);D=sys.argv[2];V=sys.argv[3];TL=json.load(open(sys.argv[4]))
DL='/tmp/claude-0/w/dl'
tag=f'storia-V-lez{N:02d}'
# test
src=f'{DL}/STORIA V/DOMANDE LEZIONE {N}.xlsx'
wb=openpyxl.load_workbook(src)
for ws in wb:
    for row in ws.iter_rows():
        for c in row:
            if c.value is not None and not isinstance(c.value,str): c.value=str(c.value)
            elif isinstance(c.value,str): c.value=c.value.strip()
wb.save(f'{D}/Storia_Lez{N}_test_finale_docente.xlsx')
for f in glob.glob(f'{D}/*PROPOSTA*'): os.remove(f)
# compiti
shutil.copy(f'{DL}/STORIA V /LEZIONE {N}.pdf',f'{D}/Storia_Lez{N}_compiti_docente.pdf')
txt=subprocess.run(['pdftotext','-layout',f'{DL}/STORIA V /LEZIONE {N}.pdf','-'],capture_output=True,text=True).stdout
open(f'{D}/Storia_Lez{N}_compiti_docente.txt','w').write(txt)
body=re.sub(r'^\s*LEZIONE\s+\d+\s*','',txt.strip())
items=[re.sub(r'\s+',' ',x).strip() for x in re.split(r'\n\s*\d+\)\s*',"\n"+body) if x.strip()]
json.dump({'titolo':f'Compiti · Storia V · Lezione {N}','stato':f'compiti del prof. Mazzotti (file «LEZIONE {N}.pdf», release mazzotti-storia-V, 14/11), testo invariato','compiti':[{'n':i+1,'tipo':'risposta_aperta','testo':t} for i,t in enumerate(items)]},open(f'{D}/compiti.json','w'),ensure_ascii=False,indent=1)
print(len(items),'compiti')
if '--mappe' in sys.argv:
    pages=[];os.makedirs('/tmp/claude-0/w/mp',exist_ok=True)
    for nome,t0,d in TL:
        if nome.startswith('MAP'):
            f=f'/tmp/claude-0/w/mp/{tag}_{nome}.png'
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t0+d-1.2:.2f}','-i',V,'-frames:v','1',f],check=True)
            pages.append(f)
    W,H=1754,1240;ims=[]
    for f in pages:
        im=Image.open(f).convert('RGB');w=W;h=int(im.height*W/im.width)
        pg=Image.new('RGB',(W,H),(238,240,244));pg.paste(im.resize((w,h),Image.LANCZOS),(0,(H-h)//2));ims.append(pg)
    ims[0].save(f'{D}/Mappe_{tag}.pdf',save_all=True,append_images=ims[1:],resolution=150)
    print(len(ims),'mappe')
