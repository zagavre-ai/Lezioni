import sys;sys.path.insert(0,'/tmp/w/b')
from dispensa import *
H=[cover_disp('MAPPE')]
for k in (1,2,3,4):
    m=MAPPE_PROF[k];H.append(map_html(m['titolo'],m['nodes'],m['edges'],set(m['nodes']),set()))
make_pdf(H,sys.argv[1])
