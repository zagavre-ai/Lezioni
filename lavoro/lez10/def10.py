import json
# Lezione 10 · WORK TODAY (solo dal materiale della docente: dispensa e videolezione)
M={
1:("Today's job market",[("Job market","businesses and workers","it. mercato del lavoro"),("Tight or slack","offers and seekers","it. teso o debole"),("New professions","IT jobs","it. nuove professioni"),("Skills first","skills over experience","it. prima le competenze"),("Job vacancies","many open jobs","it. posti vacanti")],
 ["Here is the map of this topic.","In the job market, businesses that need employees meet people who are looking for work.","A tight market has many job offers, a slack market has more people looking for work.","Technology creates new professions, especially in I T.","Many employers prefer skills to experience.","Today there are many job vacancies, but the employment rate is still low."]),
2:("Job stability",[("The past","long-term stable jobs","it. lavoro stabile"),("Today","flexibility, short-term jobs","it. lavori a breve termine"),("Gig economy","freelancers, temporary hires","it. economia dei lavoretti"),("Advantages","flexibility, extra income","it. vantaggi"),("Disadvantages","low pay, no benefits","it. svantaggi")],
 ["Now the map of job stability.","In the past, people had long-term stable jobs with the same employer.","Today there is more flexibility and less stability, with many short-term jobs.","In the gig economy, people work for a specific length of time, like freelancers.","Gig work gives flexibility, independence and an extra income.","But the pay is modest, there are no benefits, and there is a lot of stress."]),
3:("Flexibility at work",[("Anywhere, any time","digital devices","it. ovunque, in ogni momento"),("Covid-19","remote working","it. lavoro da remoto"),("Types","job sharing, hybrid","it. tipi di flessibilità"),("Flexitime","start and end time","it. orario flessibile"),("Gen Z","hybrid model","it. generazione Z")],
 ["This is the map of flexibility at work.","With digital devices, we can work anywhere and at any time.","The Covid-19 pandemic made remote working the norm.","There are many types of flexibility: job sharing, hybrid work, a condensed work week and part-time work.","With flexitime, workers choose when their working day starts and ends.","Gen Z values flexibility, and almost half of them prefer a hybrid model."]),
4:("Digital communication",[("Internal, external","staff, customers","it. interna, esterna"),("Main forms","emails, video calls","it. forme principali"),("Instant","time and money","it. in tempo reale"),("Zoom","from start-up to giant","it. Zoom")],
 ["Here is the map of digital communication.","Digital communication takes place among the staff and with customers.","Its main forms are emails, instant messaging, live chat and video conferencing.","Information arrives instantly, so companies save time and money.","Zoom grew very fast during the pandemic, and its name is now also a verb."]),
5:("Employability skills",[("Soft skills","transferable skills","it. competenze trasversali"),("How you work","initiative, deadlines","it. come lavori"),("Working with others","teamwork, negotiation","it. come lavori con gli altri"),("How you think","problem-solving, IT","it. come pensi")],
 ["Now the map of employability skills.","Businesses look for qualifications, but also for soft skills, which we use in real situations.","How you work: initiative, organisation, deadlines and learning.","How you work with others: communication, teamwork, negotiation and valuing diversity.","How you think: problem-solving, numeracy and I T skills."]),
6:("Work today",[("Job market","trends, top skills","it. mercato del lavoro"),("Job stability","gig economy","it. stabilità"),("Flexibility","hybrid, flexitime","it. flessibilità"),("Digital communication","emails, Zoom","it. comunicazione digitale"),("Employability skills","soft skills","it. occupabilità")],
 ["And now the map of the whole lesson.","Today's job market needs new skills and new professions.","Jobs are less stable, and the gig economy is growing.","Flexible working is now the norm, especially hybrid work.","Digital communication is fast and essential for business.","Employability skills make a person attractive for employers."]),
}
V={
"E10_INTRO1":"Welcome to this lesson on work today. We will look at five topics. First, today's job market. Second, job stability. Third, flexibility at work. Fourth, digital communication. And fifth, employability skills. After each topic you will see a concept map and a short quiz. You need at least eighty percent to continue. Let's begin.",
"E10_RF1":"Let's review the whole lesson. The job market is changing, and skills are more important than experience. Jobs are less stable, and the gig economy gives flexibility, but low pay. Flexible working, like hybrid work and flexitime, is now the norm. Digital communication is instant, and Zoom became a global giant. And employability skills help you to find a job and to work well. Now it is time for the final test.",
"E10_FIN1":"It is time for the final test.","E10_CMP1":"And now, your homework.","E10_GL0":"Here are the key words of the lesson, in English and in Italian.",
}
GL=[("job market","mercato del lavoro"),("employee","dipendente"),("employer","datore di lavoro"),("wage","salario"),("unemployment","disoccupazione"),("job vacancy","posto vacante"),
 ("skill","competenza"),("gig economy","economia dei lavoretti"),("freelancer","libero professionista"),("temporary","temporaneo"),("income","reddito"),("benefits","benefit, tutele"),
 ("remote working","lavoro da remoto"),("work-life balance","equilibrio vita-lavoro"),("job sharing","lavoro condiviso"),("hybrid work","lavoro ibrido"),("flexitime","orario flessibile"),("part-time","a tempo parziale"),
 ("video conferencing","videoconferenza"),("productivity","produttività"),("soft skills","competenze trasversali"),("deadline","scadenza"),("teamwork","lavoro di squadra"),("problem-solving","risoluzione dei problemi")]
V["E10_GLa"]=". ".join(t for t,_ in GL[:12])+"."
V["E10_GLb"]=". ".join(t for t,_ in GL[12:])+"."
for k,(c,r,s) in M.items():
    for i,fr in enumerate(s): V[f"E10_AN{k}_{i}"]=fr
Q={
1:("Today's job market",[
 ("What is the job market?","The market where businesses that need employees and people looking for work interact",["The market where companies sell their products","A place where people buy shares","A list of open schools"],"Job market: the market where there is an interaction between businesses that need employees and individuals who are looking for work."),
 ("What is a tight job market?","There are many job offers but few people looking for work",["There are more people looking for work than jobs","There are no job offers at all","Wages are always very low"],"Tight: there are many job offers but few people looking for work."),
 ("What happens during recessions?","Unemployment rises and wages are low",["Businesses compete for workers","Wages increase quickly","There are no unemployed people"],"During recessions, unemployment rises and there is economic stagnation, with a low level of wages."),
 ("What do many employers prefer today?","People with the right skills, rather than only qualifications",["Only people with many years of experience","Only people with a university degree","People who do not want to learn"],"Many employers prefer hiring people with the necessary skills to perform current tasks and adapt rapidly to new challenges."),
 ("Why are there many job vacancies?","Ageing population, less immigration and fewer people accepting low-wage jobs",["There are too many workers","Companies are closing","Wages are too high"],"This situation is due to an ageing population, a decline in immigration and a change in attitude towards work.")]),
2:("Job stability",[
 ("How was work in the past?","People had long-term stable jobs with the same employer",["People changed job every month","Everybody was a freelancer","Nobody had a contract"],"In the past people had long-term stable jobs with the same employer."),
 ("What is the gig economy?","Jobs that last a specific length of time, like freelance work",["Jobs in the music industry only","Jobs for life in big companies","Jobs in the public sector"],"The gig economy refers to jobs lasting a specific length of time: freelancers, independent contractors, temporary hires."),
 ("Which is an example of a gig job without specific qualifications?","Food delivery",["Digital marketer","Freelance writer","Engineer"],"It ranges from professional services to jobs that do not require specific qualifications, like food delivery services."),
 ("Which is an advantage of gig work?","Flexibility and a better work-life balance",["A high minimum wage","Free health insurance","No taxes to pay"],"Gig workers can choose the types of jobs they do, when and where they do them: work-life balance."),
 ("Which is a disadvantage of gig work?","Modest pay and no benefits",["Too much stability","Too many holidays","A fixed salary for life"],"Gig workers don't have the protection of minimum wages, health insurance and trade unions.")]),
3:("Flexibility at work",[
 ("What made it possible to work anywhere and at any time?","Digital devices",["Longer holidays","New factories","Paper documents"],"Thanks to digital devices, it is possible to work anywhere and at any time."),
 ("What changed the vision of remote working?","The Covid-19 pandemic",["A new law on holidays","The invention of the telephone","The end of the Internet"],"The Covid-19 pandemic completely changed this vision: flexible work patterns are now the norm."),
 ("What is job sharing?","Two people share one full-time job, each working part-time",["One person does two jobs","A team shares an office","Workers share their salaries"],"Job sharing: when two people share one full-time job, each one working part-time."),
 ("What is a condensed work week?","Working longer hours on fewer days",["Working fewer hours every day","Working only at night","Working seven days a week"],"Condensed work week: for example, four days of 10 hours instead of five days of 8 hours."),
 ("What do almost half of Gen Z employees prefer?","A hybrid model, combining remote and office work",["Full remote work","Only office work","Working at night"],"Almost half of them prefer a hybrid model; full remote work may make them feel isolated.")]),
4:("Digital communication",[
 ("Where does digital communication take place?","Internally among staff and externally with customers",["Only inside the office","Only with suppliers","Only on paper"],"It takes place both internally among staff and externally with customers."),
 ("Which is a main form of digital communication?","Video conferencing",["Letters by post","Fax only","Notice boards"],"Its main forms are emails, instant messaging, live chat, video conferencing and project management tools."),
 ("What is the main feature of digital communication?","Information is transmitted instantaneously",["It is very expensive","It is slower than letters","It works only in one country"],"The main feature of digital communication is that information is transmitted instantaneously."),
 ("Who invented the Zoom app in 2011?","Eric Yuan",["Bill Gates","Steve Jobs","Jeff Bezos"],"The Zoom app was invented in 2011 by Eric Yuan, a former vice president of Cisco."),
 ("What led to Zoom's explosive growth?","The Covid-19 pandemic",["A new smartphone","A football championship","A drop in prices"],"It was the Covid-19 pandemic that led to the company's explosive growth.")]),
5:("Employability skills",[
 ("What are employability skills?","Qualities that make a person attractive for employment",["Only university degrees","Only computer programs","Only years of experience"],"Employability skills: qualities and attributes making an individual attractive for employment and successful in the workplace."),
 ("What is the advantage of soft skills compared to hard skills?","They can be applied in real-world situations",["They are learnt only at school","They never change","They are only technical"],"Their main advantage is that they can be applied in practical circumstances and in real-world situations."),
 ("Which are the three types of employability skills?","How you work, how you work with others, how you think",["How you eat, sleep and study","How you dress, speak and walk","How you buy, sell and save"],"They can be divided into three types: how you work, how you work with others, how you think."),
 ("What does 'working to deadlines' mean?","Prioritising and planning, being reliable",["Working only at night","Never finishing work","Working without a plan"],"Working to deadlines: prioritizing and planning, reliability."),
 ("What does negotiation mean?","Looking for ideas that benefit everybody: give and take",["Winning every discussion","Never accepting other ideas","Working alone"],"Negotiation: looking for ideas benefitting all, 'give and take'.")]),
}
def dump():
    return {f"Q{k}":{"title":f"Quiz {k} · {t}","items":[{"p":p,"a":a,"w":w,"ref":r} for p,a,w,r in it]} for k,(t,it) in Q.items()}
if __name__=='__main__':
    import os
    json.dump([{"nome":n,"testo":t,"lingua":"en"} for n,t in V.items()],open('testi_voci.json','w'),ensure_ascii=False,indent=1)
    q=dump();json.dump(q,open('quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
    with open('Quiz_Inglese_Lez10.txt','w') as f:
        f.write("QUIZ DI FINE ARGOMENTO · INGLESE TRIENNIO AFM (Prof.ssa Fontanesi) · WORK TODAY\nDomande in inglese, solo dal materiale della docente. 5 domande per argomento · per continuare almeno l'80%. La risposta giusta è segnata con ✓.\n\n")
        for k,v in q.items():
            f.write("="*60+"\n"+v['title']+"\n"+"="*60+"\n")
            for i,x in enumerate(v['items'],1): f.write(f"{i}. {x['p']}\n   ✓ {x['a']}\n"+''.join(f"   – {w}\n" for w in x['w'])+f"   Spiegazione: {x['ref']}\n\n")
    os.makedirs('map',exist_ok=True)
    for k,(c,rr,s) in M.items():
        json.dump({"materia":"Inglese","docente":"Prof.ssa Maria Vittoria Fontanesi","titolo":c,"rami":[{"concetto":a,"parola":b,"esempio":d} for a,b,d in rr]},open(f'map/mappa{k}.json','w'),ensure_ascii=False,indent=1)
    print(len(V),'voci',sum(len(t.split()) for t in V.values()),'parole',sum(len(t) for t in V.values()),'caratteri')
