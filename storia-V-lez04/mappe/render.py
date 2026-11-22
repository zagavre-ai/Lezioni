#!/usr/bin/env python3
# Renderer generico: legge mappe.json -> mappa{k}.html, mappa{k}_finale.png, mappa{k}_tempi.json, mappa{k}.mp4 (senza audio), Mappe_dispensa.pdf
# uso: python3 render.py [--png] [--video] [--pdf] [k ...]   (senza opzioni: tutto)
import json,os,sys,subprocess,math
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
OFF=0.5; CODA=1.5; FERMA=4.0
args=sys.argv[1:]; ks=[int(a) for a in args if a.isdigit()] or [1,2,3,4,5,6]
fl=[a for a in args if a.startswith('--')]; ALL=not fl
M=json.load(open('mappe.json'))
def dur_voce(k): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'/tmp/w/voci_wt/scambio/storia-V-lez04/vox/MAP{k}.wav'],capture_output=True,text=True).stdout)
def tempi(k):
    m=M[str(k)]; T={'nodi':{},'archi':{}}
    for n in m['nodi']: T['nodi'][n['id']]={'entra':None,'acc':[]}
    for e in m['archi']: T['archi'][e['id']]=None
    for s in m['passi']:
        a=s['t0']+OFF-0.1
        for i in s['mostra']:
            en=s.get('entra_video',a)
            if T['nodi'][i]['entra'] is None: T['nodi'][i]['entra']=en
        for i in s['archi']:
            if T['archi'][i] is None: T['archi'][i]=a
        if s.get('accendi'): T['nodi'][s['accendi']]['acc'].append([round(s['t0']+OFF,3),round(s['t1']+OFF+0.1,3)])
    for i,v in T['nodi'].items(): assert v['entra'] is not None,('nodo mai mostrato',k,i)
    for i,v in T['archi'].items(): assert v is not None,('arco mai mostrato',k,i)
    dv=dur_voce(k); tot=math.ceil((OFF+dv+CODA+FERMA)*30-1e-9)/30
    return T,dv,tot
def page(k,T):
    m=dict(M[str(k)]); m['tempi']=T
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Mappa {k}</title><link rel="stylesheet" href="mappa.css"></head><body>
<div id="m"></div><script src="mappa_lib.js"></script><script>
const MAPPA={json.dumps(m,ensure_ascii=False)};
window.pronta=FONTS().then(()=>{{window.MP=buildMap(document.getElementById('m'),MAPPA);return MP.issues}});
</script></body></html>'''
def pdf_html():
    pages=[]
    for k in range(1,7):
        T,_,_=tempi(k); m=dict(M[str(k)]); m['tempi']=T; pages.append(m)
    logo=open('../../kit/docenti/Telesio_logo_blu.svg').read()
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Storia V · Mappe</title><link rel="stylesheet" href="mappa.css">
<style>@page{{size:297mm 210mm;margin:0}} html,body{{margin:0;width:297mm}} .pg{{position:relative;width:297mm;height:210mm;overflow:hidden;page-break-after:always;background:#fff}}
.scw{{position:absolute;left:0;top:14mm;width:297mm;height:calc(1080px*var(--s));overflow:hidden}} .sc{{position:absolute;left:0;top:0;width:1920px;height:1080px;}}
.pf{{position:absolute;left:12mm;right:12mm;bottom:8mm;display:flex;justify-content:space-between;font:600 11pt Fig;letter-spacing:.08em;color:#2060AF}}
.cv .lg{{position:absolute;left:18mm;top:14mm;width:60mm}} .cv .lg svg{{width:100%;height:auto;display:block}}
.cv .k{{position:absolute;left:18mm;top:78mm;font:700 13pt Fig;letter-spacing:.16em;color:#2060AF}}
.cv .t{{position:absolute;left:18mm;top:88mm;font:800 74pt/1 Bri;color:#0B1530}}
.cv .u{{position:absolute;left:18mm;top:116mm;width:26mm;height:1.6mm;background:#2060AF}}
.cv .s{{position:absolute;left:18mm;top:124mm;font:800 30pt/1.15 Bri;color:#2060AF}}
.cv .tt{{position:absolute;left:18mm;top:140mm;font:800 34pt/1.15 Bri;color:#0B1530}}</style></head><body>
<div class="pg cv"><div class="lg">{logo}</div><div class="k">STORIA V · VIDEOLEZIONE</div><div class="t">MAPPE</div><div class="u"></div><div class="s">Storia V</div><div class="tt">La prima guerra mondiale</div>
<div class="pf"><span>STORIA V</span><span>Pagina 1</span></div></div>
{''.join(f'<div class="pg"><div class="scw"><div class="sc" id="s{i+1}"></div></div><div class="pf"><span>STORIA V</span><span>Pagina {i+2}</span></div></div>' for i in range(6))}
<script src="mappa_lib.js"></script><script>
const PAG={json.dumps(pages,ensure_ascii=False)};
window.pronta=FONTS().then(()=>{{const s=(297/25.4*96)/1920;document.documentElement.style.setProperty('--s',s);
 const iss=[];PAG.forEach((m,i)=>{{const r=buildMap(document.getElementById('s'+(i+1)),m,{{nofooter:true}});r.render(1e6);iss.push(...r.issues);document.getElementById('s'+(i+1)).style.zoom=s}});return iss}});
</script></body></html>'''
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=os.environ.get('CHROMIUM_EXE','/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'))
    if ALL or '--png' in fl or '--video' in fl:
        for k in ks:
            T,dv,tot=tempi(k)
            open(f'mappa{k}.html','w').write(page(k,T))
            pg=br.new_page(viewport={'width':1920,'height':1080}); pg.goto('file://'+os.path.abspath(f'mappa{k}.html'))
            iss=pg.evaluate('window.pronta'); print('mappa',k,'problemi layout:',iss)
            pg.evaluate('MP.render(1e6)'); pg.screenshot(path=f'mappa{k}_finale.png')
            if ALL or '--video' in fl:
                n=int(round(tot*30)); ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-threads','2','-r','30',f'mappa{k}.mp4'],stdin=subprocess.PIPE)
                last=None;buf=None
                for i in range(n):
                    key=pg.evaluate(f'MP.render({i/30})')
                    if key!=last: buf=pg.screenshot(type='png'); last=key
                    ff.stdin.write(buf)
                ff.stdin.close(); ff.wait()
            json.dump({'mappa':k,'titolo':M[str(k)]['titolo'],'convenzione':'tempi in secondi di video; voce parte a +0,5 s (t_video = 0,5 + t_voce)','durata_voce_s':round(dv,3),'durata_totale_s':round(tot,4),'fotogrammi':int(round(tot*30)),
              'nodi':{i:{'entra_s':round(v['entra'],3),'acceso_giallo_s':v['acc']} for i,v in T['nodi'].items()},'archi_entrano_s':{i:round(v,3) for i,v in T['archi'].items()},
              'passi_voce':[{'t0_voce':s['t0'],'t1_voce':s['t1'],'testo':s['testo']} for s in M[str(k)]['passi']]},open(f'mappa{k}_tempi.json','w'),ensure_ascii=False,indent=1)
            pg.close()
    if ALL or '--pdf' in fl:
        open('Mappe_dispensa.html','w').write(pdf_html())
        pg=br.new_page(); pg.goto('file://'+os.path.abspath('Mappe_dispensa.html')); print('pdf problemi:',pg.evaluate('window.pronta'))
        pg.pdf(path='Mappe_dispensa.pdf',width='297mm',height='210mm',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'},prefer_css_page_size=True)
    br.close()
