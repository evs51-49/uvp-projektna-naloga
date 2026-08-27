#opomba: kodo pisem tako da bo delovala za current podatke at the time of running tko da se bojo mogoce dejanski stati spremenil z novim runnanjem kode ker se tud sama spletna stran za top games chart tko constantly updata
import shrani
import the_crossover
#import pridobi
import sys

STEVILO_STRANI = 40

osnovni_info = the_crossover.chimeraabomination_kivrne_osnovneinfo(STEVILO_STRANI)

extended_info = the_crossover.single_game_info_extractor(osnovni_info)

shrani.shrani_igre(extended_info)
#if len(sys.argv) > 1 and sys.argv[1] == "pridobi":
#    the_crossover.pridobi_htmlje(STEVILO_STRANI)
#
#osnove = the_crossover.temelji(STEVILO_STRANI)