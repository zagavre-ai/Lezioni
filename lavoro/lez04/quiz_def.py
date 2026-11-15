import json
Q={
1:("Business structures",[
 ("Which business structure is owned, controlled and run by one person?","Sole trader",["Partnership","Public limited company","Cooperative"],"Sole traders are small businesses owned, controlled and run by one person."),
 ("What does 'unlimited liability' mean for a sole trader?","They are personally responsible for all the debts of the business",["They can never lose money","The debts belong only to the bank","The business has no legal obligations"],"Sole traders have unlimited liability: they are personally responsible for all debts incurred in their business."),
 ("What is a 'sleeping' partner in a limited partnership?","A partner who only provides capital",["A partner who runs the business every day","A partner without any investment","A partner who is also an employee"],"In limited partnerships, 'sleeping' partners only provide capital."),
 ("How are profits divided between the shareholders of a limited company?","According to the number of shares they hold",["Equally among all employees","According to their age","They are never divided"],"Profits are divided between the shareholders based on the number of shares they hold (dividends)."),
 ("How is decision-making usually managed in a cooperative?","Democratically: each member has one vote",["The founder with most money decides","The government decides","Votes depend on the shares owned"],"Cooperatives are usually run in a democratic way: each member has one vote in decision-making.")]),
2:("Franchising and start-ups",[
 ("Who is the franchisor?","The company that sells the right to use its business idea",["The person who buys the right to copy the business","The bank that finances the business","The customer of the franchise"],"The franchisor sells the right to use a business idea in a new location."),
 ("What does a franchisee pay to the franchisor?","An initial fee and a percentage of the annual turnover",["Only a fixed salary","Nothing, franchising is free","Only the taxes of the franchisor"],"The franchisee pays an initial sum (franchise fee) and a percentage on the annual turnover (management service fee)."),
 ("Why is franchising a low-risk way of starting a business?","It uses an already tested and successful business model",["Because it needs no money at all","Because the franchisee can change the model freely","Because the government pays the costs"],"Franchising uses an already tested and successful business model, which lowers the possibility of failure."),
 ("Which is a disadvantage of franchising?","Limited flexibility and innovation",["A weak brand recognition","No training or support","Difficulty in raising finance from banks"],"The business model cannot be changed by the franchisee, so flexibility and innovation are limited."),
 ("What is typical of a start-up?","High costs and limited financial resources at the beginning",["A very old and traditional structure","Guaranteed success in the first year","No need for capital"],"Start-ups begin with high costs and limited financial resources, so they look for capital from several sources.")]),
3:("Business growth and multinationals",[
 ("What is internal growth?","A company uses its own resources to expand",["A company merges with another one","A company is bought by a larger one","A company moves abroad"],"In internal growth a company uses its own resources (new assets, new lines of product). It is more gradual."),
 ("What is vertical integration?","Businesses at different stages of production join together",["Businesses at the same stage join together","A company opens a new shop","A company reduces its costs"],"Vertical integration: businesses operating at different stages of production join together."),
 ("What is a takeover (or acquisition)?","A business buys another one, entirely or some of its shares",["Two similar companies form a new one","A company closes a department","A company becomes non-profit"],"In an acquisition or takeover a business buys another one, either entirely or some shares."),
 ("When does a parent company control a subsidiary?","When it owns or controls more than 50% of the voting shares",["When it owns 10% of the shares","When it has the same name","When it is in the same country"],"A parent company either owns or controls more than 50% of the voting share in the subsidiary."),
 ("Why are multinationals often the reason for debates?","Dominance of the market, cheap labour exploitation and tax avoidance",["They never create jobs","They always sell cheaper products","They do not use technology"],"Debates are about market dominance, exploitation of cheap labour in developing countries and tax avoidance.")]),
4:("Internal organisation of a company",[
 ("Why does a growing company need an internal organisation?","So that everybody understands their role and how to cooperate",["To pay fewer taxes","To avoid having customers","To reduce the number of products"],"A company needs an internal organisation so that everybody knows their role and how to cooperate."),
 ("What does an organigram show?","The structure of the departments and the chain of command",["The profits of the year","The list of customers","The prices of the products"],"Organigrams graphically represent the structure of the departments and show the chain of command."),
 ("Who is at the top of an organigram?","The Board of Directors and the CEO",["The office workers","The sales representatives","The line managers"],"On the top of an organigram you find the Board of Directors and the CEO."),
 ("What is outsourcing?","Contracting work out to external organisations",["Moving production back to the home country","Merging with a competitor","Hiring more employees"],"Outsourcing involves contracting work out to external organisations."),
 ("What is reshoring?","A business returns production to the country of origin",["A business opens a branch abroad","A business buys a competitor","A business stops production"],"Reshoring is when a business returns production or operations to the country of origin; it is the reverse of offshoring.")]),
5:("Corporate Social Responsibility",[
 ("What is CSR?","The attempt of companies to generate a positive social impact",["A tax paid to the government","A type of bank loan","A department that sells products"],"CSR is the attempt of companies to manage their business processes so as to generate a positive social impact."),
 ("Which of these are stakeholders?","Customers, suppliers, employees, shareholders and communities",["Only the shareholders","Only the competitors","Only the managers"],"Stakeholders include customers, suppliers, employees, shareholders, communities and the environment."),
 ("What does 'win-win' mean for CSR?","Both society and the company benefit",["Only the company benefits","Only society benefits","Nobody benefits"],"CSR is a win-win strategy: it benefits society and the business as well."),
 ("Which type of CSR is about donating money to worthy causes at local level?","Philanthropic responsibility",["Economic responsibility","Environmental responsibility","Legal responsibility"],"Philanthropic responsibility: improving society, for example donating money to worthy causes."),
 ("Which is an advantage of a CSR strategy?","Increase in customers' retention and loyalty",["Higher taxes","Less engaged employees","A worse public image"],"CSR improves public image, finances, customer loyalty and employees' engagement.")]),
}
def dump():
    out={}
    for k,(t,items) in Q.items():
        out[f"Q{k}"]={"title":f"Quiz {k} · {t}","items":[{"p":p,"a":a,"w":w,"ref":r} for p,a,w,r in items]}
    return out
if __name__=='__main__':
    q=dump();json.dump(q,open('quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
    with open('Quiz_Inglese_Lez4.txt','w') as f:
        f.write("QUIZ DI FINE ARGOMENTO · INGLESE TRIENNIO AFM (Prof.ssa Fontanesi) · TYPES OF BUSINESS\nDomande in inglese, solo dal materiale della docente. 5 domande per argomento · per continuare almeno l'80%. La risposta giusta è segnata con ✓.\n\n")
        for k,v in q.items():
            f.write("="*60+"\n"+v['title']+"\n"+"="*60+"\n")
            for i,x in enumerate(v['items'],1):
                f.write(f"{i}. {x['p']}\n   ✓ {x['a']}\n"+''.join(f"   – {w}\n" for w in x['w'])+f"   Spiegazione: {x['ref']}\n\n")
    print('ok',sum(len(v['items']) for v in q.values()))
