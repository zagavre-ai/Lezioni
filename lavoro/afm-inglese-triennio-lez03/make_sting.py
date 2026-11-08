# jingle breve (trans) ai cambi di sottoargomento, sotto la voce della docente
import json,subprocess
D='/home/claude/lezioni/afm-inglese-triennio-lez03/'
SL=json.load(open(D+'slides.json'));P=json.load(open(D+'sv_plan.json'))
st=P['starts'];times=[]
for k in range(1,len(SL)):
    if SL[k]['s']!=SL[k-1]['s'] and SL[k]['a']==SL[k-1]['a']: times.append(round(st[k]-0.6,2))
print(len(times),times[:10])
ins=['-i',D+'audio/audio_B_full.wav'];fl=[];lab=['[0:a]']
for j,t in enumerate(times):
    ins+=['-i','/home/claude/v5/snd/trans.wav'];fl.append(f'[{j+1}:a]aresample=48000,pan=mono|c0=0.5*c0+0.5*c1,volume=0.22,adelay={int(t*1000)}[s{j}]');lab.append(f'[s{j}]')
fc=';'.join(fl)+';'+''.join(lab)+f'amix=inputs={len(lab)}:normalize=0:duration=first[a]'
subprocess.run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',fc,'-map','[a]','-ar','48000','-ac','1',D+'audio/audio_B_sting.wav'],check=True)
json.dump(times,open(D+'sting_times.json','w'))
