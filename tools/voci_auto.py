# Genera le voci (motore di Vox Studio: Gemini, voce Kore, regia approvata), un file per blocco, poi le importa.
# Ogni file viene ricontrollato con la trascrizione: se la regia è stata letta o mancano parole, si rigenera (max 5 volte).
# uso: REGIA=B voci_auto.py cartella_lezione NOME1 NOME2 ...
import sys,os,json,subprocess,re
try:import soundfile
except ImportError:subprocess.run([sys.executable,'-m','pip','install','-q','--break-system-packages','soundfile'])
os.environ.pop('REGIA',None)  # regia di default (modello 3.8 flash), la più stabile nelle prove
sys.path.insert(0,'/home/claude/tts');import gemini_tts as G
L=os.path.abspath(sys.argv[1])+'/';V=L+'voci/';os.makedirs(V+'vox',exist_ok=True)
T=json.load(open(V+'testi_voci.json'))
if not os.path.exists(V+'importa_voce_esterna.py'):print('MANCA voci/importa_voce_esterna.py: mi fermo per non sprecare credito (copialo dal modello di lezione)');sys.exit(4)
NUM=re.compile(r"(uno|due|tre|quattro|cinque|sei|sette|otto|nove|dieci|undici|dodici|venti|trenta|quaranta|cinquanta|sessanta|settanta|ottanta|novanta|cento|mille|virgola|per cento)",re.I)
SPIA=re.compile(r'\b(bes|dsa|regia|rassicurante|coinvolgente|scandito|e-learning|docente di)\b',re.I)
for n in sys.argv[2:]:
    out=V+f'vox/{n}.wav';txt=' '.join(T[n]);nw=len(txt.split());esito='?';ricevuta=os.path.exists(out)  # voce arrivata dalla master: mai cancellarla
    for k in range(5):
        if not os.path.exists(out):
            try:G.tts(txt,out+'.tmp.wav');os.rename(out+'.tmp.wav',out)
            except RuntimeError as e:print(n,'QUOTA FINITA:',e,flush=True);sys.exit(3)
        r=subprocess.run([sys.executable,'importa_voce_esterna.py',n,out],capture_output=True,text=True,cwd=V)
        m=re.search(r'frasi trovate (\d+) / (\d+) parole diverse (\d+)',r.stdout)
        if not m:  # errore tecnico dell'importazione (modulo mancante ecc.): NON si cancella la voce, ci si ferma
            print(n,'ERRORE TECNICO IMPORTAZIONE, voce conservata in',out,'\n',r.stderr[-400:],flush=True);sys.exit(5)
        ins=' '.join(re.findall(r"\('insert', \[\], \[(.*?)\]\)",r.stdout))
        spia=bool(SPIA.search(ins)) and not SPIA.search(txt)
        # differenze vere: si ignorano quelle dovute ai numeri (la trascrizione li scrive in cifre)
        diff=0
        for op,a,b in re.findall(r"\('(\w+)', \[(.*?)\], \[(.*?)\]\)",r.stdout):
            if re.search(r'\d',b) or re.search(NUM,a):continue
            diff+=max(len(a.split(',')) if a else 0,len(b.split(',')) if b else 0)
        ok=m and m.group(1)==m.group(2) and diff<=max(4,nw*0.08) and not spia
        esito=(m.group(0)+f' (vere {diff})' if m else r.stderr[-200:])+(' REGIA LETTA' if spia else '')
        if ok:break
        if ricevuta:break
        if k<4:os.remove(out)
    print(n,'OK' if ok else 'DA CONTROLLARE',esito,'tentativi',k+1,flush=True)
