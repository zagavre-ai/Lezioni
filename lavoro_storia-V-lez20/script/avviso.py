import subprocess,json
h="""<!doctype html><html><head><meta charset='utf-8'><style>html,body{margin:0;width:1920px;height:1080px;background:transparent}
div{position:absolute;left:260px;width:1400px;bottom:60px;text-align:center;color:#fff;font-family:'Figtree';font-weight:600;font-size:24px;line-height:1.45}</style></head><body>
<div>© Centro Studi Telesio. Tutti i contenuti riprodotti in questa videolezione (testi, grafiche, animazioni, voci e registrazioni) sono di proprietà del Centro Studi Telesio. È vietata la riproduzione, anche parziale, senza autorizzazione scritta.</div></body></html>"""
open('/tmp/w/b/h/avviso.html','w').write(h)
js="""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});await p.goto('file:///tmp/w/b/h/avviso.html');await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:'/tmp/w/b/assets/avviso.png',omitBackground:true});await b.close()})()"""
open('/tmp/w/b/avviso.js','w').write(js)
subprocess.run(['node','/tmp/w/b/avviso.js'],check=True,cwd='/tmp/w')
