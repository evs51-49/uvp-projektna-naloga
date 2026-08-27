import re
import requests
import time
import html
import datetime

main_stats_page = "http://steamcharts.com/top/p.2"

HEADERS = {"User-Agent":"Mozilla/5.0"}

STEVILO = 4

vzorec_charts_for25 = re.compile(
    r'<td>(?P<stevilka>\d+)\.</td>\s*'
    r'<td class="game-name left">\s*<a href="(?P<link>[^"]+)".*?>(?P<game_name>.*?)</a>\s*</td>\s*<td class="num">(?P<number>\d+)</td>',
    #r'<td class="num">(?P<number>\d+)</td>',
    re.DOTALL
)


osnovni_profver = []
osnovni_mytrial = []
linki_iger_charts = []
linki_iger_steamstore = []
for i in range(1, 4):
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

#print(osnovni_mytrial)

#print(osnovni_mytrial, linki_iger_steamstore, len(linki_iger_steamstore))

#print(osnovni_mytrial[1].get('povezava_na_steamstore'), len(osnovni_mytrial))

vzorec_za_single_game_store = re.compile(
    r'<b>Title:</b>\s*(?P<title>.*?)<br>.*?'
    r'<b>Genre:</b>\s*.*?<span[^>]*>(?P<genres>.*?)</span>\s*<br>.*?'
    #r'<b>Developer:</b>\s*(?P<developer_block>(?:<a\s+[^>]*>.*?</a>,?\s*)+).*?'
    r'<b>Developer:</b>\s*.*?<a[^>]*>(?P<developer>.*?)</a>\s*</div>.*?'
    #r'<b>Developer:</b>\s*(?P<developer_blok>.*?)\s*</div>'
    r'<b>Publisher:</b>\s*.*?<a[^>]*>(?P<publisher>.*?)</a>\s*</div>.*?'
    r'<b>Release Date:</b>\s*(?P<release_date>.*?)(?:<br>|</div>)',
    re.DOTALL
)


pomozen_vzorec_za_zanre = re.compile(
    r'<a[^>]*>(.*?)</a>',
    re.DOTALL
)

pomozen_vzorec_za_devs = re.compile(
    r'(?:^|>)([^<>\n,]+)',
    re.DOTALL
)

veckot_osnove = []
for i in range(len(osnovni_mytrial)):
    odgovormayb = requests.get(
        osnovni_mytrial[i].get('povezava_na_steamstore'),
        headers=HEADERS
    )
    vsebinamayb = odgovormayb.text
    listeknov = vzorec_za_single_game_store.findall(vsebinamayb)
    #seznam_zanrov = pomozen_vzorec_za_zanre.findall(listeknov[0][1])
    if listeknov == []:
        infoi = {
            "mesto_na_lestvic": osnovni_mytrial[i].get('mesto_na_lestvici'),
            "povezava_steamstore": osnovni_mytrial[i].get('povezava_na_steamstore'),
            "ime": osnovni_mytrial[i].get('ime_igre'),
            "stevilo_gamerjev": osnovni_mytrial[i].get('stevilo_gamerjev'),
            "seznam_zanrov": "kys ig",
            "developer": "kys ig",
            "publisher": "kys ig",
            "release_date": "kys ig",
        }
        veckot_osnove.append(infoi)  

    else:
        seznam_zanrov = pomozen_vzorec_za_zanre.findall(listeknov[0][1])
        seznam_devs = pomozen_vzorec_za_devs.findall(listeknov[0][2])
        seznam_publishers = pomozen_vzorec_za_devs.findall(listeknov[0][3])
        infoi = {
            "mesto_na_lestvic": osnovni_mytrial[i].get('mesto_na_lestvici'),
            "povezava_steamstore": osnovni_mytrial[i].get('povezava_na_steamstore'),
            "ime": osnovni_mytrial[i].get('ime_igre'),
            "stevilo_gamerjev": osnovni_mytrial[i].get('stevilo_gamerjev'),
            "seznam_zanrov": seznam_zanrov,
            "developer": seznam_devs,
            "publisher": seznam_publishers,
            "release_date": listeknov[0][4],
        }
        veckot_osnove.append(infoi)    


print(veckot_osnove)
#






#    zanri_vseskp = match.group('genres').strip()
#    seznam_zanrov = re.findall(r'<a[^>]*>(.*?)</a>', zanri_vseskp)

#'Studio Wildcard</a>, <a href="https://store.steampowered.com/search/?developer=Instinct%20Games&snr=1_5_9__408">Instinct Games</a>, <a href="https://store.steampowered.com/search/?developer=Efecto%20Studios&snr=1_5_9__408">Efecto Studios</a>, <a href="https://store.steampowered.com/developer/SnailGamesUSA?snr=1_5_9__408">Virtual Basement LLC'