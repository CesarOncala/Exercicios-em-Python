A= list (range(10))
B= list (range(10))
soma=0
from random import randint
for i in range(0,10):
    A[i]=randint(0,100)
    B[i]=randint(0,100)
    soma+=A[i]+B[i]
print("Vetor A")
for i in range(0,10):
    print(A[i],"|",end="")
print("\n")
print("Vetor B")
for i in range(0,10):
    print(B[i],"|",end="")
print("\nA soma dos vetores é igual a: ",soma)
    
    
