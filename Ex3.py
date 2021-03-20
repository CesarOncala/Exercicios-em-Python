div=0
for i in range(1,1000):
    div=0 
    for j in range(1,i):
        if i%j==0:
            div+=j
    if div==i:
        print("O número ",i," é um número perfeito")

            
