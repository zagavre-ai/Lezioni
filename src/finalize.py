# Dopo le voci: assembla il video finale, sottotitoli, dispensa e PDF mappe
import sys, os, json, shutil
sys.path.insert(0,'/tmp/w/build')
import assemble, subs
OUT='/tmp/w/build/final/Storia_arte_V_Lez6_Parte1_1080p.mp4'; os.makedirs('/tmp/w/build/final',exist_ok=True)
shutil.rmtree(OUT+'.parti',ignore_errors=True)
TL=assemble.run(OUT)
n=subs.build(TL,assemble.ORDER,OUT.replace('.mp4','.vtt'),{'MAPPA_M1':0.0,'MAPPA_M2':0.0}); print('sottotitoli',n,'cue')
import dispensa
L=dispensa.pages(); dispensa.pdf_from(L,f'{dispensa.OUT}/Dispensa_Storia_arte_V_Simbolismo_e_Art_Nouveau.pdf',"Storia dell'arte V · Simbolismo e Art Nouveau"); dispensa.mappe_pdf()
print('FATTO')
