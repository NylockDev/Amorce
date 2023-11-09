import os
import sys
from time import sleep
sys.path.append(".")
import info
from colorama import Fore, Back, Style




def recherche(pair:int,rempli:bool):
    index_quarte=0
    index_amorce=0
    amorce =[]
    quarte = 0
    for q in range(len(QUARTE)):
        
        
        if pair in QUARTE[q]:

            index_quarte= q
            quarte = QUARTE[index_quarte]
            if rempli:
                quarte[1][0] = "Vi"
            break
    

    for a in range (len(AMORCE)):
        
        if  pair in AMORCE[a]:
            index_amorce=a
            amorce = AMORCE[index_amorce]
            if rempli:
                for i,p in enumerate(amorce):
                    if "I" in p[1]:
                       amorce[i][1]="Vi"


            break

        
    return index_quarte,index_amorce,quarte,amorce

# cable de 28 paire non rempli
QUARTE=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]


P=[ ["G","Ba"],
   ["I","Be"],
   ["G","J"],
   ["I","M"],
   ["G","N"],
   ["I","R"],
   ["G","Ve"],
   ["I","Ba"],
   ["G","Be"],
   ["I","J"],
   ["G","M"],
   ["I","N"],
   ["G","R"],
   ["I","Ve"],
   ["O","Ba"],
   ["Vi","Be"],
   ["O","J"],
   ["Vi","M"],
   ["O","N"],
   ["Vi","R"],
   ["O","Ve"],
   ["Vi","Ba"],
   ["O","Be"],
   ["Vi","J"],
   ["O","M"],
   ["Vi","N"],
   ["O","R"],
   ["Vi","Ve"]

   ]
# 

AMORCE= [1,2,3,4]

AMORCE[0]=P[0:6+1] 
AMORCE[1]=P[7:13+1]
AMORCE[2]= P[14:20+1]
AMORCE[3]= P[21:27+1]



QUARTE[0] = P[0:1+1]
QUARTE[1] = P[2:3+1]
QUARTE[2] = P[4:5+1]
QUARTE[3] = P[6:7+1]
QUARTE[4] = P[8:9+1]
QUARTE[5] = P[10:11+1]
QUARTE[6] = P[12:13+1]
QUARTE[7] = P[14:15+1]
QUARTE[8] = P[16:17+1]
QUARTE[9]=  P[18:19+1]
QUARTE[10]= P[20:21+1]
QUARTE[11]= P[22:23+1]
QUARTE[12]= P[24:25+1]
QUARTE[13]= P[26:27+1]

def reperage_paire(info_cable:list,pair_to_lcr:int):


    if pair_to_lcr > info_cable[0]:
        print(Fore.LIGHTRED_EX+" ERREUR: valeur superieur au cable lui meme")
        quit()



    # for i in P:
        # print(i)




    # for i in range( len( AMORCE)):
        # print( "AMORCE"+str(i+1),AMORCE[i])

    cable = info_cable[0]
    rempli = info_cable[1]
    # pair_to_lcr= 179
    TORON = ('Ba','Be','J','M','N','R','Ve','Vi')
    TETE = TORON
    TETE_2x=TORON
    pair = 0
    TYPE = "A"
    resultat = ""
    if cable == 28:
        pair= P[pair_to_lcr-1]
        iq,ia,quarte,amorce = recherche(pair,rempli)  
        if not pair in P[0:14]:
            TYPE = "B"
        if rempli:
            if pair[0] == "I":
                pair[0]= "Vi"

        print(f" la paire {pair_to_lcr} a pour couleur {pair} type {TYPE} est situé dans l'amorce{ia+1}:  la quarte{iq+1}: {QUARTE[iq]}") 

      
    

    if cable >28:
        

        compteur_toron = []
        compteur_index_pair = []
        index_toron = 0
        numero_toron=1
        compteur_tete = []
        index_tete = 0
        numero_tete = 1
        compteur_amorce = []
        numero_amorce = 1
        compteur_iter =[] 
        for i in range(cable):
            compteur_tete.append(i)
            compteur_index_pair.append(i)
            compteur_toron.append(i)
            compteur_amorce.append(i)
            compteur_iter.append(i)

            if i == pair_to_lcr -1:
                break
                

            if cable == 56:
                if len(compteur_toron) == 14 +1:
                    compteur_toron =[]
                    index_toron += 1

            if len(compteur_toron) == 28 +1:
                compteur_toron =[]
                numero_toron +=1
                index_toron += 1
            
            if cable  == 896 or 448:
                
                if len(compteur_tete) == 111 +1:


                    index_toron = 0
                    compteur_toron = []
                    numero_toron = 1
            # print(index_toron)
            # print("numeri toron",numero_toron) 
            # print(" xompteur toron",compteur_toron) 
            if len(compteur_tete) == 111 +1:
                compteur_tete = []
                index_tete +=1
                numero_tete += 1


            if len(compteur_index_pair) == 27 +1:
                compteur_index_pair = []

            
            # if cable == 224:
            #     if len(compteur_toron) == 27 +1:
            #         index_toron +=1
            #         numero_toron +=1
            #         compteur_toron = []


            # print(compteur_amorce)f 
            if len(compteur_amorce) == 6 +1:
                compteur_amorce = []
                numero_amorce += 1
            # print("i=",i)
            pair = P[len(compteur_index_pair)]

        if not cable == 1792:

            toron = TORON[index_toron]
        
         
            tete = TETE[index_tete]
        iq,ia,quarte,amorce=recherche(pair,rempli)
        
        resultat =""
        tag= ""
        if not pair in P[0:14]:
            TYPE = "B"
        if rempli:
            if pair[0]=="I":
                pair[0]= "Vi"

    
        amorce_exact=[1,2,3,4] 
        nbre_amorce = numero_amorce
        while not nbre_amorce in amorce_exact:
            nbre_amorce -= 4
        if not pair in AMORCE[nbre_amorce-1]:
            numero_amorce -= 1
                #amorce =AMORCE[numero_amorce-2]
    
            # print(" numero amorce: ",numero_amorce)
            # print("nombre amorce: ",nbre_amorce)
        # print("amorce:",amorce,"Quarte:",quarte)
            
        cable_make_112 = (448,896) 

        if  cable in cable_make_112:

            compteur_amorce=[]
            numero_amorce =1
            compteur_tete=[]
            for i in range(cable):
                compteur_amorce.append(i)
                compteur_tete.append(i)
                if i == pair_to_lcr -1:
                    break
                
                
                if len(compteur_tete) == 111+1:
                    compteur_tete=[]
                    numero_amorce=1
                    compteur_amorce=[]
                    

                if len(compteur_amorce) == 6+1:
                    compteur_amorce=[]
                    numero_amorce+=1

            resultat = f"""

    
la paire {pair_to_lcr} est situé dans la Too {numero_tete} Gros filin {tete} petit filin {toron},l'amorce {numero_amorce} (amorce {ia+1}), la quarte{iq+1} dont les couleur sont {quarte} paire {amorce.index(pair)+1} {pair}

                    """
            tag= f"""
Too {numero_tete}
Gros filin {tete}
Petit filin {toron}
A{numero_amorce}
Type {TYPE}
Q{iq+1} ({quarte[0][0]}-{quarte[0][1]}; {quarte[1][0]}-{quarte[1][1]})
P{amorce.index(pair)+1} ({pair[0]}-{pair[1]})
                                        """
    
        if cable == 1792:
            index_2x_tete=0
            index_toron = 0
            compteur_2x_tete=[]
            compteur_toron=[]
            numero_toron =1
            numero_2x_tete =1
            compteur_1_toron = []
            compteur_amorce=[]
            numero_amorce=1
            for i in range(cable): 
                if i == pair_to_lcr -1:
                    break
                compteur_toron.append(i)
                compteur_2x_tete.append(i)
                compteur_amorce.append(i)
                # print(numero_2x_tete)

                if len(compteur_toron) == 27+1:
                    index_toron += 1
                    numero_toron += 1
                    compteur_toron = []

                if len(compteur_2x_tete) == 223 +1:
                    index_2x_tete +=1
                    numero_2x_tete += 1
                    compteur_2x_tete = []
                    numero_amorce=1
                    compteur_amorce=[]

            # print(index_tete)
                if numero_toron ==9:
                    numero_toron = 1
                    index_toron =0
            # real_toron= [1,2,3,4]
            # while not numero_toron in real_toron:
                # numero_toron -= 4
            
                if len(compteur_amorce) == 6+1:
                    numero_amorce += 1
                    compteur_amorce=[]
            toron=TORON[index_toron]
            #tete = TETE[index_tete]
            resultat = (f"""

la paire {pair_to_lcr} est situé dans le {numero_2x_tete}e(r) 224 gros filin {TETE_2x[index_2x_tete]}, Toron{numero_toron} petit filin {TORON[index_toron]} , Amorce {numero_amorce} ( couleur de l'amorce {ia+1}),Type {TYPE}  Quarte {iq+1} dont les couleur sont  {quarte} Paire {amorce.index(pair)+1} {pair}""")
                    


            tag= f"""
{numero_2x_tete}e 224 Gros filin {TETE_2x[index_2x_tete]}
 Toron {numero_toron} Petit filin {TORON[index_toron]}
 A {numero_amorce}
 Type {TYPE}
 Q{iq+1} ({quarte[0][0]}-{quarte[0][1]}; {quarte[1][0]}-{quarte[1][1]})
 P{amorce.index(pair)+1} ({pair[0]}-{pair[1]})
                                        """

        if cable == 112 or cable == 224:
            compteur_toron=[]
            index_toron=0
            numero_toron = 1
            
            for i in range(cable):
                if i == pair_to_lcr -1:
                    break
                compteur_toron.append(i)
                if len(compteur_toron) == 28:
                    numero_toron += 1
                    index_toron +=1
                    compteur_toron = []
            
            toron=TORON[index_toron]
            resultat = (f"""


                         
la paire {pair_to_lcr} est situé dans le Toron {TORON.index(toron)+1} filin {toron} , Amorce {numero_amorce} ( amorce {ia+1}), Type {TYPE} Quarte {iq+1} dont les couleur sont  {quarte} Paire {amorce.index(pair)+1} {pair}""")
    

            tag= f"""
Toron {numero_toron}
filin {toron}
A {numero_amorce}
Type{TYPE}
Q {iq+1} ({quarte[0][0]}-{quarte[0][1]}; {quarte[1][0]}-{quarte[1][1]})
P{amorce.index(pair)+1} ({pair[0]}-{pair[1]})
                                        """
        if cable == 56:
        

            resultat =f"""
la paire {pair_to_lcr} a pour couleur {pair} est situé dans le Toron filin {TORON[index_toron]} type {TYPE} amorce {numero_amorce} ,quarte {iq+1} de couleurs {quarte}
        """
    

            tag= f"""
Toron {TORON[index_toron]}
filin {toron}
A {numero_amorce}
Type {TYPE}
Q{iq+1} ({quarte[0][0]}-{quarte[0][1]}; {quarte[1][0]}-{quarte[1][1]})
P{amorce.index(pair)+1} ({pair[0]}-{pair[1]})
                                        """
    return resultat,tag 



if __name__ == "__main__":
    

    info=[896,False]
    pair_tolc= 500

    resultat,t1g=reperage_paire(info,pair_tolc)


    print()
    # print(Fore.RED+" cable: "+str(cable)+ " paires")
    # if rempli: print(Fore.RED+"rempli: oui")
    # else: print(Fore.RED+"rempli: non")
    print(Style.BRIGHT+Fore.GREEN+ resultat)


