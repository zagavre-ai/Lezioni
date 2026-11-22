import sys,json;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from assembla import *
import scene_doc as SD
from dati import DID
CFG={
 'AP1':[dict(s=(0,),img=lambda:viz_text(['1830 → 1880','Un mondo che cambia']),chips=['Trasformazioni economiche','Trasformazioni sociali','Trasformazioni politiche e tecniche'],titolo='Un mondo che cambia in fretta'),
        dict(s=(2,),img=lambda:viz_text(['Racconto oggettivo','senza idealizzazione']),chips=['Obiettivo: raccontare la realtà','Evitare ogni idealizzazione','Denuncia sociale'],titolo="Il Realismo guarda la realtà"),
        dict(s=(4,),img=lambda:viz_text(['Emarginati','Umili lavoratori','Militari e borghesi']),chips=['Quotidianità di emarginati','Umili lavoratori delle campagne e delle città','Militari e borghesi'],titolo='I nuovi soggetti'),
        dict(s=(5,),img=lambda:viz_text(['Balzac','Flaubert','Émile Zola']),chips=['Balzac','Flaubert','Émile Zola'],titolo='Anche la letteratura')],
 'AP2':[dict(s=(0,),img='crystal',didasc=DID['crystal'],chips=['1851 · Londra, Hyde Park','Prima Esposizione universale','Joseph Paxton'],titolo='Il Crystal Palace'),
        dict(s=(2,),img=lambda:crop_img('crystal',(0.1,0.35,0.95,0.85)),didasc=DID['crystal'],chips=['Moduli prefabbricati','Facilmente assemblabili','Ferro, ghisa e vetro'],titolo='La vera rivoluzione'),
        dict(s=(3,),img=lambda:viz_text(['Più abitanti','Città sovraffollate']),chips=['Forte incremento demografico','Rischio di epidemie','Disagi sociali'],titolo='Le città crescono'),
        dict(s=(4,),img='parigi',didasc=DID['parigi'],chips=['Dal 1853 · Haussmann','Larghi viali alberati: i boulevards','Scopo politico: niente barricate'],titolo='Il piano di Haussmann')],
 'AP3':[dict(s=(0,),img=lambda:viz_text(['Unificazione','Industrializzazione','Ferrovie']),chips=['Classe operaia','Ascesa della borghesia','Nuovi quartieri borghesi'],titolo="L'Italia che cambia"),
        dict(s=(3,),img='galleria',didasc=DID['galleria'],chips=['Galleria Vittorio Emanuele II','Giuseppe Mengoni','Milano'],titolo='Stazioni, mercati e gallerie'),
        dict(s=(4,),img=lambda:viz_text(['Eclettismo','dal greco: scegliere']),chips=['Gli stili del passato come repertorio','Scelta in base alla funzione','Neogotico per le cattedrali'],titolo="L'Eclettismo"),
        dict(s=(6,),img='opera',didasc=DID['opera'],chips=["Teatro dell'Opéra · Charles Garnier",'Brighton Pavilion · John Nash'],titolo='Esempi emblematici')],
 'AP4':[dict(s=(0,),img=lambda:viz_text(['En plein air','Barbizon']),chips=['Pittura all\'aperto','Rousseau, Millet e Corot','Foresta di Fontainebleau'],titolo='La Scuola di Barbizon'),
        dict(s=(2,),img='spigolatrici',didasc=DID['spigolatrici'],chips=['Scene di vita nei campi','Solennità quasi sacra'],titolo='Jean-François Millet'),
        dict(s=(3,),img='spaccapietre',didasc=DID['spaccapietre'],chips=['Gustave Courbet','Denuncia sociale','Fatica e povertà senza idealizzazione'],titolo='Gustave Courbet'),
        dict(s=(5,),img='atelier',didasc=DID['atelier'],chips=["L'atelier del pittore",'Allegoria reale'],titolo='Un\'opera monumentale')],
 'AP5':[dict(s=(0,),img='vagone',didasc=DID['vagone'],chips=['Honoré Daumier','Disegni satirici e caricature','Critica politica e sociale'],titolo='Il vagone di terza classe'),
        dict(s=(2,),img=lambda:viz_text(['Caffè Michelangiolo','Firenze: la macchia']),chips=['Rifiuto del disegno accademico','Macchie di colore','Contrasti di luce e ombra'],titolo='I Macchiaioli'),
        dict(s=(4,),img='invedetta',didasc=DID['invedetta'],chips=['Giovanni Fattori','Fatica del lavoro e vita militare','Senza retorica eroica'],titolo='In vedetta'),
        dict(s=(5,),img=lambda:viz_text(['Silvestro Lega','Telemaco Signorini']),chips=['Lega: atmosfere domestiche calme e delicate','Signorini: i margini della società'],titolo='Gli altri protagonisti')],
 'SPIE':[dict(s=(0,),img=lambda:viz_text(['Ripasso','della Parte 1']),chips=['Tre argomenti','Dal progresso all\'Eclettismo'],titolo='Prima di continuare'),
         dict(s=(1,),img=lambda:viz_text(['1830 → 1880','Racconto oggettivo']),chips=['Trasformazioni economiche, sociali, politiche e tecniche','Denuncia sociale'],titolo='Le nuove sfide del progresso'),
         dict(s=(4,),img='crystal',didasc=DID['crystal'],chips=['Crystal Palace · Joseph Paxton','Ferro, ghisa e vetro'],titolo='Ferro, vetro e urbanistica'),
         dict(s=(6,),img='parigi',didasc=DID['parigi'],chips=['Haussmann · boulevards','Niente barricate'],titolo='Parigi dal 1853'),
         dict(s=(7,),img='galleria',didasc=DID['galleria'],chips=['Unificazione e industrializzazione','Galleria Vittorio Emanuele II'],titolo="L'Italia che cambia"),
         dict(s=(9,),img='opera',didasc=DID['opera'],chips=["Eclettismo: dal greco «scegliere»","Teatro dell'Opéra · Charles Garnier"],titolo="L'Eclettismo")]}
def crop_img(nome,v):
    im=Image.open(IMG+nome+'.png').convert('RGB');w,h=im.size
    return im.crop((round(v[0]*w),round(v[1]*h),round(v[2]*w),round(v[3]*h)))
def ap(n):
    bs=[]
    for b in CFG[n]:
        b=dict(b);im=b['img'];b['img']=im() if callable(im) else im;bs.append(b)
    # ap_piece usa la chiave dei beat: le immagini PIL non sono serializzabili -> segnaposto
    key=json.dumps([(b['s'],str(b['img']) if isinstance(b['img'],str) else 'viz',b['chips'],b['titolo']) for b in bs])
    return ap_piece(n,bs,tag=key)
def scene_pieces(prefix,names):
    kI=json.load(open('/tmp/w/b/kI.json'))['kI'];P={s['nome']:s for s in piano_scene(kI)}
    return [(n,build_scene(P[n])) for n in names]
