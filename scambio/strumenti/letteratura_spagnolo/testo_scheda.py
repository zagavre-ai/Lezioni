# testo_scheda.py VIDEO t VOCE_TESTO -> testo della scheda bianca (OCR) con gli accenti presi dalla voce per le parole minuscole
import sys,subprocess,re,unicodedata
def strip(w): return ''.join(c for c in unicodedata.normalize('NFD',w) if unicodedata.category(c)!='Mn').lower()
def ocr(V,t):
    png=subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',V,'-frames:v','1','-vf','crop=1700:560:90:300,scale=2550:-1,format=gray','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
    return subprocess.run(['tesseract','stdin','stdout','--psm','6'],input=png,capture_output=True).stdout.decode()
def testo(V,t,voce):
    o=ocr(V,t); o=re.sub(r'-\n(\w)',r'\1',o); o=' '.join(l.strip() for l in o.split('\n') if l.strip())
    o=o.replace('|','I')
    vw={}; esatte=set(w.lower() for w in re.findall(r"[\wÀ-ÿ]+",voce))
    for w in re.findall(r"[\wÀ-ÿ]+",voce):
        if w!=strip(w): vw.setdefault(strip(w),w.lower())
    def fix(m):
        w=m.group(0); s=strip(w)
        if w[:1].isupper() and w[1:2].islower() is False: return w
        if w.lower() in esatte: return w
        v=vw.get(s)
        if v and not w[:1].isupper(): return v
        if v and w[:1].isupper() and v[-1:] in 'àèéìòù' and len(v)<=4: return v[0].upper()+v[1:]  # È
        return w
    o=re.sub(r"[\wÀ-ÿ]+",fix,o)
    o=re.sub(r"\bI'(?=[A-Za-zÀ-ÿ])","l'",o)
    return o
if __name__=='__main__':
    print(testo(sys.argv[1],float(sys.argv[2]),open(sys.argv[3]).read() if len(sys.argv)>3 else ''))

import difflib
def tok(t): return re.findall(r"[\wÀ-ÿ']+|[^\w\sÀ-ÿ']",t)
def allinea(voce,ocr):
    # testo finale = voce (accenti, frasi giuste) ma dove la voce scrive un nome «come si pronuncia» si prende la scrittura vera dell'OCR
    v=tok(voce); o=tok(ocr)
    sm=difflib.SequenceMatcher(None,[strip(x) for x in v],[strip(x) for x in o],autojunk=False)
    out=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': out+=v[i1:i2]
        elif op=='replace' and (i2-i1)<=4 and (j2-j1)<=6 and all(re.fullmatch(r"[A-ZÀ-Ý][a-zà-ÿ']{2,}|[a-zà-ÿ']{3,}|1\d{3}|20\d{2}",x) for x in o[j1:j2]) and any(re.fullmatch(r"[A-ZÀ-Ý][a-zà-ÿ']{2,}|1\d{3}|20\d{2}",x) for x in o[j1:j2]):
            out+=o[j1:j2]
        elif op=='delete' or op=='replace': out+=v[i1:i2]
    s=' '.join(out)
    s=re.sub(r"\s+([.,;:!?»)])",r"\1",s); s=re.sub(r"([«(])\s+",r"\1",s); s=re.sub(r"(\w)'\s+",r"\1'",s)
    return s
