#Listas
#frutas = []

frutas = ['Banana','Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']
print(type(frutas))
print(frutas[0])
#print(frutas[6])

fruta_pedida = input('Qual é a fruta que deseja consultar ?')
print(fruta_pedida)
print(fruta_pedida.lower())
print(fruta_pedida.strip())

if (fruta_pedida in frutas):
   print('Sim, temos a fruta.')
else:
   print ('Não temos a fruta.')

# string.lower = todas as letras da palavra serão minúsculas
print(fruta_pedida.lower())

# string.upper = todas as letras da palavra serão maiúsculas
print(fruta_pedida.upper())

# string.strip = remove espaços a esquerda e a direita da palavra, caso haja
print(fruta_pedida.strip())

precos = [1525, 1120, 1464, 1200, 1330, 1356, 1312, 1531, 1232, 1234, 1250, 1114, 1553, 1147, 1303, 1296, 1309,
          1404, 1479, 1376, 1152, 1440, 1038, 1018, 1291, 1388, 1577, 1115, 1488, 1494, 1254, 1230, 1122, 1396,
          1208, 1356, 1549, 1116, 1443, 1075, 1536, 1542, 1036, 1015, 1020, 1217, 1484, 1032, 1390, 1026]
print(min(precos))
print(max(precos))

funcionarios = ['Astrid', 'Flavia', 'Talia', ...,
                'Mauricio', 'Waldemar', 'Marina']

#exibe o tamanho da lista
print(len(funcionarios))


valores = [0, 0, 0, 1, 2, 3, 4]
#conta o número de ocorrências de um determinado elemento em uma lista
print(valores.count(0))


#retorna o índice de um elemento da lista
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))


frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

# adicionar um valor no final da lista
frutas.append('Melancia')
print(frutas)

# adicionar um valor em uma posição específica
frutas.insert(2, 'Acerola')
print(frutas)

#busca o elemento pelo conteúdo
print(frutas.index('Melancia'))

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'
          .format( fruta_buscada))

#remove o elemento cujo valor foi passado por parâmetro
frutas.remove('Melancia')
print(frutas)

#remove o último elemento da lista
frutas.pop()
print(frutas)

#ordenar os valores em uma lista
numeros = [9, 6, 1, 3, 4 , 2, 8]
#ordem crescente
numeros.sort()
print(numeros)

#ordem decrescente
numeros.sort(reverse=True)
print(numeros)

# índices negativos
print(frutas)
print("Índices negativos")
print(frutas[-2])

#referência vs cópia
lista_1 = ["oi", 2, 3.14, True]
print("Lista 1: ", lista_1)
lista_2 = lista_1
print("Lista 1: ", lista_2)
lista_2[2] = 5
print("Lista 1: ", lista_1)

#fatiamento de listas
primos = [2, 3, 5, 7, 11]
print(primos[1:2])
#[3]
print(primos[2:4])
#[5, 7]
print(primos[:3]) # observe que o início não precisa ser definido
#[2, 3, 5]
print(primos[3:]) # observe que o fim não precisa definido
#[7, 11]
print(primos[:])
#[2, 3, 5, 7, 11]

#repetição
lista_a = [4, 2, 8, 6, 5]
print(lista_a)
lista_b = lista_a * 2
print(lista_b)
lista_b[3] = 999
print(lista_a)
print(lista_a)

#tuplas
meses = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")
print(meses)
print(meses[8])
len(meses)

#listas e tuplas juntas
ponto1 = (3,5)
ponto2 = (4,6)
ponto3 = (7,8)
grafico = [ponto1, ponto2, ponto3]
print(grafico)

#acessando uma parte da informação da tupla dentro da lista
print(grafico[0])
print(grafico[2][1])

#set
colecao = {11122233344, 22233344455, 33344455566}
colecao.add(44455566677) #vai adicionar pois não existe ainda
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!