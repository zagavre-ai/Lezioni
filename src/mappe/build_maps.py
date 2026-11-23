#!/usr/bin/env python3
"""Mappe BES animate (lez06). Uso: python3 build_maps.py M1|M2|all [--pagina N] [--solo png|pdf|video|html]
Rilegge i tempi dalla voce corrente (/tmp/w/vox/ se c'è la voce vera, altrimenti /tmp/w/vox_prov/)."""
import os,sys,json,subprocess,argparse,wave
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE); sys.path.insert(0,'/tmp/w/build')
import timing
from defs import MAPS
TXT={v['nome']:v['testo'] for v in json.load(open('/tmp/w/voci/testi_voci.json'))}
PIECES='/tmp/w/build/pieces'; PDFD='/tmp/w/build/pdf'
def data(M,pagina):
    nome=M['voce']; w=timing.wav_words(nome,TXT[nome]); D=timing.dur(nome)
    al=timing.align([s['cue'] for s in M['steps']],w)
    steps=[]
    for i,(s,(a,b)) in enumerate(zip(M['steps'],al)):
        t0=max(a-0.15,2.6 if i==0 else 0); steps.append(dict(t0=round(t0,2),t1=round(b,2),boxes=s['boxes'],arrows=s['arrows'],hl=s['hl'],cam=s['cam']))
    # i tempi devono essere crescenti
    for i in range(1,len(steps)):
        if steps[i]['t0']<steps[i-1]['t0']+0.3: steps[i]['t0']=round(steps[i-1]['t0']+0.3,2)
    for i in range(len(steps)-1): steps[i]['t1']=max(steps[i]['t1'],steps[i]['t0']+0.6); steps[i]['t1']=min(steps[i]['t1'],steps[i+1]['t0']+0.4)
    steps[-1]['t1']=max(steps[-1]['t1'],D)
    end=D+4.0; zoomT=max(steps[-1]['t0']+1.0,D-1.6)
    return dict(W=M['W'],H=M['H'],titolo=M['titolo'],pagina=pagina,boxes=M['boxes'],
                arrows=[dict(f=a['f'],t=a['t'],l=a['l'],o=a['o']) for a in M['arrows']],steps=steps,end=round(end,2),zoomT=round(zoomT,2),zoomEnd=round(D,2)),D
def write_html(M,pagina):
    d,D=data(M,pagina); h=open(f'{HERE}/tpl.html').read().replace('__DATA__',json.dumps(d,ensure_ascii=False))
    p=f'{HERE}/map_{M["nome"]}.html'; open(p,'w').write(h); json.dump(d,open(f'{HERE}/map_{M["nome"]}.json','w'),ensure_ascii=False,indent=1); return p,d,D
def run(M,pagina,solo):
    n=M['nome']; p,d,D=write_html(M,pagina)
    if solo in (None,'png'): subprocess.run(['node',f'{HERE}/render.js','png',p,f'{PIECES}/MAPPA_{n}_finale.png'],check=True,cwd=HERE)
    if solo in (None,'pdf'): subprocess.run(['node',f'{HERE}/render.js','pdf',p,f'{PDFD}/mappa_{n}.pdf'],check=True,cwd=HERE)
    if solo in (None,'video'):
        total=int(round(d['end']*30)); out=f'{PIECES}/MAPPA_{n}.mp4'; vp=timing.voice_path(M['voce'])
        af=f"aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.03,afade=t=out:st={D-0.04:.3f}:d=0.04,apad=whole_dur={d['end']:.3f}"
        ff=subprocess.Popen(['ffmpeg','-y','-v','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-i',vp,'-af',af,'-map','0:v','-map','1:a',
            '-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-threads','2','-c:a','aac','-b:a','192k','-ar','48000','-t',f"{d['end']:.3f}",'-movflags','+faststart',out],stdin=subprocess.PIPE)
        nd=subprocess.Popen(['node',f'{HERE}/render.js','frames',p,'-','30',str(total)],stdout=ff.stdin,cwd=HERE)
        nd.wait(); ff.stdin.close(); ff.wait()
        print(n,'durata',d['end'],'s','voce',round(D,1),'s')
if __name__=='__main__':
    a=argparse.ArgumentParser(); a.add_argument('mappa'); a.add_argument('--pagina',type=int,default=1); a.add_argument('--solo'); o=a.parse_args()
    os.makedirs(PIECES,exist_ok=True); os.makedirs(PDFD,exist_ok=True)
    for k in (list(MAPS) if o.mappa=='all' else [o.mappa]): run(MAPS[k],o.pagina,o.solo)
