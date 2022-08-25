print("Estamos " + "estudando", "Python", "pela primeira vez!")

idade = input("Digite a sua idade")
print(idade)
print(type(idade))

print("Nova Idade")
nova_idade = int(idade)
print(nova_idade)
print(type(nova_idade))

print(nova_idade * 5)

linguagem = "Java"
quantidade = "terceira"
print("Estamos", "estudando", linguagem, "pela " + quantidade , "vez!", sep="-")
print("Estamos estudando {} pela {} vez!".format(linguagem, quantidade))


