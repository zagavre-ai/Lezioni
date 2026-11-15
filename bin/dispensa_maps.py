# Inserisce le mappe nella dispensa: «Mappa della lezione» dopo la copertina, e la mappa di ogni argomento in fondo alla sua sezione.
import sys, json, importlib.util, os
from pypdf import PdfReader, PdfWriter
sys.path.insert(0, '/home/claude/w/bin')
NN = sys.argv[1]; from conf import CONF
C = CONF[NN]; N = C['N']; D = f'/home/claude/w/l{NN}/'
sp = importlib.util.spec_from_file_location('spec', D + 'spec.py'); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
U = json.load(open(D + 'unita.json')); base = D + f'out/Letteratura_Lez{N}_dispensa_A4.pdf'
r = PdfReader(base)
fin = [a for a in m.AN if a.get('finale')][0]['id']
mp = {}
for a in m.AN:
    if a['kind'] == 'mappa' and not a.get('finale'): mp[int(a['dopo'][1:])] = a['id']   # l'ultima mappa dell'argomento
w = PdfWriter(); w.add_page(r.pages[0]); w.add_page(PdfReader(D + f'an/{fin}_dispensa.pdf').pages[0])
i = 1
for u in U:
    for _ in u['pages']:
        w.add_page(r.pages[i]); i += 1
    if u['k'] in mp: w.add_page(PdfReader(D + f'an/{mp[u["k"]]}_dispensa.pdf').pages[0])
while i < len(r.pages): w.add_page(r.pages[i]); i += 1
o = D + f'out/Letteratura_Lez{N}_dispensa_A4_mappe.pdf'; w.write(o); print(o, len(w.pages), 'pagine')
