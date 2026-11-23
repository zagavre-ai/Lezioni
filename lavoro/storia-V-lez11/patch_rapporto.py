s = open('/home/user/work/build/rapporto.py').read()
old = "voci=open(B+'/voci_stato.txt').read() if os.path.exists(B+'/voci_stato.txt') else ''"
new = '''NEWV=['BENV1_R2','MP1','MP23','MP4','COMP1','COMP2']
miss=[n for n in NEWV if not os.path.exists(f'{W}/vc/scambio/storia-V-lez11/vox/{n}.wav')]
if miss:
    voci=("**ATTENZIONE: questo video NON è definitivo.** Le voci "+', '.join(miss)+" non sono ancora arrivate dalla master: nel video ci sono silenzi della durata stimata al posto del benvenuto in copertina (0:15-0:32), delle 3 mappe del prof (la sincronia ramo per ramo è stimata sul testo) e della lettura dei compiti. Per questo lo stato è IN_MONTAGGIO e non REVISIONATA. Appena arrivano si ricodifica una volta sola (circa 40 minuti). Le altre voci (AN, SC, R, GL, RIEP, FIN, COMPI) sono le Kore già generate dalla master. Le voci R3, R4, SC6_1..SC6_4 hanno i bordi non puliti (misura dell'agente separato: ampiezza fino a 0,54 nei primi/ultimi 50 ms): richieste come _R2; nel montaggio ogni voce ha comunque dissolvenza di 30 ms.")
else:
    voci="Tutte le voci nuove sono arrivate e sono state montate (BENV1_R2, MP1, MP23, MP4, COMP1, COMP2)."'''
assert old in s
open('/home/user/work/build/rapporto.py', 'w').write(s.replace(old, new))
