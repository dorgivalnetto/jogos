import random


def jogar():
    print("Jogo de Adivinhação")

    nome = "Dorgival "
    sobrenome = "Netto"
    print("Olá ", nome, sobrenome, sep="_")
    print("Olá Sr. {1} {0}".format(nome, sobrenome))

    numero_secreto = round(random.random() * 100)
    print(numero_secreto)
    # numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Digite o nível de dificuldade"))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    while (rodada <= total_tentativas):
        print("Tentativa ", rodada, "de", total_tentativas)
        print("Tentativa {} de {} ".format(rodada, total_tentativas))
        chute = int(input("Digite o seu número: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um valor entre 1 e 100")
            continue

        print("Você digitou: ", chute)

        acertou = numero_secreto == chute
        print(type(acertou))
        maior = chute > numero_secreto
        print(type(maior))

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto!")
            else:
                print("Você errou! O seu chute foi menor que o número secreto!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        rodada += 1


if(__name__ == "__main__"):
    jogar()