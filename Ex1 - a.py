n=int(input(print("Digite o valor de 'N'")))
s=0
print("S= ",end="")
for i in range(1,n):
    s+=(i-1)/i
    if i>1:
        print((i-1),"/",i,"+",end="")
print("\nO valor de S é igual a: ",s)
    
