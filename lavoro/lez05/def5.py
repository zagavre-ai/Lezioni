import json
M={
1:("The concept of marketing",[("Product-oriented","until the 1950s","it. orientato al prodotto"),("Market-oriented","customer first","it. orientato al mercato"),("Needs and wants","target customers","it. bisogni e desideri"),("Marketing process","four steps","it. analisi, strategia, mix, controllo")],
 ["Here is the map of this topic.","The old model was product-oriented: good products were enough.","Today the model is market-oriented, and the customer comes first.","Companies must know the needs and wants of their target customers.","The marketing process has four steps: analysis, strategy, mix and control."]),
2:("Market research",[("Primary research","field, new data","it. ricerca sul campo"),("Secondary research","desk, existing data","it. ricerca a tavolino"),("Quantitative data","numbers","it. dati numerici"),("Qualitative data","opinions","it. opinioni, valori")],
 ["Now the map of market research.","Primary research is done directly with consumers. It is useful, but expensive.","Secondary research uses existing sources. It is cheaper, but less precise.","Quantitative data are numbers, collected with surveys.","Qualitative data are opinions and beliefs, collected in focus groups."]),
3:("STP",[("Segmentation","smaller groups","it. segmenti di mercato"),("Targeting","best segments","it. mercato obiettivo"),("Positioning","unique position","it. posizionamento"),("Market map","price and quality","it. mappa del mercato")],
 ["This is the map of the STP process.","Segmentation divides the market into groups: demographic, geographic, psychographic and behavioural.","Targeting means choosing the most attractive segments.","Positioning gives the product a unique place, different from competitors.","A market map shows positions according to price and quality."]),
4:("The marketing mix",[("Product","features, USP","it. prodotto"),("Price","internal, external factors","it. prezzo"),("Promotion","advertising, PR","it. promozione"),("Place","distribution","it. distribuzione"),("7Ps","evidence, process, people","it. servizi")],
 ["Here is the map of the marketing mix.","Product: its features and appearance, and its unique selling points.","Price: how much customers pay, set with internal and external factors.","Promotion: how customers are informed, with advertising and public relations.","Place: where products are made available and distributed.","The 7Ps add physical evidence, process and people, especially for services."]),
5:("Branding and pricing",[("Brand names","easy to remember","it. nome del marchio"),("Logos","identity and values","it. logo"),("Own-brand","retailers' brands","it. marchio del distributore"),("Types of prices","five kinds","it. prezzi di penetrazione, civetta")],
 ["Now the map of branding and pricing.","A good brand name is positive and easy to remember.","A logo shows the identity and the values of a company.","Retailers create own-brand products under their name.","There are five types of prices: penetration, psychological, economy, luxury and promotional."]),
6:("Digital marketing",[("Channels","websites, social media","it. canali digitali"),("Content and email","video, newsletters","it. contenuti, email"),("SEO","search engines","it. ottimizzazione per i motori"),("Challenges","privacy, mobile","it. sfide")],
 ["This is the map of digital marketing.","The main channels are websites and social media marketing.","Content marketing and email marketing keep customers interested.","SEO helps customers to find products in search engines.","The challenges are privacy rules, mobile viewing and omnichannel strategies."]),
7:("Marketing",[("Concept","customer first","it. il cliente al centro"),("Market research","primary, secondary","it. ricerca di mercato"),("STP","segment, target, position","it. strategia"),("Marketing mix","4Ps, 7Ps","it. marketing mix"),("Branding, pricing","identity, price","it. marchio, prezzo"),("Digital","channels, SEO","it. marketing digitale")],
 ["And now the map of the whole lesson.","The concept of marketing puts the customer first.","Market research collects primary and secondary data.","The STP process chooses the segments and the position.","The marketing mix has four Ps, or seven.","Branding builds loyalty, and pricing communicates quality.","Digital marketing reaches customers on their favourite platforms."]),
}
V={
"E5_INTRO1":"Welcome to this lesson on marketing. Today we will look at six topics. First, the concept of marketing. Second, market research. Third, the marketing strategy, called S T P. Fourth, the marketing mix. Fifth, branding and pricing. And sixth, digital marketing. After each topic you will see a concept map and a short quiz. You need at least eighty percent to continue. Let's begin.",
"E5_RF1":"Let's review the whole lesson. Marketing puts the customer first. Market research collects the information. The S T P process chooses segments and positions. The marketing mix has four Ps, or seven. Branding builds loyalty, and price communicates quality. And digital marketing reaches customers online. Now it is time for the final test.",
"E5_FIN1":"It is time for the final test.","E5_CMP1":"And now, your homework.","E5_GL0":"Here are the key words of the lesson, in English and in Italian.",
}
GL=[("target customer","cliente obiettivo"),("needs and wants","bisogni e desideri"),("market research","ricerca di mercato"),("survey","sondaggio"),("focus group","gruppo di discussione"),("quantitative data","dati quantitativi"),
 ("qualitative data","dati qualitativi"),("segmentation","segmentazione"),("positioning","posizionamento"),("marketing mix","marketing mix"),("unique selling point","punto di forza unico"),("brand identity","identità del marchio"),
 ("own-brand","marchio del distributore"),("penetration price","prezzo di penetrazione"),("psychological price","prezzo psicologico"),("loyalty","fedeltà"),("digital channel","canale digitale"),("SEO","ottimizzazione per i motori di ricerca"),
 ("omnichannel","multicanale"),("brand awareness","notorietà del marchio"),("advertising","pubblicità"),("distribution channel","canale di distribuzione"),("physical evidence","evidenza fisica"),("customer service","servizio clienti")]
V["E5_GLa"]=". ".join(t for t,_ in GL[:12])+"."
V["E5_GLb"]=". ".join(t for t,_ in GL[12:])+"."
for k,(c,r,s) in M.items():
    for i,fr in enumerate(s): V[f"E5_AN{k}_{i}"]=fr
Q={
1:("The concept of marketing",[
 ("What characterised the product-oriented model?","Companies assumed that high-quality goods would bring success",["Companies studied the needs of every customer","Companies reduced their prices every year","Companies sold only services"],"Companies took for granted that their business would be successful if they produced high-quality goods."),
 ("Why did the model start to change?","The number of competitors grew and trade became more global",["Goods and services became scarce","Customers stopped buying products","Governments forbade competition"],"With more competitors and an overabundance of goods, the model started to change."),
 ("What is the priority of the concept of marketing?","Customers' satisfaction",["The lowest production cost","The number of employees","The size of the factory"],"The concept of marketing considers customers' satisfaction the priority."),
 ("What is a target market?","A particular group of customers",["The cheapest shop in town","A competitor's product","A type of price"],"The target market is a particular group of customers chosen in the marketing strategy."),
 ("What happens in the implementation and control step?","Companies monitor results and modify the marketing mix",["Companies stop the production","Companies identify the first opportunity","Companies choose a logo"],"After the launch, companies constantly monitor results and modify the marketing mix.")]),
2:("Market research",[
 ("What is market research?","Collecting and analysing information about what people want, need and buy",["Producing goods at a lower cost","Choosing the best logo","Selling products online"],"It is the process of collecting and analysing information about what people want, need and buy."),
 ("What is primary (field) research?","Research conducted directly with consumers to collect new information",["Research using only government reports","Research done without customers","Research about competitors' logos"],"Primary research is conducted directly with consumers and collects new information (primary data)."),
 ("Which is an example of field research?","A focus group",["A government statistic","A newspaper article","A bank report"],"Examples of primary research: surveys, consumer panels and focus groups."),
 ("What is a disadvantage of secondary (desk) research?","Data are not always relevant or updated",["It is very expensive","It needs focus groups","It collects only new data"],"Desk research is cheaper than field research, but data are not always relevant or updated."),
 ("What are qualitative data?","Descriptive information, such as opinions and beliefs",["Information expressed only as numbers","Charts about population size","Test scores"],"Qualitative data are descriptive information which cannot be measured numerically.")]),
3:("The marketing strategy (STP)",[
 ("What does STP stand for?","Segmentation, Targeting and Positioning",["Selling, Trading and Pricing","Strategy, Tactics and Promotion","Supply, Technology and Production"],"STP is an acronym for Segmentation, Targeting and Positioning."),
 ("What is a segment?","A smaller group of the market with similar characteristics",["A type of product","A competitor","A distribution channel"],"In segmentation the market is divided into smaller groups with similar characteristics."),
 ("Which criterion answers the question 'where?'","Geographic",["Demographic","Psychographic","Behavioural"],"Geographic (where?), demographic (who?), psychographic (why?), behavioural (how?)."),
 ("What does targeting involve?","Evaluating each segment and selecting the most attractive ones",["Setting the lowest price","Designing a logo","Dividing the company into departments"],"Targeting is the evaluation of the commercial attractiveness of each segment and the selection of the target market."),
 ("What does a market map show?","The positions a product can take according to price and quality",["The shops of a city","The employees of a company","The history of a brand"],"A market map shows the positions a product can take on the market according to price and quality.")]),
4:("The marketing mix",[
 ("What are the 4Ps of marketing?","Product, price, promotion, place",["People, process, product, price","Plan, produce, pack, post","Profit, power, position, publicity"],"The 4Ps are product, price, promotion and place."),
 ("What are Unique Selling Points (USP)?","Features that make a product different, like design or colour",["The lowest prices on the market","The shops of a franchise","The customers of a brand"],"Manufacturers differentiate products through features that become their Unique Selling Points."),
 ("Which two kinds of factors influence the price?","Internal and external factors",["Local and global factors","Social and ethical factors","Digital and physical factors"],"Price is set by considering internal factors (production cost) and external factors (competing prices)."),
 ("What does 'promotion' mean in the marketing mix?","How customers are informed about products",["Where products are sold","How much products cost","How products are made"],"Promotion is the process of making a business and its products known to potential customers."),
 ("Which are the three extra Ps of the 7Ps?","Physical evidence, process and people",["Profit, plan and power","Packaging, price and position","Promotion, place and product"],"The extended marketing mix adds physical evidence, process and people.")]),
5:("Branding and pricing",[
 ("What is branding?","A technique to differentiate products from competitors' ones",["A way to reduce production costs","A type of market research","A tax for companies"],"Branding is a technique used by companies to differentiate their products from competitors' ones."),
 ("Which is an example of a brand name that is an invented word?","Google",["McDonald's","General Motors","American Airlines"],"Invented words: Google. Family names: McDonald's. Descriptive: General Motors. Geographical: American Airlines."),
 ("What are own-brand products?","Products that supermarkets market under their own name",["Products without a logo","Products made by the customer","Products sold only online"],"Supermarket chains buy products from manufacturers and market them under their name or a new brand name."),
 ("What is a penetration price?","A low price to enter a new market and gain market share",["A very high price for exclusivity","A price just below a round number","A price reduced for one year"],"Penetration price: offering a low price to enter a new market and/or gain market share."),
 ("What is an odd (psychological) price?","A price just below a round number, like 9,99",["A price much higher than competitors","A temporary discount","A price fixed by the government"],"Odd or psychological prices create the perception of a good deal (9,99 instead of 10).")]),
6:("Digital marketing",[
 ("Why do companies need digital marketing strategies?","To reach target customers on the platforms they use most",["To avoid using the Internet","To reduce the number of customers","To stop advertising"],"Companies need to reach their target customers on the platforms they use the most."),
 ("What is Content Marketing?","Online material that sparks interest without directly promoting a brand",["Sending newsletters only","Paying for search results","Selling products in shops"],"Content marketing creates online material that doesn't directly promote a brand but sparks interest in its products."),
 ("What does SEO stand for?","Search Engine Optimisation",["Social Engagement Operations","Sales and Export Office","Secure Email Organisation"],"Search Engine Optimisation: most customers use searches to find products and services."),
 ("Which is a challenge of digital marketing?","Complying with privacy and data sharing regulations",["Having too few customers","Printing catalogues","Opening physical shops"],"Companies need to comply with privacy laws, some of them transnational (GDPR)."),
 ("What is an omnichannel strategy?","Using email, social media, website, SEO and newsletters together",["Using only one social network","Selling only in physical shops","Avoiding mobile devices"],"Omnichannel strategies include email, social media, website, SEO and newsletters.")]),
}
def dump():
    return {f"Q{k}":{"title":f"Quiz {k} · {t}","items":[{"p":p,"a":a,"w":w,"ref":r} for p,a,w,r in it]} for k,(t,it) in Q.items()}
if __name__=='__main__':
    import os
    json.dump([{"nome":n,"testo":t,"lingua":"en"} for n,t in V.items()],open('testi_voci.json','w'),ensure_ascii=False,indent=1)
    q=dump();json.dump(q,open('quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
    with open('Quiz_Inglese_Lez5.txt','w') as f:
        f.write("QUIZ DI FINE ARGOMENTO · INGLESE TRIENNIO AFM (Prof.ssa Fontanesi) · MARKETING\nDomande in inglese, solo dal materiale della docente. 5 domande per argomento · per continuare almeno l'80%. La risposta giusta è segnata con ✓.\n\n")
        for k,v in q.items():
            f.write("="*60+"\n"+v['title']+"\n"+"="*60+"\n")
            for i,x in enumerate(v['items'],1): f.write(f"{i}. {x['p']}\n   ✓ {x['a']}\n"+''.join(f"   – {w}\n" for w in x['w'])+f"   Spiegazione: {x['ref']}\n\n")
    os.makedirs('map',exist_ok=True)
    for k,(c,rr,s) in M.items():
        json.dump({"materia":"Inglese","docente":"Prof.ssa Maria Vittoria Fontanesi","titolo":c,"rami":[{"concetto":a,"parola":b,"esempio":d} for a,b,d in rr]},open(f'map/mappa{k}.json','w'),ensure_ascii=False,indent=1)
    print(len(V),'voci',sum(len(t.split()) for t in V.values()),'parole')
