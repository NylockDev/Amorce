# IMPORT AREA

import os,sys
from time import sleep
from colorama import Fore, Back, Style,init
sys.path.append("app")
from app import *





# END OF IMPORT AREA


# THE MAIN FUNCTION
# module colorama init with an effects autoreset
init(autoreset=True)

def main():

    #LOGO= os.system(" cat opp.txt | lolcat")
    #print(type(LOGO))
    if os.name=='posix':
        os.system(" figlet AMORCE | lolcat")
        print(Fore.CYAN+"●❯────────────────❮●●❯────────────────❮●)")
        print(); print()
        os.system(" cat opp | lolcat")
    else:

        motif="./opp.txt"
        with open(motif,'r')as motif:
            for i in motif.read():
                print(Fore.CYAN+i,end='')
        print()       

    print()
    print()
    print(Style.BRIGHT+Fore.LIGHTGREEN_EX+'    [1]'+Fore.CYAN+" Determiner une paire dans un câble (ex: 232e paire dans un cable de 448p)")






































if __name__=="__main__":
    main()
