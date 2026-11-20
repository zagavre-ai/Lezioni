import sys,os,json,re
sys.path.insert(0,'/tmp/L18/lib')
from assemble import *
import slides
from slides import R as SR
from content5 import *
from PIL import Image
PAGES=json.load(open(ST+'/pages.json'))
S=lambda n,x,s:f'{ST}/S{n}{x}_{s}.png'
IMGp=lambda k:f'{ST}/IMG{k}_p.png'
DEF={
'D0':(0,194.4,[(0,ST+'/cover_p.png'),(96.5,ST+'/intro2_p.png')]),
'D1':(194.4,537.75,[(194.4,S(1,'a',0)),(204.3,S(1,'a',1)),(217.1,S(1,'a',2)),(282.6,S(1,'a',3)),(372.6,S(1,'b',1)),(448.4,S(1,'b',2))]),
'D2':(537.75,1048.2,[(537.75,S(2,'a',0)),(538.1,S(2,'a',1)),(664.0,S(2,'a',2)),(760.6,S(2,'b',1)),(904.4,S(2,'b',2))]),
'D3':(1048.2,1559.5,[(1048.2,S(3,'a',0)),(1091.2,S(3,'a',1)),(1232.4,S(3,'a',2)),(1331.8,S(3,'b',1)),(1402.6,S(3,'b',2)),(1549.3,IMGp('lenin'))]),
'D4':(1559.5,2107.3,[(1559.5,S(4,'a',0)),(1563.5,S(4,'a',1)),(1621.2,S(4,'a',2)),(1663.5,S(4,'a',3)),(1830.1,S(4,'b',1)),(1981.0,S(4,'b',2)),(2084.5,S(4,'b',3)),(2102.3,IMGp('trockij'))]),
'D5':(2107.3,2368.0,[(2107.3,S(5,'a',0)),(2119.2,S(5,'a',1)),(2179.4,S(5,'a',2)),(2198.0,S(5,'a',3)),(2250.0,S(5,'b',1)),(2329.0,S(5,'b',2)),(2359.4,S(5,'b',3))]),
'D6':(2368.0,2728.8,[(2368.0,S(6,'a',0)),(2374.2,S(6,'a',1)),(2460.3,S(6,'b',1)),(2610.2,S(6,'b',2))]),
'D7':(2728.8,2906.5,[(2728.8,S(7,'a',0)),(2729.2,S(7,'a',1)),(2765.7,S(7,'a',2)),(2787.7,S(7,'a',3)),(2793.6,S(7,'b',1)),(2830.0,S(7,'b',2))]),
'D8':(2906.5,3152.4,[(2906.5,S(8,'a',0)),(2926.2,S(8,'a',1)),(2944.3,S(8,'a',2)),(3003.5,S(8,'b',1)),(3081.6,S(8,'b',2)),(3121.7,S(8,'b',3))]),
'D9':(3152.4,3423.27,[(3152.4,S(9,'a',0)),(3152.7,S(9,'a',1)),(3216.4,S(9,'a',2)),(3318.9,S(9,'b',1)),(3336.3,S(9,'b',2)),(3369.5,IMGp('brest')),(3389.5,IMGp('urss'))])}
SEG=[];T0=[0.0]
def reset():SEG.clear();T0[0]=0.0
def add(name,raw,frames,aud,lastpng):
    SEG.append(dict(name=name,raw=raw,frames=frames,aud=aud,last=lastpng,start=T0[0]));T0[0]+=frames/FPS
def prevpng():return SEG[-1]['last'] if SEG else None
def card_seg(name,src,aud,d=0.3):
    out=f'{SG}/{name}.mp4'
    if prevpng():mp4_enter(src,prevpng(),out,d)
    elif not os.path.exists(out):shutil.copy(src,out)
    lp=last_png(out,f'{SG}/{name}_last.png');add(name,out,nframes(out),aud,lp)
def still_seg(name,seq,aud,cam=None,blend=9):
    out=f'{SG}/{name}.mp4';n=stills2(seq,out,prev=prevpng(),blend=blend,cam=cam) or nframes(out)
    add(name,out,n,aud,seq[-1][0])
def vdur(n):return dur(vn(n))
TR=W+'/trans_s.wav'
if not os.path.exists(TR):run(['ffmpeg','-y','-loglevel','error','-i',SND+'/trans.wav','-t','1.4','-af','afade=t=out:st=0.8:d=0.6,volume=0.5','-ac','2','-ar','48000',TR])
# profprof audio pulito
if not os.path.exists(W+'/prof_clean.wav'):
    run(['ffmpeg','-y','-loglevel','error','-i',W+'/prof5.mp4','-vn','-af',"aresample=48000,highpass=f=80,arnndn=m="+W+"/kit/home/claude/kit/02_Video/sh.rnnn,loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.89:level=false",'-ac','2','-ar','48000',W+'/prof_clean.wav'])
def dseg(name):
    a,b,ev=DEF[name];N=fr(b-a);fs=[fr(t-a) for t,_ in ev]+[N]
    p=f'{W}/pa_{name}.wav'
    if not os.path.exists(p):run(['ffmpeg','-y','-loglevel','error','-ss',f'{a:.3f}','-t',f'{N/FPS:.3f}','-i',W+'/prof_clean.wav','-ac','2','-ar','48000',p])
    seq=[(pp,fs[i+1]-fs[i]) for i,(t,pp) in enumerate(ev)]
    still_seg(name,seq,[(0,p,1.0)],cam=a)
def copyright_imgs():
    cp=ST+'/cp_white.png'
    if os.path.exists(cp):return
    r=SR();txt="© Centro Studi Telesio. Tutti i contenuti riprodotti in questa videolezione (testi, grafiche, animazioni, voci e registrazioni) sono di proprietà del Centro Studi Telesio. È vietata la riproduzione, anche parziale, senza autorizzazione scritta."
    for col,nm in (('#ffffff','cp_white'),('#5a6786','cp_slate')):
        open(W+'/html/_cp.html','w').write(f"<meta charset=utf-8><style>{slides.CSS}body{{background:transparent}}</style><div style='position:absolute;left:210px;width:1500px;top:{985 if col=='#ffffff' else 914}px;text-align:center;font-family:FG;font-size:24px;line-height:1.3;font-weight:500;color:{col}'>{txt}</div>")
        r.pg.goto('file://'+W+'/html/_cp.html');r.pg.evaluate("document.fonts.ready");r.pg.wait_for_timeout(200);r.pg.screenshot(path=f'{ST}/{nm}.png',omit_background=True)
    r.close()
    for cv in ('cover_np','cover2_np'):
        a=Image.open(f'{ST}/{cv}.png').convert('RGBA');b=Image.open(ST+'/cp_slate.png').convert('RGBA');Image.alpha_composite(a,b).convert('RGB').save(f'{ST}/{cv}_c.png')
copyright_imgs()
def head(part):
    sg=f'{SG}/SIGLA.mp4'
    if not os.path.exists(sg):
        run(['ffmpeg','-y','-loglevel','error','-i','/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4','-i',ST+'/cp_white.png','-filter_complex',"[1:v]format=rgba[c];[0:v][c]overlay=enable='between(t,13,15)',format=yuv420p[v]",'-map','[v]']+ENC+[sg+'.t.mp4']);os.rename(sg+'.t.mp4',sg)
    sa=W+'/sigla_audio.wav'
    if not os.path.exists(sa):run(['ffmpeg','-y','-loglevel','error','-i','/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4','-vn','-ac','2','-ar','48000',sa])
    add('SIGLA',sg,nframes(sg),[(0,sa,1.0)],last_png(sg,SG+'/SIGLA_last.png'))
    cv='cover_np' if part==1 else 'cover2_np';vv='B0' if part==1 else 'B2';nB=fr(0.8+vdur(vv)+0.8)
    still_seg(f'BENV{part}',[(f'{ST}/{cv}_c.png',90),(f'{ST}/{cv}.png',nB-90)],[(0.8,vn(vv),1.0),(0,TR,1.0)],blend=24)
def topic(k):
    card_seg(f'T{k}',f'{W}/cards/T{k}.mp4',[(0,SND+'/titolo.wav',1.0),(0,TR,1.0)])
    dseg(f'D{k}')
    # approfondimento
    v=f'AN{AN1[k]}';vd=vdur(v)
    if k in ANMAP:
        seq=[(f'{ST}/A{k}_0.png',fr(0.8+vd+1.0))];aud=[(0.8,vn(v),1.0)]
    else:
        st,_=align_(v) if False else __import__('align').sentence_times(vn(v),re.split(r'(?<=[.!?])\s+',TXT[v]))
        ANC=json.load(open(ST+'/anc.json'))[str(k)];cnt=[len(x) for x in ANC];idx=0;starts=[]
        for c in cnt:starts.append(st[idx][0]);idx+=c
        t0=0.8;ev=[(0,f'{ST}/A{k}_0.png')]+[(max(0.3,t0+starts[i]-0.1),f'{ST}/A{k}_{i+1}.png') for i in range(len(cnt))]
        tot=t0+vd+1.2;fs=[fr(x) for x,_ in ev]+[fr(tot)];seq=[(p,fs[i+1]-fs[i]) for i,(_,p) in enumerate(ev)];aud=[(t0,vn(v),1.0)]
    still_seg(f'AN{k}',seq,aud+[(0,TR,1.0)])
    if k in (2,4,6,8):
        m={2:1,4:2,6:3,8:4}[k];nm=f'MA{m}';st,_=align_(nm);t0=0.9;vd=vdur(nm)
        card_seg(f'MAP{m}',f'{W}/mp2/o{m}/mappa.mp4',[(t0,vn(nm),1.0),(0,TR,1.0)])
    card_seg(f'P{k}',f'{W}/cards/P{k}.mp4',[(0,SND+'/repaso.wav',1.0),(0.9,vn(f'P{k}'),1.0),(0,TR,1.0)])
    rows=len(SCH[k]);seq=[(f'{ST}/P{k}_0.png',fr(1.0))];aud=[];t=1.0
    for r_ in range(rows):
        v=vdur(f'SC{k}_{r_+1}');g=2.2 if r_<rows-1 else 0.0;seq.append((f'{ST}/P{k}_{r_+1}.png',fr(v+g)));aud.append((t+0.1,vn(f'SC{k}_{r_+1}'),1.0));t+=v+g
    seq.append((f'{ST}/P{k}_end.png',fr(2.8)))
    still_seg(f'SCH{k}',seq,aud+[(0,TR,1.0)])
    card_seg(f'Q{k}',f'{W}/cards/Q{k}.mp4',[(0.5,SND+'/quiz.wav',1.0),(0,TR,1.0)])
def gloss(gk,T,v1):
    vd=vdur(v1);ss=re.split(r'(?<=[.!?])\s+',TXT[v1]);from align import sentence_times
    c=f'{W}/al_{v1}_g.json'
    if os.path.exists(c):t,_=json.load(open(c))
    else:t,d=sentence_times(vn(v1),ss);json.dump([t,d],open(c,'w'))
    t1=1.2;ev=[(0,0)]+[(t1+t[i+1][0]-0.1,i+1) for i in range(len(T))]
    tot=t1+vd+2.0;fs=[fr(x) for x,_ in ev]+[fr(tot)]
    seq=[(f'{ST}/{gk}_{s}.png',fs[i+1]-fs[i]) for i,(_,s) in enumerate(ev)]
    still_seg(gk,seq,[(t1,vn(v1),1.0),(0,TR,1.0)])
def tail(part):
    fin='/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4';fa=W+'/fin_audio.wav'
    if not os.path.exists(fa):run(['ffmpeg','-y','-loglevel','error','-i',fin,'-vn','-ac','2','-ar','48000',fa])
    card_seg(f'FIN{part}',fin,[(0,fa,1.0),(0,SND+'/finale.wav',0.8),(0,TR,1.0)])
def save(part):
    json.dump([[s['name'],round(s['start'],3),round(s['frames']/FPS,3)] for s in SEG],open(f'{W}/timeline_P{part}.json','w'))
    json.dump(SEG,open(f'{W}/seg_P{part}.json','w'));print('Parte',part,'totale',round(T0[0],1),'s',sum(s['frames'] for s in SEG),'fotogrammi',flush=True)
if __name__=='__main__':
    part=int(sys.argv[1])
    reset();head(part)
    if part==1:
        dseg('D0')
        for k in range(1,5):topic(k)
        gloss('GL1',TERMS1,'GL1');card_seg('RIEP1',f'{W}/cards/F1.mp4',[(0.9,vn('RF1'),1.0),(0,TR,1.0)])
    else:
        card_seg('RIP',f'{W}/cards/RIP.mp4',[(0,SND+'/repaso.wav',1.0),(0.9,vn('RIP2'),1.0),(0,TR,1.0)])
        for k in range(5,10):topic(k)
        gloss('GL2',TERMS2,'GL2');card_seg('RIEP2',f'{W}/cards/F2.mp4',[(0.9,vn('RF2'),1.0),(0,TR,1.0)])
    tail(part);save(part)
