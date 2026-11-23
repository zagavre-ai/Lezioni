# Master → chat: aggiunge un messaggio in scambio/<tag>/DALLA_MASTER.txt nel ramo voci-<tag> di ogni chat (o di quelle indicate).
# uso: python3 scrivi_alle_chat.py "testo" [tag1 tag2 ...]
import subprocess,sys,os,shutil,time
R=os.environ.get('REPO',os.getcwd());msg=sys.argv[1];only=sys.argv[2:]
sh=lambda c:subprocess.run(c,shell=True,cwd=R,capture_output=True,text=True)
for l in sh('git ls-remote origin "refs/heads/voci-*"').stdout.split('\n'):
    if not l.strip():continue
    b=l.split('refs/heads/')[1];tag=b[5:]
    if only and tag not in only:continue
    wt=f'/tmp/wt_msg_{tag}';shutil.rmtree(wt,ignore_errors=True);sh('git worktree prune')
    sh(f'git fetch -q origin {b}:refs/remotes/origin/{b} --force');sh(f'git worktree add -q -f {wt} origin/{b}')
    d=f'{wt}/scambio/{tag}';os.makedirs(d,exist_ok=True);f=d+'/DALLA_MASTER.txt'
    old=open(f).read() if os.path.exists(f) else ''
    open(f,'w').write(f"[{time.strftime('%d/%m %H:%M')}] {msg}\n\n"+old)
    r=subprocess.run(f'git add -f scambio && git commit -qm "messaggio dalla master" && git push -q origin HEAD:refs/heads/{b}',shell=True,cwd=wt,capture_output=True,text=True)
    sh(f'git worktree remove --force {wt}');print(tag,'ok' if r.returncode==0 else r.stderr[-150:])
