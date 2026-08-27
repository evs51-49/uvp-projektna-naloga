#main stats page -> single game page stats -> actual game on steam (nvm the last one can be skipped)
import re
import requests
import time
import html
import datetime

#main_stats_page = "http://steamcharts.com/top/p.2"

HEADERS = {"User-Agent":"Mozilla/5.0"}

#STEVILO = 4

vzorec_charts_for25 = re.compile(
    r'<td>(?P<stevilka>\d+)\.</td>\s*'
    r'<td class="game-name left">\s*<a href="(?P<link>[^"]+)".*?>(?P<game_name>.*?)</a>\s*</td>\s*<td class="num">(?P<number>\d+)</td>',  
    re.DOTALL
)

def chimeraabomination_kivrne_osnovneinfo(stevilo_strani):
    osnovni_profver = []
    osnovni_mytrial = []
    linki_iger_charts = []
    linki_iger_steamstore = []

    for i in range(1, stevilo_strani + 1):
        odgovor_i = requests.get(
            f"https://steamcharts.com/top/p.{i}",
            headers=HEADERS
        )

        vsebina_i = odgovor_i.text

        listek_i = vzorec_charts_for25.findall(vsebina_i)

        for j in range(25):
            linki_iger_charts.append("https://steamcharts.com" + listek_i[j][1])
            linki_iger_steamstore.append("https://store.steampowered.com" + listek_i[j][1])
            info_j = {
                "mesto_na_lestvici": listek_i[j][0],
                "povezava_na_steamstore": "https://store.steampowered.com" + listek_i[j][1],
                "ime_igre": listek_i[j][2].strip(),
                "stevilo_gamerjev": listek_i[j][3].strip()
            }
            osnovni_mytrial.append(info_j)

    return osnovni_mytrial

        #for najdba in vzorec_charts_for25.finditer(vsebina_i):
        #    #print(najdba)
        #    #print(counter)
        #    #counter += 1
#
        #    povezava = "https://store.steampowered.com" + najdba["link"]
#
        #    info = {
        #        "mesto_na_lestvici": najdba["stevilka"],
        #        "povezava": povezava,
        #        "ime_igre": najdba["game_name"],
        #    }
#
        #    osnove.append(info)
        #
        #    print(osnove)
        #    return osnove


def chimeraabomination_kivrne_listlinkov(stevilo_strani):
    osnovni_profver = []
    osnovni_mytrial = []
    linki_iger_charts = []
    linki_iger_steamstore = []

    for i in range(1, stevilo_strani + 1):
        odgovor_i = requests.get(
            f"https://steamcharts.com/top/p.{i}",
            headers=HEADERS
        )

        vsebina_i = odgovor_i.text

        listek_i = vzorec_charts_for25.findall(vsebina_i)

        for j in range(25):
            linki_iger_charts.append("https://steamcharts.com" + listek_i[j][1])
            linki_iger_steamstore.append("https://store.steampowered.com" + listek_i[j][1])
            info_j = {
                "mesto_na_lestvici": listek_i[j][0],
                "povezava_na_steamstore": "https://store.steampowered.com" + listek_i[j][1],
                "ime_igre": listek_i[j][2].strip(),
                "stevilo_gamerjev": listek_i[j][3].strip(),
            }
            osnovni_mytrial.append(info_j)

    return linki_iger_steamstore









#hotla delat kt mamo v zapiskih/na githubu ampak mi ni hotl shrant zato sm skp dala oboje. therefore "chimera" above. it is inspired by:

#def pridobi_htmlje(stevilo_strani):
#    for i in range(1, stevilo_strani + 1):
#        odgovor = requests.get(
#            f"https://steamcharts.com/top/p.{i}",
#            headers=HEADERS
#        )
#
#        if odgovor.status_code != 200:
#            print("napaka", i, odgovor.status_code)
#            continue
#
#        vsebina = odgovor.text
#        dat = open(f"stran{i}.html", "w")
#        dat.write(vsebina)
#        dat.close()
#
#        time.sleep(1)
#
#
#def temelji(st_strani):
#    osnove = []
#    counter = 0
#    for i in range(1,st_strani + 1):
#        dat = open(f"stran{i}.html")
#        vsebina = dat.read()
#        dat.close()
#
#        for najdba in vzorec_charts_for25.finditer(vsebina):
#            print(najdba)
#            print(counter)
#            counter += 1
#
#            povezava = "https://store.steampowered.com" + najdba["link"]
#
#            info = {
#                "mesto_na_lestvici": najdba["stevilka"],
#                "povezava": povezava,
#                "ime_igre": najdba["game_name"],
#            }
#
#            osnove.append(info)
#
#    print(osnove)
#    return osnove
#



#    zanri_vseskp = match.group('genres').strip()
#    seznam_zanrov = re.findall(r'<a[^>]*>(.*?)</a>', zanri_vseskp)

vzorec_za_single_game_store = re.compile(
    r'<b>Title:</b>\s*(?P<title>.*?)<br>.*?'
    r'<b>Genre:</b>\s*.*?<span[^>]*>(?P<genres>.*?)</span>\s*<br>.*?'
    r'<b>Developer:</b>\s*.*?<a[^>]*>(?P<developer>.*?)</a>\s*</div>.*?'
    r'<b>Publisher:</b>\s*.*?<a[^>]*>(?P<publisher>.*?)</a>\s*</div>.*?'
    r'<b>Release Date:</b>\s*(?P<release_date>.*?)(?:<br>|</div>)',
    re.DOTALL
)


pomozen_vzorec_za_zanre = re.compile(
    r'<a[^>]*>(.*?)</a>',
    re.DOTALL
)

pomozen_vzorec_za_devs_in_publishers = re.compile(
    r'(?:^|>)([^<>\n,]+)',
    re.DOTALL
)


def single_game_info_extractor(temelji):
    veckot_osnove = []
    for i in range(len(temelji)):
        odgovormayb = requests.get(
            temelji[i].get('povezava_na_steamstore'),
            headers=HEADERS
        )

        vsebinamayb = odgovormayb.text
        listek = vzorec_za_single_game_store.findall(vsebinamayb)
        if listek == []:
            infoi = {
                "mesto_na_lestvi": temelji[i].get('mesto_na_lestvici'),
                "povezava_steamstore": temelji[i].get('povezava_na_steamstore'),
                "ime": temelji[i].get('ime_igre'),
                "stevilo_gamerjev": temelji[i].get('stevilo_gamerjev'),
                "seznam_zanrov": 'ni :/',
                "developer": 'ni :/',
                "publisher": 'ni :/',
                "release_date": 'ni :/'
            }
            veckot_osnove.append(infoi)

        else:
            seznam_zanrov = pomozen_vzorec_za_zanre.findall(listek[0][1])
            seznam_devs = pomozen_vzorec_za_devs_in_publishers.findall(listek[0][2])
            seznam_publishers = pomozen_vzorec_za_devs_in_publishers.findall(listek[0][3])
            infoi = {
                "mesto_na_lestvi": temelji[i].get('mesto_na_lestvici'),
                "povezava_steamstore": temelji[i].get('povezava_na_steamstore'),
                "ime": temelji[i].get('ime_igre'),
                "stevilo_gamerjev": temelji[i].get('stevilo_gamerjev'),
                "seznam_zanrov": seznam_zanrov,
                "developer": seznam_devs,
                "publisher": seznam_publishers,
                "release_date": listek[0][4],
            }
            veckot_osnove.append(infoi) 

    return veckot_osnove








#HERE IS WHERE WE GO BY THE RANKS -- 25 GAMES AT THE TIME, COLLECT RANK + LINKS PUT EM IN A LIST TO GET TO STEAMSTORE

#odgovor1 = requests.get(
#    f"http://steamcharts.com/top/p.2",
#    headers=HEADERS
#)
#vsebina1 = odgovor1.text
#dat1 = open("stranii3.html", "w", encoding="utf-8")
#dat1.write(vsebina1)
#dat1.close()
#time.sleep(1)
#
#
#vzorec1 = re.compile(
#    r'<td>(?P<stevilka>\d+)\.</td>\s*'
#    r'<td class="game-name left">\s*<a href="(?P<link>[^"]+)".*?>(?P<game_name>.*?)</a>',
#    re.DOTALL
#)
#
#html_koda1 = vsebina1
#
#listek = vzorec1.findall(html_koda1)
#for i in range(25):
#    listek[i][2].strip()
#
#print(listek[1][2].strip())
#print(listek)
#
#
#linki_iger_charts = []
#linki_iger_steamstore = []
#for i in range(25):
#    linki_iger_charts.append("https://steamcharts.com" + listek[i][1])
#    linki_iger_steamstore.append("https://store.steampowered.com" + listek[i][1])
#
#print([[[linki_iger_charts]]], [[[linki_iger_steamstore]]])
#print(html_koda)
#
#
#
#
#
##HERE IS SINGLE GAME -- COLLECT INFO OF THE GAME
#
#odgovor2 = requests.get(
#    f"https://store.steampowered.com/app/629520/Soundpad/",
#    headers=HEADERS
#)
#vsebina2 = odgovor2.text
#dat2 = open("stran2.html", "w", encoding="utf-8")
#dat2.write(vsebina2)
#dat2.close()
#time.sleep(1)
#
#
#vzorec2 = re.compile(
#    r'<b>Title:</b>\s*(?P<title>.*?)<br>.*?'
#    r'<b>Genre:</b>\s*.*?<span[^>]*>(?P<genres>.*?)</span>\s*<br>.*?'
#    r'<b>Developer:</b>\s*.*?<a[^>]*>(?P<developer>.*?)</a>\s*</div>.*?'
#    r'<b>Publisher:</b>\s*.*?<a[^>]*>(?P<publisher>.*?)</a>\s*</div>.*?'
#    r'<b>Release Date:</b>\s*(?P<release_date>.*?)(?:<br>|</div>)',
#    re.DOTALL
#)
#
#html_koda2 = vsebina2
#
#match = vzorec2.search(html_koda2)
#if match:
#    ime = match.group('title').strip()
#    zanri_vseskp = match.group('genres').strip()
#    seznam_zanrov = re.findall(r'<a[^>]*>(.*?)</a>', zanri_vseskp)
#    dev = match.group('developer').strip()
#    založnik = match.group('publisher').strip()
#    datum = match.group('release_date').strip()
#    print(f"Založnik: {založnik}")
#    print(f"Datum izida: {datum}")
#    print(f"Ime je {ime}")
#    print(f"Žanri: {str(seznam_zanrov)}")
#    print(f"devs: {dev}")
#else:
#    print("nothin")
#
#
#
#

#lowk useless here but i need track rec

#match = vzorec.search(html_koda)
#if match:
#    linkkk = match.group('link').strip()
#    ime_igre = match.group('game_name').strip()
#    mesto_na_lestvici = match.group('stevilka').strip()
#    
#    print(f"link na steam: {linkkk}")
#    print(f"ime: {ime_igre}")
#    print(f"full link: {str("https://steamcharts.com" + linkkk)}")
#
#    print(f"mesto na lestvici: {mesto_na_lestvici}")
#    
#else:
#    print("nothin")

#end of useless track rec