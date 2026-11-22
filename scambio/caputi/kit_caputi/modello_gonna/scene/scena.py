# scena.py: rende una scena HTML (funzione render(t) + setSteps) in un mp4 con le voci.
# uso da python: fai(html, voci=[nomi], out, lead=1.0, gap=0.7, coda=3.0, extra={} ) -> durata
import json, subprocess, os
from playwright.sync_api import sync_playwright
D = '/home/claude/lavoro'   # CAMBIA: cartella che contiene voci/vox/NOME.wav
def dur(n):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{D}/voci/vox/{n}.wav'],capture_output=True,text=True).stdout)
def piano(voci, lead=1.0, gap=0.7, pause=None):
    t = lead; steps = []
    for i, v in enumerate(voci):
        if v is None:            # pausa senza voce
            steps.append([round(t,3), pause or 3.0, None]); t += (pause or 3.0) + gap; continue
        d = dur(v); steps.append([round(t,3), d, v]); t += d + gap
    return steps, t
def fai(html, voci, out, lead=1.0, gap=0.7, coda=3.0, pause=None, trasparente=False, scatto=None):
    steps, t = piano(voci, lead, gap, pause); tot = t + coda
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://' + html); pg.wait_for_timeout(400)
        pg.evaluate(f"setSteps({json.dumps([[s[0], s[1]] for s in steps])})")
        if scatto is not None:
            pg.evaluate(f"render({scatto})"); pg.screenshot(path=out.replace('.mp4', '.png')); br.close(); return tot
        vid = out.replace('.mp4', '_muto.mp4')
        ff = subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',vid], stdin=subprocess.PIPE)
        for i in range(int(tot*30)):
            pg.evaluate(f"render({i/30})"); ff.stdin.write(pg.screenshot(type='png'))
        ff.stdin.close(); ff.wait(); br.close()
    ins = []; flt = []; k = 0
    for st, d, v in steps:
        if v is None: continue
        ins += ['-i', f'{D}/voci/vox/{v}.wav']; flt.append(f'[{k}:a]aresample=48000,afade=t=in:d=0.02,afade=t=out:st={max(0,d-0.04):.3f}:d=0.04,adelay={int(st*1000)}|{int(st*1000)}[a{k}]'); k += 1
    fc = ';'.join(flt) + ';' + ''.join(f'[a{i}]' for i in range(k)) + f'amix=inputs={k}:normalize=0,apad,atrim=0:{tot}[a]'
    subprocess.run(['ffmpeg','-v','error','-y'] + ins + ['-i', vid, '-filter_complex', fc, '-map', f'{k}:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', out], check=True)
    os.remove(vid); json.dump(steps, open(out.replace('.mp4', '.steps.json'), 'w'))
    return tot
