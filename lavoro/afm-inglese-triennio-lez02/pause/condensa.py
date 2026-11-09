# Taglio delle pause della docente (decisione Inglese): pause > 1,0 s portate a 0,6 s, dissolvenza 0,2 s sui tagli.
# Scrive mappa.json (pezzi tenuti), pk_c.jsonl (trascrizione sul tempo nuovo) e docente_c.mkv (webcam 412x310 + audio B).
# uso: python3 condensa.py piano | python3 condensa.py video   (riprende dai pezzi .ok)
import json,re,sys,os,subprocess
D='/home/claude/ing2/';FR=30.0
q=lambda t:round(round(t*FR)/FR,4)
END=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+'audio/audio_B_full.wav'],capture_output=True,text=True).stdout)
END=q(min(END,3283.9))
L=open(D+'audio/sil35.log').read()
S=[(float(a)-float(b),float(a)) for a,b in re.findall(r'silence_end: ([\d.]+) \| silence_duration: ([\d.]+)',L)]
W=[]
for l in open(D+'pk.jsonl'): W+=json.loads(l)['w']
WT=[t for t,_ in W]
import bisect
cuts=[];skip=0
for s,e in S:
    if e-s<=1.0: continue
    a,b=q(s+0.3),q(e-0.3)
    if s<0.5: cuts.append((0.0,q(e-0.6)));continue
    i=bisect.bisect_left(WT,s+0.25)
    if i<len(WT) and WT[i]<e-0.45: skip+=1;continue
    if b-a>=0.2: cuts.append((a,b))
cc=[]
for a,b in cuts:
    if cc and a-cc[-1][1]<0.3: cc[-1]=(cc[-1][0],b)  # pezzo tenuto troppo corto: unisco i due tagli
    else: cc.append((a,b))
cuts=cc
if END-cuts[-1][1]<0.5: END=cuts[-1][0];cuts=cuts[:-1]
K=[];p=0.0
for a,b in cuts:
    if a>0: K.append([p,a])
    p=b
K.append([p,END])
out=0.0;M=[]
for a,b in K: M.append([round(a,4),round(b,4),round(out,4)]);out+=b-a
print('pause tagliate',len(cuts),'saltate (parole dentro)',skip,'tolti %.1f s'%(END-out),'durata nuova %.1f s (%.2f min)'%(out,out/60))
json.dump({'pezzi':M,'tagli':cuts,'fine':END,'durata':round(out,4)},open(D+'mappa.json','w'))
def nuovo(t):
    j=bisect.bisect_right([m[0] for m in M],t)-1
    a,b,o=M[max(0,j)];return round(o+min(max(t-a,0),b-a),3)
with open(D+'pk_c.jsonl','w') as f:
    for l in open(D+'pk.jsonl'):
        d=json.loads(l);d['t']=nuovo(d['t']);d['e']=nuovo(d['e']);d['w']=[[nuovo(t),w] for t,w in d['w']];f.write(json.dumps(d,ensure_ascii=False)+'\n')
if len(sys.argv)>1 and sys.argv[1]=='video':
    # gruppi di ~6 minuti; il confine di gruppo cade a metà di un pezzo (riprese continue: nessuno stacco)
    P=[list(m[:2])+[False,False] for m in M]  # a,b,taglio_prima,taglio_dopo
    for k in range(len(P)):
        P[k][2]=k>0;P[k][3]=k<len(P)-1
    G=[[]];acc=0.0
    for k,pz in enumerate(P):
        a,b,tp,td=pz
        if acc+(b-a)>360 and b-a>4 and G[-1]:
            m=q((a+b)/2);G[-1].append([a,m,tp,False]);G.append([[m,b,False,td]]);acc=b-m
        else:
            G[-1].append(pz);acc+=b-a
    os.makedirs(D+'cc',exist_ok=True);X=0.1;XF=0.2
    VF="crop=1040:780:490:130,scale=412:310:flags=lanczos,normalize=blackpt=black:whitept=white:smoothing=30:independence=0.6:strength=0.6,hqdn3d=2:2:3:3,unsharp=5:5:0.6,eq=contrast=1.05:saturation=1.08:gamma=1.04,format=yuv420p"
    lista=[]
    for g,pz in enumerate(G):
        o=D+f'cc/g{g:02d}.mkv';lista.append(o)
        if os.path.exists(o+'.ok'):continue
        ex=[(a-(X if tp else 0),b+(X if td else 0)) for a,b,tp,td in pz]
        s0=max(0,ex[0][0]-2);s1=ex[-1][1]+1
        n=len(ex);fl=f'[0:v]fps=30,{VF},split={n}'+''.join(f'[v{i}]' for i in range(n))+f';[1:a]aformat=sample_rates=48000:channel_layouts=mono,asplit={n}'+''.join(f'[a{i}]' for i in range(n))
        for i,(a,b) in enumerate(ex):
            fl+=f';[v{i}]trim=start={a-s0:.4f}:end={b-s0:.4f},setpts=PTS-STARTPTS[V{i}];[a{i}]atrim=start={a-s0:.4f}:end={b-s0:.4f},asetpts=PTS-STARTPTS[A{i}]'
        lv,la,Lc='V0','A0',ex[0][1]-ex[0][0]
        for i in range(1,n):
            fl+=f';[{lv}][V{i}]xfade=transition=fade:duration={XF}:offset={Lc-XF:.4f}[xv{i}];[{la}][A{i}]acrossfade=d={XF}:c1=tri:c2=tri[xa{i}]'
            lv,la=f'xv{i}',f'xa{i}';Lc+=(ex[i][1]-ex[i][0])-XF
        tot=sum(b-a for a,b,_,_ in pz)
        subprocess.run(['ffmpeg','-v','error','-y','-ss','%.3f'%s0,'-t','%.3f'%(s1-s0),'-i',D+'orig/lez.mp4','-ss','%.3f'%s0,'-t','%.3f'%(s1-s0),'-i',D+'audio/audio_B_full.wav',
            '-filter_complex',fl,'-map',f'[{lv}]','-map',f'[{la}]','-t','%.4f'%tot,'-c:v','libx264','-preset','veryfast','-crf','14','-r','30','-c:a','pcm_s16le','-ar','48000',o],check=True)
        open(o+'.ok','w').close();print('gruppo',g,len(pz),'pezzi',round(tot,1),'s',flush=True)
    open(D+'cc/lista.txt','w').write(''.join(f"file '{x}'\n" for x in lista))
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',D+'cc/lista.txt','-c','copy',D+'docente_c.mkv'],check=True)
    print('docente_c.mkv',subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+'docente_c.mkv'],capture_output=True,text=True).stdout.strip(),'attesa',round(out,3))
