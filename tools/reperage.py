from colorama import Fore, Back, Style
import os
import sys
from time import sleep
sys.path.append(".")
import info

def general():

# structure dun cable 28p non rempli
    quarte=[  1,   2,  3,  4,  5,    6,   7,  8,  9, 10, 11, 12,  13, 14]
    paire1={
    1: [     "G"," G","G","G", "G",  "G","G","o","o","o","o",  "o","o", "o"],
        2:[  "Ba","J","N","ve","be", "M","R","Ba","J","N","Ve","Be","M","R"]}
    paire2={1:["I","I","I","I","I","I","I","Vi","Vi","Vi","Vi","Vi","Vi","Vi"],
        2:[  "Be","M","R","Ba","J","N","Ve","Be","M","R","Ba","J","N","Ve"]}
    
    AMORCES={1:{ 'quartes':quarte[0:4],
                'paires':[paire1[1][0:4],  # la premiere couleur de la paire 1
               paire1[2][0:4],  # la 2e couleur de la paire 1 ainsi de suite ...
               paire2[1][0:3],
               paire2[2][0:3]
                        ]},
            
            2:{ 'quartes':quarte[3:7],
               'paires':[paire2[1][3:7],  # la premiere premier paire est la paire 2 
               paire2[2][3:7],  # la 2e couleur de la paire 1 ainsi de suite ...
               paire1[1][4:7],
               paire1[2][4:7]
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
    return AMORCES  


def reperage_paire(info_cable:list,pair_to_lct:int):
    
    
    capacite = info_cable[0]
    rempli = info_cable[1]
    
    liste_cable = info.liste_cable
    amorces = general()
       
    # paire se recherche
    wanted_pair= 1 
    
    # debut des calculs
    interval_de_recherche= pair_to_lct

   
    quarte=0
    amorce=1
    toron= 1
    #pair=[]
    compteur_iter=[]
    
    compteur_amorce=[]
    compteur_toron= []
    compteur_tete=[]
    compteur_quarte=[]
    
    for i in range(interval_de_recherche):
        compteur_iter.append(i)

        compteur_amorce.append(i)
        compteur_toron
        compteur_tete
        if len(compteur_quarte) == 13:
            nbre_amorce= 1
            amorce += 1
            compteur_quarte=[]
        if i ==14:
            amorce=2
            
        elif i ==4:
            #index_quarte += 1
            pass
        if amorce == 4:
            toron+= 1

        if len(compteur_iter) == pair_to_lct:
            break

        




    amorce_exact=[1,2,3,4] 

    while not amorce in amorce_exact:
		
	    amorce -= 4
    
    print("amorce:",amorce,"Quarte:",quarte)






dicte=[ 28,True ]

pair = 23
reperage_paire(dicte,pair)

