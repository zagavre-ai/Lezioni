import sys,os,json,subprocess,re,difflib,unicodedata
sys.path.insert(0,'/home/user/work/build')
NEW=['BENV1_R2','MP1','MP23','MP4','COMP1','COMP2']
vc='/home/user/work/vc'
subprocess.run(['git','-C',vc,'fetch','-q','origin','voci-storia-V-lez11'])
subprocess.run(['git','-C',vc,'merge','-q','--no-edit','FETCH_HEAD'])
have=[n for n in NEW if os.path.exists(f'{vc}/scambio/storia-V-lez11/vox/{n}.wav')]
print('arrivate:',have,'mancano:',[n for n in NEW if n not in have])
