#Funções:__________________________________________________________________
def cadastro():
    resp=input(print("Deseja cadastrar alguém?"))
    if resp.upper()!= "N":
        while resp.upper()!= "N":
            arq=open("teste.txt","a")
            nome=input(print("Digite seu nome"))
            arq.write("Olá"+";"+nome+";")
            arq.write("\n")
            arq.close()
            resp=input(print("Deseja continuar?"))

def pesquisa():
    pesquisa="s"
    while pesquisa!="n" and pesquisa!="N" and pesquisa!= "Não" and pesquisa!="não":
        ler=open("teste.txt","r")
        linha="a"
        resultado= list(range(3)) 
        pesquisa=input(print("Digite um nome"))
        while linha!="":
            linha=ler.readline()
            if linha!="":
                resultado=linha.split(';')
                if resultado[1]==pesquisa:
                    print(resultado[0],",",resultado[1],resultado[2])
        ler.close()            
        pesquisa=input(print("Deseja continuar? S/N"))
#Main:____________________________________________________________________
print("Hey")
o="s"
while o.upper()!="N":
    cadastro()
    pesquisa()
    o=input(print("Continuar com o sistema S/N?"))
    
    #[[0 for c in range(3)] for l in range(10)]


