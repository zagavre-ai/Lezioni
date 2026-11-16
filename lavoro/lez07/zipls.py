import sys, struct, subprocess, io, zipfile
url=sys.argv[1]; size=int(sys.argv[2])
def rng(a,b):
    return subprocess.run(['curl','-sSL','-r',f'{a}-{b}',url],capture_output=True,check=True).stdout
tail=rng(size-4*1024*1024,size-1)
# find EOCD / zip64
i=tail.rfind(b'PK\x05\x06')
cd_size,cd_off=struct.unpack('<II',tail[i+12:i+20])
if cd_off==0xffffffff:
    j=tail.rfind(b'PK\x06\x06')
    cd_size,cd_off=struct.unpack('<QQ',tail[j+40:j+56])
base=size-len(tail)
if cd_off<base:
    cd=rng(cd_off,cd_off+cd_size-1)
else:
    cd=tail[cd_off-base:cd_off-base+cd_size]
p=0
while p<len(cd) and cd[p:p+4]==b'PK\x01\x02':
    comp,csz,usz=struct.unpack('<HII',cd[p+10:p+12]+cd[p+20:p+28])
    nl,el,cl=struct.unpack('<HHH',cd[p+28:p+34])
    off=struct.unpack('<I',cd[p+42:p+46])[0]
    name=cd[p+46:p+46+nl].decode('utf8','replace')
    ex=cd[p+46+nl:p+46+nl+el]
    # zip64 extra
    q=0
    while q<len(ex):
        hid,hl=struct.unpack('<HH',ex[q:q+4])
        if hid==1:
            vals=ex[q+4:q+4+hl]; k=0
            if usz==0xffffffff: usz=struct.unpack('<Q',vals[k:k+8])[0];k+=8
            if csz==0xffffffff: csz=struct.unpack('<Q',vals[k:k+8])[0];k+=8
            if off==0xffffffff: off=struct.unpack('<Q',vals[k:k+8])[0];k+=8
        q+=4+hl
    print(f'{off}\t{csz}\t{usz}\t{comp}\t{name}')
    p+=46+nl+el+cl
