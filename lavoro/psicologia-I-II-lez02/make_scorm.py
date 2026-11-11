# Pacchetto SCORM 1.2 per SoluzioneFAD dalla lezione interattiva (player con esercizi, soglia 80 %).
# uso: python3 make_scorm.py <parte> [hd|leggero]
#  - completamento: tutti gli esercizi superati + video arrivato alla fine
#  - punteggio: primo tentativo di ogni esercizio (0-100) · ripresa dal punto in cui si era (suspend_data)
#  - nella versione SCORM la "modalità prova" (salto libero) è nascosta
import sys,os,shutil,subprocess,re
part=sys.argv[1];q=sys.argv[2] if len(sys.argv)>2 else 'hd'
D='/home/claude/lezioni/psicologia-I-II-lez02/';SRC=D+f'consegna/Tecnologie_Lez1_Parte{part}/Lezione_interattiva/'
NAME=f'Tecnologie_Lez1_Parte{part}';OUT=D+f'scorm/{NAME}_{q}/'
shutil.rmtree(OUT,ignore_errors=True);os.makedirs(OUT)
VID=f'{NAME}_VIDEO.mp4'
if q=='hd':shutil.copy(SRC+VID,OUT+VID)
else:subprocess.run(['ffmpeg','-v','error','-y','-i',SRC+VID,'-vf','scale=1280:720','-c:v','libx264','-preset','veryfast','-crf','27','-c:a','aac','-b:a','96k','-movflags','+faststart',OUT+VID],check=True)
shutil.copy(SRC+'esercizi.html',OUT+'esercizi.html')
P=open(SRC+'index.html').read()
JS=r"""
/* ---- SCORM 1.2 (SoluzioneFAD): si collega alla piattaforma se c'è, altrimenti funziona da solo ---- */
(function(){try{var dm=document.getElementById('demo');dm.checked=false;var l=dm.closest('label')||dm.parentNode;l.style.display='none'}catch(e){}})();
var SC=(function(){var api=null,ok=false,chiuso=false,resume=0,ultimo=0;
 function trova(w){var n=0;while(w){try{if(w.API)return w.API}catch(e){}if(w.parent&&w.parent!==w&&n<12){w=w.parent;n++}else break}return null}
 api=trova(window);if(!api&&window.opener){try{api=trova(window.opener)}catch(e){}}
 function g(k){try{return String(api.LMSGetValue(k)||'')}catch(e){return ''}}
 function s(k,x){try{api.LMSSetValue(k,String(x))}catch(e){}}
 function tutti(){for(var q=1;q<=NQ;q++)if(!DONE[q])return false;return true}
 function agg(){if(!ok||chiuso)return;var got=0,tot=0;for(var q=1;q<=NQ;q++){tot+=MAX[q]||0;if(DONE[q])got+=FIRST[q]||0}
  if(tot)s('cmi.core.score.raw',Math.round(100*got/tot));
  s('cmi.suspend_data',JSON.stringify({d:DONE,f:FIRST,t:Math.floor(v.currentTime||0)}));
  s('cmi.core.lesson_location',Math.floor(v.currentTime||0));
  if(tutti()&&(v.ended||(DUR&&v.currentTime>=DUR-2)))s('cmi.core.lesson_status','completed');
  try{api.LMSCommit('')}catch(e){}}
 function init(){if(!api)return;try{ok=String(api.LMSInitialize(''))==='true'}catch(e){ok=false}if(!ok)return;
  var st=g('cmi.core.lesson_status');if(st===''||st==='not attempted')s('cmi.core.lesson_status','incomplete');
  s('cmi.core.score.min',0);s('cmi.core.score.max',100);
  var sd=g('cmi.suspend_data');
  if(sd){try{var o=JSON.parse(sd);DONE=o.d||{};FIRST=o.f||{};resume=+o.t||0;if(ready)fr.contentWindow.postMessage({telesio:'restore',first:FIRST,done:DONE},'*');upd()}catch(e){}}
  try{api.LMSCommit('')}catch(e){}}
 function chiudi(){if(!ok||chiuso)return;agg();chiuso=true;try{api.LMSFinish('')}catch(e){}}
 sv=agg;
 v.addEventListener('loadedmetadata',function(){if(resume>0&&resume<v.duration-2){try{v.currentTime=resume}catch(e){}}});
 v.addEventListener('timeupdate',function(){if(ok&&Math.abs(v.currentTime-ultimo)>15){ultimo=v.currentTime;agg()}});
 v.addEventListener('ended',agg);
 window.addEventListener('pagehide',chiudi);window.addEventListener('beforeunload',chiudi);
 init();return {agg:agg,chiudi:chiudi,attivo:function(){return ok}}})();
"""
i=P.rindex('</script></body></html>');P=P[:i]+JS+P[i:]
open(OUT+'index.html','w').write(P)
TIT=re.search(r'<title>(.*?)</title>',P);TIT=TIT.group(1) if TIT else NAME
MAN=f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="telesio.{NAME.lower()}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata><schema>ADL SCORM</schema><schemaversion>1.2</schemaversion></metadata>
  <organizations default="org1">
    <organization identifier="org1">
      <title>{TIT}</title>
      <item identifier="item1" identifierref="res1" isvisible="true"><title>{TIT}</title></item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="res1" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/><file href="esercizi.html"/><file href="{VID}"/>
    </resource>
  </resources>
</manifest>
'''
open(OUT+'imsmanifest.xml','w').write(MAN)
z=D+f'scorm/{NAME}_SCORM_{q}.zip'
if os.path.exists(z):os.remove(z)
subprocess.run(['zip','-q','-r','-0' if q=='hd' else '-6',z,'.'],cwd=OUT,check=True)
print(z,round(os.path.getsize(z)/1e6,1),'MB')
