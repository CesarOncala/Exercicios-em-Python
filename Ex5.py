A= [[0,0,0],[0,0,0],[0,0,0]]
B= [[0,0,0],[0,0,0],[0,0,0]]
soma=0
dif=0
somaa=0
somab=0
from random import randint
for i in range(0,3):
    for j in range(0,3):
        A[i][j]=randint(10,100)
        B[i][j]=randint(10,100)
        soma+= A[i][j]+B[i][j]
        somaa+=A[i][j]
        somab+=B[i][j]
if somaa>somab:
    dif=somaa-somab
else:
    dif=somab-somaa

print("Matriz A")
for i in range(0,3):
    print()
    for j in range(0,3):
        print(A[i][j],"|",end="")

print("\n\nMatriz B")
for i in range(0,3):
    print()
    for j in range(0,3):
        print(B[i][j],"|",end="")
        
print("\n\nA soma das matrizes é equivalente a: ",soma)
print("A diferença das matrizes é de: ",dif)

        
