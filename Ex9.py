vetor= list (range(0,10))
from random import randint
o=0
for i in range(0,10):
    vetor[i]=randint(0,100)
for i in range(0,10):
    print(vetor[i],"|",end="")
for i in range(0,10):
    if vetor[i]%3==0:
        o=o+1
        print("\n\nO número",vetor[i]," é multiplo de 3")
print("\nNo total temos",o," multiplos de 3")
