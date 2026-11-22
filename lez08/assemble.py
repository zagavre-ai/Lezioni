# montaggio finale di una Parte: pezzi + transizioni (trans.wav + dissolvenza) + volume -16 LUFS + codifica
import sys, os, json, subprocess, re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan import *
B='/tmp/w/b'; KIT='/home/user/Lezioni/kit'; OUT='/tmp/w/out'; os.makedirs(OUT,exist_ok=True)
ENC=['-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000','-ac','2']
def norm_video(src,dst):
    if not os.path.exists(dst): 
        r=sh(['ffmpeg','-v','error','-y','-i',src,'-vf','fps=30,scale=1920:1080,format=yuv420p']+ENC+[dst]); 
        if r.returncode: raise SystemExit(r.stderr)
    return dst
def dur(f): return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).stdout)
def edge_png(f,which,out):
    if which=='first': sh(['ffmpeg','-v','error','-y','-i',f,'-frames:v','1',out])
    else: sh(['ffmpeg','-v','error','-y','-sseof','-0.15','-i',f,'-update','1','-frames:v','1',out])
def transizione(a,b,name):
    dst=f'{B}/tr_{name}.mkv'
    if os.path.exists(dst): return dst
    edge_png(a,'last',f'{B}/tr_{name}_a.png'); edge_png(b,'first',f'{B}/tr_{name}_b.png')
    r=sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t','0.8','-i',f'{B}/tr_{name}_a.png','-loop','1','-framerate','30','-t','0.8','-i',f'{B}/tr_{name}_b.png','-i',f'{KIT}/suoni/trans.wav',
      '-filter_complex','[0:v][1:v]xfade=transition=fade:duration=0.8:offset=0,format=yuv420p[v];[2:a]atrim=0:0.8,afade=t=out:st=0.55:d=0.25,aformat=channel_layouts=stereo,apad=whole_dur=0.8[a]','-map','[v]','-map','[a]','-t','0.8']+ENC+[dst])
    if r.returncode: raise SystemExit(r.stderr)
    return dst
def piece(name): return f'{B}/p_{name}.mkv'
def lista(parte):
    L=[]
    sig=norm_video(f'{KIT}/sigle/Sigla_Storia_arte_15s.mp4',f'{B}/n_sigla.mkv'); L.append(('sigla',sig))
    if parte==1:
        L+= [('intro',piece('intro')),('P0_intro',piece('P0_intro'))]
    else:
        L+= [('spiegone',piece('spiegone'))]
    for n in PARTE[parte]:
        L+=[(f'titolo{n}',piece(f'titolo{n}')),(f'T{n}',piece(f'T{n}')),(f'approf{n}',piece(f'approf{n}')),(f'pillola{n}',piece(f'pillola{n}')),(f'quiz{n}',piece(f'quiz{n}'))]
    if parte==1: L.append(('fine1',piece('fine1')))
    else:
        L+=[('glossario',piece('glossario')),('ripasso',piece('ripasso')),('mappa',piece('mappa')),('verifica',piece('verifica')),
            ('sigla_finale',norm_video(f'{KIT}/sigle/Sigla_finale_5s_con_avviso_diritti.mp4',f'{B}/n_sigla_finale.mkv')),('compiti_intro',piece('compiti_intro')),('compiti',piece('compiti'))]
    return L
def assembla(parte):
    L=lista(parte); out=[]; tl=[]; t=0.0
    for k,(name,f) in enumerate(L):
        if not os.path.exists(f): raise SystemExit(f'manca {f}')
        if k>0 and name!='sigla_finale' or (k>0):
            tr=transizione(L[k-1][1],f,f'{parte}_{k}'); out.append(tr); t+=0.8
        out.append(f); d=dur(f); tl.append({'pezzo':name,'inizio':round(t,2),'fine':round(t+d,2)}); t+=d
    lst=f'{OUT}/lista_P{parte}.txt'; open(lst,'w').write(''.join(f"file '{x}'\n" for x in out))
    json.dump(tl,open(f'{OUT}/timeline_pezzi_P{parte}.json','w'),ensure_ascii=False,indent=1)
    # audio: concatena, misura e porta a -16 LUFS (solo guadagno, timbro intatto)
    all_=f'{OUT}/audio_P{parte}.wav'
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vn','-c:a','pcm_s16le',all_])
    m=sh(['ffmpeg','-hide_banner','-i',all_,'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-']).stderr
    j=json.loads(m[m.rindex('{'):m.rindex('}')+1])
    ln=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
    norm=f'{OUT}/audio16_P{parte}.wav'; sh(['ffmpeg','-v','error','-y','-i',all_,'-af',ln,'-ar','48000','-c:a','pcm_s16le',norm])
    vid=f'{OUT}/Storia_arte_V_Lez8_Parte{parte}_1080p.mp4'
    crf=os.environ.get('CRF','19')
    r=sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-i',norm,'-map','0:v','-map','1:a','-c:v','libx264','-preset','veryfast','-crf',crf,'-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','-shortest',vid])
    if r.returncode: raise SystemExit(r.stderr)
    print(vid,round(os.path.getsize(vid)/1048576),'MB',round(dur(vid)/60,1),'min',j['input_i'],'->-16'); return vid
if __name__=='__main__':
    assembla(int(sys.argv[1]))
