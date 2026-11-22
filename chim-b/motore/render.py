# render.py: rende una scena HTML in mp4 muto, rendendo solo i fotogrammi che cambiano.
# La scena espone render(t) e sig() (firma dello stato). uso: render_scena(html, dati_json, durata, out_mp4, trasparente=False)
import json, subprocess, os, sys, hashlib
from playwright.sync_api import sync_playwright
SIG = "(()=>{let s=document.body.innerHTML;let h=0;for(let i=0;i<s.length;i++){h=(h*31+s.charCodeAt(i))|0}return h+':'+s.length})()"
def render_scena(html, dati, durata, out, fps=30, alpha=False, t0=0.0):
    n = int(round(durata * fps))
    vf = ['-c:v','qtrle','-pix_fmt','argb'] if alpha else ['-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p']
    ff = subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(fps),'-i','-']+vf+[out], stdin=subprocess.PIPE)
    last = None; buf = None; nshot = 0
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium', args=['--no-sandbox']); pg = br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://' + os.path.abspath(html)); pg.wait_for_timeout(500)
        pg.evaluate('d=>setData(d)', dati)
        pg.evaluate("document.fonts.ready")
        for i in range(n):
            pg.evaluate(f'render({t0 + i / fps})')
            s = pg.evaluate(SIG)
            if s != last:
                buf = pg.screenshot(type='png', omit_background=alpha); last = s; nshot += 1
            ff.stdin.write(buf)
        ff.stdin.close(); ff.wait(); br.close()
    return n, nshot
if __name__ == '__main__':
    html, datafile, dur, out = sys.argv[1:5]
    print(render_scena(html, json.load(open(datafile)), float(dur), out))
