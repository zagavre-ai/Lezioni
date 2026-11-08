import asyncio,sys
from playwright.async_api import async_playwright
PART=int(sys.argv[1]);URL=f'file:///home/claude/lezioni/afm-inglese-triennio-lez03/consegna/Tecnologie_Lez1_Parte{PART}/Lezione_interattiva/index.html'
FILL='''(args)=>{var q=args[0],wrong=args[1];var acts=E.filter(function(e){return e.quiz===q});var n=0;
 acts.forEach(function(e){e.items.forEach(function(it,i){var rs=[].slice.call(document.querySelectorAll('input[name="mc'+e.id+i+'"]'));
  var tgt=(wrong&&i===0)?rs.find(function(r){return r.value!==it.a}):rs.find(function(r){return r.value===it.a});tgt.checked=true;tgt.dispatchEvent(new Event('change',{bubbles:true}));n++})});return n}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        pg=await b.new_page(viewport={'width':1280,'height':900});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(URL);await pg.wait_for_function('document.getElementById("v").duration>100 && ready',timeout=30000)
        fo=[f for f in pg.frames if 'esercizi' in f.url][0]
        nq=await pg.evaluate('NQ')
        for q in range(1,nq+1):
            await pg.evaluate(f'(function(){{var v=document.getElementById("v");v.currentTime=STOPS[{q-1}]-1.2;v.play()}})()')
            await pg.wait_for_function(f'open=={q}',timeout=15000)
            h1=await fo.evaluate('document.querySelector("h1").innerText')
            n=await fo.evaluate(FILL,[q,q==1])
            await fo.click('button.btn:not(.sec)')
            sc=await fo.evaluate('document.querySelector(".score").innerText')
            dis=await fo.evaluate('[...document.querySelectorAll("button")].find(b=>b.textContent.includes("Continua")).disabled')
            print(q,h1,'| domande',n,'|',sc[:110],'| Continua disattivato:',dis)
            if dis:
                await fo.click('button:has-text("Riprova")');await fo.evaluate(FILL,[q,False]);await fo.click('button.btn:not(.sec)')
                print('   dopo Riprova:',(await fo.evaluate('document.querySelector(".score").innerText'))[:90])
            await fo.click('button:has-text("Continua il video")');await pg.wait_for_timeout(700)
            assert await pg.evaluate('open')==0 and not await pg.evaluate('document.getElementById("v").paused')
        print('totale',await pg.evaluate('document.getElementById("tot").textContent'),'errori pagina',errs)
        await b.close()
asyncio.run(main())
