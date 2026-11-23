import subprocess,os,sys,glob
B='origin/voci-storia-arte-V-lez03';P='scambio/storia-arte-V-lez03/vox/'
subprocess.run(['git','-C','/home/user/Lezioni','fetch','-q','origin','voci-storia-arte-V-lez03'])
names=[x.split('/')[-1][:-4] for x in subprocess.run(['git','-C','/home/user/Lezioni','ls-tree','-r','--name-only',B,P],capture_output=True,text=True).stdout.split() if x.endswith('.wav')]
new=[]
for n in names:
    f=f'/tmp/w/vox/{n}.wav';blob=subprocess.run(['git','-C','/home/user/Lezioni','show',f'{B}:{P}{n}.wav'],capture_output=True).stdout
    if not os.path.exists(f) or os.path.getsize(f)!=len(blob):
        open(f,'wb').write(blob);new.append(n)
print('nuove/aggiornate:',new)
for n in new:
    if not os.path.exists(f'/tmp/w/voxasr/{n}.json'):
        subprocess.run(['python3','/home/user/Lezioni/kit/tools/trascrivi.py',f'/tmp/w/vox/{n}.wav',f'/tmp/w/voxasr/{n}'],capture_output=True)
print('trascritte')
