# Numerazione pagine unica per video e dispensa (solo le schede bianche hanno il piè di pagina)
import sys; sys.path.insert(0, '/home/user/w18')
from piano import PEZZI
ORDINE = []   # chiavi in ordine di comparsa
_seen = set()
def _add(k):
    if k not in _seen: _seen.add(k); ORDINE.append(k)
for pid, a, b, arg, st in PEZZI:
    for _, sid, _ in st: _add(sid)
    if arg in ('A1','A2','A3','A4','A5','A6','A7'): _add('AP_' + arg)
    if arg == 'A4': _add('MAP2')
    if arg == 'A7': _add('MAP3')
_add('MAP1')
PG = {k: i + 1 for i, k in enumerate(ORDINE)}
if __name__ == '__main__': print(PG)
