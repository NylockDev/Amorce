# IMPORT AREA
try:
    from colorama import Fore, Back, Style,init
except ModuleNotFoundError:
    print("\033[31m"+" ERREUR: le module colorama n'est pas installé faite pip install -r requirement.txt ou pip install colorama"+"\033[0m")
    exit()
import os,sys
if os.name== 'nt':
    sys.stderr.write(Fore.RED+" ERREUR: ce programme n'est pas compatible avec les systèmes windows")
    sys.exit(0)
from time import sleep
sys.path.append("app")
# sys.path.append("util")
from app import *





# END OF IMPORT AREA


# THE MAIN FUNCTION
# module colorama init with an effects autoreset
init(autoreset=True)


def main():
    
# structure dun cable 28p non rempli
    quarte=[  1,   2,  3,  4,  5,    6,   7,  8,  9, 10, 11, 12,  13, 14]
    paire1={
    1: [     "G"," G","G","G", "G",  "G","G","o","o","o","o",  "o","o", "o"],
        2:[  "Ba","J","N","ve","be", "M","R","Ba","J","N","Ve","Be","M","R"]}
    paire2={1:["I","I","I","I","I","I","I","Vi","Vi","Vi","Vi","Vi","Vi","Vi"],
        2:[  "Be","M","R","Ba","J","N","Ve","Be","M","R","Ba","J","N","Ve"]}
    amorces={1:{ 'quartes':quarte[0:4],
                'paires':[paire1[1][0:4],  # la premiere couleur de la paire 1
               paire1[2][0:4],  # la 2e couleur de la paire 1 ainsi de suite ...
               paire2[1][0:4],
               paire2[2][0:4]
                        ]},
            
            2:{ 'quartes':quarte[3:7],
               'paires':[paire2[1][3:7],  # la premiere premier paire est la paire 2 
               paire2[2][3:7],  # la 2e couleur de la paire 1 ainsi de suite ...
               paire1[1][4:8],
               paire1[2][4:8]
                       ]},
            
            3:{ 'quartes':quarte[7:11],
               'paires':[paire1[1][7:11],  # la premiere couleur de la paire 1
               paire1[2][7:11],  # la 2e couleur de la paire 1 ainsi de suite ...
               paire2[1][7:10],
               paire2[2][7:10]
                            ]},
            
            4:{ 'quartes':quarte[10:15],
               'paires':[paire2[1][10:14],  # la premiere couleur de la paire 1
               paire2[2][10:14],  # la 2e couleur de la paire 1 ainsi de suite ...
               paire1[1][11:14],
               paire1[2][11:14]



                       ]  }}
    
    for key,value in amorces.items():
        print(f" amorce{key} :{value}")

    # util.clear()
    ok=" 【✔】"
    description = " le programme ultime pour les etudiants en RIT"

    #LOGO= os.system(" cat opp.txt | lolcat")
    #print(type(LOGO))
    if os.name=='posix':
        os.system(" figlet projet AMORCE | lolcat")
        print( Fore.CYAN+"[Ghithub:"+Fore.RED+"NylockDev]")
        print(Fore.CYAN+"●❯────────────────❮●●❯─────●❯────────────────❮●●❯──────────────────❮●)")
        print(Back.RED+"version pour Linux🐧"); print()
        os.system(" cat opp | lolcat")
    else:

        motif="./opp.txt"
        with open(motif,'r')as motif:
            for i in motif.read():
                print(Fore.CYAN+i,end='')
        print()       

    print()
    print("                  "+description.upper())
    print()
    print(" que veux tu faire avec le programme, choisir un numero")
    print()
    print(Style.BRIGHT+Fore.LIGHTGREEN_EX+'    [1]'+Fore.CYAN+" Determiner une paire dans un câble (ex: 232e p  dans un cable de 448p)")
    print(Style.BRIGHT+Fore.LIGHTBLUE_EX+"    [2]"+Fore.YELLOW+" avoir la composition d'un câble")
    print(Fore.YELLOW+"    [3]"+Fore.CYAN+" avoir la ...")
    print(Fore.LIGHTWHITE_EX+"    [4]"+Style.BRIGHT+Fore.BLUE+" localiser ...")
    
    while True:
   
        choix = input(' VOTRE CHOIX'+ Fore.CYAN+ ' ')

        if choix == '1':
            pass
        elif choix == '2':
            pass
        elif choix == '3':
            pass
        elif choix == '4':
            pass
        else:
            print(Fore.RED+ " ERREUR: CHOIX INVALIDE")





































if __name__=="__main__":
    main()
