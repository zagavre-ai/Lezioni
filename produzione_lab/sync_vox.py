import sys,subprocess,os
tag,W=sys.argv[1],sys.argv[2]+'/vox/';os.makedirs(W,exist_ok=True);R='/home/user/Lezioni'
subprocess.run(['git','-C',R,'fetch','-q','origin','voci-'+tag],capture_output=True)
ls=subprocess.run(['git','-C',R,'ls-tree','-r','--name-only','origin/voci-'+tag],capture_output=True,text=True).stdout.split()
n=0
for f in ls:
    if '/vox/' in f and f.split('/')[-1]!='ESITI.txt':
        d=W+os.path.basename(f)
        if not os.path.exists(d):
            open(d,'wb').write(subprocess.run(['git','-C',R,'show','origin/voci-%s:%s'%(tag,f)],capture_output=True).stdout);n+=1
    if f.endswith('ESITI.txt'):open(W+'ESITI.txt','wb').write(subprocess.run(['git','-C',R,'show','origin/voci-%s:%s'%(tag,f)],capture_output=True).stdout)
    if f.endswith('DALLA_MASTER.txt'):print('DALLA_MASTER:',subprocess.run(['git','-C',R,'show','origin/voci-%s:%s'%(tag,f)],capture_output=True,text=True).stdout[:500])
print('nuovi file voce',n,'| totale',len([x for x in os.listdir(W) if x.endswith('.wav')]))
