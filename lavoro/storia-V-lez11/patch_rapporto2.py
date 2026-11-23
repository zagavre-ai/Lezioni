s = open('/home/user/work/build/rapporto.py').read()
i = s.index("NEWV=[")
j = s.index("sev=open(")
new = '''import os as _o
VX=f'{W}/vc/scambio/storia-V-lez11/vox/'
c3=_o.path.exists(VX+'COMP3.wav')
mp4r=_o.path.exists(VX+'MP4_R2.wav');c1r=_o.path.exists(VX+'COMP1_R2.wav')
voci=("Voci nuove arrivate dalla master e montate: BENV1_R2 (benvenuto senza nome), MP1, MP23, MP4, COMP1, COMP2 e le rigenerate R3_R2, R4_R2, SC6_1_R2…SC6_4_R2 (bordi). Trascritte e confrontate con il testo (similarità 0,75–1,0; le differenze sono nomi stranieri sbagliati dal riconoscimento automatico, non ascoltati).\\n"
 "- **MP4 difettosa**: legge ad alta voce le istruzioni di stile («Dizione italiana cristallina? Timbro luminoso e accogliente…») e ripete la domanda. Montata solo la parte corretta (dal secondo «Su che cosa si basa il totalitarismo di Stalin?», da 16,95 s alla fine), senza altre modifiche."+(" Arrivata la MP4_R2: da sostituire." if mp4r else " Richiesta la rigenerazione (MP4_R2): se arriva si sostituisce.")+"\\n"
 "- **COMP1 difettosa**: ripete l'esercizio 1 e legge l'esercizio 2 con l'anno sbagliato (1924 invece di 1929) prima di ripeterlo giusto. Montati 0–16,95 s e 29,05 s–fine con 0,4 s di pausa."+(" Arrivata la COMP1_R2: da sostituire." if c1r else " Richiesta la rigenerazione (COMP1_R2).")+"\\n"
 +("- COMP3 (chiusura dei compiti «Svolgi i compiti qui sotto e premi Consegna…») arrivata e montata.\\n" if c3 else "- **COMP3 NON arrivata**: la frase di chiusura dei compiti (voce e schermo) è montata con una tenuta muta di 7 s al posto della voce (scheda muta oltre 2,5 s: da sostituire appena arriva).\\n")
 +"- I compiti sono letti dalle voci COMP1 e COMP2 (parole esatte del prof) e si accendono uno alla volta con il bordo giallo (regola del 22/11). Il piano della master prevedeva una voce sola COMPITI: avevo già richiesto COMP1 e COMP2 prima del messaggio.\\n"
 "- Le schede Quiz e Verifica dicono «Rispondi · premi Controlla · poi Continua» (regola 22/11 22:30).")
'''
open('/home/user/work/build/rapporto.py', 'w').write(s[:i] + new + s[j:])
