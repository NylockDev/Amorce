
def recherche(pair:int,toron:tuple=(1,"Ba"))
    for q,a in range(len(QUARTE),len(AMORCE)):
        
        index_quarte = QUARTE[q].index(pair)
        index_amorce = AMORCE[a].index(pair)
        print(index_amorce)

        
            

        indexor.append(q)
        indexor.append(a)
        
        if len(indexor) ==2:
            break

# cable de 28 paire non rempli

QUARTE=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

P=[ ("G","Ba"),
   ("I","Be"),
   ("G","J"),
   ("I","M"),
   ("G","N"),
   ("I","R"),
   ("G","Ve"),
   ("I","Ba"),
   ("G","Be"),
   ("I","J"),
   ("G","M"),
   ("I","N"),
   ("G","R"),
   ("I","Ve"),
   ("O","Ba"),
   ("Vi","Be"),
   ("O","J"),
   ("Vi","M"),
   ("O","N"),
   ("Vi","R"),
   ("O","Ve"),
   ("Vi","Ba"),
   ("O","Be"),
   ("Vi","J"),
   ("O","M"),
   ("Vi","N"),
   ("O","R"),
   ("Vi","Ve")

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



# for r,i in enumerate(QUARTE):
    # print(r+1," ",i)




# for i in P:
    # print(i)


# print(len(P))
#print(("Vi","J") in P)



# for i in range( len( AMORCE)):
   # print( "AMORCE"+str(i+1),AMORCE[i])

cable = 28
pair_to_lcr= 23
rempli = True

if cable <=28:
    pair= P[pair_to_lcr-1]
recherche(pair)    
    
#amorce = AMORCE[indexor[1]]
#quarte = QUARTE[indexor[0]]
print(f" la paire {pair_to_lcr} a pour couleur {pair} est situé dans l'amorce {indexor[1]} la quarte {indexor[0]} dont les couleurs sont {QUARTE[indexor[0]]}")
print(indexor)
for i in range(pair_to_lcr):

    pass
