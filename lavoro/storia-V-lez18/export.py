import sys,os,json,re,subprocess,hashlib,shutil
W='/home/user/work18';O=W+'/out';D=W+'/consegna';os.makedirs(D,exist_ok=True)
def tool_name(n):
    if re.match(r'^P\d[abc]_\d+$',n):return 'D'+n[1:]
    if n in('IN1','IN2'):return 'D0_'+n[2:]
    if re.match(r'^D\d+_\d+$',n):return 'K'+n[1:]
    return n
for w in ('1','2'):
    tl=json.load(open(f'{O}/timeline_Storia_Lez18_Parte{w}.json'))
    json.dump([[tool_name(n),t,d] for n,t,d in tl],open(f'{D}/timeline_Parte{w}.json','w'),ensure_ascii=False)
    v=f'{O}/Storia_Lez18_Parte{w}_1080p.mp4'
    dst=f'{D}/Storia_Lez18_Parte{w}_1080p.mp4'
    if os.path.exists(v):shutil.copy(v,dst)
    h=hashlib.sha256()
    for ch in iter(lambda:open(dst,'rb').read(1<<24),b''):break
    with open(dst,'rb') as f:
        while True:
            b=f.read(1<<24)
            if not b:break
            h.update(b)
    open(dst+'.sha256','w').write(f'{h.hexdigest()}  Storia_Lez18_Parte{w}_1080p.mp4\n')
    if os.path.exists(f'{O}/Storia_Lez18_Parte{w}.vtt'):shutil.copy(f'{O}/Storia_Lez18_Parte{w}.vtt',D)
    subprocess.run(['python3','/home/user/Lezioni/kit/tools/scheda_da_timeline.py',dst,f'{D}/timeline_Parte{w}.json',W+'/scambio/storia-V-lez18/quiz.json',f"L'Italia repubblicana · Parte {w}",f'{D}/scheda_pubblicazione_Parte{w}.json','Storia'])
for f in ('Storia_Lez18_dispensa.pdf','Storia_Lez18_mappe.pdf'):
    if os.path.exists(f'{O}/{f}'):shutil.copy(f'{O}/{f}',D)
shutil.copy(W+'/verifica_finale.json',D);shutil.copy(W+'/compiti.txt',D+'/Storia_Lez18_compiti_docente.txt')
shutil.copy(W+'/src/DOMANDE LEZIONE 18.xlsx',D+'/Storia_Lez18_test_finale_docente.xlsx')
shutil.copy(W+'/scambio/storia-V-lez18/quiz.json',D+'/quiz_argomenti.json')
print(os.listdir(D))
