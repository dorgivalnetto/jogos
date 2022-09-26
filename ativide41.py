#Atividade do Slide 41 da Aula 06
n = int(input("Digite a quantidade de pessoas que você quer adicionar"))
#criamos um dicionário vazio
cadastro = {}

for i in range(n):
    #Se tiver um espaço no final do texto o split() já "separa" para adicionar uma nova entrada
    (nome, CPF, idade) = input("Digite o nome, CPF e a idade").split()
    idade = int(idade)
    if not(CPF in cadastro):
        cadastro[CPF] = (nome, idade)
        print(cadastro[CPF], "adicionado")

for (CPF, dados) in cadastro.items():
    print("Imprimindo", dados[0], CPF, dados[1])


