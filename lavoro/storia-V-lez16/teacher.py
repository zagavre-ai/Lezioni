from pieces import *
def kw_of(a):return a['kw']
def build_teacher(ch,prev_png,numbering):
    nome=ch['nome'];out=f'{OUT}/{nome}.mkv'
    rr=chunk_ranges(ch['s0'],ch['s1']);m,D=build_map(rr);nF=fr(D);Dq=nF/FPS
    states=[];a=ARGS[ch['arg']-1] if ch['arg'] else None
    if ch['arg']==0:
        p=numbering('cover');states=[(0,png(cover(["Gli anni Sessanta","tra crisi e progressi"],[x['nome'] for x in ARGS],True,p),'cover_t'))]
    else:
        lastw=None;pn=None;eb=f"{a['n']:02d} · {a['nome']}"
        tl=2 if len(a['tit'])>48 else 1
        for v in ch['views']:
            f0=fr(to_edit(m,v[1]) if v[1]>0 else 0)
            if v[0]=='c':
                win=tuple(v[2])
                if win!=lastw:pn=numbering(('p',nome,win));lastw=win
                cards=[a['cards'][i] for i in win]
                lit=None if v[3] is None else win.index(v[3])
                html=slide(eb,a['tit'],cards,lit,pn,a['kw'],tl=tl)
            else:
                im=IMG[v[2]];pn=numbering(('img',v[2]));lastw=None
                html=image_slide(eb,im['tit'],f"{B}/img/{im['f']}",pn,a['kw'],tl=2 if len(im['tit'])>48 else 1)
            states.append((f0,png(html,f"s{a['n']}")))
    flush()
    sa,sf,sm=still_inputs(states,nF)
    fc=[sf];n=len(rr)
    inp=sa+['-i',SND+'trans.wav'];k=sm+1
    prevk=None
    if prev_png:
        inp+=['-loop','1','-t','0.4','-i',prev_png];prevk=k;k+=1
    vk=[];ak=[]
    for (x,y) in rr:
        inp+=['-ss',f'{x:.4f}','-t',f'{y-x:.4f}','-i',W+'/orig.mp4'];vk.append(k);k+=1
        inp+=['-ss',f'{x:.4f}','-t',f'{y-x:.4f}','-i',W+'/aud/prof_clean.wav'];ak.append(k);k+=1
    for i,(x,y) in enumerate(rr):
        fc.append(f"[{vk[i]}:v]setpts=PTS-STARTPTS,crop={CAM[2]}:{CAM[3]}:{CAM[0]}:{CAM[1]},scale=412:309:flags=lanczos[c{i}]")
        fc.append(f"[{ak[i]}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={y-x-0.015:.4f}:d=0.015[a{i}]")
    fc.append(''.join(f"[c{i}]" for i in range(n))+f"concat=n={n}:v=1:a=0,fps=30,trim=end_frame={nF}[cam]")
    fc.append(''.join(f"[a{i}]" for i in range(n))+f"concat=n={n}:v=0:a=1,pan=stereo|c0=c0|c1=c0[pa]")
    fc.append("[bg][cam]overlay=1428:148:shortest=0:eof_action=pass[vbase]")
    fc.append(f"[{sm}:a]volume=1.0[tr];[pa][tr]amix=inputs=2:normalize=0:duration=first[am]")
    if prev_png:fc.append(trans_filter(str(prevk),'vout'));vmap='[vout]'
    else:vmap='[vbase]'
    cmd=['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map',vmap,'-map','[am]','-t',f'{Dq:.4f}']+V_ENC+A_ENC+[out]
    sh(cmd);return out,Dq
if __name__=='__main__':
    import sys
    cnt={'n':0,'k':{}}
    def numbering(k):
        if k not in cnt['k']:cnt['n']+=1;cnt['k'][k]=cnt['n']
        return cnt['k'][k]
    ch=[c for c in CH if c['nome']==sys.argv[1]][0]
    o,d=build_teacher(ch,None,numbering);print(o,d,dur(o),nframes(o))
