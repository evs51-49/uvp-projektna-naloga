import csv

def shrani_igre(igre):
    dat = open("igre.csv", "w", encoding="utf-8")
    pisatelj = csv.writer(dat)
    pisatelj.writerow(
        [
            "mesto_na_lestvi",
            "povezava_steamstore",
            "ime",
            "stevilo_gamerjev",
            "seznam_zanrov",
            "developer",
            "publisher",
            "release_date",
        ]
    )

    dat2 = open("devs.csv", "w", encoding="utf-8")
    pisatelj2 = csv.writer(dat2)
    pisatelj2.writerow(["ime", "developer"])

    dat3 = open("zanri.csv", "w", encoding="utf-8")
    pisatelj3 = csv.writer(dat3)
    pisatelj3.writerow(["ime", "zanr"])

    videni_devs = set()

    for igra in igre:
        pisatelj.writerow(
            [
                igra["mesto_na_lestvi"],
                igra["povezava_steamstore"],
                igra["ime"],
                igra["stevilo_gamerjev"],
                igra["seznam_zanrov"],
                igra["developer"],
                igra["publisher"],
                igra["release_date"],
            ]
        )

        for dev in igra["developer"]:
            pisatelj2.writerow([igra["ime"], dev])
            if dev not in videni_devs:
                videni_devs.add(dev)
                

        for zanr in igra["seznam_zanrov"]:
            pisatelj3.writerow([igra["ime"], zanr])

    dat.close()
    dat2.close()
    dat3.close()
        

