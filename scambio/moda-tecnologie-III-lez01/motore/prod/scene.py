# Motore delle scene HTML: render(t) -> fotogrammi (solo stati distinti) -> mp4 muto + wav mixato delle voci e dei jingle
import sys,json,os,subprocess,hashlib
from playwright.sync_api import sync_playwright
FPS=30
SND='/home/user/lav/kit/home/claude/v5/snd/'
def dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
def video(html,data,steps,D,outdir,name,extra=None):
    os.makedirs(outdir,exist_ok=True)
    N=int(round(D*FPS));cache={};frames=[]
    with sync_playwright() as p:
        br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://'+html);pg.evaluate('document.fonts.ready.then(()=>true)');pg.wait_for_timeout(300)
        pg.evaluate('([d,s])=>{window.DATA=d;setData(d);setSteps(s)}',[data,steps])
        pg.evaluate('document.fonts.ready.then(()=>true)')
        if extra:pg.evaluate(extra)
        for f in range(N):
            pg.evaluate('t=>render(t)',f/FPS)
            h=hashlib.md5(pg.evaluate('document.body.innerHTML').encode()).hexdigest()
            if h not in cache:
                fn=f'{outdir}/{name}_{len(cache):05d}.png';pg.screenshot(path=fn);cache[h]=fn
            frames.append(cache[h])
        pg.evaluate('t=>render(t)',max(0,D-0.4));pg.screenshot(path=f'{outdir}/{name}.page.png')
        open(f'{outdir}/{name}.page.txt','w').write(pg.evaluate('document.body.innerText'))
        br.close()
    runs=[]
    for fn in frames:
        if runs and runs[-1][0]==fn:runs[-1][1]+=1
        else:runs.append([fn,1])
    lst=f'{outdir}/{name}.txt'
    with open(lst,'w') as o:
        for fn,n in runs:o.write(f"file '{fn}'\nduration {n/FPS:.6f}\n")
        o.write(f"file '{runs[-1][0]}'\n")
    out=f'{outdir}/{name}.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf',f'fps={FPS},format=yuv420p','-frames:v',str(N),'-c:v','libx264','-preset','veryfast','-crf','17',out],check=True)
    for fn in set(frames):
        try:os.remove(fn)
        except:pass
    return out
def audio(voci,D,out,jingle=None):
    """voci=[(wav,start_s)]; jingle=[(nome.wav,start_s)] dalla cartella snd. Dissolvenza 20 ms in, 40 ms out sulle voci."""
    ins=[];flt=[];k=0
    for w,st in voci:
        d=dur(w);ins+=['-i',w];ms=int(st*1000)
        flt.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={max(0,d-0.04):.3f}:d=0.04,adelay={ms}|{ms}[a{k}]');k+=1
    for n,st in (jingle or []):
        ins+=['-i',SND+n];ms=int(st*1000)
        flt.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{k}]');k+=1
    if k==0:
        subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',f'{D:.3f}','-c:a','pcm_s16le',out],check=True);return out
    fc=';'.join(flt)+';'+''.join(f'[a{i}]' for i in range(k))+f'amix=inputs={k}:normalize=0,apad,atrim=0:{D:.3f}[a]'
    subprocess.run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc,'-map','[a]','-c:a','pcm_s16le','-ar','48000',out],check=True)
    return out
