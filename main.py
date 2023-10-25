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

    if os.name=='posix':
        os.system(" figlet AMORCE | lolcat")
        print(Fore.CYAN+"●❯────────────────❮●●❯────────────────❮●)")
        print(); print()
        os.system(" cat opp | lolcat")
    else:

        motif="./opp.txt"
        with open(motif,'r')as motif:
            for i in motif.read():
                print(i,end='')
        print()        





































if __name__=="__main__":
    main()
