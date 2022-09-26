#Exemplo Crie um programa que retorna uma lista com todos os números pares
# entre 2 e um número n, inclusive

n = int(input('Digite um numero: '))
lista = []
#limite inferior = 2, limite superior n+1, 2 a 2
for i in range(2,n+1,2):
    lista = lista + [i]
    print(lista)

# inicializa vetor de notas com 0
notas = [0] * 3
soma = 0
# preenche vetor de notas, sem usar append
for i in range(3):
    notas[i] = float(input("Digite a nota do aluno " + str(i) + ": "))
    soma = soma + notas[i]
    print("A media da turma é", soma/3)

# Exemplo Programa que lê uma lista do teclado, soma 1 aos elementos da
# lista e imprime a lista resultante
continua = True
lista = []
while(continua):
    n= int(input('Digite um numero: '))
    lista.append(n)
    op= input('Deseja continuar? (s/n): ')
    if op!= 's' and op!= 'S':
        continua = False
print(lista)
for i in range(len(lista)):
    lista[i] = lista[i] + 1
print(lista)

#Encontrar o elemento de valor 10 na lista [1, 2, 10, 5, 20] e retornar a posição
# em que ele foi encontrado
lista = [1, 2, 10, 5, 20]
valor = 10
pos = -1
for i in range(len(lista)-1,-1,-1):
    if lista[i] == valor:
        pos = i
print(pos)

lista = [1, 2, 10, 5, 20]
pos = lista.index(10)
print(pos)


#Faça um programa que percorre uma lista com o seguinte formato:
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]],
# ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que
# cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália,
# o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:
# (a) o total de faltas do campeonato (b) o time que fez mais faltas
# (c) o time que fez menos faltas

#4. Faça um programa que percorre duas listas e intercala os elementos de ambas,
# formando uma terceira lista.  A terceira lista deve começar pelo primeiro
# elemento da lista menor.
# Exemplo:  lista1 = [1, 2, 3, 4]
# lista2 = [10, 20, 30, 40, 50, 60]
# lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]


idades = [33, 27, 18, 83]

print("Lista idades", idades)

print(type(idades))

print("Tamanho da lista idades", len(idades))

print("Elemento na posição 0", idades[0])

idades.append(91)
print("Adicionando 91 no final da lista", idades)

idades.insert(0, 20)
print("Adicionando na posição 0 o elemento 20", idades)

#O que acontece?
idades.append([18, 23])
print(idades)

#estende uma lista adicionando elementos
idades.extend([18, 23])
print(idades)

idades.remove(18)
print(idades)

#remove todos os elementos de uma lista
idades.clear()
print(idades)

idades = [33, 27, 18, 83]
print(idades)

print(28 in idades)

if 27 in idades:
    idades.remove(27)
print(idades)

idades_prox_ano = []
for idade in idades:
    idades_prox_ano.append(idade+1)
print(idades_prox_ano)

idade_prox_ano = [(idade + 1) for idade in idades]
print(idade_prox_ano)

