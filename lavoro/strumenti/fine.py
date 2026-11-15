#!/usr/bin/env python3
# Chiusura di una lezione quando le voci Kore sono arrivate. uso: fine.py 4|5
import sys,os,subprocess,json,shutil,re,glob
N=sys.argv[1];W={'4':'/home/user/w4','5':'/home/user/w5'}[N];M={'4':'main.py','5':'main5.py'}[N]
T=f'afm-inglese-triennio-lez0{N}';R='/home/user/Lezioni';K=R+'/kit/tools'
TIT={'4':'Types of business','5':'Marketing'}[N]
def sh(c,**k): 
    r=subprocess.run(c,shell=isinstance(c,str),**k)
    if r.returncode: raise SystemExit(f'ERRORE: {c}')
os.chdir(W)
# 1 voci
os.makedirs('voci/wav',exist_ok=True)
sh(f'cd {R} && git fetch -q origin voci-{T}')
files=subprocess.check_output(f'cd {R} && git ls-tree -r origin/voci-{T} --name-only',shell=True,text=True).split()
vox=[f for f in files if '/vox/' in f]
for f in vox:
    if f.endswith('.wav'):
        open(f'voci/wav/{os.path.basename(f)}','wb').write(subprocess.check_output(f'cd {R} && git show origin/voci-{T}:{f}',shell=True))
    elif f.endswith('ESITI.txt'): open('voci/ESITI.txt','wb').write(subprocess.check_output(f'cd {R} && git show origin/voci-{T}:{f}',shell=True))
print('voci scaricate',len(glob.glob('voci/wav/*.wav')))
# 2 montaggio
sh(f'MODE=kore python3 {M}')
tl=json.load(open('out_kore/timeline.json'))
# 3 codifica finale unica
OUT=f'Inglese_Lez{N}_Parte1_1080p.mp4'
sh(f'CRF=19 python3 {K}/finale_a_pezzi.py out_kore/lista.txt {OUT}')
# 4 sottotitoli (Whisper base) nei tempi del video finale
raw={'4':'sub4_raw.json','5':'sub5_raw.json'}[N]
sh(f'pdftotext ENG_Amm_Lez0{N}_Dispensa.pdf d.txt')
sh(f'python3 /home/user/mkvtt.py {raw} out_kore/timeline.json bounds.json d.txt Inglese_Lez{N}_Parte1.vtt')
# 5 controlli
sh(f'python3 {K}/controllo_finale.py {OUT} out_kore/timeline.json Inglese_Lez{N}_Parte1.vtt --tag {T} --parte 1 --titolo "{TIT}" --voci kore || true')
sh(f'python3 {K}/controllo_jingle.py {OUT} out_kore/timeline.json || true')
print('FINE passo automatico')
