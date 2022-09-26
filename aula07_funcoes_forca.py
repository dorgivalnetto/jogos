import random

def jogar():

    imprime_abertura()

    carrega_palavra_secreta()

    palavra_secreta = carrega_palavra_secreta()

    letras_certas = inicializa_letras_certas(palavra_secreta)

    acertou = False
    enforcou = False
    tentativas = 1

    while(not enforcou and not acertou):
        chute = solicita_chute()

        if chute in palavra_secreta:
                verifica_chute_coreto(palavra_secreta, chute, letras_certas)
        else:
            if (tentativas >= len(palavra_secreta)):
                enforcou = True
                print("Você acertou apenas as letras ", letras_certas)
                print("Enforcou! A palavra secreta é {}".format(palavra_secreta))

        print("Tentativas restantes", len(palavra_secreta) - tentativas)
        print(letras_certas)
        tentativas += 1


def imprime_abertura():
    print("***************************")

    print("*** Bem-vindo ao Jogo ***")

    print("***************************")


def carrega_palavra_secreta():
    palavras = ['Monitor', 'Teclado', 'Mouse',
                'Impressora', 'Notebook', 'Scanner']

    # print(random.randrange(1, len(palavras)))
    # print(palavras[random.randrange(1, len(palavras))])
    palavra_secreta = palavras[random.randrange(0, len(palavras))].lower()
    print(palavra_secreta)

    return palavra_secreta

def inicializa_letras_certas(palavra_secreta):
    letras_certas = []
    for letra in palavra_secreta:
        print(letra)
        letras_certas.append('_')
    print(letras_certas)
    return letras_certas

def solicita_chute():
    chute = input("Digite uma letra")
    chute = chute.lower()
    chute = chute.strip()
    return chute

def verifica_chute_coreto(palavra_secreta, chute, letras_certas):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_certas[posicao] = letra
            print("Encontrei a letra {} na posição {}".format(chute, posicao))
            if letras_certas.count("_") == 0:
                print("Acertou A palavra secreta é {}".format(palavra_secreta))
                acertou = True
        posicao += 1
# início da execução do programa
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    jogar() # chamada da função principal do programa

# O uso do “if __name__ == ‘__main__’” para a chamada da função main
# permite que esse arquivo contendo uma ou várias funções seja
# incluído em outros programas (usando “import” e suas variações)
# sem a necessidade de reescrever ou copiar o código.


