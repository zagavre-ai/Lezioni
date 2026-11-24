import sys, os, json, pickle, subprocess, re
sys.path.insert(0,'/home/claude/w/code')
from assemble import *
def load_ctx(part):
    d=pickle.load(open(f'{W}/ctx{part}.pkl','rb'))
    c=Ctx(part,None);c.clips=d['clips'];c.timeline=d['timeline'];c.dispensa=d['dispensa'];c.page=d['page'];return c
def nome_timeline(c,idx,n_counter):
    k=c['kind'];a=c['arg']
    if k=='titolo': return f'T{a}'
    if k=='prof': return f'D{a}_{n_counter}'
    if k=='quiz': return f'Q{a}'
    if k=='verifica': return 'VF'
    if k=='approfondimento': return 'AP'+str(a)+'_'+c['label'].split()[-1]
    if k=='mappa': return 'MP'+str(a if a else 'F')
    if k=='pillola': return f'RP{a}'
    if k=='copertina': return 'CO'
    if k=='sigla': return 'SG'
    return k[:2].upper()+(str(a) if a else '')
def master(ctx):
    L=[];tl=[];t=0.0;cnt={}
    for i,c in enumerate(ctx.clips):
        if i>0:
            j=junction(ctx,i);L.append(j);d=dur(j);tl.append(['TR',round(t,3),round(d,3)]);t+=d
        nm=nome_timeline(c,i,cnt.setdefault(c['arg'],0)+1)
        if c['kind']=='prof': cnt[c['arg']]+=1
        d=dur(c['path']);L.append(c['path']);tl.append([nm,round(t,3),round(d,3)]);t+=d
    lst=f'{OUTD}/part{ctx.part}.txt';open(lst,'w').write(''.join(f"file '{p}'\n" for p in L))
    m=f'{OUTD}/part{ctx.part}_master.mkv'
    r=sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',m])
    if r.returncode: raise SystemExit(r.stderr[-600:])
    return m,tl
def loud(m):
    r=sh(['ffmpeg','-v','info','-i',m,'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'])
    j=json.loads(r.stderr[r.stderr.rfind('{'):r.stderr.rfind('}')+1]);return j
def encode(m,out,crf=19):
    j=loud(m)
    af=(f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true,aresample=48000")
    r=sh(['ffmpeg','-v','error','-y','-i',m,'-c:v','libx264','-preset','veryfast','-crf',str(crf),'-r','30','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-af',af,'-movflags','+faststart',out])
    if r.returncode: raise SystemExit(r.stderr[-800:])
    return j
if __name__=='__main__':
    part=int(sys.argv[1]);crf=int(sys.argv[2]) if len(sys.argv)>2 else 19
    ctx=load_ctx(part);ctx.rend=None
    m,tl=master(ctx)
    json.dump(tl,open(f'{W}/timeline_Parte{part}.json','w'),ensure_ascii=False)
    out=f'{W}/out/Storia_Lez21_Parte{part}_1080p.mp4'
    j=encode(m,out,crf)
    print('FATTO',out,round(os.path.getsize(out)/1e6,1),'MB',j['input_i'])
