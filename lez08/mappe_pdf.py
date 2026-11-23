# PDF delle mappe: copertina identica a quella delle slide + «MAPPE», poi la mappa (vettoriale) in A4 orizzontale
import sys, os, json, subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import mappa8, dispensa
from gfx import *; from plan import *
OUT='/tmp/w/out'; Z=1123/1920
cov=f'<div class="logo">{LOGO}</div><div class="rule"></div><div class="label" style="font-size:30px">{MATERIA.replace(" V","")} · Videolezione</div><div class="label" style="top:200px;font-size:48px;color:#0B1530">MAPPE</div><div class="title" style="font-size:120px;top:300px;width:1760px">{esc(TITOLO)}</div><div class="bar" style="top:480px"></div>'
dispensa.to_pdf([dispensa.page(1,cov)],f'{OUT}/_cop_mappe.pdf')
h=mappa8.html()
allb=[list(mappa8.BOX.keys()),list(mappa8.EDGES.keys()),0,1]
h=h.replace('</body>',f'<script>window.addEventListener("load",()=>{{render([{json.dumps(allb)}],100)}})</script></body>').replace('html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden}','@page{{size:297mm 210mm;margin:0}}html,body{{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden}}body{{position:relative;top:138px}}'.replace('{{','{').replace('}}','}'))
open('/tmp/w/b/mappa_pdf.html','w').write(h)
js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file:///tmp/w/b/mappa_pdf.html');await p.waitForTimeout(800);await p.pdf({path:'/tmp/w/out/_mappa.pdf',width:'297mm',height:'210mm',printBackground:true,tagged:true,scale:0.5849,margin:{top:0,right:0,bottom:0,left:0}});await b.close()})()"
open('/tmp/w/b/mp.js','w').write(js); subprocess.run(['node','/tmp/w/b/mp.js'],check=True)
subprocess.run(['pdfunite',f'{OUT}/_cop_mappe.pdf',f'{OUT}/_mappa.pdf',f'{OUT}/Storia_arte_V_Lez8_mappe_A4.pdf'],check=True)
print('ok')
