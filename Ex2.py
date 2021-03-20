maior=0
menor=100000000
o=0
media=0
o2=0
for i in range(0,15):
    alt=float(input(print("Digite sua altura")))
    sex=str(input(print("Digite seu sexo")))
    if alt> maior:
        maior=alt
    if alt<menor:
        menor=alt
    if sex.upper()=="F" or sex.upper()=="FEMININO":
        media+=alt
        o2+=1
    if sex.upper()=="M" or sex.upper()=="MASCULINO":
        o+=1
print("\nA maior altura é: ",maior," e a menor altura é: ",menor)
print("\nA média de altura das mulheres é igual a: ",(media/o2))
print("\nO número de homens é: ",o)
        
