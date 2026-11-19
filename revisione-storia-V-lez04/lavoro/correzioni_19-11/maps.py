# -*- coding: utf-8 -*-
# Mappe della lezione 4 ridisegnate con kit/tools/mappa.py (testo dalle mappe del prof / dalle sue slide). Uso: python3 maps.py N [N...]
import json, os, sys, wave, subprocess
sys.path.insert(0, '/tmp/claude-0/w')
KIT = '/home/user/w/b04/kit/tools'
VOX = '/home/user/w/vox04/scambio/storia-V-lez04/vox'
OUT = '/home/user/w/l04/work/maps'
T = {x['nome']: x['testo'] for x in json.load(open('/home/user/w/vox04/scambio/storia-V-lez04/testi_voci.json'))}
R = lambda c, p='', e='', s=None: dict(concetto=c, parola=p, esempio=e, **({'sotto': s} if s else {}))
# n argomento -> (voce, centro, [(ramo, chiave nella voce)])
M = {
 1: ('MAP1', "L'Europa all'inizio del Novecento", [
     (R("Alleanze contrapposte", "è divisa in", "Triplice alleanza e Triplice intesa"), "alleanze contrapposte"),
     (R("Guglielmo II di Germania", "destabilizza", "politica estera e coloniale aggressiva"), "Guglielmo"),
     (R("Crisi dell'Impero ottomano", "destabilizza", "concorrenza tra Austria-Ungheria e Russia"), "crisi dell'Impero")]),
 2: ('MAPN2', "Le crisi coloniali e i Balcani", [
     (R("Crisi marocchine", "1905 e 1911", "Francia e Germania vicine allo scontro"), "Primo ramo"),
     (R("Giovani Turchi", "1908", "indebolimento dell'Impero ottomano"), "Secondo"),
     (R("Crisi bosniaca", "1908", "annessione della Bosnia-Erzegovina"), "Terzo"),
     (R("Guerre balcaniche", "1912-1913", "Stati balcanici contro l'Impero ottomano"), "Quarto"),
     (R("Polveriera d'Europa", "Balcani", "scontro tra Austria e Russia"), "Infine")]),
 3: ('MAP2', "L'attentato di Sarajevo", [
     (R("Alleanze contrapposte", "fa scattare"), "alleanze contrapposte"),
     (R("Attacco tedesco alla Francia", "con"), "attacco tedesco"),
     (R("Battaglie a est", "con", "Tannenberg, laghi Masuri, Leopoli"), "battaglie di Tannenberg"),
     (R("Guerra di posizione", "cui segue", "nelle trincee"), "Poi la guerra di posizione")]),
 4: ('MAPN4', "I fronti e la trincea", [
     (R("Guerra di movimento fallita", "Schlieffen", "fermato sulla Marna"), "guerra di movimento"),
     (R("Guerra di posizione", "trincee", "800 chilometri di trincee"), "Nasce la guerra di posizione"),
     (R("Fronte orientale", "russi", "sconfitti a Tannenberg e Masuri"), "A est"),
     (R("Nuove armi", "assalti", "mitragliatrici, artiglieria, filo spinato, gas"), "Le nuove armi"),
     (R("Inferno delle trincee", "traumi", "fango, malattie, traumi psicologici"), "Nelle trincee")]),
 5: ('MAP3', "L'Italia", [
     (R("Liberali conservatori", "interventisti", "firmano il Patto di Londra"), "liberali conservatori"),
     (R("Nazionalisti", "interventisti", "manifestazioni per l'intervento"), "nazionalisti, che"),
     (R("Liberali progressisti", "neutralisti"), "liberali progressisti"),
     (R("Socialisti", "neutralisti"), "socialisti.")]),
 6: ('MAP4', "La Prima guerra mondiale", [
     (R("Guerra globale e totale", "è una"), "guerra globale e totale"),
     (R("1916", "nel", "gigantesche e inutili battaglie"), "Nel millenovecentosedici"),
     (R("1917", "nel", "", ["ritiro della Russia", "intervento degli Stati Uniti"]), "Nel millenovecentodiciassette")]),
 7: ('MAPN7', "La guerra totale", [
     (R("Mobilitazione economica", "produzione", "controllo e razionamento"), "Primo ramo"),
     (R("Fronte interno", "civili", "privazioni e mercato nero"), "Secondo"),
     (R("Donne in fabbrica", "emancipazione", "lavoro e diritti"), "Terzo"),
     (R("Guerra sui mari", "blocco", "blocco navale e sottomarini"), "Quarto"),
     (R("Genocidio degli armeni", "1915", "oltre un milione di vittime"), "Infine")]),
 8: ('MAPN8', "Il 1917", [
     (R("Russia fuori dalla guerra", "Brest-Litovsk", "pace con gli Imperi centrali"), "Primo ramo"),
     (R("Stati Uniti in guerra", "aprile", "a fianco dell'Intesa"), "Secondo"),
     (R("Caporetto", "disfatta", "crollo delle linee italiane"), "Terzo"),
     (R("Resistenza sul Piave", "Grappa", "nuova linea difensiva"), "Quarto"),
     (R("Svolta di Diaz", "Cadorna", "migliori condizioni dei soldati"), "Infine")]),
 9: ('MAP5', "L'anno 1918", [
     (R("Offensiva tedesca", "inizia con", "l'Intesa risponde ad Amiens"), "offensiva tedesca"),
     (R("Sconfitta austriaca", "fronte italiano", "armistizio del 4 novembre 1918"), "sconfitta austriaca"),
     (R("Rivoluzione in Germania", "porta a", "armistizio dell'11 novembre 1918"), "rivoluzione in Germania")]),
 10: ('MAP6', "La Conferenza di pace di Parigi", [
     (R("Quattordici punti di Wilson", "ispirata da", "autodeterminazione dei popoli"), "Quattordici punti"),
     (R("Società delle Nazioni", "che sostengono", "nuovo organismo internazionale"), "Società delle Nazioni"),
     (R("Francia e Regno Unito", "condizionata da"), "condizionata"),
     (R("Pace punitiva", "che vogliono", "per la Germania"), "punitiva")]),
 11: ('MAPN11', "Il bilancio della guerra", [
     (R("Diciassette milioni di morti", "umano", "soprattutto giovani"), "diciassette milioni"),
     (R("Influenza spagnola", "dopo la guerra", "oltre 40 milioni di vittime"), "influenza spagnola"),
     (R("Mutilati", "40 milioni di feriti", "simbolo della guerra industriale"), "feriti"),
     (R("Smobilitazione dei reduci", "difficile", "Stati impoveriti, poco lavoro"), "smobilitazione"),
     (R("Nostalgia delle trincee", "traumi", "nevrosi e cameratismo"), "nostalgia")]),
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
    tl = json.load(open('/home/user/w/l04/work/piece_n.json'))
    for n in map(int, sys.argv[1:]): build(n, tl[f'mappa{n}'] / 30)
