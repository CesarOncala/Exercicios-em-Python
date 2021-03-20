class data:
    dia=0
    mês=0
    ano=0
class aluno:
    nome=""
    idade=0
    curso=""
    dataN=data()

a= aluno()
aluno=list(range(2))
for i in range(0,1):
    aluno=list(range(2))
    a.nome=input(print("Digite seu nome"))
    a.curso=input(print("Digite o nome de seu curso"))
    a.idade=input(print("Digite sua idade"))
    print("Digite sua data de nascimento")
    a.dataN.dia=input(print("Dia"))
    a.dataN.mês=input(print("Mês"))
    a.dataN.ano=input(print("Ano"))
    aluno[i]=a


for o in range(len(aluno)):
    print(aluno[o].nome,"\n",aluno[o].curso,"\n",aluno[o].idade,"\n",aluno[o].dataN.dia,"/",aluno[o].dataN.mês,"/",aluno[o].dataN.ano)

    
