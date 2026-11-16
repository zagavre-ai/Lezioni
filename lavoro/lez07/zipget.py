# uso: zipget.py URL OFFSET CSIZE OUT  (estrae una voce deflate da uno zip remoto, in streaming)
import sys,subprocess,struct,zlib
url,off,csz,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
p=subprocess.Popen(['curl','-sSL','--retry','5','-r',f'{off}-{off+30+65535+csz}',url],stdout=subprocess.PIPE)
h=p.stdout.read(30);assert h[:4]==b'PK\x03\x04',h[:4]
meth=struct.unpack('<H',h[8:10])[0];nl,el=struct.unpack('<HH',h[26:30]);p.stdout.read(nl+el)
d=zlib.decompressobj(-15) if meth==8 else None;left=csz
with open(out+'.part','wb') as f:
    while left>0:
        b=p.stdout.read(min(1<<20,left))
        if not b: raise SystemExit('troncato')
        left-=len(b);f.write(d.decompress(b) if d else b)
    if d: f.write(d.flush())
p.kill()
import os;os.rename(out+'.part',out);print('ok',out)
