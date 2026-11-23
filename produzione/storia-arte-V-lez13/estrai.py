#!/usr/bin/env python3
# Scarica dalla release SOLO i file che servono, anche se stanno dentro uno zip grande (lettura a pezzi via HTTP).
# Uso:
#   python3 estrai_da_release.py <tag> --elenca                      -> file della release e contenuto degli zip
#   python3 estrai_da_release.py <tag> "<pezzo del nome>" <cartella>  -> scarica i file (o i membri degli zip) che contengono quel testo
# Esempio: python3 estrai_da_release.py moda-chimica-III-IV "Lezione 3/" /home/claude/chim03
import sys, os, subprocess, struct, json, zlib
R = 'zagavre-ai/lezioni'
T=''
def api(p): return json.loads(subprocess.run(['curl','-sS','https://api.github.com/'+p], capture_output=True, text=True).stdout)
def url(aid):
    return subprocess.run(['curl', '-sS', '-o', '/dev/null', '-w', '%{redirect_url}', '-H',
                           'Accept: application/octet-stream', f'https://api.github.com/repos/{R}/releases/assets/{aid}'],
                          capture_output=True, text=True).stdout
def rng(u, a, b): return subprocess.run(['curl', '-sS', '--retry', '5', '-r', f'{a}-{b}', u], capture_output=True).stdout
def scarica(u, out, size):
    for _ in range(8):
        subprocess.run(['curl', '-sS', '--retry', '5', '-C', '-', '-o', out, u])
        if os.path.exists(out) and os.path.getsize(out) == size: return
        u = None or u
    raise SystemExit(f'download incompleto: {out}')
def membri(u, size):
    tail = rng(u, max(0, size - 70000), size - 1); i = tail.rfind(b'PK\x05\x06')
    cd_size, cd_off = struct.unpack('<II', tail[i + 12:i + 20])
    if cd_off == 0xFFFFFFFF:
        j = tail.rfind(b'PK\x06\x06'); cd_size, cd_off = struct.unpack('<QQ', tail[j + 40:j + 56])
    cd = rng(u, cd_off, cd_off + cd_size - 1); p = 0; out = []
    while p + 46 <= len(cd) and cd[p:p + 4] == b'PK\x01\x02':
        met = struct.unpack('<H', cd[p + 10:p + 12])[0]
        csz, usz = struct.unpack('<II', cd[p + 20:p + 28]); n, e, c = struct.unpack('<HHH', cd[p + 28:p + 34])
        loff = struct.unpack('<I', cd[p + 42:p + 46])[0]; nm = cd[p + 46:p + 46 + n].decode('utf-8', 'replace')
        ex = cd[p + 46 + n:p + 46 + n + e]; q = 0
        while q + 4 <= len(ex):  # zip64: dimensioni e offset veri
            hid, hl = struct.unpack('<HH', ex[q:q + 4]); d = ex[q + 4:q + 4 + hl]; k = 0
            if hid == 1:
                if usz == 0xFFFFFFFF: usz = struct.unpack('<Q', d[k:k + 8])[0]; k += 8
                if csz == 0xFFFFFFFF: csz = struct.unpack('<Q', d[k:k + 8])[0]; k += 8
                if loff == 0xFFFFFFFF: loff = struct.unpack('<Q', d[k:k + 8])[0]; k += 8
            q += 4 + hl
        out.append(dict(nome=nm, metodo=met, csz=csz, usz=usz, off=loff)); p += 46 + n + e + c
    return out
def estrai(u, m, cartella):
    h = rng(u, m['off'], m['off'] + 29); n, e = struct.unpack('<HH', h[26:30]); ini = m['off'] + 30 + n + e
    out = os.path.join(cartella, os.path.basename(m['nome'])); tmp = out + '.parte'
    pos = os.path.getsize(tmp) if os.path.exists(tmp) else 0; blocco = 64 << 20
    with open(tmp, 'ab') as f:
        while pos < m['csz']:
            b = rng(u, ini + pos, ini + min(m['csz'], pos + blocco) - 1)
            if not b: u = None; raise SystemExit('connessione persa: rilancia, riprende da dove era')
            f.write(b); pos += len(b)
    if m['metodo'] == 0: os.replace(tmp, out)
    else:
        d = zlib.decompressobj(-15)
        with open(tmp, 'rb') as fi, open(out, 'wb') as fo:
            while True:
                b = fi.read(16 << 20)
                if not b: break
                fo.write(d.decompress(b))
            fo.write(d.flush())
        os.remove(tmp)
    if os.path.getsize(out) != m['usz']: raise SystemExit(f'dimensione sbagliata: {out}')
    print('OK', out, round(m['usz'] / 1048576), 'MB')
if __name__ == '__main__':
    tag = sys.argv[1]; rel = api(f'repos/{R}/releases/tags/{tag}')
    elenca = sys.argv[2] == '--elenca'
    if not elenca: chiave, cartella = sys.argv[2], sys.argv[3]; os.makedirs(cartella, exist_ok=True)
    for a in rel['assets']:
        u = url(a['id'])
        if elenca: print('·', a['name'], round(a['size'] / 1048576), 'MB')
        if a['name'].lower().endswith('.zip'):
            for m in membri(u, a['size']):
                if elenca: print('   ', m['nome'], round(m['usz'] / 1048576), 'MB')
                elif chiave in m['nome'] and not m['nome'].endswith('/'):
                    estrai(url(a['id']), m, cartella)
        elif not elenca and chiave in a['name']:
            out = os.path.join(cartella, a['name']); scarica(u, out, a['size']); print('OK', out)
