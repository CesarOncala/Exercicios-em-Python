def inversor(n1):
    inverso=int(str(n1)[::-1])
    if n1==inverso:
        print("\nO número",n1," é palindromo")
    else:
        print("\nO número",n1," Não é palindromo")
            
       
        
n1=int(input(print("Digite um número inteiro de 4 algarismos")))

inversor(n1)

