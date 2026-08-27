# uvp-projektna-naloga
projektna naloga

delala sem z podatki iz steam charts (page1: https://steamcharts.com/top/p.1) in potem z spletnimi stranmi posamezne igre na lestvici (in seveda na sgteam-u) ((primer: https://store.steampowered.com/app/105600/Terraria/))
na začetku sem mislila da bi bilo treba iti iz ene spletne strani na drugo še preko vmesne ((primer: https://steamcharts.com/app/105600)) ampak zaradi lepega indeksiranja iger in strukture link-ov tega na srečo ni bilo potrebno izvajati

nobenih posebnih extentionov (ie takih ki jih nebi jemali na predavanjih) nisem uporabljala tako da se mi zdi vam ni treba nič dodatnega nalagati. ((pandas, jupyter notebook, re, requests, csv))

dodatno: 
1)z tem prvim commitom je koda verjetno še 'grda' -- veliko stvari zakomentiranih + ena funkcija ki je ubistvu na koncu nisem uporabila -- to sem pustila tam zato da imam vpogled v to kaj ni delalo ter zato ne ponavljala napak po nepotrebnem, ampak bom upam da počistila do dejanske oddaje.  
2)file test_of_shame3 je nepotreben za projekt ampak mi je pomagal z preverjanjem tega kaj vn vržejo posamezne funkcije in na tej točki sem čustveno navezana.
3) file the_crossover ima vlogo 'pridobi' in 'izlusci' datotek kot bi bile v zapiskih na githubu. to je tudi file z največ zakomentirane kode, tako da pro tip: s tem komitom je dejanska uporabna (nezakontirana koda) do line 218. opomba: crossover ima vlogo teh dveh file-ov ker mi na začetku računalnik ni hotel ustvariti pravih datotek v pravi mapi tako da sem problem samo zaobšla z združitvijo funkcij in kakšno dodatno for zanko. kasneje mi je sicer uspelo ugotoviti kaj je bilo narobe ampak do takrat mi je že ta nova verzija delala in "why fix something that's not broken"
4) ai načeloma nisem uporabljala, z izjemo prvih dveh regex izrazov. uporabila sem ga tako da sem najprej v sami kodi razbrala dober (enostaven + unique) izsek iz katerega se da razbrati podatke (npr ime igre inb developer/publisher so bili na 3 različnih mestih v kodi spletne strani), to mesto screenshottala in vprašala google. ((zakaj samo prvih 2-krat? ker se je potem ko sem pisala bolj komplicirano/daljšo kodo tokrat zmotil da mi je šel na živce in sem mogla njegovo kodo toliko spremeniti da je bilo v bistvu vseeno če jo naredim sama)) screenshoti pogovora so spodaj, saj se mi zdi da ste to omenili na predavanjih da je treba dodati ((upam da dela??? readme je dodal pot? or something???)):
<img width="313" height="321" alt="Screenshot 2026-08-27 180813" src="https://github.com/user-attachments/assets/83940e4f-700f-411e-9d8a-a2f55628e9b9" />
<img width="310" height="354" alt="Screenshot 2026-08-27 180748" src="https://github.com/user-attachments/assets/c9cabf69-299c-4d23-92de-bdb70e6f53f6" />


*) steam charts se redno in velikokrat updata in moja koda je spisana tako da vedno zajame najbolj aktualne podatke tako če/ko boste sami zagnali kodo obstaja možnost da bo lestvica drugačna kot ko sem kodo bognala sama in zato datoteke igre.csv ipd imele nekoliko drugačno zaporedje/sestavo

