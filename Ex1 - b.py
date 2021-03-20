n=int(input(print("Digite o termo 'N'")))
s=100
for i in range(1,n+1):
    if i%2==0:
        s+=i
    else:
        s-=i
print("O valor de S passou de 100 para: ",s)
    
