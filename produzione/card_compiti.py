#!/usr/bin/env python3
"""Rifa la scheda «Compiti» (5 s, muta) partendo dal fotogramma della scheda consegnata:
cambia solo la riga di descrizione. uso: card_compiti.py base.mp4 t_compiti "testo riga" out.mp4"""
import sys, os, subprocess, tempfile
sys.path.insert(0, '/home/user/Lezioni/kit/tools')
V, T, TXT, OUT = sys.argv[1], float(sys.argv[2]), sys.argv[3], sys.argv[4]
d = tempfile.mkdtemp(); png = d + '/f.png'
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', str(T + 1.5), '-i', V, '-frames:v', '1', png], check=True)
from playwright.sync_api import sync_playwright
import mappa as M
from PIL import Image
bg='#%02x%02x%02x'%Image.open(png).convert('RGB').getpixel((5,5))
html = f'''<html><head><style>{M.font_css()}html,body{{margin:0;width:1920px;height:1080px;overflow:hidden}}
img{{position:absolute;left:0;top:0}}.cop{{position:absolute;left:100px;top:600px;width:1700px;height:82px;background:{bg}}}
.t{{position:absolute;left:140px;top:616px;font-family:Figtree,Arial;font-size:40px;color:#fff;white-space:nowrap}}</style></head>
<body><img src="file://{png}"><div class="cop"></div><div class="t">{TXT}</div></body></html>'''
open(d + '/p.html', 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium'); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
    pg.goto('file://' + d + '/p.html'); pg.wait_for_timeout(400); pg.screenshot(path=d + '/n.png'); b.close()
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-t', '5', '-i', d + '/n.png', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', '5', '-r', '30',
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', OUT], check=True)
subprocess.run(['cp', d + '/n.png', OUT + '.png'])
