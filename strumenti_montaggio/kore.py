import os, json, subprocess, re
W='/home/claude/w'
VOX='/home/user/Lezioni/scambio/storia-V-lez21/vox'
PROV=f'{W}/vox_prov'
OUT=f'{W}/out'
os.makedirs(OUT,exist_ok=True); os.makedirs(f'{W}/voc',exist_ok=True)
# voce logica -> nome del file da usare (versioni rifatte)
USA={'BEN1':'BEN1_R4','BEN2':'BEN2_R4','AP3_0':'AP3_0_R2','AP3_1':'AP3_1_R2','AP3_3':'AP3_3_R2','AP5_1':'AP5_1_R2',
     'SC3_1':'SC3_1_R2','SC3_2':'SC3_2_R2','SC3_3':'SC3_3_R2','SC3_4':'SC3_4_R2','LG1':'LG1_R2','MA3_4':'MA3_4_R2','MA2_6':'MA2_6_R2','MA2_1':'MA2_1_R2','MA4_2':'MA4_2_R2','MB4_0':'MB4_0_R2','SC7_2':'SC7_2_R2','PI1':'PI1_R2'}
TESTI={x['nome']:x['testo'] for x in json.load(open(f'{W}/testi_voci.json'))}
def sh(c): return subprocess.run(c,capture_output=True,text=True)
def dur(p):
    return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).stdout.strip())
def real(n): return os.path.exists(f'{VOX}/{n}.wav')
NO_OLD={'BEN1','BEN2'}   # le voci vecchie dicono il nome del docente: mai usarle
USATE={}
BLOCK={'MA3_4','MA2_6'}   # voci difettose (testo dello stile letto ad alta voce / pronuncia russa): provvisorie finche' la master non le rifa
def _fonte(nome):
    if nome in BLOCK and not real(USA.get(nome,nome)): return f'{PROV}/{USA.get(nome,nome)}.wav' if os.path.exists(f'{PROV}/{USA.get(nome,nome)}.wav') else f'{PROV}/{nome}.wav',nome,False
    cand=[USA.get(nome,nome)]
    if nome in USA and nome not in NO_OLD: cand.append(nome)
    for c in cand:
        if real(c): return f'{VOX}/{c}.wav',c,True
    c=USA.get(nome,nome)
    return f'{PROV}/{c}.wav',c,False
def voce(nome):
    """ritorna (percorso wav pulito, durata, testo, reale?) : taglia il silenzio, dissolvenza 30 ms, 0,12 s di silenzio in coda"""
    src,n,isreal=_fonte(nome)
    if not os.path.exists(src): raise SystemExit(f'manca la voce {n}')
    tag='r' if isreal else 'p'
    o=f'{W}/voc/{n}_{tag}2.wav'
    if not os.path.exists(o):
        sh(['ffmpeg','-v','error','-y','-i',src,'-af','silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.02,areverse','-ar','48000','-ac','2',f'/tmp/_v_{os.getpid()}.wav'])
        d2=dur(f'/tmp/_v_{os.getpid()}.wav')
        sh(['ffmpeg','-v','error','-y','-i',f'/tmp/_v_{os.getpid()}.wav','-af',f'afade=t=in:d=0.03,afade=t=out:st={max(0,d2-0.04):.3f}:d=0.04,apad=pad_dur=0.14','-ar','48000','-ac','2',o])
    USATE[nome]=(n,isreal)
    return o,dur(o),TESTI.get(n,TESTI.get(nome,'')),isreal
def mix(specs,total,out,tail=0.0):
    """specs: [(wav, start_s, gain_db)] -> wav stereo 48k di durata total"""
    cmd=['ffmpeg','-v','error','-y']
    for p,_,_ in specs: cmd+=['-i',p]
    cmd+=['-f','lavfi','-t',f'{total:.3f}','-i','anullsrc=r=48000:cl=stereo']
    fl=[]
    for i,(p,s,g) in enumerate(specs):
        fl.append(f'[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g}dB,adelay={int(s*1000)}|{int(s*1000)}[a{i}]')
    ins=''.join(f'[a{i}]' for i in range(len(specs)))+f'[{len(specs)}:a]'
    fl.append(f'{ins}amix=inputs={len(specs)+1}:normalize=0:duration=longest,atrim=0:{total:.3f},apad=whole_dur={total:.3f}[o]')
    cmd+=['-filter_complex',';'.join(fl),'-map','[o]','-ar','48000','-ac','2',out]
    r=sh(cmd)
    if r.returncode: raise SystemExit(r.stderr[-600:])
    return out
JING={k:f'/home/user/Lezioni/kit/suoni/{k}.wav' for k in ('titolo','repaso','quiz','trans','finale')}
def mux(video,audio,out,dur_s):
    r=sh(['ffmpeg','-v','error','-y','-i',video,'-i',audio,'-map','0:v','-map','1:a','-c:v','copy','-c:a','pcm_s16le','-t',f'{dur_s:.3f}',out])
    if r.returncode: raise SystemExit(r.stderr[-600:])
# --- tempi delle frasi dentro una voce: da ASR se c'e', altrimenti proporzionali ai caratteri ---
def frasi(testo):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«"])',testo.strip()) if s.strip()]
def tempi_frasi(nome,testo,d):
    """tempi (inizio,fine) di ogni frase dentro la voce: da ASR (token con tempi) se disponibile, altrimenti proporzionali ai caratteri"""
    f=frasi(testo);n=sum(len(x) for x in f)
    nn=USA.get(nome,nome);fa=f'{W}/voci_asr/{nn}.json'
    if os.path.exists(fa) and real(nn):
        j=json.load(open(fa));tk=j['tokens'];ts=j['ts']
        starts=[];ends=[];new=True
        for t,x in zip(ts,tk):
            if new and x.strip() not in ('.','?','!'): starts.append(t);new=False
            if x.strip() in ('.','?','!') and not new: ends.append(t+0.25);new=True
        if len(starts)==len(f):
            off=ts[0]-0.08
            while len(ends)<len(starts): ends.append(d)
            res=[(max(0.0,s-off),min(d,e-off)) for s,e in zip(starts,ends)]
            return f,res
    t=0.1;res=[]
    for x in f:
        L=len(x)/n*(d-0.2);res.append((t,t+L));t+=L
    return f,res
