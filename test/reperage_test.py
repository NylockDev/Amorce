import sys
from colorama import Fore,Back, Style, init

init(autoreset=True)
sys.path.append("..")
rempli = False
from tools import reperage_paire

#CABLE
info=[    896                    ,


      False]
# PAIR A LOCALISER

pair_tolc=        697





resultat=reperage_paire(info,pair_tolc)


print()
print(Fore.RED+" cable: "+str(info[0])+ " paires")
if rempli: print(Fore.RED+"rempli: oui")
else: print(Fore.RED+"rempli: non")
print(Style.BRIGHT+Fore.GREEN+ resultat)
