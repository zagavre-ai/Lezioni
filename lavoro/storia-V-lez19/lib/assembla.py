# Assembla una Parte: lista concat -> finale_a_pezzi (x264 veryfast CRF 19, AAC 192k 48 kHz) -> misure. uso: assembla.py 1|2
import sys,json,os,subprocess
sys.path.insert(0,'/home/claude/w19/lib')
W='/home/claude/w19';OUT=W+'/out'
n=sys.argv[1]
tl=json.load(open(f'{W}/timeline_P{n}.json'))
lst=f'{W}/lista_P{n}.txt'
open(lst,'w').write(''.join(f"file '{OUT}/{it['id']}.mkv'\n" for it in tl))
vid=f'{W}/final/Storia_Lez19_Parte{n}_1080p.mp4';os.makedirs(W+'/final',exist_ok=True)
r=subprocess.run(['python3','/home/user/Lezioni/tools/finale_a_pezzi.py',lst,vid],capture_output=True,text=True)
print(r.stdout[-600:],r.stderr[-600:])
