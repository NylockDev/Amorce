import sys
from colorama import Fore,Back, Style, init

init(autoreset=True)
sys.path.append("..")
rempli = False
from tools import reperage_paire

#CABLE
info=[28                  ,


      False]
# PAIR A LOCALISER

pair_tolc=      7





resultat,tag=reperage_paire(info,pair_tolc)


print()
print(Fore.RED+" cable: "+str(info[0])+ " paires")
if rempli: print(Fore.RED+"rempli: oui")
else: print(Fore.RED+"rempli: non")
print(Style.BRIGHT+Fore.GREEN+ str(resultat))
print(Fore.YELLOW+tag)
