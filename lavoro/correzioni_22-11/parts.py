# -*- coding: utf-8 -*-
import sys, os, json, subprocess
sys.path.insert(0,'/home/work/build')
from pieces_z import *
from pieces_x import ap_piece, ripasso_piece
import assemble as AS, layout, prof, plan as PL
SND='/home/user/Lezioni/kit/suoni';SIG='/home/user/Lezioni/kit/sigle'
PARTI={1:[1,2,3],2:[4,5],3:[6,7,8]};POFF={1:0,2:3,3:5}
FIN={1:'FZ1',2:'FZ2',3:'FZ3'}
def v48(path):
    if path.startswith(SND) or '/aud/' in path: return path
    nm=os.path.basename(os.path.dirname(os.path.dirname(path)))+'_'+os.path.basename(path)
    out=f'/home/work/build/vox48/{os.path.basename(os.path.dirname(path))}_{os.path.basename(path)}'
    if not os.path.exists(out): av.wav48(path,out,loud=-16)
    return out
def ev48(evs):
    out=[]
    for e in evs:
        if e[1]=='wav' and not (e[2].startswith(SND) or '/aud/' in e[2]): out.append((e[0],'wav',v48(e[2]),'fade'))
        else: out.append(tuple(e))
    return out
def sigla_piece(which,out):
    src=f'{SIG}/Sigla_Storia_15s.mp4' if which=='in' else f'{SIG}/Sigla_finale_5s_con_avviso_diritti.mp4'
    wav=f'/home/work/build/aud/sigla_{which}.wav'
    if not os.path.exists(wav): av.sh(['ffmpeg','-y','-v','error','-i',src,'-vn','-ac','2','-ar','48000','-c:a','pcm_s16le',wav])
    if not os.path.exists(out): av.norm_encode(src,out)
    return dict(path=out,audio=[(0,'wav',wav)])
def intro_piece(out,page=1):
    a,b=prof.cut_points.__wrapped__() if hasattr(prof.cut_points,'__wrapped__') else (None,None)
    S=PL.S;a=S[0]['inizio']-0.15;b=min(S[PL.START[1]]['inizio']-0.15,S[PL.START[1]-1]['fine']+1.2)
    subs=prof.kept(a,b);N=sum(int(round((y-x)*30)) for x,y in subs) if len(subs)>1 else int(round((subs[0][1]-subs[0][0])*30))
    render([('cover_box',cover_html(1,True,page))],'/home/work/build/lit')
    av.prof_piece(subs,[('/home/work/build/lit/cover_box.png',N)],out)
    return dict(path=out,subs=subs,N=N)
def build(P,final=True):
    L,plans=layout.layout(P);O=f'/home/work/build/pieces'
    T=AS.Timeline();S=lambda f:SND+'/'+f
    def add(name,path,audio=None,**k):
        return T.add(name,path,ev48(audio or []),**k)
    # --- apertura
    s=sigla_piece('in',f'{O}/sigla_in.mp4');add('sigla',s['path'],s['audio'],tag='sigla')
    if P>1:
        sp=spiegone_piece(P,f'{O}/spiegone{P}.mp4');add('spiegone',sp['path'],sp['audio'],tag='spiegone')
    cp=cover_piece(P,f'{O}/cover{P}.mp4');add('cover',cp['path'],cp['audio'],tag='cover')
    if P==1:
        ip=intro_piece(f'{O}/intro1.mp4');add('intro',ip['path'],[(0,'prof',ip['subs'])],tag='prof')
    dp=dcp_piece(P,f'{O}/dcp{P}.mp4');add('dicosaparliamo',dp['path'],dp['audio'],tag='dcp')
    off=POFF[P]
    for pos,n in enumerate(PARTI[P],1):
        g=pos+off
        add(f'titolo{g}',f'/home/work/build/old/titolo{g}.mp4',[(0,'wav',S('titolo.wav'))],tag=f'titolo{g}')
        j=json.load(open(f'{O}/P{P}_T{n}.mp4.json'))
        add(f'prof{g}',f'{O}/P{P}_T{n}.mp4',[(0,'prof',[tuple(x) for x in j['subs']])],tag='prof',argomento=n,cut=j['cut'])
        ap=ap_piece(n,L[n]['ap']);add(f'approfondimento{g}',ap['path'],ap['audio'],tag=f'ap{g}')
        if n in layout.MAPDOPO:
            k=layout.MAPDOPO[n];mp=map_piece(k,f'{O}/map{k}.mp4',L[n]['map']);add(f'mappa{k}',mp['path'],mp['audio'],tag=f'mappa{k}')
        add(f'pillola{g}',f'/home/work/build/old/pillola{g}.mp4',[(0,'wav',S('repaso.wav')),(0.9,'wav',vpath(f'PI{n}'))],tag=f'pillola{g}')
        rp=ripasso_piece(n,L[n]['schema']);add(f'schema{g}',rp['path'],rp['audio'],tag=f'schema{g}')
        add(f'quiz{g}',f'/home/work/build/old/quiz{g}.mp4',[(0.5,'wav',S('quiz.wav'))],tag=f'quiz{g}')
    gp=gloss_piece(P,f'{O}/gloss{P}.mp4',L['gloss']);add('glossario',gp['path'],gp['audio'],tag='glossario')
    add('riepilogo',f'/home/work/build/old/riepilogo_P{P}.mp4',[(0.8,'wav',vpath(FIN[P]))],tag='riepilogo')
    if P==3:
        vp=verifica_piece(f'{O}/verifica.mp4');add('verifica',vp['path'],vp['audio'],tag='verifica')
        s2=sigla_piece('out',f'{O}/sigla_out.mp4');add('siglafinale',s2['path'],s2['audio'],tag='sigla')
        ci=compiti_intro(f'{O}/compiti_intro.mp4');add('compiti_intro',ci['path'],ci['audio'],tag='compiti')
        cm=compiti_piece(f'{O}/compiti.mp4',L['gloss']+1);add('compiti',cm['path'],cm['audio'],tag='compiti')
    else:
        s2=sigla_piece('out',f'{O}/sigla_out.mp4');add('siglafinale',s2['path'],s2['audio'],tag='sigla')
    for i in range(1,len(T.pieces)):
        if T.pieces[i]['name']!='cover' or True: T.pieces[i]['audio'].append((0,'wav',S('trans.wav')))
    return T
if __name__=='__main__':
    P=int(sys.argv[1]);T=build(P)
    json.dump([[p['name'],round(p['start']/30,3),p['n']] for p in T.pieces],open(f'/home/work/build/out_timeline_P{P}.json','w'),indent=1)
    print('durata',round(T.total_frames()/30,1),'pezzi',len(T.pieces))
    out=AS.finish(T,P,'/home/work/build/out',f'Storia_Lez17_Parte{P}_1080p');print(out)
