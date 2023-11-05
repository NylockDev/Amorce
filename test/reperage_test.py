import sys

sys.path.append("..")

from tools import reperage_paire

#CABLE
info=[    1792                    ,


      False]
# PAIR A LOCALISER

pair_tolc=        500





resultat=reperage_paire(info,pair_tolc)


print()
print(Fore.RED+" cable: "+str(cable)+ " paires")
if rempli: print(Fore.RED+"rempli: oui")
else: print(Fore.RED+"rempli: non")
print(Style.BRIGHT+Fore.GREEN+ resultat)
