# confini dei pezzi della prof (secondi sull'originale) e mappa dei tempi dopo l'accorciamento delle pause
import json,re
L='/home/user/lav/lez01/'
SIL=json.load(open(L+'silenzi.json'))
def sil_tra(a,b):return [(x,y) for x,y in SIL if x>=a-0.01 and y<=b+0.01]
# (inizio pezzo, fine pezzo) per argomento 1..10  [secondi]
PEZZI={
 0:(0.0,20.85),
 1:(20.88,300.95), 2:(301.50,824.65), 3:(825.36,1221.85), 4:(1221.82,1758.2),
 5:(1758.54,2100.8), 6:(2104.47,2422.42), 7:(2422.41,2781.23), 8:(2784.12,3178.33), 9:(3179.08,3841.40), 10:(3841.91,4466.6)}
def pause_da_tagliare(a,b,W):
    """silenzi interni a [a,b] >1.2 s e subito dopo una parola che chiude frase -> (inizio_taglio, fine_taglio): si tiene 0,3 s per lato"""
    out=[]
    for x,y in SIL:
        if x<a+0.3 or y>b-0.3 or y-x<=1.2:continue
        prec=[w for t,w,_ in W if t<=x+0.05]
        if prec and re.search(r'[.?!]$',prec[-1]):
            out.append((x+0.3,y-0.3))
    return out
def intervalli(a,b,W):
    cuts=pause_da_tagliare(a,b,W);iv=[];c=a
    for x,y in cuts:iv.append((c,x));c=y
    iv.append((c,b));return iv
class Mappa:
    def __init__(s,iv):
        s.iv=iv;s.off=[];t=0
        for x,y in iv:s.off.append(t);t+=y-x
        s.dur=t
    def __call__(s,t):
        for (x,y),o in zip(s.iv,s.off):
            if t<=y:return o+max(0,t-x)
        return s.dur
