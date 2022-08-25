import random

# definimos uma função chamada jogar()
# : definem o início de um bloco da função
def jogar():
    print("Bem-vindo ao Jogo da Forca")

    palavras = ['Monitor', 'Teclado', 'Mouse', 'Impressora', 'Notebook', 'Scanner']
    palavra_secreta = palavras[random.randrange(1, len(palavras))].lower()

    enforcou = False
    acertou = False

    tentativas = 1

    #definindo a lista de letras acertadas de acordo com o tamanho da palavra
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append('_')
    print(letras_acertadas)

    #definindo o game loop
    while(not enforcou and not acertou):
        chute = input("Digite uma letra")

        # string.lower = todas as letras da palavra serão minúsculas
        chute = chute.lower()

        #remove espaços a esquerda e a direita da palavra, caso haja
        chute = chute.strip()

        print("Tentativa: ", tentativas, "de ", len(palavra_secreta))

        if(chute in palavra_secreta):

            posicao = 0

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[posicao] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, posicao))
                    if letras_acertadas.count("_") == 0:
                        print("Você venceu! A palavra secreta é {}".format(palavra_secreta))
                        acertou = True
                posicao += 1
        else:
            if(tentativas >= len(palavra_secreta)):
                enforcou = True
                print("Você acertou apenas as letras ", letras_acertadas)
                print("Enforcou! A palavra secreta é {}".format(palavra_secreta))

        print("Tentativas restantes", len(palavra_secreta)-tentativas)
        print(letras_acertadas)
        tentativas += 1




if(__name__ == "__main__"):
    jogar()