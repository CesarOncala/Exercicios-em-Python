R= list (range(10))
S= list (range(10))
V= list (range(20))
o=0
from random import randint
for i in range(0,10):
    R[i]=randint(10,100) 
    S[i]=randint(10,100) 
for i in range(0,2):
    exist=False
    for j in range(0,o):
        if R[i]==V[j]:
            exist=True
    if exist==False:
        V[o]=R[i]
        o=o+1
for i in range(0,10):
    exist=False
    for j in range(0,o):
        if S[i]==V[j]:
            exist=True
    if exist==False:
        V[o]=S[i]
        o=o+1

print("\nVetor R")
for i in range(0,10):
    print(R[i],"|",end="")
print("\nVetor S")
for i in range(0,10):
    print(S[i],"|",end="")
print("\nVetor V")
for i in range(0,o):
    print(V[i],"|",end="")
        


    
