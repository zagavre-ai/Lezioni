# -*- coding: utf-8 -*-
# Mappe della lezione 4 ridisegnate con kit/tools/mappa.py (testo dalle mappe del prof / dalle sue slide). Uso: python3 maps.py N [N...]
import json, os, sys, wave, subprocess
sys.path.insert(0, '/tmp/claude-0/l17')
KIT = '/home/user/w/b04/kit/tools'
VOX = '/home/user/w/vox17/scambio/storia-V-lez17/vox'
OUT = '/home/user/w/l17/work/maps'
T = {x['nome']: x['testo'] for x in json.load(open('/home/user/w/vox17/scambio/storia-V-lez17/testi_voci.json'))}
R = lambda c, p='', e='', s=None: dict(concetto=c, parola=p, esempio=e, **({'sotto': s} if s else {}))
# n argomento -> (voce, centro, [(ramo, chiave nella voce)])
M = {
 1: ('MPR1', "La crisi degli anni Settanta", [
     (R("Guerra del Kippur", "causata da", "attacco di Egitto e Siria a Israele (1973)"), "Kippur"),
     (R("Aumento del prezzo del petrolio", "provoca"), "aumento"),
     (R("Calo della produzione", "da cui deriva"), "calo"),
     (R("Disoccupazione", "da cui deriva"), "disoccupazione"),
     (R("Inflazione", "da cui deriva"), "inflazione")]),
 2: ('MAPN2', "Tensioni e accordi in Medio Oriente", [
     (R("Camp David", "1978", "accordi tra Sadat e Begin"), "camp David"),
     (R("Libano", "1975-1982", "guerra civile e invasione israeliana"), "libano:"),
     (R("Intifada", "1987", "rivolta palestinese e Hamas"), "intifada:")]),
 3: ('MAPN3', "Iran e guerra con l'Iraq", [
     (R("Caduta dello Shah", "1979", "rivoluzione popolare"), "caduta dello shah"),
     (R("Repubblica Islamica", "Khomeini", "teocrazia basata sulla sharia"), "repubblica islamica"),
     (R("Crisi degli ostaggi", "1979", "assalto all'ambasciata americana"), "crisi degli ostaggi"),
     (R("Guerra Iran-Iraq", "1980-1988", "quasi due milioni di morti"), "guerra iran-iraq")]),
 4: ('MAPN4', "Da Nixon a Reagan", [
     (R("Apertura alla Cina", "1972", "Nixon e Mao contro l'URSS"), "apertura alla cina"),
     (R("Distensione", "SALT I", "accordi di Helsinki"), "distensione"),
     (R("Watergate e Carter", "1974", "dimissioni di Nixon"), "watergate e carter"),
     (R("Svolta di Reagan", "1981", "linea dura e scudo spaziale"), "svolta di reagan")]),
 5: ('MAPN5', "America Latina", [
     (R("Cile", "1973", "golpe di Pinochet"), "cile:"),
     (R("Argentina", "1976-1983", "i desaparecidos"), "argentina:"),
     (R("Ritorno alla democrazia", "1982", "crisi e sconfitta nelle Falkland"), "ritorno alla democrazia:")]),
 6: ('MPR2', "Il neoliberismo", [
     (R("Meno Stato, più mercato", "critica", "l'intervento dello Stato"), "critica"),
     (R("Servizi ai privati", "pratica"), "affidamento"),
     (R("Riduzione delle tasse", "promette"), "riduzione delle tasse"),
     (R("Reagan", "Stati Uniti", "dal 1981 al 1988"), "Reagan"),
     (R("Thatcher", "Regno Unito", "dal 1979 al 1990"), "Thatcher")]),
 7: ('MPR3', "Michail Gorbačev", [
     (R("Trasparenza e ristrutturazione", "riforme (1985)"), "Introduce"),
     (R("Autonomia dell'Est europeo", "riconosce"), "Riconosce"),
     (R("Caduta del Muro di Berlino", "9 novembre 1989"), "Muro"),
     (R("Tentativo di colpo di Stato", "1991"), "tentativo"),
     (R("Fine dell'URSS", "dicembre 1991"), "dissoluzione dell'Unione")]),
 8: ('MAPN8', "La svolta della Cina", [
     (R("Riforme di Deng", "Quattro modernizzazioni", "la Cina si apre al capitalismo"), "riforme di deng"),
     (R("Nessuna apertura politica", "Partito Comunista", "controllo assoluto dello Stato"), "nessuna apertura"),
     (R("Piazza Tienanmen", "1989", "carri armati contro i manifestanti"), "piazza tienanmen")]),
}
def vdur(nome):
    w = wave.open(f'{VOX}/{nome}.wav'); return w.getnframes() / w.getframerate()

def build(n, total_s):
    voce, centro, rami = M[n]; testo = T[voce]; d = vdur(voce)
    os.makedirs(f'{OUT}/{n}', exist_ok=True)
    j = dict(materia='Storia V', docente='Prof. Giorgio Mazzotti', titolo=centro, rami=[r for r, _ in rami])
    json.dump(j, open(f'{OUT}/{n}/mappa.json', 'w'), ensure_ascii=False, indent=1)
    low = testo.lower(); tempi = []
    for _, key in rami:
        p = low.find(key.lower()); p = max(p, 0)
        tempi.append(round(0.5 + d * p / len(testo) * 0.98 + 0.4, 2))   # voce parte a 0,5 s
    tempi[0] = max(tempi[0], 1.0)
    subprocess.run(['python3', f'{KIT}/mappa.py', f'{OUT}/{n}/mappa.json', '--out', f'{OUT}/{n}', '--durata', f'{total_s:.3f}', '--tempi', ','.join(map(str, tempi))], check=True, capture_output=True, env=dict(os.environ, PLAYWRIGHT_BROWSERS_PATH='/opt/pw-browsers'))
    print(n, voce, 'voce %.1f s' % d, 'tempi', tempi, flush=True)

if __name__ == '__main__':
    tl = json.load(open('/home/user/w/l17/work/piece_n.json'))
    for n in map(int, sys.argv[1:]): build(n, tl[f'mappa{n}'] / 30)
