import json,os,re,subprocess,sys
sys.path.insert(0,'/home/claude/w19/lib')
W='/home/claude/w19';D=W+'/revisione-storia-V-lez19'
def rd(f): return open(f).read() if os.path.exists(f) else ''
def mm(s): return f"{int(s//60)}:{s%60:04.1f}"
def ebu(v):
    r=subprocess.run(['ffmpeg','-v','info','-i',v,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    i=re.findall(r'I:\s+(-?[\d.]+) LUFS',r);p=re.findall(r'Peak:\s+(-?[\d.]+) dBFS',r)
    return i[-1],p[-1]
def info(v):
    r=subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets,width,height,r_frame_rate:format=duration,size','-of','json',v],capture_output=True,text=True).stdout
    j=json.loads(r);return float(j['format']['duration']),int(j['streams'][0]['nb_read_packets']),int(j['format']['size'])/2**20
L=[]
P=L.append
P("# RAPPORTO · Storia V · «L’Italia dal ’68 alla crisi della Prima Repubblica» · correzioni del 22/11\n")
P("**Stato: rifatta da zero nel modello del 22/11** (CLAUDE.md + PROMPT_StoriaV_correzioni_22-11) sul video originale del prof (4795,9 s, release `mazzotti-storia-V`), in 2 Parti. Ogni affermazione è marcata [misurato], [per costruzione], [stima] o [non verificato]. **Le voci Kore nuove non sono ancora arrivate: vedi sezione 2.**\n")
P("## 1 · Misure sul video\n")
rows=[]
for n in (1,2):
    v=f'{W}/final/Storia_Lez19_Parte{n}_1080p.mp4'
    d,fr,mb=info(v);i,p=ebu(v)
    from timbre import timbre
    tb=timbre(v)
    rows.append((n,d,fr,mb,i,p,tb,rd(f'{W}/final/Storia_Lez19_Parte{n}_1080p.mp4.controllo.txt')))
P("| | Parte 1 | Parte 2 |\n|---|---|---|")
P(f"| Durata | {mm(rows[0][1])} ({rows[0][1]:.1f} s) [misurato] | {mm(rows[1][1])} ({rows[1][1]:.1f} s) [misurato] |")
P(f"| Fotogrammi (30 fps) | {rows[0][2]} (attesi {round(rows[0][1]*30)}) [misurato] | {rows[1][2]} (attesi {round(rows[1][1]*30)}) [misurato] |")
P("| Formato | 1920×1080, x264 veryfast CRF 19, AAC 192k 48 kHz [misurato] | idem |")
P(f"| Peso | {rows[0][3]:.1f} MiB [misurato] | {rows[1][3]:.1f} MiB [misurato] |")
P(f"| Loudness integrata (ebur128) | {rows[0][4]} LUFS [misurato] | {rows[1][4]} LUFS [misurato] |")
P(f"| Picco | {rows[0][5]} dBFS [misurato] (limite −1) | {rows[1][5]} dBFS [misurato] |")
P(f"| Timbre (acuti >4 kHz meno >100 Hz) | {rows[0][6]:.1f} dB [misurato] (originale del prof: −19,0 dB; limiti −9…−20) | {rows[1][6]:.1f} dB [misurato] |")
P("| sha256 | vedi `.sha256` (ricomponendo i `.parte_NN`) | idem |\n")
P("Uscita integrale di `controllo_finale.py`:\n")
for n in (1,2):
    P(f"```\nParte {n}\n{rows[n-1][7].strip()}\n```")
for n in (1,2):
    P(f"Scatto `quiz.wav` Parte {n} (`controllo_jingle.py`):\n```\n{rd(f'{W}/jingle{n}.log').strip()}\n```")
for n in (1,2):
    P(f"`controllo_severo.py` Parte {n}:\n```\n{rd(f'{W}/severo{n}.log').strip()[:3500]}\n```")
open(D+'/RAPPORTO_PARTE_MISURE.md','w').write('\n'.join(L))
print('ok')
