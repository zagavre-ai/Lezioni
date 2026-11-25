import json,re,sys,os,subprocess,wave,numpy as np
sys.path.insert(0,'/tmp/w14/build');sys.path.insert(0,'/tmp/w14')
import gen
from evid import ricostruisci
gen.PROFON=False;gen.DARK=True
E=gen.E
WAV='/tmp/w14/SPG_1_48k.wav'
j=json.load(open('/tmp/w14/tr/SPG_1.json'))
W=[(t,re.sub(r'[^a-zàèéìòù]','',w.lower())) for t,w in ricostruisci(j)]
D=[("Primo argomento","Pirandello e la crisi del primo Novecento",["Pirandello nasce a Girgenti, da una famiglia borghese agiata, e vive il dissesto delle miniere di zolfo.","La moglie Antonietta si ammala di mente: eventi privati che alimentano la sua visione del mondo.","La vita è un flusso continuo che l'uomo cerca inutilmente di fissare in forme stabili: è la crisi dell'io."]),
("Secondo argomento","La visione del mondo e l'umorismo",["L'umorismo distingue l'avvertimento del contrario, il comico, dal sentimento del contrario, il drammatico e tragico.","L'identità si riduce a una maschera imposta dalle convenzioni sociali; la famiglia e il lavoro imprigionano l'uomo.","La via di fuga è la follia, l'immaginazione o la natura."]),
("Terzo argomento","Il fu Mattia Pascal",["Un piccolo borghese creduto morto si costruisce una nuova identità, Adriano Meis, ma fallisce e diventa il forestiere della vita.","Nei Quaderni di Serafino Gubbio operatore le macchine alienano l'uomo e lo riducono a schiavo."]),
("Quarto argomento","Uno, nessuno e centomila",["È l'approdo della parabola pirandelliana: Vitangelo Moscarda accetta la perdita d'identità come condizione positiva e liberatoria.","Rifiuta il proprio nome e rinasce nella natura."])]
def find(word,after,k=0):
    c=[t for t,w in W if w==word and t>=after]
    return c[k] if len(c)>k else after+1
LEN=len(wave.open(WAV).readframes(10**9))/4/48000
starts=[];cur=0
for lab,_,_ in D:
    cur=find('argomento',cur+0.5)-1.2;starts.append(max(cur,0));cur+=0.5
ends=starts[1:]+[LEN+0.2]
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
OFF=0.5;nf=round((OFF+LEN+1.0)*30)
def html(i,k):
    lab,title,items=D[i]
    body=f'<div style="position:absolute;left:80px;top:146px;width:1760px"><div class="lab">RIPASSO · {E(lab.upper())}</div><div class="tit" style="margin-top:34px;font-size:{58 if len(title)>40 else 64}px">{E(title)}</div><div class="bar"></div><div style="margin-top:36px;display:flex;flex-direction:column;gap:20px">'
    for q in range(k):
        on=' on' if q==k-1 else ''
        body+=f'<div class="card nc{on}" style="font-size:40px;line-height:1.5;padding-top:18px;padding-bottom:18px"><div class="n">{q+1}</div><div>{E(items[q])}</div></div>'
    return gen.page(body+'</div></div>',None,prof=False)
segs=[]
for i,(lab,title,items) in enumerate(D):
    # tempi delle carte: prima parola di ogni frase
    ts=[starts[i]]
    cur=starts[i]
    for it in items:
        f=re.sub(r'[^a-zàèéìòù]','',it.split()[0].lower());cur=find(f,cur+0.3);ts.append(cur)
    # stato 0 (titolo) fino alla prima carta, poi 1..n
    for k in range(len(items)+1):
        a=starts[i] if k==0 else ts[k]
        b=(ts[k+1] if k<len(items) else ends[i])
        if k==0: b=ts[1]
        nm=f'spg_{i}_{k}';gen.scrivi(nm,html(i,k));segs.append((nm,a,b))
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
parts=[];cum=0
for q,(nm,a,b) in enumerate(segs):
    f0=0 if q==0 else round((OFF+a)*30);f1=nf if q==len(segs)-1 else round((OFF+b)*30);k=f1-f0
    if k<=0: continue
    po=f'/tmp/w14/vc/s{q}.mp4';subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i',f'/tmp/w14/build/png/{nm}.png','-frames:v',str(k),*ENC,po],check=True);parts.append(po)
open('/tmp/w14/vc/ls.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','/tmp/w14/vc/ls.txt','-c','copy','/tmp/w14/vc/SPG.mp4'],check=True)
w=wave.open(WAV);V=np.frombuffer(w.readframes(w.getnframes()),np.int16).reshape(-1,2);w.close()
a=np.zeros((nf*1600,2),np.int16);o=int(OFF*48000);a[o:o+len(V)]=V[:len(a)-o]
w=wave.open('/tmp/w14/vc/SPG.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(48000);w.writeframes(a.tobytes());w.close()
meta=json.load(open('/tmp/w14/vc/meta.json'));meta['SPG']={'frames':nf,'wav':'/tmp/w14/vc/SPG.wav'};json.dump(meta,open('/tmp/w14/vc/meta.json','w'))
print('ok',nf,[round(x,1) for x in starts])
