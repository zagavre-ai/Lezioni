# pezzi animati: schede blu scuro (titolo, pillola, quiz, ripasso, glossario, compiti), introduzione, approfondimenti
import sys, os, json, subprocess, numpy as np, cv2, re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan import *; from gfx import *; import frames
B='/tmp/w/b'; OP='/tmp/w/op'; VOX='/tmp/w/vox'; os.makedirs(VOX,exist_ok=True)
HERE=os.path.dirname(os.path.abspath(__file__))
TESTI={v['nome']:v['testo'] for v in json.load(open('/tmp/w/voci/testi_voci.json'))}
def shots(man):
    mf=f'{B}/man_a{os.getpid()}.json'; json.dump(man,open(mf,'w')); r=subprocess.run(['node',f'{HERE}/shot.js',mf],capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr)
# ---------- voci (vere se presenti, altrimenti provvisorie) ----------
def voce(nome):
    """-> (wav, durata, [(tempo, parola)] o None)"""
    real=f'/home/user/Lezioni/scambio/storia-arte-V-lez08/vox/{nome}.wav'
    if os.path.exists(real):
        d=float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',real]).stdout)
        tj=f'{VOX}/{nome}.json'
        return real,d,(json.load(open(tj)) if os.path.exists(tj) else None)
    p=f'{VOX}/prov_{nome}.wav'; n=len(TESTI[nome].split()); d=round(n/2.45+0.8,2)
    if not os.path.exists(p): sh(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'anoisesrc=d={d}:c=pink:a=0.03:r=48000','-ac','2',p])
    return p,d,None
def tempi_marcatori(nome,marc):
    """istante (s) in cui la voce dice ciascun marcatore (parola, in ordine); con voce vera usa la trascrizione, altrimenti proporzione"""
    w=TESTI[nome].lower().replace(':',' ').replace(',',' ').replace('.',' ').split(); wav,d,tw=voce(nome)
    out=[]; pos=0
    for m in marc:
        m=m.lower()
        k=next((i for i in range(pos,len(w)) if w[i]==m),None)
        if k is None: k=pos
        pos=k+1; out.append(k)
    if tw:  # trascrizione: cerca la stessa parola nella sequenza dell'ASR
        asr=[(t,x.strip().lower().strip('.,:;?')) for t,x in tw]; res=[]; j=0
        for m,k in zip(marc,out):
            m=m.lower(); f=next((t for t,x in asr[j:] if x==m),None)
            if f is None: f=k/len(w)*d
            else: j=next(i for i in range(j,len(asr)) if asr[i][1]==m)+1
            res.append(max(f-0.1,0))
        return res
    return [k/len(w)*d for k in out]
# ---------- sfondo blu scuro animato ----------
def dark_bg(t):
    W,H=192,108; base=np.zeros((H,W,3),np.float32); base[:]=(11,21,48)
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
    def blob(cx,cy,r,col,a):
        g=np.exp(-(((xx-cx)**2+(yy-cy)**2)/(2*r*r)))[...,None]; return g*np.array(col,np.float32)*a
    img=base+blob(W*(0.25+0.15*np.sin(t*0.35)),H*(0.35+0.2*np.cos(t*0.27)),32,(32,96,175),0.55)+blob(W*(0.78+0.12*np.cos(t*0.3)),H*(0.7+0.15*np.sin(t*0.42)),38,(32,96,175),0.40)+blob(W*(0.55+0.2*np.sin(t*0.21)),H*(0.2+0.1*np.cos(t*0.5)),22,(255,230,0),0.06)
    return cv2.resize(np.clip(img,0,255).astype(np.uint8),(1920,1080),interpolation=cv2.INTER_CUBIC)
class Dark:
    def __init__(s,layer_png,off=0.0):
        im=cv2.imread(layer_png,cv2.IMREAD_UNCHANGED); s.rgb=cv2.cvtColor(im[...,:3],cv2.COLOR_BGR2RGB).astype(np.float32); s.a=(im[...,3:4].astype(np.float32)/255.0); s.off=off
    def frame(s,t):
        bg=dark_bg(t+s.off).astype(np.float32); return (bg*(1-s.a)+s.rgb*s.a).astype(np.uint8)
DCSS='''<style>*{box-sizing:border-box;margin:0;padding:0}html,body{width:1920px;height:1080px;background:transparent;overflow:hidden;font-family:'Figtree';color:#fff}
.k{position:absolute;left:0;right:0;text-align:center;font-weight:700;letter-spacing:.2em;font-size:30px;color:#FFE600;text-transform:uppercase}
.h{position:absolute;left:120px;right:120px;text-align:center;font-family:'Bricolage Grotesque';font-weight:800;line-height:1.08}
.ln{position:absolute;left:170px;right:170px;font-size:48px;font-weight:600;line-height:1.22;padding:18px 34px 18px 70px;border-radius:18px;background:rgba(255,255,255,.07);border:5px solid transparent;opacity:.5}
.ln.on{opacity:1;background:rgba(255,255,255,.14);border-color:#FFE600}
.ln .d{position:absolute;left:24px;top:30px;width:22px;height:22px;border-radius:50%;background:#7f8db0}.ln.on .d{background:#FFE600}
.ln b{font-weight:800;color:#FFE600}
.ft{position:absolute;left:0;right:0;bottom:44px;text-align:center;font-weight:700;letter-spacing:.2em;font-size:22px;color:#9fb4dc}
</style>'''
def dark_html(body): return f'<!doctype html><html><head><meta charset="utf-8">{DCSS}</head><body>{body}<div class="ft">STORIA DELL\'ARTE V</div></body></html>'
def lines_html(label,title,lines,active,top=330,step=None,fs=48):
    n=len(lines); avail=1080-top-110; h=step or min(150,avail//max(n,1))
    ls=''.join(f'<div class="ln {"on" if i==active else ""}" style="top:{top+i*h}px;font-size:{fs}px;opacity:{1 if i==active else (.55 if i<active else 0)}"><span class="d"></span>{l}</div>' for i,l in enumerate(lines))
    return dark_html(f'<div class="k" style="top:90px">{esc(label)}</div><div class="h" style="top:150px;font-size:70px">{esc(title)}</div>{ls}')
# ---------- audio e codifica di un pezzo ----------
def mix_audio(parts,total,out):
    """parts=[(wav,inizio,volume)] -> wav stereo 48k lungo total"""
    ins=[];fl=[]
    for k,(w,st,vol) in enumerate(parts):
        ins+=['-i',w]; fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={vol},adelay={int(st*1000)}|{int(st*1000)}[a{k}]')
    mix=''.join(f'[a{k}]' for k in range(len(parts)))
    fc=';'.join(fl)+f';{mix}amix=inputs={len(parts)}:normalize=0:duration=longest,apad=whole_dur={total:.3f},atrim=0:{total:.3f}[o]'
    r=sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc,'-map','[o]','-ar','48000','-ac','2','-c:a','pcm_s16le',out])
    if r.returncode: raise SystemExit(r.stderr)
def emit(pid,tl,total,parts,fade=8):
    wav=f'{B}/a_{pid}.wav'; mix_audio(parts,total,wav)
    out=f'{B}/p_{pid}.mkv'
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-i',wav,'-map','0:v','-map','1:a','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-c:a','pcm_s16le','-shortest',out],stdin=subprocess.PIPE)
    frames.render_timeline(tl,total,ff.stdin,fade); ff.stdin.close(); ff.wait(); return out
SU=f'{KIT}/suoni'
def titolo_arg(n):
    h=dark_html(f'<div class="k" style="top:330px">Argomento {n}</div><div class="h" style="top:400px;font-size:104px">{esc(ARG[n])}</div>')
    f=f'{B}/ti_{n}'; open(f+'.html','w').write(h); shots([{'html':f+'.html','out':f+'.png','transparent':True}])
    return emit(f'titolo{n}',[(0,Dark(f+'.png'))],3.6,[(f'{SU}/titolo.wav',0.0,0.8)])
def quiz_card(n):
    h=dark_html(f'<div class="k" style="top:300px">Argomento {n} · {esc(ARG[n])}</div><div class="h" style="top:370px;font-size:190px">Quiz</div><div class="h" style="top:640px;font-size:52px;font-weight:700">5 domande · per continuare serve almeno l\'80%</div>')
    f=f'{B}/qz_{n}'; open(f+'.html','w').write(h); shots([{'html':f+'.html','out':f+'.png','transparent':True}])
    return emit(f'quiz{n}',[(0,Dark(f+'.png'))],4.6,[(f'{SU}/quiz.wav',0.5,0.8)])
PILL={1:["l'Impero tedesco è una potenza in crescita: 67 milioni di abitanti","la metropoli porta disagio, alienazione e agorafobia","agorafobia: paura delle folle e degli spazi aperti","Freud e Simmel studiano nevrosi e solitudine","1907: a Monaco nasce il Deutscher Werkbund"],
 2:["le Secessioni: Monaco, Vienna, Berlino","artisti dissidenti contro le accademie ufficiali","l'Espressionismo va dall'esteriore all'interiorità emotiva","forme distorte e colori antinaturalistici","reazione al conformismo borghese"],
 3:["James Ensor: angoscia, maschere e scheletri","Edvard Munch: lutti e vicende personali","La bambina malata (1885-86): ricordo autobiografico","L'urlo (1893): icona dell'angoscia contemporanea","Pubertà: un'ombra inquietante"],
 4:["Die Brücke nasce a Dresda nel 1905","forme spigolose e colori violenti","Potsdamer Platz: nevrosi urbana di Berlino","Strada a Berlino: prospettiva stravolta","Cinque donne per la strada: mercificazione"],
 5:["Der Blaue Reiter nasce a Monaco nel 1911","pittura lirica, spirituale, verso l'astrazione","Marc: Grandi cavalli azzurri e Piccoli cavalli gialli","Kandinskij traduce la musica in pittura","Klee: infanzia, ironia e geometria"],
 6:["Vienna: legami con la Secessione","Kokoschka: realtà deformata, colori pastosi","La sposa del vento: relazione tormentata","Schiele: erotismo, nudo e tormento interiore","L'abbraccio (1917): linea tagliente"]}
MARC=['primo','secondo','terzo','quarto','quinto']
def pillola(n):
    nome=VOCI[n][1]; wav,d,_=voce(nome); L=PILL[n]; T=tempi_marcatori(nome,MARC[:len(L)]); J=3.3
    man=[];tl=[]
    for k in range(-1,len(L)):
        f=f'{B}/pi_{n}_{k}'; open(f+'.html','w').write(lines_html("Ripasso · "+LAB[n].split(' · ')[1] if False else "Pillola di ripasso",ARG[n],L,k,top=360)); man.append({'html':f+'.html','out':f+'.png','transparent':True})
    shots(man); total=J+d+1.4
    tl.append((0,Dark(f'{B}/pi_{n}_-1.png',0)))
    for k in range(len(L)): st=J+T[k]; tl.append((st,Dark(f'{B}/pi_{n}_{k}.png',st)))
    return emit(f'pillola{n}',tl,total,[(f'{SU}/repaso.wav',0.0,0.8),(wav,J,1.0)])
# ---------- approfondimenti (voce Kore, solo dal materiale del prof) ----------
AP_BOX=(80,190,1100,700)
def panel(t,sub=''):
    return f'<div style="position:absolute;left:80px;top:190px;width:1100px;height:700px;border-radius:26px;background:#F5F8FC;box-shadow:0 12px 34px rgba(70,80,100,.18);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:50px"><div style="font-family:\'Bricolage Grotesque\';font-weight:800;font-size:92px;line-height:1.05;color:#0B1530">{esc(t)}</div><div style="font-size:48px;font-weight:600;margin-top:30px;color:#2060AF;line-height:1.25">{esc(sub)}</div></div>'
def chips(ch):
    out=''; n=len(ch)
    for i,c in enumerate(ch):
        on=i==n-1
        out+=f'<div style="position:relative;margin-bottom:22px;background:{"#fff" if on else "#F5F8FC"};border:6px solid {"#FFE600" if on else "transparent"};border-radius:18px;padding:18px 26px;font-size:40px;font-weight:700;line-height:1.2;box-shadow:0 8px 22px rgba(70,80,100,.14);opacity:{1 if on else .6}">{esc(c)}</div>'
    return f'<div style="position:absolute;left:1240px;top:190px;width:600px">{out}</div>'
APP={
1:[(None,('panel',"L'Impero tedesco","primi anni del Novecento"),None),
   ('sessantasette',('panel',"67 milioni","di abitanti"),"Berlino: centro di filosofi, artisti e architetti"),
   ('tram',('panel',"Tram e vie affollate","meno spazio personale"),"La vicinanza forzata riduce lo spazio personale"),
   ('agorafobia',('panel',"Agorafobia","la paura delle folle e degli spazi aperti"),"Agorafobia: paura delle folle e degli spazi aperti"),
   ('freud',('panel',"Sigmund Freud","piantine per collegare le fobie agli spazi"),"Freud: piantine per collegare fobie e spazi"),
   ('millenovecentotré',('panel',"1903 · Georg Simmel","molte relazioni superficiali: solitudine"),"1903, Dresda: Georg Simmel e la solitudine")],
2:[(None,('panel',"Le Secessioni","artisti dissidenti contro le accademie"),None),
   ('monaco',('panel',"Monaco","1892"),"1892: Secessione di Monaco"),
   ('vienna',('panel',"Vienna","1897"),"1897: Secessione di Vienna"),
   ('berlino',('panel',"Berlino","1898"),"1898: Secessione di Berlino"),
   ("l'impressionismo",('panel',"Impressionismo","dall'esterno: ciò che l'artista vede"),"Impressionismo: l'impressione dall'esterno"),
   ("l'espressionismo",('panel',"Espressionismo","l'interiorità emotiva e spirituale"),"Espressionismo: l'interiorità emotiva"),
   ('conformismo',('panel',"Contro il conformismo","forme distorte, colori antinaturalistici"),"Reazione al conformismo borghese")],
3:[(None,('art','bambina_malata',(0.38,0.4),(0.5,0.5)),"1885-86: La bambina malata"),
   ('sofie',('art','bambina_malata',(0.32,0.45),(0.5,0.5)),"Autobiografia: la sorella Sofie"),
   ("l'urlo",('art','urlo',(0.5,0.45),(0.5,0.5)),"1893: L'urlo"),
   ('rosso',('art','urlo',(0.5,0.12),(0.5,0.5)),"Il cielo rosso sangue"),
   ('diagonale',('art','urlo',(0.3,0.8),(0.5,0.5)),"La diagonale della ringhiera")],
4:[(None,('art','potsdamer',(0.5,0.5),(0.5,0.5)),"1914: Potsdamer Platz"),
   ('sfondo',('art','potsdamer',(0.7,0.12),(0.5,0.5)),"Stazione e arcate rosse deformate"),
   ('primo',('art','potsdamer',(0.4,0.78),(0.5,0.5)),"Due donne su una piattaforma rotonda"),
   ('silhouette',('art','potsdamer',(0.85,0.5),(0.5,0.5)),"Silhouette maschili in nero"),
   ('colori',('art','potsdamer',(0.5,0.5),(0.5,0.5)),"Colori lividi e stridenti")],
5:[(None,('art','grandi_cavalli',(0.3,0.55),(0.5,0.5)),"1911: Der Blaue Reiter"),
   ('grandi',('art','grandi_cavalli',(0.25,0.6),(0.5,0.5)),"Grandi cavalli azzurri"),
   ('kandinskij,',('art','impressione3',(0.5,0.5),(0.5,0.5)),"Kandinskij: la musica in pittura"),
   ('schönberg',('art','impressione3',(0.3,0.4),(0.5,0.5)),"Dopo un concerto di Schönberg"),
   ('astrattismo',('art','composizione7',(0.5,0.5),(0.5,0.5)),"L'inizio dell'astrattismo")],
6:[(None,('art','sposa_vento',(0.45,0.55),(0.5,0.5)),"1913-14: La sposa del vento"),
   ('alma',('art','sposa_vento',(0.4,0.5),(0.5,0.5)),"La relazione con Alma Mahler"),
   ('conchiglia',('art','sposa_vento',(0.5,0.6),(0.5,0.5)),"Una conchiglia alla deriva"),
   ('pennellate',('art','sposa_vento',(0.6,0.4),(0.5,0.5)),"Pennellate vorticose"),
   ('egon',('art','schiele',(0.5,0.3),(0.5,0.5)),"Egon Schiele: autoritratto nudo")],
}
def approfondimento(n):
    nome=VOCI[n][0]; wav,d,_=voce(nome); beats=APP[n]; total=d+1.6
    marc=[b[0] for b in beats[1:]]
    # tempi: marcatori dopo il primo; il primo comincia a 0.6 (voce parte a 0.6)
    T=tempi_marcatori(nome,[m.strip(',') for m in marc]); V0=0.6
    times=[0.0]+[V0+t for t in T]
    man=[]; states=[]; chs=[]
    for k,(m,left,chip) in enumerate(beats):
        if chip: chs.append(chip)
        body=(panel(left[1],left[2]) if left[0]=='panel' else '')+chips(chs[-4:])
        h=base(f"Approfondimento · {ARG[n]}",'',None,None,False).replace('@@BODY@@',body)
        f=f'{B}/ap_{n}_{k}'; open(f+'.html','w').write(h); man.append({'html':f+'.html','out':f+'.png'})
    shots(man)
    tl=[]
    for k,(m,left,chip) in enumerate(beats):
        t0=times[k]; t1=times[k+1] if k+1<len(beats) else total
        if left[0]=='art':
            tl.append((t0,frames.Art(f'{B}/ap_{n}_{k}.png',f'{OP}/{left[1]}.png',AP_BOX,max(t1-t0,2.0)+1.5,0.28,left[2],left[3])))
        else: tl.append((t0,frames.Static(f'{B}/ap_{n}_{k}.png')))
    return emit(f'approf{n}',tl,total,[(wav,V0,1.0)])


# ---------- voci concatenate (spiegone, glossario, mappa, compiti) ----------
def concat_voci(nome,parti,gap=0.45):
    """crea la voce unica `nome` unendo le voci in `parti`; ritorna (wav,durata,offsets)"""
    TESTI[nome]=' '.join(TESTI[p] for p in parti)
    ws=[voce(p) for p in parti]; offs=[]; t=0
    for w,d,_ in ws: offs.append(t); t+=d+gap
    out=f'{VOX}/cc_{nome}_{"real" if all(os.path.exists(f"/home/user/Lezioni/scambio/storia-arte-V-lez08/vox/{p}.wav") for p in parti) else "prov"}.wav'
    ins=[]; fl=[]
    for k,(w,d,_) in enumerate(ws): ins+=['-i',w]; fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,apad=pad_dur={gap}[x{k}]')
    fc=';'.join(fl)+';'+''.join(f'[x{k}]' for k in range(len(ws)))+f'concat=n={len(ws)}:v=0:a=1[o]'
    r=sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc,'-map','[o]','-c:a','pcm_s16le',out])
    if r.returncode: raise SystemExit(r.stderr)
    return out,t,offs
_voce_orig=voce
def voce(nome):
    if nome in CONC: return CONC[nome]
    return _voce_orig(nome)
CONC={}
def registra_concat(nome,parti):
    CONC[nome]=None; CONC.pop(nome)
    r=concat_voci(nome,parti); CONC[nome]=(r[0],r[1],None); return r
# ---------- introduzione animata: copertina + presentazione degli argomenti (niente riquadro del prof) ----------
def intro_anim(_=0):
    nome='A0_COPERTINA'; wav,d,_=voce(nome); V0=0.9
    T=tempi_marcatori(nome,['primo','secondo','terzo','quarto','quinto','sesto'])
    L=[f"{esc(ARG[k])}" for k in range(1,7)]
    man=[]
    cov=dark_html('<div class="k" style="top:300px">Storia dell\'arte · Videolezione</div><div class="h" style="top:370px;font-size:170px">'+esc(TITOLO)+'</div>')
    open(f'{B}/in_c.html','w').write(cov); man.append({'html':f'{B}/in_c.html','out':f'{B}/in_c.png','transparent':True})
    for k in range(-1,6):
        open(f'{B}/in_{k}.html','w').write(lines_html("Argomenti",TITOLO,L,k,top=330,step=102,fs=46)); man.append({'html':f'{B}/in_{k}.html','out':f'{B}/in_{k}.png','transparent':True})
    shots(man); total=V0+d+1.5
    tl=[(0,Dark(f'{B}/in_c.png',0))]
    st=V0+T[0]-0.8; tl.append((st,Dark(f'{B}/in_-1.png',st)))
    for k in range(6): s=V0+T[k]; tl.append((s,Dark(f'{B}/in_{k}.png',s)))
    return emit('intro',tl,total,[(wav,V0,1.0)])
# ---------- spiegone d'apertura della Parte 2 ----------
def spiegone(_=0):
    wav,d,offs=registra_concat('S_SPIEGONE',['S_SPIEGONE_1','S_SPIEGONE_2']); V0=0.6; total=d+1.6
    beats=[(None,('panel',"Ripasso","tutto quello che abbiamo visto nella Parte precedente"),None),
     ('sessantasette',('panel',"67 milioni","di abitanti: l'Impero tedesco"),"L'Impero tedesco e la metropoli"),
     ('agorafobia',('panel',"Agorafobia","paura delle folle e degli spazi aperti"),"Disagio, alienazione, agorafobia"),
     ('freud',('panel',"Freud e Simmel","nevrosi e solitudine dell'individuo iperstimolato"),"Freud e Georg Simmel"),
     ('millenovecentosette',('panel',"1907","nasce a Monaco il Deutscher Werkbund"),"1907: Deutscher Werkbund"),
     ('secessioni',('panel',"Le Secessioni","Monaco, Vienna, Berlino"),"Le Secessioni"),
     ('precursori',('art','bambina_malata',(0.4,0.45),(0.5,0.5)),"I precursori: Ensor e Munch"),
     ('l\'urlo',('art','urlo',(0.5,0.45),(0.5,0.5)),"Munch: L'urlo"),
     ('infine',('art','potsdamer',(0.5,0.5),(0.5,0.5)),"Die Brücke e Kirchner"),
     ('strada',('art','strada_berlino',(0.5,0.5),(0.5,0.5)),"Strada a Berlino"),
     ('cinque',('art','cinque_donne',(0.5,0.5),(0.5,0.5)),"Cinque donne per la strada")]
    marc=[b[0] for b in beats[1:]]
    T=tempi_marcatori('S_SPIEGONE',marc); times=[0.0]+[V0+t for t in T]
    man=[]; chs=[]
    for k,(m,left,chip) in enumerate(beats):
        if chip: chs.append(chip)
        body=(panel(left[1],left[2]) if left[0]=='panel' else '')+chips(chs[-4:])
        h=base("Ripasso della Parte precedente",'',None,None,False).replace('@@BODY@@',body)
        f=f'{B}/sp_{k}'; open(f+'.html','w').write(h); man.append({'html':f+'.html','out':f+'.png'})
    shots(man); tl=[]
    for k,(m,left,chip) in enumerate(beats):
        t0=times[k]; t1=times[k+1] if k+1<len(beats) else total
        if left[0]=='art': tl.append((t0,frames.Art(f'{B}/sp_{k}.png',f'{OP}/{left[1]}.png',AP_BOX,max(t1-t0,2.0)+1.5,0.2,left[2],left[3])))
        else: tl.append((t0,frames.Static(f'{B}/sp_{k}.png')))
    return emit('spiegone',tl,total,[(wav,V0,1.0)])
# ---------- glossario animato ----------
GLOS=[("Espressionismo","sposta il baricentro dall'estetica esteriore all'interiorità emotiva e spirituale"),("Secessione","gruppo di artisti dissidenti che si oppongono alle accademie ufficiali"),
 ("Agorafobia","la paura delle folle e degli spazi aperti"),("Designer","figura intellettuale che progetta oggetti in serie, distinta dall'artigiano esecutore"),
 ("Deutscher Werkbund","associazione nata a Monaco nel 1907 per unire arte e industria"),("Die Brücke (il ponte)","gruppo fondato a Dresda nel 1905"),
 ("Der Blaue Reiter (il Cavaliere Azzurro)","gruppo fondato a Monaco nel 1911, orientato verso l'astrazione"),("Astrattismo","elementi figurativi che cedono il passo a macchie e linee pure"),
 ("Primitivismo","riscoperta dell'arte primitiva africana e oceanica"),("Iperstimolazione","eccesso di stimoli della vita metropolitana, che schiaccia l'individualità")]
def glossario(_=0):
    wav,d,offs=registra_concat('G_GLOSSARIO',['G_GLOSSARIO_1','G_GLOSSARIO_2']); V0=0.8; total=V0+d+1.6
    marc=['espressionismo','secessione','agorafobia','designer','deutscher','die','der','astrattismo','primitivismo','iperstimolazione']
    # il primo marcatore ('espressionismo') e' la prima occorrenza dopo 'il glossario della lezione'
    T=tempi_marcatori('G_GLOSSARIO',marc); man=[]; tl=[]
    def pagina(active):
        lines=[f'<b>{esc(t)}</b> · {esc(x)}' for t,x in GLOS]
        return lines
    for k in range(-1,10):
        pg=0 if k<5 else 1; sub=GLOS[pg*5:pg*5+5]; act=k-pg*5 if k>=0 else -1
        lines=[f'<b>{esc(t)}</b> · {esc(x)}' for t,x in sub]
        open(f'{B}/gl_{k}.html','w').write(lines_html("Glossario",f"Glossario · {pg+1} di 2",lines,act,top=270,step=150,fs=40)); man.append({'html':f'{B}/gl_{k}.html','out':f'{B}/gl_{k}.png','transparent':True})
    shots(man); tl.append((0,Dark(f'{B}/gl_-1.png',0)))
    for k in range(10): s=V0+T[k]; tl.append((s,Dark(f'{B}/gl_{k}.png',s)))
    return emit('glossario',tl,total,[(f'{SU}/repaso.wav',0.0,0.7),(wav,V0+0.0,1.0)] if False else [(wav,V0,1.0)])
# ---------- ripasso finale ----------
RIP=[ "L'Impero tedesco e la metropoli: disagio, alienazione, agorafobia","Le Secessioni: dalla estetica esteriore all'interiorità","Ensor e Munch: precursori della pittura dell'angoscia","Die Brücke e Kirchner: la nevrosi urbana di Berlino","Der Blaue Reiter: colore, spiritualità, astrattismo","Vienna: Kokoschka e Schiele, tormento e introspezione"]
def ripasso_finale(_=0):
    nome='R_RIPASSO_FINALE'; wav,d,_=voce(nome); V0=3.3
    T=tempi_marcatori(nome,['primo','secondo','terzo','quarto','quinto','sesto']); man=[]
    for k in range(-1,6):
        open(f'{B}/rf_{k}.html','w').write(lines_html("Ripasso finale","Argomento per argomento",RIP,k,top=300,step=115,fs=42)); man.append({'html':f'{B}/rf_{k}.html','out':f'{B}/rf_{k}.png','transparent':True})
    shots(man); total=V0+d+1.5; tl=[(0,Dark(f'{B}/rf_-1.png',0))]
    for k in range(6): s=V0+T[k]; tl.append((s,Dark(f'{B}/rf_{k}.png',s)))
    return emit('ripasso',tl,total,[(f'{SU}/repaso.wav',0.0,0.8),(wav,V0,1.0)])
# ---------- verifica di sbarramento e compiti ----------
def verifica(_=0):
    h=dark_html('<div class="k" style="top:290px">Per proseguire</div><div class="h" style="top:360px;font-size:130px">Verifica finale</div><div class="h" style="top:560px;font-size:52px;font-weight:700">10 domande · serve almeno l\'80% per superarla</div>')
    open(f'{B}/ve.html','w').write(h); shots([{'html':f'{B}/ve.html','out':f'{B}/ve.png','transparent':True}])
    return emit('verifica',[(0,Dark(f'{B}/ve.png'))],4.6,[(f'{SU}/quiz.wav',0.5,0.8)])
def compiti_intro(_=0):
    h=dark_html('<div class="h" style="top:380px;font-size:170px">Compiti</div>')
    open(f'{B}/ci.html','w').write(h); shots([{'html':f'{B}/ci.html','out':f'{B}/ci.png','transparent':True}])
    return emit('compiti_intro',[(0,Dark(f'{B}/ci.png'))],3.6,[(f'{SU}/titolo.wav',0.0,0.8)])
COMP=["Quali contraddizioni sociali e psicologiche caratterizzano la metropoli moderna all'inizio del Novecento e in che modo pensatori come Sigmund Freud e Georg Simmel analizzano le nuove nevrosi urbane come l'agorafobia e l'iperstimolazione dell'individuo?",
"Come nasce la figura moderna del designer in risposta alle esigenze dell'industria e quali obiettivi si pone il Deutscher Werkbund fondato a Monaco nel 1907?",
"Qual è il contributo dei precursori James Ensor ed Edvard Munch allo sviluppo di una pittura incentrata sull'angoscia e sull'interiorità, e quali differenze stilistiche e tematiche distinguono i due principali gruppi espressionisti tedeschi, Die Brücke e Der Blaue Reiter?",
"Quali sono le caratteristiche specifiche dell'Espressionismo austriaco rispetto a quello tedesco e in che modo Oskar Kokoschka ed Egon Schiele esprimono il tormento interiore e l'introspezione psicologica nelle loro opere?"]
def compiti(_=0):
    wav,d,_=voce('COMPITI'); V0=0.6
    T=tempi_marcatori('COMPITI',['prima','seconda','terza','quarta','svolgi']); man=[]
    for k in range(-1,5):
        if k<4:
            body=f'<div class="k" style="top:70px">Compiti</div><div class="h" style="top:120px;font-size:60px">{"Domanda "+str(k+1)+" di 4" if k>=0 else "Leggi e svolgi i compiti"}</div>'
            if k>=0: body+=f'<div class="ln on" style="top:230px;left:120px;right:120px;font-size:46px;line-height:1.28"><span class="d"></span>{esc(COMP[k])}</div>'
        else:
            body='<div class="k" style="top:360px">Compiti</div><div class="h" style="top:430px;font-size:76px">Svolgi i compiti qui sotto e premi «Consegna»</div><div class="h" style="top:640px;font-size:46px;font-weight:700">Arrivano al docente nel tuo quaderno dei compiti</div>'
        open(f'{B}/co_{k}.html','w').write(dark_html(body)); man.append({'html':f'{B}/co_{k}.html','out':f'{B}/co_{k}.png','transparent':True})
    shots(man); total=V0+d+1.5; tl=[(0,Dark(f'{B}/co_-1.png',0))]
    for k in range(5): s=V0+T[k]; tl.append((s,Dark(f'{B}/co_{min(k,4)}.png',s)))
    return emit('compiti',tl,total,[(wav,V0,1.0)])


def fine_parte1(_=0):
    h=dark_html('<div class="k" style="top:360px">Fine della Parte 1</div><div class="h" style="top:430px;font-size:90px">Continua nella Parte 2</div>')
    open(f'{B}/f1.html','w').write(h); shots([{'html':f'{B}/f1.html','out':f'{B}/f1.png','transparent':True}])
    return emit('fine1',[(0,Dark(f'{B}/f1.png'))],4.5,[(f'{SU}/finale.wav',0.0,0.7)])

if __name__=='__main__':
    which=sys.argv[1]; args=[int(x) for x in sys.argv[2:]]
    for n in args: print(globals()[which](n),flush=True)

