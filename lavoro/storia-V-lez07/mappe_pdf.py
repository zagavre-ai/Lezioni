import sys,os
sys.path.insert(0,'/home/claude/w/b')
from dispensa import *
pages=[]
out=f'{B}/dp/mappe_cover.png'; txt=shot_page(cover_diss(mappe=True),8,out); pages.append((out,txt+['MAPPE','Storia','GLI STATI UNITI: DAL BOOM ECONOMICO AL NEW DEAL'],('cover',0,0)))
for n in (1,2,3):
    d=map_scene(n); out=f'{B}/dp/mappe_{n}.png'
    txt=shot_page(d['html'],d['dur']-0.5,out,n+1)
    # piè di pagina con numero
    pages.append((out,txt,('map',n,0)))
make_pdf(pages,B+'/Storia_Lez7_mappe.pdf','Storia · MAPPE · Gli Stati Uniti: dal boom economico al New Deal')
print('ok')
