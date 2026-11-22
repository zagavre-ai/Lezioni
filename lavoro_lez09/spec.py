import json,re
SEG=json.load(open('/home/user/Lezioni/w/trascr.json'))
def mmss(s):
    m,x=s.split(':');return int(m)*60+float(x)
def seg_at(s):
    t=mmss(s) if isinstance(s,str) else s
    return min(range(len(SEG)),key=lambda i:abs(SEG[i]['inizio']-t))
def S0(s):return SEG[seg_at(s)]['inizio']
def E_before(s):return SEG[seg_at(s)-1]['fine']
# argomenti: (n, titolo argomento, inizio, fine) ; fine = fine del segmento PRIMA del segmento indicato
ARGS=[
 (0,'INTRO','0:02','1:47'),
 (1,'La svolta autoritaria e le «Leggi Fascistissime»','1:47','5:07'),
 (2,'La fascistizzazione dello Stato e le misure repressive','5:07','14:59'),
 (3,'Il consolidamento del potere e la fabbrica del consenso','14:59','22:56'),
 (4,'L’educazione e la fascistizzazione della gioventù','22:56','28:02'),
 (5,'La riforma scolastica Gentile e i libri di testo','28:02','31:59'),
 (6,'Il controllo dei media e i Patti Lateranensi','32:01','36:16'),
 (7,'Politica economica: il corporativismo','36:16','41:28'),
 (8,'Quota 90, agricoltura e autarchia','41:28','48:04'),
 (9,'Ruolo della donna e demografia','48:04','50:43'),
 (10,'L’Impero coloniale e le Leggi Razziali','50:43','60:18'),
 (11,'RIEPILOGO','60:18','67:00'),
]
def arg_range(n):
    a=[x for x in ARGS if x[0]==n][0]
    i0=seg_at(a[2]);
    if n==0:return 0.45,SEG[seg_at(a[3])-1]['fine']
    i1=seg_at(a[3])-1 if a[3]!='67:00' else len(SEG)-1
    return SEG[i0]['inizio'],SEG[i1]['fine']

PDF=json.load(open('/home/user/Lezioni/w/lav/pdf_cards.json'))
def card(p,i):return PDF[str(p)]['cards'][i]
# per argomento: lista di (pagina,indice card,ancora) in ordine di tempo; immagini (jpg,da,a,didascalia)
CARDS={
 1:[(2,0,'2:04'),(2,1,'2:25'),(2,2,'2:40'),(2,3,'4:33')],
 2:[(3,0,'5:07'),(3,1,'7:14'),(3,2,'7:47'),(3,3,'8:59'),(3,4,'11:28')],
 3:[(4,0,'15:03'),(4,1,'15:31'),(4,2,'17:53'),(4,3,'19:22')],
 4:[(7,0,'23:47'),(7,1,'24:12'),(7,2,'25:15'),(7,3,'26:59')],
 5:[(9,0,'28:39'),(9,1,'28:54'),(9,2,'29:55')],
 6:[(10,0,'32:01'),(10,1,'32:23'),(10,2,'33:52')],
 7:[(13,1,'36:28'),(13,0,'38:05'),(13,1,'40:23')],
 8:[(15,0,'41:28'),(13,2,'42:05'),(15,1,'42:49'),(13,3,'44:34'),(15,2,'46:57')],
 9:[(12,1,'48:20'),(12,0,'48:38'),(12,3,'48:56'),(12,2,'49:01'),(12,4,'50:01')],
 10:[(15,3,'50:43'),(17,0,'52:52'),(17,1,'53:10'),(17,2,'55:23'),(17,3,'58:50'),(17,4,'59:04')],
}
IMMAGINI={3:[('i-005.jpg','20:12','21:01'),('i-006.jpg','21:02','21:22')],
          4:[('i-010.jpg','25:44','25:54')],6:[('i-014.jpg','34:03','34:27')],
          8:[('i-018.jpg','42:08','42:29'),('i-021.jpg','46:26','46:37')],10:[('i-024.jpg','53:31','54:20')]}
