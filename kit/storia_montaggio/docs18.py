import json,sys,os,re,shutil,subprocess
import openpyxl
OUT=os.environ.get('OUT','/tmp/w18/out');os.makedirs(OUT,exist_ok=True)
N=sys.argv[1] if len(sys.argv)>1 else '18';SRC=sys.argv[2] if len(sys.argv)>2 else '/tmp/w18'
TIT=sys.argv[3] if len(sys.argv)>3 else "L'Italia repubblicana"
Q=json.load(open(f'{SRC}/scambio/storia-V-lez{N}/quiz.json'))
json.dump(Q,open(f'{OUT}/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
L=[f'QUIZ DI ARGOMENTO · Storia · {TIT}','STATO: da ricontrollare dalla master (approvazioni delegate, regola del 13/11)','']
for k in sorted(Q,key=lambda x:int(x[1:])):
    q=Q[k];n=k[1:];tt=q['title'].split(' · ',1)[1]
    L.append(f'\n== Argomento {n} · {tt} ==')
    for i,it in enumerate(q['items'],1):
        opts=[(it['a'],True)]+[(w,False) for w in it['w']]
        # ordine fisso ma non sempre la prima: ruota di i
        r=(i*2+int(n))%4;opts=opts[-r:]+opts[:-r] if r else opts
        L.append(f'{i}. {it["p"]}')
        for j,(o,ok) in enumerate(opts):L.append(f'   {"ABCD"[j]}) {o}'+('  <-- giusta' if ok else ''))
        L.append(f'   Spiegazione: {it["e"]}')
open(f'{OUT}/Quiz_Storia_Lez{N}.txt','w').write('\n'.join(L)+'\n')
# test finale: Excel del prof, numeri riscritti come testo
wb=openpyxl.load_workbook(glob:=[f'{SRC}/prof/test/STORIA V/DOMANDE LEZIONE {N}.xlsx'][0])
ch=0
for ws in wb:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value,(int,float)) and not isinstance(c.value,bool):
                c.value=str(c.value).rstrip('0').rstrip('.') if isinstance(c.value,float) else str(c.value);c.number_format='@';ch+=1
wb.save(f'{OUT}/Storia_Lez{N}_test_finale_docente.xlsx');print('numeri come testo:',ch)
# compiti
pdf=f'{SRC}/prof/compiti/STORIA V /LEZIONE {N}.pdf'
shutil.copy(pdf,f'{OUT}/Storia_Lez{N}_compiti_docente.pdf')
txt=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout
items=[re.sub(r'\s+',' ',x).strip() for x in re.split(r'\n\s*(?=\d\)\s)',re.sub(r'^LEZIONE \d+\s*','',txt.strip()))]
items=[re.sub(r'^\d\)\s*','',x) for x in items if x]
open(f'{OUT}/Storia_Lez{N}_compiti_docente.txt','w').write('\n\n'.join(f'{i}) {x}' for i,x in enumerate(items,1))+'\n')
json.dump({'titolo':f'Compiti · Storia V · Lezione {N}','stato':f'compiti del prof. Mazzotti (file «LEZIONE {N}.pdf», release mazzotti-storia-V, 14/11), testo invariato','compiti':[{'n':i,'tipo':'risposta_aperta','testo':x} for i,x in enumerate(items,1)]},open(f'{OUT}/compiti.json','w'),ensure_ascii=False,indent=1)
print(len(items),'compiti');print(open(f'{OUT}/Storia_Lez{N}_compiti_docente.txt').read()[:400])
