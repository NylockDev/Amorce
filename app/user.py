from colorama import Fore,Back,Style
import sys,os
sys.path.append(os.path.abspath("../"))
sys.path.append(".")
import os
from util import clear, afficher_heure

def menu():
    print(Fore.BLUE)
    art=("""
    ___           _      _                                _
  / _ \_ __ ___ (_) ___| |_    __ _  __ _  ___ _ __   __| | __ _
 / /_)/ '__/ _ \| |/ _ \ __|  / _` |/ _` |/ _ \ '_ \ / _` |/ _` |
/ ___/| | | (_) | |  __/ |_  | (_| | (_| |  __/ | | | (_| | (_| |
\/    |_|  \___// |\___|\__|  \__,_|\__, |\___|_| |_|\__,_|\__,_|
              |__/                  |___/
              """)
    print(art)
    print(Fore.RESET)

    print(Fore.CYAN+"    BIENVENUE DANS LE PROJET AGENDA")

    
    query=input(""" 
    Que voulez vous faire?
        1) enregistrez un evenement
        2) enregistrez une note
        3) calculer la moyenne 
        4) consulter l'agenda
        5) voir les notes

    """+Fore.RESET)
    return query


def menu_evenement():
    print(Style.BRIGHT+Fore.BLUE+ " Quel evenement soitiez vous enregistrer\n1)devoir\n2)interrogation\n3) examen "+Style.RESET_ALL)
    choix=input()
    return choix


def menu_note():
    choix_matiere=input(Fore.CYAN+" dans quel matiere souhaite tu enregistrer une note? "+Fore.RESET)



def menu_moyenne():
    choix=input(Fore.BLUE+""" 
    quel moyenne?
    1) moyenne trimestriel ou semestriel
    2) moyenne d'une matiere
    """+ Fore.RESET)



def menu_voir_notes():
    art=("""
.　　　 ＿＿＿
　　 ／　　　▲
 ／￣　 ヽ　■■
●　　　　　■■
ヽ＿＿＿　　■■
　　　　）＝｜
　　　／　｜｜
　 ∩∩＿＿とﾉ
　しし───┘
    """)
    print(f"""
    {art} ok les notes de quels matieres souhaitiez vous consultez?
    """)

def agenda():
    pass

if __name__=="__main__":
    menu()
    menu_note()
    menu_evenement()
    menu_voir_notes()
    menu_moyenne()
    menu_voir_notes()
