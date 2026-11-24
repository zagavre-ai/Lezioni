import sys,time;sys.path.insert(0,'/home/claude/w/code')
from extras import *
SIGLA='/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4';SIGF='/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4'
def sigla(ctx,fin=False):
    out=f'{OUTD}/sig{"f" if fin else "i"}.mkv'
    if not os.path.exists(out): to_clip(SIGF if fin else SIGLA,out)
    ctx.add(out,'sigla','Sigla finale' if fin else 'Sigla Storia',None)
def intro_prof(ctx,args):
    R_=ctx.rend;a0=dict(segs=[(0,17)]);B=snap(build(a0));cam,aud=extract_arg('a0',B)
    png=f'{SL}/intro.png';pg=ctx.dpage(png,'Il mondo dal 2001 ad oggi · argomenti')
    R_.load(intro_slide_html([a['tit'] for a in args],pg));R_.shot(png)
    out=f'{OUTD}/p{ctx.part}_intro.mkv'
    if not os.path.exists(out): make_piece('a0',cam,aud,0,fr(B['dur']),[(0,fr(B['dur']),png)],out)
    ctx.add(out,'prof','Introduzione del docente',0,anim=False)
def part1(r):
    ctx=Ctx(1,r);args=ARG[:3]
    sigla(ctx)
    out=f'{OUTD}/p1_cop.mkv';png=f'{SL}/cop1.png'
    if not os.path.exists(out): copertina_scene(r,1,[a['tit'] for a in args],out,png=png,voce_nome='BEN1')
    ctx.add(out,'copertina','Copertina',None,png=png,testo='Il mondo dal 2001 ad oggi')
    intro_prof(ctx,args)
    for a in args: build_arg(ctx,a)
    fine_parte(ctx,'FZ1_R3','Fine della prima parte')
    sigla(ctx,True)
    return ctx
def part2(r):
    ctx=Ctx(2,r);args=ARG[3:]
    sigla(ctx)
    spiegone(ctx)
    out=f'{OUTD}/p2_cop.mkv';png=f'{SL}/cop2.png'
    if not os.path.exists(out): copertina_scene(r,2,[a['tit'] for a in args]+['Glossario, ripasso e verifica finale'],out,png=png,voce_nome='BEN2')
    ctx.add(out,'copertina','Copertina · seconda parte',None,png=png,testo='Il mondo dal 2001 ad oggi · seconda parte')
    for a in args: build_arg(ctx,a)
    glossario(ctx,'')
    ripasso_finale(ctx)
    mappa_finale(ctx)
    verifica(ctx)
    fine_parte(ctx,'FIN1','Fine della lezione')
    sigla(ctx,True)
    compiti(ctx)
    return ctx
if __name__=='__main__':
    which=sys.argv[1];r=R();t0=time.time()
    ctx=part1(r) if which=='1' else part2(r)
    print('clips',len(ctx.clips),'durata clip',round(sum(c['dur'] for c in ctx.clips)/60,1),'min',time.time()-t0,flush=True)
    import pickle;pickle.dump(dict(clips=ctx.clips,timeline=ctx.timeline,dispensa=ctx.dispensa,page=ctx.page),open(f'{W}/ctx{which}.pkl','wb'))
    r.close()
