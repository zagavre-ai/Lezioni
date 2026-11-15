# Testi per la voce Kore (inglese B1) e mappe. Nomi con prefisso E4_ (nuovi).
import json
M={ # mappe: titolo centro, rami (concetto, parola, esempio), frasi (intro + una per ramo)
1:("Business structures",[("Sole traders","one owner","it. un titolare · bakers"),("Partnerships","shared risk","it. soci · lawyers"),("Limited companies","shares","it. azioni · LTD, PLC"),("Cooperatives","one member, one vote","it. cooperativa · social goals")],
   ["Let's put this topic on a map.","Sole traders: one owner, and unlimited liability. Think of bakers and plumbers.","Partnerships: the partners share responsibility, profits and losses.","Limited companies: owners hold shares, and their liability is limited.","Cooperatives: members decide together, with one vote each."]),
2:("Franchising and start-ups",[("Franchising","franchisor, franchisee","it. affiliante, affiliato"),("Franchise fees","initial fee","it. quota iniziale · turnover"),("Start-ups","young, innovative","it. impresa nuova · crowdfunding"),("Start-up hubs","favourable context","it. polo · Silicon Valley")],
   ["Here is the map of this topic.","Franchising: the franchisee buys the right to use the franchisor's business model.","The franchisee pays an initial fee, and a percentage of the annual turnover.","Start-ups are young, innovative companies with high costs, and high risk.","They thrive in hubs of technology, like Silicon Valley, London or Boston."]),
3:("Business growth",[("Internal growth","own resources","it. crescita interna"),("External growth","integration","it. horizontal · vertical"),("Merger or takeover","join or buy","it. fusione · acquisizione"),("Multinationals","parent, subsidiary","it. società madre · controllata")],
   ["Now the map of business growth.","Internal growth: a company uses its own resources. It is more gradual.","External growth is faster: a business integrates with other organisations, horizontally or vertically.","In a merger, similar companies join. In a takeover, one company buys another.","Multinationals operate in more than one country. A parent company controls its subsidiaries."]),
4:("Internal organisation",[("Departments","areas of work","it. reparti"),("Organigram","chain of command","it. organigramma"),("Top management","Board, CEO","it. amministratore delegato"),("Outsourcing, reshoring","outside or back home","it. esternalizzare · rimpatriare")],
   ["This is the map of the internal organisation.","A growing company is divided into departments, each with its own area of work.","The organigram shows the chain of command: who is responsible for what.","At the top we find the Board of Directors and the CEO.","Outsourcing gives work to outside companies. Reshoring brings production back to the home country."]),
5:("Corporate Social Responsibility",[("Social impact","stakeholders","it. portatori di interesse"),("Types of CSR","four kinds","it. ambientale, etica"),("Win-win","doing well by doing good","it. vantaggio per tutti"),("Advantages","reputation, loyalty","it. reputazione, fedeltà")],
   ["Here is the map of CSR.","CSR means creating a positive social impact for all stakeholders.","There are environmental, economic, philanthropic and ethical types of CSR.","It is a win-win strategy: the company does good, and does well.","The advantages are a better reputation, loyal customers and engaged employees."]),
6:("Types of business",[("Business structures","four models","it. strutture"),("Franchising, start-ups","tested or new","it. affiliazione · nuove imprese"),("Growth","internal or external","it. crescita · multinazionali"),("Organisation","departments","it. organigramma"),("CSR","do good, do well","it. responsabilità sociale")],
   ["And now the map of the whole lesson.","Business structures: sole traders, partnerships, limited companies and cooperatives.","Franchising uses a tested model. Start-ups are new, and risky.","Businesses grow in an internal or external way. Multinationals operate in many countries.","The internal organisation divides the company into departments, with a clear chain of command.","Finally, CSR: do good, and do well."]),
}
V={ # voci singole
"E4_INTRO1":"Welcome to this lesson on types of business. Today we will look at five topics. First, business structures. Second, franchising and start-ups. Third, business growth and multinationals. Fourth, the internal organisation of a company. And fifth, corporate social responsibility. After each topic you will see a concept map and a short quiz. You need at least eighty percent to continue. Let's begin.",
"E4_R1":"Quick review. Sole traders have unlimited liability. Partners share profits and risks. Limited companies have their own legal identity. Cooperatives are run in a democratic way.",
"E4_R2":"Quick review. Franchising means using another company's brand and business model. Start-ups are young, innovative companies, with high risk.",
"E4_R3":"Quick review. Growth can be internal or external. A merger joins companies of similar size. A takeover is when a business buys another one. Multinationals operate in more than one country.",
"E4_R4":"Quick review. Companies are divided into departments. The organigram shows the chain of command. Outsourcing uses external organisations, and reshoring brings production back home.",
"E4_R5":"Quick review. Corporate social responsibility means creating a positive social impact. It improves reputation and loyalty. It is a win-win strategy.",
"E4_RF1":"Let's review the whole lesson. A business can be a sole trader, a partnership, a limited company or a cooperative. Franchising and start-ups are two ways to start a business. Companies grow in an internal or external way, and multinationals operate in many countries. Organigrams show the chain of command. And corporate social responsibility helps companies to do good, and to do well. Now it is time for the final test.",
"E4_FIN1":"It is time for the final test.",
"E4_CMP1":"And now, your homework.",
"E4_GL0":"Here are the key words of the lesson, in English and in Italian.",
}
GL=[("sole trader","ditta individuale"),("unlimited liability","responsabilità illimitata"),("partnership","società di persone"),("sleeping partner","socio accomandante"),("limited company","società a responsabilità limitata"),("share","azione"),("shareholder","azionista"),("dividend","dividendo"),("cooperative","cooperativa"),("franchisor","affiliante"),("franchisee","affiliato"),("turnover","fatturato"),
    ("start-up","impresa in fase di avvio"),("merger","fusione"),("takeover","acquisizione"),("parent company","società madre"),("subsidiary","società controllata"),("organigram","organigramma"),("chain of command","catena di comando"),("outsourcing","esternalizzazione"),("reshoring","rimpatrio della produzione"),("stakeholder","portatore di interesse"),("win-win","vantaggioso per tutti"),("reputation","reputazione")]
V["E4_GLa"]=". ".join(t for t,_ in GL[:12])+"."
V["E4_GLb"]=". ".join(t for t,_ in GL[12:])+"."
for k,(c,r,s) in M.items():
    for i,fr in enumerate(s): V[f"E4_AN{k}_{i}"]=fr
if __name__=='__main__':
    L=[{"nome":n,"testo":t,"lingua":"en"} for n,t in V.items()]
    json.dump(L,open('testi_voci.json','w'),ensure_ascii=False,indent=1)
    w=sum(len(t.split()) for t in V.values());print(len(L),'voci',w,'parole, stima',round(w/2.4/60,1),'min')
    for k,(c,rr,s) in M.items():
        json.dump({"materia":"Inglese","docente":"Prof.ssa Maria Vittoria Fontanesi","titolo":c,"rami":[{"concetto":a,"parola":b,"esempio":d} for a,b,d in rr]},open(f'map/mappa{k}.json','w'),ensure_ascii=False,indent=1)
