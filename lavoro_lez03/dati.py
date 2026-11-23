# Dati della lezione 3 · Il Realismo: testo delle slide del prof (parole sue), didascalie, parole chiave
import subprocess,re
PDF='/tmp/w/slide/s.pdf'
def _page(p):
    t=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),PDF,'-'],capture_output=True,text=True).stdout
    return re.sub(r'\s+',' ',t).strip()
TIT={2:'Le nuove sfide del progresso e il racconto della realtà',3:"L'architettura del ferro, del vetro e l'urbanistica",6:"L'Italia che cambia tra città e campagne",
 8:"L'architettura dell'Eclettismo",11:'La pittura realista in Francia – la Scuola di Barbizon',12:'Jean-François Millet e Gustave Courbet',
 16:'Il Realismo italiano: Honoré Daumier e i Macchiaioli',18:'I protagonisti dei Macchiaioli',20:'I protagonisti dei Macchiaioli'}
LAB={2:['Contesto storico','Nascita del Realismo','Obiettivo principale','Letteratura e arte','Nuovi soggetti'],
 3:['Le Grandi Esposizioni','Il Crystal Palace','Urbanistica e risanamento','Il piano di Haussmann a Parigi','Scopo politico del piano'],
 6:['Unificazione e industrializzazione','Fenomeni sociali','Rinnovamento urbano','Nuove strutture','Sviluppo nelle campagne'],
 8:['Definizione di Eclettismo','Caratteristiche','Molteplicità di approcci','Il Brighton Pavilion',"Il Teatro dell'Opera di Parigi"],
 11:['Pittura en plein air','I precursori','La Scuola di Barbizon','Caratteristiche della scuola','Camille Corot'],
 12:["L'epica contadina di Millet",'Opere di Millet','Courbet e la realtà autentica','I contrasti di Courbet',"L'atelier del pittore"],
 16:['La denuncia di Daumier','Il Realismo in Italia','I Macchiaioli in Toscana','La tecnica della "macchia"'],
 18:['Giovanni Fattori','Opere di Fattori'],20:['Silvestro Lega','Opere di Lega','Telemaco Signorini']}
def cards(p):
    t=_page(p)
    pos=[t.index(l+':') for l in LAB[p]]
    out=[]
    for i,l in enumerate(LAB[p]):
        e=pos[i+1] if i+1<len(pos) else len(t)
        body=t[pos[i]+len(l)+1:e].strip()
        out.append([(l+':',True),(body,False)])
    return out
KW={2:['Realismo','1830–1880','Denuncia sociale','Balzac, Flaubert, Zola'],
 3:['Esposizione universale','Crystal Palace','Ferro, ghisa e vetro','Piano di Haussmann','Boulevards'],
 4:['Esposizione universale','Crystal Palace','Joseph Paxton'],5:['Piano di Haussmann','Boulevards','Parigi'],
 6:['Unificazione','Industrializzazione','Classe operaia e borghesia','Villaggi operai'],
 7:['Galleria Vittorio Emanuele II','Giuseppe Mengoni','Milano'],
 8:['Eclettismo = «scegliere»','Brighton Pavilion','Opera di Parigi'],
 9:['Charles Garnier','Teatro dell\'Opéra','1861–1875'],10:['Pedrocchino e Caffè Pedrocchi','Mole Antonelliana'],
 11:['En plein air','Scuola di Barbizon','Constable','Camille Corot'],12:['Millet','Courbet','Realtà autentica'],
 13:['Jean-François Millet','Le spigolatrici','Silenziosa dignità'],14:['Gustave Courbet','Gli spaccapietre','Denuncia sociale'],
 15:["L'atelier del pittore",'Allegoria reale','Gustave Courbet'],16:['Honoré Daumier','Caricature','Macchiaioli','Macchia'],
 17:['Honoré Daumier','Il vagone di terza classe'],18:['Giovanni Fattori','La rotonda dei bagni Palmieri'],
 19:['Giovanni Fattori','In vedetta'],20:['Silvestro Lega','Il pergolato','Telemaco Signorini'],21:['Telemaco Signorini','La toeletta del mattino']}
DID={'crystal':'Joseph Paxton, Crystal Palace a Londra, 1851 (distrutto nel 1937).','parigi':'Parigi, veduta aerea.',
 'galleria':'Giuseppe Mengoni, Galleria Vittorio Emanuele II, 1863-77. Milano.','opera':"Charles Garnier, Teatro dell'Opéra, 1861-77. Parigi, veduta aerea.",
 'pedrocchino':'Giuseppe Jappelli, Pasticceria detta Il Pedrocchino (1831-42) e Caffè Pedrocchi (dal 1817; facciata meridionale). Padova.',
 'mole':'Alessandro Antonelli, Mole Antonelliana. 1862-89. Torino.','spigolatrici':"Jean-François Millet, Le spigolatrici, 1857; olio su tela, 83,5 per 110 centimetri. Parigi, Musée d'Orsay.",
 'spaccapietre':'Gustave Courbet, Gli spaccapietre, 1849; olio su tela, 165 per 257 centimetri, già a Dresda, Gemäldegalerie (opera distrutta durante i bombardamenti della Seconda guerra mondiale).',
 'atelier':"Gustave Courbet, L'atelier del pittore.",'vagone':'Honoré Daumier, Il vagone di terza classe, 1863-65; olio su tela, 65 per 90 centimetri. Ottawa (Canada), National Gallery of Canada.',
 'rotonda':'Giovanni Fattori, La rotonda dei bagni Palmieri, 1866; olio su tavola, 12 per 35 centimetri. Firenze, Galleria d\'arte moderna.',
 'invedetta':'Giovanni Fattori, In vedetta, 1871 circa; olio su tela, 37 per 56 centimetri. Collezione privata.',
 'brighton':'John Nash, Brighton Pavilion, dal 1815. Brighton.','angelus':"Jean-François Millet, L'Angelus, 1857-59.",'pergolato':'Silvestro Lega, Il pergolato, 1868.','agitate':'Telemaco Signorini, La sala delle agitate al Bonifazio di Firenze, 1865.',
 'toeletta':'Telemaco Signorini, La toeletta del mattino, 1898; olio su tela, 120 per 175 centimetri. Collezione privata.'}
if __name__=='__main__':
    for p in LAB:
        for c in cards(p):print(p,c[0][0],'|',c[1][0][:60])
