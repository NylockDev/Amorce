import sys
from colorama import Fore,Back, Style, init

init(autoreset=True)
sys.path.append("..")
rempli = True
from tools import reperage_paire

#CABLE
info=[896                 ,


      True]
# PAIR A LOCALISER

pair_tolc=      490
8





resultat,tag=reperage_paire(info,pair_tolc)


print()
print(Fore.RED+" cable: "+str(info[0])+ " paires")
if rempli: print(Fore.RED+"rempli: oui")
else: print(Fore.RED+"rempli: non")
print(Style.BRIGHT+Fore.GREEN+ str(resultat))
print(Fore.YELLOW+tag)
