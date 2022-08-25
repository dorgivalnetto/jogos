
#gerar um número aleatório
import random
#numero_secreto = int(random.random()*100)
#print(numero_secreto)

#numero_secreto = random.random()*100
#numero_secreto = int(random.random()*100)
#print(numero_secreto)

numero_secreto = random.randrange(1, 101)
print(numero_secreto)


print("Qual o nível de dificuldade?")
print("(1) Fácil, (2) Médio, (3) Difícil")

nivel = int(input("Digite o nível de dificuldade"))

if (nivel == 1):
   total_de_tentativas = 20
elif (nivel == 2):
   total_de_tentativas = 10
else:
   total_de_tentativas = 5

# Solicita ao usuário que informe um valor.
# Devemos armazenar esse valor em uma variável
chute = int(input("Digite o número entre 1 e 100:"))
print("Você digitou o número", chute)
print(type(chute))

if (chute < 1 or chute > 100):
    print("Você deve digitar um valor entre 1 e 100")

#agora precisamos verificar se o chute do usuário é igual ou diferente
#ao número secreto

if(chute == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")

#Por que não exibe "Você acertou"?
print(type(chute))
print(type(numero_secreto))

#Precisamos utilizar uma função que converte o chute para inteiro
numero = int(chute)
print(type(numero))

if(numero == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")

# vamos verificar se o número chutado é maior
# ou menor que o número secreto
if(numero == numero_secreto):
    print("Você acertou!")
else:
    if(numero > numero_secreto):
        print("O número", numero, "é maior que o número secreto")
    elif(numero < numero_secreto):
        print("O número", numero, "é menor que o número secreto")

#queremos que o usuário consiga tentar várias vezes
#total_de_tentativas = 3
rodada_atual = 1
pontos = 1000

#for rodada_atual in range(1, total_de_tentativas + 1):
while (rodada_atual <= total_de_tentativas):
    print("Tentativa ", rodada_atual, "de", total_de_tentativas)
    print("Tentativa {} de {} ".format(rodada_atual, total_de_tentativas))
    chute = int(input("Digite o seu número: "))

    if(chute < 1 or chute > 100):
        print("Você deve digitar um valor entre 1 e 100")
        continue

    if (chute == numero_secreto):
        print("Você acertou! E fez {} pontos!".format(pontos))
        print("Você acertou! E fez", pontos, "pontos!")
        print("Você acertou! E fez " + pontos + "pontos!")

        break
    else:
        if (chute > numero_secreto):
            print("O número", chute, "é maior que o número secreto")
        elif (chute < numero_secreto):
            print("O número", chute, "é menor que o número secreto")

    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

    rodada_atual += 1




