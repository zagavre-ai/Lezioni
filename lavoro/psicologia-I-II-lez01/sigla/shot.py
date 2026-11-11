import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/lezioni/psicologia-I-II-lez01/sigla/sigla.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(400)
    for t in [float(x) for x in sys.argv[1:]]:
        pg.evaluate("t=>draw(t)",t);pg.screenshot(path='/home/claude/lezioni/psicologia-I-II-lez01/fr/sg_%s.png'%t)
    print(errs)
