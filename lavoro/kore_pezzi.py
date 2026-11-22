# Tutti i pezzi con voce Kore (o provvisoria) e le schede blu. Uso: python3 kore_pezzi.py [nome ...]  (senza argomenti: tutti)
import sys, os, re, json, subprocess, hashlib
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import tlib, kore, mappe, struttura as S, mont
from kore import vox, tempi_unita, digits, scena, TESTI
from mont import sh, B, dur
SND='/home/user/Lezioni/kit/suoni/'
IMGS={'stemma':'/tmp/w/hr/s-004.png','parata':'/tmp/w/hr/s-007.png','poster':'/tmp/w/hr/s-009.png','goebbels':'/tmp/w/hr/s-012.png'}
TIT={a['n']:a['titolo'] for a in S.ARG}
import pagine as PG
PN=PG.numera()
os.makedirs(f'{B}/k',exist_ok=True);os.makedirs('/tmp/w/kh',exist_ok=True)
QUEUE=[]
def png(key,html,omit=False):
    h=hashlib.md5((html+str(omit)).encode()).hexdigest()[:10];p=f'/tmp/w/kh/{key}_{h}.png'
    if not os.path.exists(p):
        hp=p[:-4]+'.html';open(hp,'w').write(html);QUEUE.append(dict(html=hp,png=p,omit=omit))
    return p
def flush():
    if QUEUE:
        json.dump(QUEUE,open('/tmp/w/kq.json','w'));sh(['node','/home/user/Lezioni/lavoro/shot.js','/tmp/w/kq.json']);QUEUE.clear()
def frasi(t): return [x for x in re.split(r'(?<=[.?!])\s+',t.strip()) if x]
def loud_gain(wav):
    """guadagno (dB) per portare la voce a -16 LUFS; 0 per le provvisorie silenziose"""
    r=sh(['ffmpeg','-v','info','-i',wav,'-af','ebur128','-f','null','-'],check=False).stderr
    m=re.findall(r'I:\s+(-?[\d.]+) LUFS',r)
    if not m: return 0.0
    v=float(m[-1]);return 0.0 if v<-60 else max(-20,min(20,-16-v))
def concat_voci(nomi,gap,out):
    """voci in fila con pause; ritorna (inizi, durata)"""
    import wave,numpy as np
    parts=[];t=0;starts=[]
    for nm in nomi:
        w,_=vox(nm);d,sr=kore._read(w);d=d*10**(loud_gain(w)/20) if _ else d
        starts.append(t);parts.append(d);parts.append(np.zeros(int(gap*sr),np.float32));t+=len(d)/sr+gap
    x=np.concatenate(parts[:-1]) if parts else np.zeros(1)
    import soundfile as sf
    sf.write(out,x,24000,subtype='PCM_16');return starts,len(x)/24000
def jingle(name,start,tot,vol=1.0):
    return (SND+name,start,vol)
def mix_audio(parti,tot,out):
    """parti: [(wav, inizio_s, volume_lineare)] -> wav 48k mono lungo `tot`"""
    ins=[];fc=[]
    for i,(w,t,v) in enumerate(parti):
        ins+=['-i',w];fc.append(f'[{i}:a]aresample=48000,aformat=channel_layouts=mono,adelay={int(t*1000)},volume={v}[a{i}]')
    fc.append(''.join(f'[a{i}]' for i in range(len(parti)))+f'amix=inputs={len(parti)}:duration=longest:normalize=0,apad=whole_dur={tot:.3f},atrim=0:{tot:.3f}[o]')
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc),'-map','[o]','-c:a','pcm_s16le','-ar','48000',out]);return out
def gradient(tot,out):
    if not os.path.exists(out) or dur(out)<tot-0.05:
        sh(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'gradients=s=1920x1080:c0=0B1530:c1=1B3A7A:c2=0B1530:c3=2060AF:nb_colors=4:speed=0.015:rate=30:d={tot:.3f}','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30',out])
    return out
def pezzo_blu(nome,label,titolo,sotto,audio_parti,tot):
    """scheda blu animata (fondo sfumato che si muove) con testo che entra in dissolvenza; audio_parti: [(wav,t,vol)]"""
    p=png(nome,tlib.blu(label,titolo,sotto),omit=True);flush()
    D=round(tot*30)/30;g=gradient(D+0.1,f'{B}/k/grad_{int(D*30)}.mp4')
    au=mix_audio(audio_parti,D,f'{B}/k/{nome}_a.wav') if audio_parti else None
    out=f'{B}/k/{nome}.mkv'
    ins=['-i',g,'-loop','1','-framerate','30','-t',f'{D:.3f}','-i',p]
    fc=f"[1:v]format=rgba,fade=in:st=0.15:d=0.5:alpha=1[t];[0:v][t]overlay=0:0:format=auto,format=yuv420p,trim=0:{D:.3f}[v]"
    m=['-map','[v]']
    if au: ins+=['-i',au];m+=['-map','2:a']
    else:
        ins+=['-f','lavfi','-t',f'{D:.3f}','-i','anullsrc=r=48000:cl=mono'];m+=['-map','2:a']
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc]+m+['-frames:v',str(round(D*30)),'-r','30','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000',out]);return out
def prep_voce(nome,out):
    """voce normalizzata a -16 LUFS, con dissolvenze di 30 ms (nessuna voce troncata)"""
    w,real=vox(nome);g=loud_gain(w) if real else 0.0;d=dur(w)
    sh(['ffmpeg','-v','error','-y','-i',w,'-af',f'volume={g}dB,afade=t=in:st=0:d=0.03,afade=t=out:st={max(0,d-0.04):.3f}:d=0.04','-ar','24000','-c:a','pcm_s16le',out]);return out,d,real
# ---------------- pezzi ----------------
def T_n(n): return pezzo_blu(f'T{n}',f'ARGOMENTO {n}',TIT[n],None,[(SND+'titolo.wav',0.2,1.0)],4.0)
def Q_n(n):
    return pezzo_blu(f'Q{n}','QUIZ',f'Quiz · {TIT[n]}',"5 domande · per continuare serve almeno l'80%",[(SND+'quiz.wav',0.5,1.0)],5.0)
def PI_n(n):
    nm='P4_R2' if n==4 else f'P{n}';w,d,_=prep_voce(nm,f'{B}/k/{nm}_n.wav')
    return pezzo_blu(f'PI{n}','RIPASSO',TIT[n],'Guarda lo schema e ripeti ad alta voce',[(SND+'repaso.wav',0.0,0.55),(w,1.2,1.0)],max(3.4,1.2+d+0.7))
SCN={1:5,2:4,3:5,4:5,5:4,6:5,7:6,8:4}
def righe_schema(n):
    out=[]
    for k in range(1,SCN[n]+1):
        nm=f'SC{n}_{k}'
        if nm+'_R2' in TESTI: nm+='_R2'
        out.append(nm)
    return out
def PS_n(n):
    nomi=righe_schema(n);gap=0.7
    # normalizza ogni riga
    preps=[prep_voce(nm,f'{B}/k/{nm}_n.wav') for nm in nomi]
    import soundfile as sf,numpy as np
    parts=[];starts=[];t=0
    for (w,d,real) in preps:
        x,sr=sf.read(w);starts.append(t);parts.append(x);parts.append(np.zeros(int(gap*sr)));t+=len(x)/sr+gap
    x=np.concatenate(parts[:-1]);a=f'{B}/k/PS{n}_voce.wav';sf.write(a,x,24000,subtype='PCM_16');tot=len(x)/24000
    cards=[dict(lead=None,testo=digits(TESTI[nm])) for nm in nomi]
    # lead = parte prima dei due punti, in grassetto
    for c in cards:
        if ':' in c['testo'][:40]: c['lead']=c['testo'].split(':')[0]+':'
    stati=[]
    h,_=tlib.scheda_cards(f'RIPASSO · {n}',TIT[n],PN[f'PS{n}'],cards,None,'');stati.append((0.0,png(f'PS{n}_x',h)))
    for i in range(len(cards)):
        h,_=tlib.scheda_cards(f'RIPASSO · {n}',TIT[n],PN[f'PS{n}'],cards,i,'');stati.append((starts[i],png(f'PS{n}_{i}',h)))
    flush()
    return scena(f'PS{n}',stati,a,tot+1.0,f'{B}/k/PS{n}.mkv',lead=0.5,tail=0.9)
def unita_card_scene(nome,voce,label,titolo,cards,units_all,side_fn=None,tot_extra=0.8,skip=0,pag=None):
    """scena generica: cards lit con la voce; units_for_cards = testi delle unità lette (stessa lunghezza di cards)"""
    w,d,real=prep_voce(voce,f'{B}/k/{voce}_n.wav')
    # tempi: unità = frasi in lettura; tempi_unita lavora sulla voce originale (stessa durata)
    starts,dd=tempi_unita(voce,units_all)
    stati=[];h,_=tlib.scheda_cards(label,titolo,pag,cards,None,side_fn(None) if side_fn else '');stati.append((0.0,png(nome+'_x',h)))
    for i in range(len(cards)):
        h,_=tlib.scheda_cards(label,titolo,pag,cards,i,side_fn(i) if side_fn else '');stati.append((starts[i+skip],png(f'{nome}_{i}',h)))
    flush()
    return scena(nome,stati,w,dd+tot_extra,f'{B}/k/{nome}.mkv',lead=0.6,tail=0.9)
AP_SIDE={3:('stemma','Lo stemma nazista'),5:('poster','Un poster di propaganda nazista'),7:('goebbels','Joseph Goebbels')}
def AP_n(n):
    t=TESTI[f'AP{n}'];fs=frasi(t);q=fs[0];corpo=fs[1:]
    cards=[dict(lead=None,testo=digits(f)) for f in corpo]
    years=[re.findall(r'\b(1[89]\d\d)\b',c['testo']) for c in cards]
    def side(i):
        if n in AP_SIDE: k,cap=AP_SIDE[n];return tlib.side_img(IMGS[k],cap)
        if i is None: return ''
        last=''
        for j in range(i+1):
            if years[j]: last=years[j][0]
        return tlib.side_chip(last) if last else ''
    return unita_card_scene(f'AP{n}',f'AP{n}',f'APPROFONDIMENTO · {n}',digits(q),cards,[q]+corpo,side,skip=1,pag=PN[f'AP{n}'])
def GL_n(parte):
    nm='GL1' if parte==1 else 'GL2';fs=frasi(TESTI[nm]);corpo=fs[1:]
    cards=[]
    for f in corpo:
        lead=f.split(':')[0]+':' if ':' in f else None
        cards.append(dict(lead=lead,testo=digits(f)))
    return unita_card_scene(f'GL{parte}',nm,'GLOSSARIO','Parole chiave',cards,fs,None,skip=1,pag=PN[f'GL{parte}'])
def RIEP_n(parte):
    nm='RF1_R2' if parte==1 else 'RF2';fs=frasi(TESTI[nm]);corpo=fs[1:]
    cards=[]
    for f in corpo:
        lead=f.split(':')[0]+':' if re.match(r'^(Primo|Secondo|Terzo|Quarto):',f) else None
        cards.append(dict(lead=lead,testo=digits(f)))
    return unita_card_scene(f'RIEP{parte}',nm,'RIPASSO FINALE','Ripasso finale',cards,fs,None,skip=1,pag=PN[f'RIEP{parte}'])
def COVERV(parte):
    args=[(a['n'],a['titolo']) for a in S.ARG if a['n'] in (S.PARTE1 if parte==1 else S.PARTE2)]
    p=png(f'cover{parte}',tlib.copertina('La Germania da Weimar al nazismo',args,False,parte if parte==2 else None))
    flush();nm='BENV' if parte==1 else 'BENV2'
    w,d,_=prep_voce(nm,f'{B}/k/{nm}_n.wav')
    return scena(f'COVERV{parte}',[(0.0,p)],w,d,f'{B}/k/COVERV{parte}.mkv',lead=0.7,tail=1.0)
def MAP_n(k):
    nm=f'M{k}';voce=f'MAP{k}N'
    M=mappe.MAPPE[nm];fs=frasi(TESTI[voce])
    U={1:["Quali sono il programma e la struttura del Partito nazista?","Il partito nazista","sostiene un'ideologia,","basata su: l'idea di popolo,","il nazionalismo,","l'antisemitismo","e l'antibolscevismo.","Si dota di squadre armate,","che sono le squadre d'assalto, cioè le SA,","e le squadre di protezione, cioè le SS.","Trova in Hitler","un oratore trascinante","e un leader indiscusso."],
       2:["Come giunge al potere Hitler?","La crisi del millenovecentoventinove","favorisce il successo elettorale dei nazisti.","Questo porta a Hitler cancelliere, il trenta gennaio millenovecentotrentatré.","Hitler cancelliere decreta l'emergenza","e chiede e ottiene i pieni poteri."],
       3:["Come funziona il regime nazista?","Il regime nazista","si dota di strumenti di repressione, come","la Gestapo, cioè la polizia segreta,","il Tribunale del popolo","e i campi di concentramento.","Cerca il consenso attraverso","la Forza attraverso la gioia,","la Gioventù hitleriana","e gli spettacoli di massa, cioè i raduni.","In economia","pratica un massiccio intervento dello Stato,","con lo scopo di potenziare l'esercito."]}[k]
    w,d,real=prep_voce(voce,f'{B}/k/{voce}_n.wav')
    starts,dd=tempi_unita(voce,U)
    stati=[(0.0,png(f'map{k}_t',mappe.stato_html(nm,-1)))]
    # stato 0: solo titolo e legenda (nessun riquadro)
    base=mappe.stato_html(nm,0)
    for i in range(len(M['ordine'])):
        stati.append((max(0.0,starts[i+1]-0.1),png(f'map{k}_{i}',mappe.stato_html(nm,i))))
    fin=png(f'map{k}_fin',mappe.stato_html(nm,None,True))
    tfin=dd+0.5;stati.append((tfin,fin))
    flush()
    return scena(f'MAP{k}',stati,w,tfin+4.0,f'{B}/k/MAP{k}.mkv',lead=0.6,tail=0.5)
def SPG2():
    nm='SPG2';fs=frasi(TESTI[nm]);corpo=fs[1:]
    cards=[dict(lead=(f.split(':')[0]+':') if re.match(r'^(Primo|Secondo|Terzo|Quarto) argomento:',f) else None,testo=digits(f)) for f in corpo]
    w,d,real=prep_voce(nm,f'{B}/k/{nm}_n.wav');starts,dd=tempi_unita(nm,fs)
    imap=[i for i,c in enumerate(corpo) if 'mappa del partito' in c.lower()]
    st=[]
    def side(i):
        if i is None: return ''
        t=corpo[i]
        if 'NSDAP' in t or 'nazionalsocialista' in t: return tlib.side_img(IMGS['stemma'],'Lo stemma nazista')
        return ''
    h,_=tlib.scheda_cards('RIPASSO DELLA PARTE PRECEDENTE','Che cosa abbiamo visto',PN["('spg', 2)"],cards,None,'');st.append((0.0,png('spg_x',h)))
    for i in range(len(cards)):
        if i in imap:
            st.append((starts[i+1],png('spg_map',mappe.stato_html('M1',None,True))))
        else:
            h,_=tlib.scheda_cards('RIPASSO DELLA PARTE PRECEDENTE','Che cosa abbiamo visto',PN["('spg', 2)"],cards,i,side(i));st.append((starts[i+1],png(f'spg_{i}',h)))
    flush()
    return scena(nm,st,w,dd+0.8,f'{B}/k/{nm}.mkv',lead=0.6,tail=0.9)
def FIN_blu(parte):
    nm='FIN1' if parte==1 else 'FIN2';w,d,_=prep_voce(nm,f'{B}/k/{nm}_n.wav')
    lab='FINE DELLA PARTE' if parte==1 else 'FINE DELLA LEZIONE'
    tit='Fine della prima parte' if parte==1 else 'La lezione è finita'
    return pezzo_blu(f'FIN{parte}',lab,tit,None,[(SND+'finale.wav',0.0,0.5),(w,0.8,1.0)],max(3.0,0.8+d+0.8))
def VER():
    w,d,_=prep_voce('VER',f'{B}/k/VER_n.wav')
    return pezzo_blu('VER','VERIFICA FINALE','Verifica finale',"10 domande · per superarla serve almeno l'80%",[(SND+'quiz.wav',0.5,1.0),(w,1.0,1.0)],max(5.0,1.0+d+0.9))
def CINTRO():
    w,d,_=prep_voce('CINTRO',f'{B}/k/CINTRO_n.wav')
    return pezzo_blu('CINTRO','FINE LEZIONE','Compiti',None,[(SND+'titolo.wav',0.2,1.0),(w,0.8,1.0)],3.5)
COMP=[('C1',"Quali accordi internazionali e quali indicatori economici caratterizzarono il periodo di ripresa e stabilizzazione della Repubblica di Weimar nella seconda metà degli anni Venti?"),
 ('C2',"Quali conseguenze sociali ed economiche ebbe il crollo di Wall Street del 1929 sulla Germania e in che modo favorì l'ascesa politica di Adolf Hitler e del Partito Nazista fino alla nomina a Cancelliere?"),
 ('C3',"Attraverso quali passaggi legislativi ed episodi di violenza politica Hitler trasformò la Germania in uno Stato totalitario tra il 1933 e il 1934?"),
 ('C4','In cosa consistette il processo di "nazificazione" della società tedesca e quali provvedimenti caratterizzarono le politiche razziste, antisemite ed economiche del regime?')]
def COMPITO(k):
    nm,testo=COMP[k-1];w,d,_=prep_voce(nm,f'{B}/k/{nm}_n.wav')
    cards=[dict(lead=f'Compito {k}',testo=f'Compito {k}: '+testo)]
    h,_=tlib.scheda_cards('COMPITI',f'Compito {k} di 4',PN[f'COMPITO{k}'],cards,0,'')
    p=png(f'comp{k}',h);flush()
    return scena(f'COMPITO{k}',[(0.0,p)],w,d+max(3.0,len(testo)/14),f'{B}/k/COMPITO{k}.mkv',lead=0.7,tail=1.0)
def notice_png():
    t="© Centro Studi Telesio. Tutti i contenuti riprodotti in questa videolezione (testi, grafiche, animazioni, voci e registrazioni) sono di proprietà del Centro Studi Telesio. È vietata la riproduzione, anche parziale, senza autorizzazione scritta."
    h=f'<!doctype html><html><head><meta charset="utf-8"><style>{tlib.BASE_CSS}html,body{{background:transparent!important}}.n{{position:absolute;left:260px;width:1400px;bottom:70px;text-align:center;font:700 24px/1.4 Fig;color:#fff}}</style></head><body><div class="n">{t}</div></body></html>'
    p=png('notice',h,omit=True);flush();return p
def FINALE():
    p=notice_png();out=f'{B}/k/FINALE.mkv'
    sh(['ffmpeg','-v','error','-y','-i','/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4','-loop','1','-framerate','30','-t','5','-i',p,'-filter_complex',"[1:v]format=rgba,fade=in:st=1.0:d=0.5:alpha=1[n];[0:v][n]overlay=0:0:format=auto,format=yuv420p[v]",'-map','[v]','-map','0:a','-frames:v','150','-r','30','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000',out]);return out
def SIGLA():
    out=f'{B}/k/SIGLA.mkv'
    sh(['ffmpeg','-v','error','-y','-i','/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4','-frames:v','450','-r','30','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000',out]);return out
def D0_DI_slides():
    args1=[(a['n'],a['titolo']) for a in S.ARG if a['n'] in S.PARTE1]
    c=png('cover1_cam',tlib.copertina('La Germania da Weimar al nazismo',args1,True))
    d=png('di_cosa',tlib.di_cosa_parliamo(args1,PN["('di', 1)"],True));flush();return c,d
ALL={}
for n in range(1,9):
    ALL[f'T{n}']=lambda n=n:T_n(n);ALL[f'Q{n}']=lambda n=n:Q_n(n);ALL[f'PI{n}']=lambda n=n:PI_n(n);ALL[f'PS{n}']=lambda n=n:PS_n(n);ALL[f'AP{n}']=lambda n=n:AP_n(n)
for k in (1,2,3): ALL[f'MAP{k}']=lambda k=k:MAP_n(k)
for p in (1,2): ALL[f'GL{p}']=lambda p=p:GL_n(p);ALL[f'RIEP{p}']=lambda p=p:RIEP_n(p);ALL[f'COVERV{p}']=lambda p=p:COVERV(p);ALL[f'FIN{p}']=lambda p=p:FIN_blu(p)
ALL.update(SPG2=SPG2,VER=VER,CINTRO=CINTRO,FINALE=FINALE,SIGLA=SIGLA)
for k in (1,2,3,4): ALL[f'COMPITO{k}']=lambda k=k:COMPITO(k)
if __name__=='__main__':
    nomi=sys.argv[1:] or list(ALL)
    manifest_p=f'{B}/k/manifest.json';man=json.load(open(manifest_p)) if os.path.exists(manifest_p) else {}
    for nm in nomi:
        try:
            d=ALL[nm]();print(nm,'OK',d if isinstance(d,float) else '',flush=True)
        except SystemExit as e: print(nm,'ERRORE',str(e)[:400],flush=True)
    json.dump({'provvisorie':kore.PROV},open(f'{B}/k/prov_{"_".join(nomi[:2])}.json','w'))
