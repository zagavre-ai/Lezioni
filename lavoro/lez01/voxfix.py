#!/usr/bin/env python3
# Voci Kore ricevute dalla master: normalizza a -16 LUFS, trascrive e confronta parola per parola, misura i bordi, allinea gli eventi.
import os,sys,re,json,subprocess,wave
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import numpy as np,voci
from asm import sh,WK,dur_wav
SRC='/home/user/Lezioni/scambio_voci/vox/'   # copia locale di scambio/storia-arte-V-lez01/vox/
PRO=WK+'vox16/';ASR=WK+'vox_asr/';os.makedirs(PRO,exist_ok=True);os.makedirs(ASR,exist_ok=True)
def norm16(nome):
    src=SRC+f'NC_{nome}.wav';dst=PRO+f'NC_{nome}.wav'
    if os.path.exists(dst):return dst
    r=subprocess.run(['ffmpeg','-hide_banner','-i',src,'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
    j=json.loads(r[r.rfind('{'):])
    af=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
    sh(['ffmpeg','-v','error','-y','-i',src,'-af',af,'-ar','48000','-ac','2','-c:a','pcm_s16le',dst]);return dst
def trascrivi(nome):
    out=ASR+f'NC_{nome}'
    if not os.path.exists(out+'.json'):
        sh(['python3','/home/user/Lezioni/kit/tools/trascrivi.py',SRC+f'NC_{nome}.wav',out])
    return json.load(open(out+'.json'))
def norm(t):
    t=t.lower().replace("'",' ').replace('’',' ');t=re.sub(r'[^a-zàèéìòùáíóúç ]',' ',t);return t.split()
def confronta(nome):
    atteso=norm(voci.per_voce(voci.VOCI[nome]))
    segs=trascrivi(nome);got=norm(' '.join(s['testo'] for s in segs))
    # distanza di edit su parole
    n,m=len(atteso),len(got);D=np.zeros((n+1,m+1),int);D[:,0]=range(n+1);D[0,:]=range(m+1)
    for i in range(1,n+1):
        for j in range(1,m+1):D[i,j]=min(D[i-1,j]+1,D[i,j-1]+1,D[i-1,j-1]+(atteso[i-1]!=got[j-1]))
    # parole diverse (dall'allineamento)
    i,j=n,m;diff=[]
    while i>0 or j>0:
        if i>0 and j>0 and D[i,j]==D[i-1,j-1]+(atteso[i-1]!=got[j-1]):
            if atteso[i-1]!=got[j-1]:diff.append((atteso[i-1],got[j-1]))
            i-=1;j-=1
        elif i>0 and D[i,j]==D[i-1,j]+1:diff.append((atteso[i-1],''));i-=1
        else:diff.append(('',got[j-1]));j-=1
    return D[n,m]/max(1,n),diff[::-1]
def bordi(nome):
    a=SRC+f'NC_{nome}.wav'
    x=np.frombuffer(sh(['ffmpeg','-v','error','-i',a,'-ac','1','-ar','48000','-f','s16le','-']).stdout.encode('latin1') if False else subprocess.run(['ffmpeg','-v','error','-i',a,'-ac','1','-ar','48000','-f','s16le','-'],capture_output=True).stdout,np.int16)/32768
    n=int(0.05*48000);return float(np.abs(x[:n]).max()),float(np.abs(x[-n:]).max())
def tempi_parole(nome):
    """[(t,parola)] ASR della voce, per allineare gli eventi"""
    segs=trascrivi(nome);W=[]
    for s in segs:
        cur=None
        for t,w in s['parole']:
            if w.startswith(' ') or cur is None:
                if cur:W.append(tuple(cur))
                cur=[t,w.strip()]
            else:cur[1]+=w
        if cur:W.append(tuple(cur))
    return [(t,w) for t,w in W if re.search(r'\w',w)]
def tempo_evento(nome,frazione,vd):
    """istante (s) in cui la voce arriva a 'frazione' del testo: usa le parole trascritte se ci sono, altrimenti la proporzione"""
    f=PRO.replace('vox16','vox_asr')+f'NC_{nome}.json'
    if not os.path.exists(f):return frazione*vd
    W=tempi_parole(nome)
    if not W:return frazione*vd
    return max(0.0,W[min(len(W)-1,int(round(frazione*len(W))))][0]-0.05)
def main():
    righe=[]
    for nome in voci.VOCI:
        p=SRC+f'NC_{nome}.wav'
        if not os.path.exists(p):righe.append((nome,'MANCA'));continue
        d=dur_wav(p);a,b=bordi(nome);err,diff=confronta(nome);norm16(nome)
        righe.append((nome,round(d,1),f'{a:.3f}',f'{b:.3f}',f'{err*100:.1f}%',diff[:10]))
    for r in righe:print(r)
    json.dump([list(map(str,r)) for r in righe],open(WK+'esiti_voci.json','w'),ensure_ascii=False)
if __name__=='__main__':main()
