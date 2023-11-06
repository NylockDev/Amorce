# IMPORT AREA
try:
    from colorama import Fore, Back, Style,init
except ModuleNotFoundError:
    print("\033[31m"+" ERREUR: le module colorama n'est pas installé faite pip install -r requirement.txt ou pip install colorama"+"\033[0m")
    exit()
import os,sys
from time import sleep
sys.path.append("app")
sys.path.append("tools")
from app import *
from tools import (LISTE, 
                   info, 
                   liste_serie_nr, 
                   liste_serie_rempli,
                   liste_cable,
                   reperage_paire,


                   )




# END OF IMPORT AREA


# THE MAIN FUNCTION
# module colorama init with an effects autoreset
init(autoreset=True)


def main():
    
    util.clear()
    ok=" 【✔】"
    description = " le programme ultime pour les etudiants en RIT"
    logo="""
            

┏━┓░░░░░░░┏┓░░░┏┓░  ┏━━┓┏━┳━┓┏━┓┏━┓┏━┓┏━┓
┃╋┃┏┳┓┏━┓░┣┫┏━┓┃┗┓  ┃┏┓┃┃┃┃┃┃┃┃┃┃╋┃┃┏┛┃┳┛
┃┏┛┃┏┛┃╋┃┏┛┃┃┻┫┃┏┫  ┃┣┫┃┃┃┃┃┃┃┃┃┃┓┫┃┗┓┃┻┓
┗┛░┗┛░┗━┛┗━┛┗━┛┗━┛  ┗┛┗┛┗┻━┻┛┗━┛┗┻┛┗━┛┗━┛




    """
    ico = """
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱   ╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
┃╭━╮┃╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╯╰╮   ┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
┃╰━╯┃╭━╮╭━━╮╱╰╯╭━━╮╰╮╭╯   ┃┃╱┃┃╭╮╭╮╭━━╮╭━╮╭━━╮╭━━╮
┃╭━━╯┃╭╯┃╭╮┃╱╭╮┃┃━┫╱┃┃╱   ┃╰━╯┃┃╰╯┃┃╭╮┃┃╭╯┃╭━╯┃┃━┫
┃┃╱╱╱┃┃╱┃╰╯┃╱┃┃┃┃━┫╱┃╰╮   ┃╭━╮┃┃┃┃┃┃╰╯┃┃┃╱┃╰━╮┃┃━┫
╰╯╱╱╱╰╯╱╰━━╯╱┃┃╰━━╯╱╰━╯   ╰╯╱╰╯╰┻┻╯╰━━╯╰╯╱╰━━╯╰━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱╱╱╰━╯╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱    
    """

    indispo=Fore.RED+" [INDISPONIBLE]"
    #LOGO= os.system(" cat opp.txt | lolcat")
    #print(type(LOGO))
    # os.name='nt'
    if os.name=='posix':
        os.system(" figlet projet AMORCE | lolcat")
        print( Fore.CYAN+"[Ghithub:"+Fore.RED+"NylockDev]")
        print(Fore.CYAN+"●❯────────────────❮●●❯─────●❯────────────────❮●●❯──────────────────❮●)")
        print(Back.RED+"version pour Linux🐧\nV1.0.1"); print()
        os.system(" cat opp | lolcat")
    else:

        print(Fore.CYAN+"       "+ico)
        print(Fore.BLUE+"                                     V1.0.1-forWin")
        print(Fore.RED+" ◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆For Windows ◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬+ ")
        print()       

    print()
    print("                  "+description.upper())
    print()
    print(" que veux tu faire avec le programme, choisir un numero")
    print()
    print(Style.BRIGHT+Fore.LIGHTGREEN_EX+'    [1]'+Fore.CYAN+" Determiner une paire dans un câble (ex: 232e p  dans un cable de 448p)")
    print()
    print(Style.BRIGHT+Fore.LIGHTBLUE_EX+"    [2]"+Fore.YELLOW+" afficher la liste des composition de câble")
    print()
    print(Fore.YELLOW+"    [3]"+Fore.CYAN+" Determiner l'appartenance d'une quarte  à un faicseau",indispo)
    print()
    print(Fore.LIGHTWHITE_EX+"    [4]"+Style.BRIGHT+Fore.BLUE+" Donner les couleurs d'une paire a partir des informations fourni ",indispo)
    print()
    print(Style.BRIGHT+" Tapez 'q' pour quiter")
    
    while True:
   
        choix = input(' VOTRE CHOIX'+ Fore.CYAN+ ' ')
        # choix='1'
        if choix == '1':
            util.clear()
            print(logo)

            while True:
                print(Fore.CYAN+" Le cable est-il rempli ou non si ce n'est pas donné tapez 's' pour rentrez plutot la serie")
                msg_err=" tapez 'oui' ou 'non' ou 's'  "

                contenance_oil = input( msg_err)            
                if contenance_oil == 'oui':
                    contenance_oil = True
                    break

                elif contenance_oil == 'non':

                    contenance_oil = False
                    break

                elif contenance_oil == 's':

                    serie = input(" quel est la serie? ")

                    if serie in liste_serie_nr:
                        contenance_oil = False
                        break
                    
                    elif serie in liste_serie_rempli:
                        contenance_oil = True
                        break
                    else:
                        print(" la serie n'est pas reconnu")
                else:
                    print(Fore.RED+" Entreé Invalide")

            while True:
                try:
                    cable = int(input(Fore.YELLOW+" Quel est la capacité du cable? ex(1792)  "))
                    if not cable in liste_cable:
                        print(Fore.RED+"cable standardisé non reconnue ")
                        for i in liste_cable:
                            print(Back.YELLOW+f" CABLE STANDARDISE: {i}p ")
                    elif cable < 28:
                        print(" les cables inferieurs à 28 paires ne sont pas pris en charge")
                    else:
                        pair_to_lct=1e11
                        while pair_to_lct > cable:
                            pair_to_lct = int(input("Entrez maitenant la paire que vous souhaitiez localiser dans le cable de "+str(cable)+" paires "))
                            print(Fore.LIGHTRED_EX+" NB: la paire à localiser ne doit pas etre superieur au cable!")
                            if pair_to_lct <= cable:
                                break
                        break
                except ValueError:
                    print(Fore.RED+" entrez une valeur numerique")
                    sleep(2)
                    util.clear()
                    print(logo)



            info_cable= [cable,
                        contenance_oil]

            #print(info_cable)
            resultat=reperage_paire(info_cable,pair_to_lct)
            art = """
┈┈┈╱▔▔▔╲
▇▔▔┈▍▍┃┈┃╭━╮eab5ec4d9d85201b261c1d8e2cd0dd532ac4f1c9
╲━━╯┈┈┃┈┃╰╮┃
┈▔▔▔┃┈╰━╯╲┃┃
┈┈┈┈┃┃┃┈┈▕┃┃
┈┈┈┈┃┃┃╭┛▕╯┃
┈┈┈┈┗┻┛┗━╯━╯

            """

            print()
            print(Fore.BLUE+" cable: "+str(cable)+ " paires")
            if contenance_oil: print(Fore.BLUE+"rempli: oui")
            else: print(Fore.BLUE+"rempli: non")
            print(Style.BRIGHT+Fore.GREEN+art+ resultat)
            
            break
            
        elif choix == '2':
            for i in LISTE:
                print(Fore.CYAN+i,end='')
                sleep(0.01)
        elif choix == '3':
            print("Fonction non dispo pour le moment")
        elif choix == '4':
            print(Style.BRIGHT+" Fonctionnalité Indisponible")
        elif choix =='q':
            
            print(Fore.CYAN+" MERCI!!")
            print(r"""
  ✋
   \ 😜                         Auteur:    { Kouadio Toussaint }
      ((>
     / \
                  """,end='')
            quit()

        
        else:
            print(Fore.RED+ " ERREUR: CHOIX INVALIDE")

    



































if __name__=="__main__":
    main()
