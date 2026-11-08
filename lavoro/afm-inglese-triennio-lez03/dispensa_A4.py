# Dispensa A4 orizzontale: una pagina per slide (tutte le frasi del PDF della docente), senza riquadro della docente.
# uso: python3 dispensa_A4.py uscita.pdf
import sys,json,re
D='/home/claude/lezioni/afm-inglese-triennio-lez03/'
sys.path.insert(0,D);import gen_moda as G
OUT=sys.argv[1]
G.build(path=D+'slides_disp.html')
s=open(D+'slides_disp.html').read()
s=s.replace('<title>','<title>').replace('<head>','<head><title>Inglese – Dispensa</title>',1)
s=s.replace('</style>','''
.sheet.a4{width:297mm!important;height:210mm!important;background:#fff!important;margin:0!important}
.a4 .doc,.a4 .sp,.a4 .kw{display:none!important}
.a4 .bd{width:91.6cqw!important;height:auto!important;max-height:50cqw;overflow:visible!important;box-shadow:none!important}
.a4 .tt{width:91.6cqw!important}
.a4 .nk{display:none!important}
.a4 .ft{top:65.6cqw!important}
.a4 .bd *{opacity:1!important;filter:none!important}
.cover{display:flex;flex-direction:column;justify-content:center;padding:0 9cqw}
.cover .k{font:800 1.2cqw FG;letter-spacing:.2em;color:#2060AF;text-transform:uppercase}
.cover .t{font:800 6cqw BG;color:#0B1530;margin:1.2cqw 0 .8cqw;letter-spacing:-.02em}
.cover .b{width:8cqw;height:.5cqw;background:#2060AF;border-radius:.3cqw;margin-bottom:2.4cqw}
.cover .m{font:700 1.8cqw FG;color:#0B1530}
.cover ol{font:600 1.6cqw FG;color:#1A1A1A;margin:2cqw 0 0;line-height:1.7}
@page{size:A4 landscape;margin:0}
</style>''',1)
s=s.replace('</body>','''<script>
document.querySelectorAll('.sheet').forEach(x=>{x.classList.remove('s16');x.classList.add('a4');x.querySelectorAll('.on,.dim,.cur,.past').forEach(e=>e.classList.remove('on','dim','cur','past'))});
const c=document.createElement('div');c.className='sheet a4 cover';
c.innerHTML='<div class="k">Dispensa didattica · Inglese</div><div class="t">Production</div><div class="b"></div><div class="m">Inglese – Prof.ssa Maria Vittoria Fontanesi</div><ol><li>Production and sectors of production</li><li>Economies of scale</li><li>Quality control and smart manufacturing</li><li>Relocation of business operations</li><li>Focus: the circular economy</li></ol>';
document.getElementById('root').prepend(c);
document.querySelectorAll('.sheet:not(.cover) .ft span:last-child').forEach((e,i)=>e.textContent='Pagina '+(i+2));
</script></body>''',1)
open(D+'slides_disp.html','w').write(s)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.goto('file://'+D+'slides_disp.html');pg.wait_for_timeout(1500)
    over=pg.evaluate("[...document.querySelectorAll('.a4 .bd')].map((bd,i)=>{const l=bd.lastElementChild;if(!l)return 0;return l.getBoundingClientRect().bottom>bd.closest('.sheet').querySelector('.ft').getBoundingClientRect().top-8?i+2:0}).filter(x=>x)")
    print('pagine troppo piene:',over)
    pg.pdf(path=OUT,landscape=True,format='A4',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
import subprocess
print(subprocess.run(['pdfinfo',OUT],capture_output=True,text=True).stdout.split('Pages:')[1].split('\n')[0].strip(),'pagine')
