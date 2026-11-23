# Cartine del prof: pulite (QR, cerchietto), grandi e con zoom sulle zone di cui parla il prof. File finali in img/z_<pagina>_<zoom>.png
from PIL import Image, ImageFilter
import os
D = '/tmp/claude-0/l15/img/'
AW, AH = 1316, 716   # area disponibile nella slide
def fit(im):
    w, h = im.size; k = min(AW / w, AH / h)
    return im.resize((max(1, int(w * k)), max(1, int(h * k))), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2, percent=40, threshold=2))
def side(files):
    ims = [Image.open(D + f).convert('RGB') for f in files]
    if len(ims) == 1: return ims[0]
    h = max(i.size[1] for i in ims); ims = [i.resize((int(i.size[0] * h / i.size[1]), h), Image.LANCZOS) for i in ims]
    W = sum(i.size[0] for i in ims) + 30 * (len(ims) - 1); m = Image.new('RGB', (W, h), 'white'); x = 0
    for i in ims: m.paste(i, (x, 0)); x += i.size[0] + 30
    return m
BASE = {6: ['c_p06.png'], 8: ['c_p08_x34.png', 'c_p08_x35.png'], 11: ['c_p11.png'], 13: ['c_p13.png'], 15: ['c_p15_x52.png']}
REG = {11: {1: (320, 360, 1120, 780), 2: (340, 100, 1140, 520), 3: (840, 140, 1554, 516), 4: (840, 300, 1554, 676), 5: (760, 680, 1520, 1080)},
       13: {1: (0, 100, 580, 1215), 2: (585, 100, 1175, 1215)}}
for pg, fs in BASE.items():
    im = side(fs); fit(im).save(f'{D}z_{pg}_0.png')
    for z, box in REG.get(pg, {}).items(): fit(im.crop(box)).save(f'{D}z_{pg}_{z}.png')
print(sorted(f for f in os.listdir(D) if f.startswith('z_')))
