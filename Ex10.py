# Função
def elementos(o,matriz,vetor): 
    for i in range(0,3): #abaixo da diagonal principal
     for j in range(0,3):
        if i>j:
            vetor[o]=matriz[i][j]
            o+=1
    for i in range(0,3): #acima da diagonal principal
     for j in range(0,3):
        if i<j:
            vetor[o]=matriz[i][j]
            o+=1
    print()
    print()
    for i in range(0,o):
        print(vetor[i],"|",end="")
# Main        
matriz= [[2,0,0,],
         [0,0,0,],
         [0,0,0,]]
vetor= list(range(9))
o=0
from random import randint

for i in range(0,3):
    for j in range(0,3):
        matriz [i][j]=randint(0,100)
for i in range(0,3):
    print()
    for j in range(0,3):
       print(matriz [i][j],"|",end="")
elementos(o,matriz,vetor)




            




       

