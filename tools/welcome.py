from colorama import Fore,init
from time import sleep
import os

init(autoreset=True)

def hello():

    art="""
 █▄░▒█ █░░▒█ █░░░ █▀▀▀█ █▀▀█ █░▄▀   █▀▀▄ █▀▀▀ █░░▒█
 █▒█▒█ █▄▄▄█ █░░░ █░░▒█ █░░░ █▀▄░   █░▒█ █▀▀▀ ▒█▒█░
 █░░▀█ ░▒█░░ █▄▄█ █▄▄▄█ █▄▄█ █░▒█   █▄▄▀ █▄▄▄ ░▀▄▀░
"""


    msg="""
Bienvenue dans AMORCE, le programme phare dédié \naux etudiants en Reseau informatique et telecom.\nce script a été spécifiquement élaboré pour le cours de réseau d'acces\n,visant a repérer les couleurs des conducteurs dans un cable\nn'hesitez pas à l'utiliser librement et à contribuer à son amelioration
"""


    print(Fore.GREEN+art)

    sleep(0.4)

    for i in msg:
        print(Fore.GREEN+i,end='')
        sleep(0.01)

    print()
    print("\033[35m Auteur: Kouadio Toussaint Adou Alias NylockDev \033[0m")

if __name__=='__main__':
    hello()
