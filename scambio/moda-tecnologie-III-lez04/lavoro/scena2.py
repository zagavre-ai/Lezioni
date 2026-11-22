# render parallelo di scene HTML con funzione render(t) -> mp4 (15 fps reali, duplicati a 30)
import os, sys, json, subprocess, shutil
from multiprocessing import Pool
FPS_R=15
def _worker(a):
    html,steps,idx,outdir,trasp=a
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox'])
        pg=b.new_page(viewport={'width':1920,'height':1080}); pg.goto('file://'+html); pg.wait_for_timeout(500)
        pg.evaluate(f"setSteps({json.dumps(steps)})")
        for i in idx:
            pg.evaluate(f"render({i/FPS_R})")
            pg.screenshot(path=f'{outdir}/f{i:06d}.png',omit_background=trasp)
        b.close()
def render(html,steps,tot,out,trasp=False,workers=4):
    """html: file; steps: [[t,dur],..]; tot: durata s; out: mp4 (muto). trasp: qtrle con alpha (.mov)"""
    n=int(round(tot*FPS_R)); td=out+'.fr'; shutil.rmtree(td,ignore_errors=True); os.makedirs(td)
    chunks=[list(range(k,n,workers)) for k in range(workers)]
    with Pool(workers) as P: P.map(_worker,[(html,steps,c,td,trasp) for c in chunks])
    nf=round(tot*30)
    cod=['-c:v','qtrle','-pix_fmt','argb'] if trasp else ['-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p']
    subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS_R),'-i',f'{td}/f%06d.png','-vf','fps=30','-frames:v',str(nf)]+cod+['-r','30',out],check=True)
    shutil.rmtree(td,ignore_errors=True)
def mix(video,voci,tot,out,jingles=(),vol_j=0.6):
    """voci: [(t_inizio, wav)] ; jingles: [(t, wav)] ; aggiunge audio (48k, dissolvenze 20-40 ms sulle voci)"""
    ins=[];fl=[];k=0
    for t,w in voci:
        d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',w],capture_output=True,text=True).stdout)
        ins+=['-i',w]; fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=mono,afade=t=in:d=0.02,afade=t=out:st={max(0,d-0.04):.3f}:d=0.04,adelay={int(t*1000)}:all=1[a{k}]');k+=1
    for t,w in jingles:
        ins+=['-i',w]; fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=mono,volume={vol_j},adelay={int(t*1000)}:all=1[a{k}]');k+=1
    if k==0:
        subprocess.run(['ffmpeg','-v','error','-y','-i',video,'-f','lavfi','-i','anullsrc=r=48000:cl=mono','-shortest','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000',out],check=True);return
    fc=';'.join(fl)+';'+''.join(f'[a{i}]' for i in range(k))+f'amix=inputs={k}:normalize=0:dropout_transition=0,apad,atrim=0:{tot:.3f}[a]'
    subprocess.run(['ffmpeg','-v','error','-y']+ins+['-i',video,'-filter_complex',fc,'-map',f'{k}:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',f'{tot:.3f}',out],check=True)
