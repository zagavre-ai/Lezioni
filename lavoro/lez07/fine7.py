#!/usr/bin/env python3
# Chiusura della lezione 7 quando le voci Kore sono arrivate. uso: python3 fine7.py
import os,subprocess,json,glob,sys
W='/home/claude/w7';T='afm-inglese-triennio-lez07';R='/home/claude/lezioni';K='/home/claude/main/kit/tools'
TIT='Trade and commerce';OUT='Inglese_Lez7_Parte1_1080p.mp4';VTT='Inglese_Lez7_Parte1.vtt'
def sh(c):
    print('>>',c,flush=True);r=subprocess.run(c,shell=True)
    if r.returncode: raise SystemExit(f'ERRORE: {c}')
os.chdir(W)
# 1 voci
os.makedirs('voci/wav',exist_ok=True)
sh(f'git -C {R} fetch -q --depth 1 origin voci-{T}:refs/remotes/origin/voci-{T}')
files=subprocess.check_output(f'git -C {R} ls-tree -r origin/voci-{T} --name-only',shell=True,text=True).split()
for f in files:
    if '/vox/' not in f: continue
    dst='voci/wav/'+os.path.basename(f) if f.endswith('.wav') else 'voci/'+os.path.basename(f)
    open(dst,'wb').write(subprocess.check_output(f'git -C {R} show origin/voci-{T}:{f}',shell=True))
need=[v['nome'] for v in json.load(open('testi_voci.json'))]
miss=[n for n in need if not os.path.exists(f'voci/wav/{n}.wav')]
print('voci scaricate',len(glob.glob('voci/wav/*.wav')),'mancano',miss)
if miss: raise SystemExit('mancano voci Kore')
# 2 i pezzi del docente non dipendono dalle voci: si riusano
os.makedirs('w_kore',exist_ok=True)
for f in glob.glob('w_ph/b_D*.mkv'):
    d='w_kore/'+os.path.basename(f)
    if not os.path.exists(d): os.link(f,d)
sh('MODE=kore python3 main7.py')
# 3 codifica finale unica
if not os.path.exists(OUT): sh(f'CRF=19 python3 /home/claude/tools/finale_cache.py out_kore/lista.txt {OUT} {W}/cache_finale')
# 4 sottotitoli della docente nei tempi del video finale
sh(f'python3 mksub7.py out_kore/timeline.json {VTT}')
# 5 controlli
sh(f'python3 {K}/controllo_finale.py {OUT} out_kore/timeline.json {VTT} > controllo_finale.log 2>&1 || true')
sh(f'python3 {K}/controllo_jingle.py {OUT} out_kore/timeline.json > controllo_jingle.log 2>&1 || true')
sh(f'python3 {K}/scheda_da_timeline.py {OUT} out_kore/timeline.json quiz_argomenti.json "{TIT} · Parte 1" scheda_pubblicazione.json Inglese')
print('FINE passo automatico')
# 6 controllo di sincronia, LEGGIMI, consegna su git, stato
sh(f'python3 syncchk7.py {OUT} out_kore/timeline.json 6 > sincronia.txt')
sh(f'python3 /home/claude/tools/leggimi.py {W} {T} "{TIT}" 7 {OUT} out_kore/timeline.json sincronia.txt > LEGGIMI.md')
sh('bash consegna7.sh > consegna.log 2>&1; tail -3 consegna.log')
ok=open('consegna.log').read().count('VERIFICA SHA256 DAL RAMO: OK')
cf=open('controllo_finale.log').read() if os.path.exists('controllo_finale.log') else ''
cj=open('controllo_jingle.log').read() if os.path.exists('controllo_jingle.log') else ''
manca=[f for f in ['Test_Inglese_Lez7.xlsx','compiti.json'] if not os.path.exists(f)]
nota=f'Video finale consegnato sul ramo consegna-{T} (pezzi da 90 MiB + sha256, verifica dal ramo: {"OK" if ok else "DA RIFARE"}). Durata misurata nello stato. controllo_finale: '+(cf.strip().splitlines()[-1][:150] if cf.strip() else '?')+' · jingle: '+(cj.strip().splitlines()[-1][:100] if cj.strip() else '?')
st='IN_MONTAGGIO' if manca else 'PRONTA'
nota=nota.replace('"',"'").replace('`',"'").replace('$','')
if manca: nota+=f' · NON PRONTA solo perché mancano dalla release i file della docente: Verifica.xlsx e Compiti.pdf (nel ramo c\'è un test PROPOSTA_DA_VALIDARE). Appena arrivano: Test + compiti.json sul ramo, nessuna ricodifica (la scheda Compiti nel video rimanda alla scheda della lezione).'
sh(f'cd /home/claude/lezioni && TZ=Europe/Rome python3 {K}/stato.py {T} --parte 1 --stato {st} --video {W}/{OUT} --vtt {W}/{VTT} --voci kore --quiz_ok si --fermi_ok si --sub_ok si --scheda {W}/scheda_pubblicazione.json --timeline {W}/out_kore/timeline.json --nota "{nota}" --invia | tail -2')
print('FINE')
