# IMPORT AREA
try:
    from colorama import Fore, Back, Style,init
except ModuleNotFoundError:
    print("\033[31m"+" ERREUR: le module colorama n'est pas installé executez \" pip install -r requirement.txt ou pip install colorama\"\033[0m")
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
                    hello

                   )




# END OF IMPORT AREA


# THE MAIN FUNCTION
# module colorama init with an effects autoreset
init(autoreset=True)


def main():
    
    
    
    if not os.path.exists('.done'):
        hello()
        print("Taper sur la touche entrer pour continuer")
        input()
        done=open('.done','w')
        done.close()
    util.clear()
    ok=" 【✔】"
    description = " le programme ultime pour les etudiants en RIT"
    logo="""
            
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╭━╮╭━━╮╭━━╮╭━━╮╭━╮╭━━╮╭━━╮╭━━╮   ╭━━╮╭━━╮╭╮╭━╮╭━━╮
┃╭╯┃┃━┫┃╭╮┃┃┃━┫┃╭╯┃╭╮┃┃╭╮┃┃┃━┫   ┃╭╮┃┃╭╮┃┣┫┃╭╯┃┃━┫
┃┃╱┃┃━┫┃╰╯┃┃┃━┫┃┃╱┃╭╮┃┃╰╯┃┃┃━┫   ┃╰╯┃┃╭╮┃┃┃┃┃╱┃┃━┫
╰╯╱╰━━╯┃╭━╯╰━━╯╰╯╱╰╯╰╯╰━╮┃╰━━╯   ┃╭━╯╰╯╰╯╰╯╰╯╱╰━━╯
╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱   ┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱   ╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱

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
    
    new=Fore.GREEN+"[NEW]"
    indispo=Fore.RED+" [INDISPONIBLE]"
    #LOGO= os.system(" cat opp.txt | lolcat")
    #print(type(LOGO))
# os.name='nt'
    if os.name=='posix':
        os.system(" figlet projet AMORCE | lolcat")
        print( Fore.CYAN+"[Github:"+Fore.RED+"NylockDev]")
        print(Fore.CYAN+"●❯────────────────❮●●❯─────●❯────────────────❮●●❯──────────────────❮●)")
        print(Back.RED+"version pour nt et posix\nV1.1.0"); print()
        os.system(" cat opp | lolcat")
    else:

        print(Fore.CYAN+"       "+ico)
        print(Fore.BLUE+"                                     V1.1.0")
        print(Fore.RED+" ◆ ▬▬▬▬▬▬▬▬▬▬▬▬ ◆For Windows ◆ ▬▬▬▬▬▬ ▬▬▬▬▬▬+ ")
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
    print(Fore.BLUE+"    [5] afficher le tableau de la structure du cable de 28 paires"+Fore.GREEN+" "+new)
    print()
    print(Style.BRIGHT+" Tapez 'q' pour quiter")
    
    while True:
   
        choix = input(' VOTRE CHOIX'+ Fore.CYAN+ ' ')
        # choix='1'
        if choix == '1':
            util.clear()
            print(logo)

            print(Fore.CYAN+" Le cable est-il rempli oui ou non? ou tapez 's' pour rentrez plutot la serie du cable")
            while True:
                msg_err=" tapez 'oui' ou 'non' ou 's'  "

                contenance_oil = input( msg_err)            
                if contenance_oil == 'oui':
                    contenance_oil = True
                    break

                elif contenance_oil == 'non':

                    contenance_oil = False
                    break

                elif contenance_oil == 's':
                    while True:
                        serie = input(" quel est la serie? ")

                        if serie in liste_serie_nr:
                            contenance_oil = False
                            break

                        elif serie in liste_serie_rempli:
                            contenance_oil = True
                            break

                        else:
                            print(Fore.RED+" la serie n'est pas reconnu")
                    break
                else:
                    print(Fore.RED+" Entreé Invalide")

            while True:
                try:
                    cable = int(input(Fore.YELLOW+" Quel est la capacité du cable? ex(224)  "))
                    if not cable in liste_cable:
                        print(Fore.RED+"cable standardisé non reconnue ")
                        for i in liste_cable:
                            print(Fore.YELLOW+f" cable de: {i}p ")
                        print("sont reconnus")
                    elif cable < 28:
                        print(" les cables inferieurs à 28 paires ne sont pas pris en charge")
                    else:
                        pair_to_lct=1e11
                        while pair_to_lct > cable:
                            pair_to_lct = int(input(Fore.LIGHTBLUE_EX+"Entrez maitenant la paire que vous souhaitiez reperer dans le cable de "+str(cable)+" paires "))
                            if pair_to_lct > cable:
                                print(Fore.LIGHTRED_EX+"ERREUR:  la paire à reperer ne peut pas être superieur au cable!")
                        break
                except ValueError:
                    print(Fore.RED+" entrez une valeur numerique svp")
                    util.barre_chargement()
                    util.clear()
                    print(logo)



            info_cable= [cable,
                        contenance_oil]

            #print(info_cable)
            resultat,tag=reperage_paire(info_cable,pair_to_lct)
            art = r"""
┴┬┴┬／￣＼＿／￣＼
┬┴┬┴▏　　▏▔▔▔▔＼
┴┬┴／＼　／　　　　　　﹨
┬┴∕　　　　　　　／　　　）
┴┬▏　　　　　　　　●　　▏
┬┴▏　　　　　　　　　　　▔█◤
┴◢██◣　　　　　　 ＼＿＿／
┬█████◣　　　　　　／　
┴█████████████ ◣
◢██████████████▆▄
█◤◢██ ◣◥█████████ ◤＼
◥◢ ████　████████◤　　 ＼
┴█████　██████◤　　　　　 ﹨
┬│　　　│█████ ◤　　　　　　　▏
┴│　　　│　　　　　　　　　　　　▏
┬∕　　　∕　　　　／▔▔▔＼　　   　 ∕
*∕＿＿_／﹨　　　∕　　　　﹨   　　／
┬┴┬┴┬┴＼ 　　 ＼_　　　　﹨　      ＼_
┴┬┴┬┴┬┴ ＼＿＿＿＼　　　 ﹨＿＿＿＿＼
            """
            mark="""
 █▄░▒█ █░░▒█ █░░░ █▀▀▀█ █▀▀█ █░▄▀   █▀▀▄ █▀▀▀ █░░▒█
 █▒█▒█ █▄▄▄█ █░░░ █░░▒█ █░░░ █▀▄░   █░▒█ █▀▀▀ ▒█▒█░
 █░░▀█ ░▒█░░ █▄▄█ █▄▄▄█ █▄▄█ █░▒█   █▄▄▀ █▄▄▄ ░▀▄▀░
            """
            util.clear()

            print()
            print(Fore.BLUE+" cable: "+str(cable)+ " paires")
            if contenance_oil: print(Fore.BLUE+" rempli: oui")
            else: print(Fore.BLUE+" rempli: non")
            print(Style.DIM+Fore.LIGHTBLUE_EX+mark)
            for i in resultat:
                print(Fore.GREEN+i,end='')
                sleep(0.02)
            print()
            util.barre_chargement()
            for i in tag:
                print(Fore.YELLOW+Style.BRIGHT+i,end="")
                sleep(0.02)
            print()
            print("Tapez entrer pour continuer ou n'importe quoi pour quiter")
            choix=input()
            if choix=="":
                main()
            
            else:  
                print(ok)
                quit()
                
            
        elif choix == '2':
            for i in LISTE:
                print(Fore.CYAN+i,end='')
                sleep(0.01)
        elif choix == '3':
            print(Fore.RED+"Fonctionnalité indisponible")
        elif choix == '4':
            print(Fore.RED+" Fonctionnalité Indisponible")
        elif choix == '5':
            print("Ouverture du fichier pdf...")
            if os.name=='posix':
                os.system("xdg-open doc/quarte.pdf")
            else: os.system("start doc/quarte.pdf ")

            util.clock()
        elif choix =='q':
            
            print(Fore.CYAN+" MERCI!!")
            print(r"""
  ✋
   \ 😜                         Auteur:    { Kouadio Toussaint }
      |                          Ghithub :  { NylockDev  }
      |                          mail:     {adoutoussaint5@gmail.com}
      ((>
     / \
                  """,end='')
            quit()

        
        else:
            print(Fore.RED+ " ERREUR: CHOIX INVALIDE")

    













if __name__=="__main__":
    main()
