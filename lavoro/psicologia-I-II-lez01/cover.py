from playwright.sync_api import sync_playwright
import json
D='/home/claude/lezioni/psicologia-I-II-lez01/'
ARG=['Le scienze umane come strumento','I temi vicini ai giovani','Scienze umane e scienze della natura','I fattori del comportamento','Le discipline e il percorso di studio']
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://'+D+'slides_spoken.html');pg.wait_for_timeout(1200)
    pg.evaluate("""(A)=>{const s=document.querySelectorAll('.sheet')[0];document.querySelectorAll('.sheet').forEach((x,i)=>x.style.display=i?'none':'');
    s.querySelector('.ey').textContent='Psicologia · Scienze umane';
    s.querySelector('.tt').textContent='Introduzione alle scienze umane';
    s.querySelector('.bd').innerHTML='<div style="background:#fff;border:.08cqw solid #DCE3EE;border-radius:1.1cqw;padding:1.4cqw 2cqw;box-shadow:0 .7cqw 2cqw rgba(11,21,48,.07)"><div style="font:800 1.05cqw FG;letter-spacing:.16em;color:#2060AF;text-transform:uppercase;margin-bottom:.8cqw">In questa lezione</div>'+A.map((t,i)=>'<div style="display:flex;align-items:center;gap:1.2cqw;font-size:1.75cqw;font-weight:600;line-height:1.3;margin:.55cqw 0"><span style="flex:none;width:2.4cqw;height:2.4cqw;border-radius:.7cqw;background:#EEF3FA;color:#2060AF;font:800 1.35cqw BG;display:flex;align-items:center;justify-content:center">'+(i+1)+'</span>'+t+'</div>').join('')+'</div>';
    s.querySelector('.kw').style.display='none';const nk=s.querySelector('.nk');if(nk)nk.style.display='none';s.querySelector('.ft span:last-child').textContent='';}""",ARG)
    pg.query_selector_all('.sheet')[0].screenshot(path=D+'sv/s000_cover.png')
