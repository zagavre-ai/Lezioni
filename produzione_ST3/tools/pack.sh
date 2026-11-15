#!/bin/bash
# pack.sh NN "Titolo lezione" PARTI   -> pacchetto cons + ramo consegna + stato
NN=$1; TIT="$2"; PARTI=$3; N=${NN#0}; D=/home/user/lav/l$NN; TAG=storia-III-lez$NN; T=/home/user/lav/tools
cd $D; rm -rf cons; mkdir cons
for p in $PARTI; do V=fin/Storia_III_Lez${N}_Parte${p}_1080p.mp4
 python3 /home/user/Lezioni/kit/tools/scheda_da_timeline.py $V p$p/timeline.json quiz_argomenti.json "Storia III · Lezione $N · Parte $p" cons/scheda_pubblicazione_Parte$p.json "Storia" >/dev/null
 python3 - <<P
import json
s=json.load(open('cons/scheda_pubblicazione_Parte$p.json'));T=json.load(open('p$p/timeline.json'));d={n:t for n,t,l in T}
s['t_verifica']=d['VER'];s['t_compiti']=d['COMP'];s['t_compiti_intro']=d['CINTRO'];s['compiti']='COMPITI_MANCANTI'
json.dump(s,open('cons/scheda_pubblicazione_Parte$p.json','w'),ensure_ascii=False,indent=1)
P
 python3 /home/user/Lezioni/kit/tools/testo_youtube.py cons/scheda_pubblicazione_Parte$p.json "Storia III|Storia III" "Prof. Giorgio Mazzotti" "Lezione $N · $TIT" $p p$p/timeline.json > cons/testo_youtube_Parte$p.txt
 cp p$p/timeline.json cons/timeline_Parte$p.json; cp p$p/sottotitoli.vtt cons/Storia_III_Lez${N}_Parte$p.vtt
 (cd fin && split -b 94371840 -d -a 2 Storia_III_Lez${N}_Parte${p}_1080p.mp4 ../cons/Storia_III_Lez${N}_Parte${p}_1080p.mp4.parte_ && sha256sum Storia_III_Lez${N}_Parte${p}_1080p.mp4 > ../cons/Storia_III_Lez${N}_Parte${p}_1080p.mp4.sha256)
done
python3 - <<P
import json
Q=json.load(open('quiz_argomenti.json'));o=[]
for k,v in Q.items():
    o.append(v['title'])
    for i,it in enumerate(v['items'],1):
        o.append('%d. %s'%(i,it['p']));o.append('   * %s'%it['a']);[o.append('   - %s'%w) for w in it['w']];o.append('   Spiegazione: %s'%it['e'])
    o.append('')
open('cons/Quiz_Storia_III_Lez${N}.txt','w').write('\n'.join(o))
P
cp quiz_argomenti.json cons/; cp DOMANDE.LEZIONE.$N.xlsx cons/Storia_III_Lez${N}_test_finale_docente.xlsx
python3 $T/dispensa.py $D cons/Storia_III_Lez${N}_dispensa.pdf | tail -1
echo "Storia III · Lezione $N · consegna 15/11. Video a pezzi da 90 MB: riunisci con  cat Storia_III_Lez${N}_ParteN_1080p.mp4.parte_* > Storia_III_Lez${N}_ParteN_1080p.mp4  e controlla con il file .sha256. Test finale: Excel del docente. Compiti: COMPITI_MANCANTI (file non presente nella release); nel video ci sono le schede Verifica finale e Compiti (t_verifica e t_compiti nelle schede di pubblicazione)." > cons/LEGGIMI.txt
B=consegna-$TAG; W=/tmp/wt_cons$NN; cd /home/user/Lezioni; rm -rf $W; git worktree add -q --detach $W; cd $W; git checkout -q --orphan $B; git rm -rfq . >/dev/null 2>&1; mkdir -p $B; cp $D/cons/* $B/; git add -f $B; git -c user.name="Telesio ST3" -c user.email="st3@telesio.invalid" commit -qm "consegna $TAG"; git push -q origin HEAD:refs/heads/$B 2>&1 | tail -1; cd /home/user/Lezioni; git worktree remove --force $W
for p in $PARTI; do python3 kit/tools/stato.py $TAG --parte $p --stato PRONTA --video $D/fin/Storia_III_Lez${N}_Parte${p}_1080p.mp4 --vtt $D/cons/Storia_III_Lez${N}_Parte$p.vtt --scheda $D/cons/scheda_pubblicazione_Parte$p.json --timeline $D/cons/timeline_Parte$p.json --voci kore --quiz_ok si --fermi_ok si --sub_ok si | grep -E "NON PRONTA|durata\""; done
python3 kit/tools/stato.py $TAG --nota "PRONTA 15/11. Sottotitoli Whisper base; controllo di attacco ~75% (falsi negativi su voce bassa). Compiti del prof non presenti nella release." --invia | tail -1
