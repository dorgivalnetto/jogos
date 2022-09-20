#Declaração implícita
got = ("GameofThrones", 2011, 2019, 9.4)
print(got)
#('Game of Thrones', 2011, 2019, 9.4)
print(type(got))
#<class'tuple'>

#Declaração explícita
got2 = tuple(["Game of Thrones", 2011, 2019, 9.4])
print(got2)
#('GameofThrones',2011,2019,9.4)
print(type(got2))
#<class'tuple'>

#empresas = ("Google","Facebook","Amazon")
#empresas[1] ="Samsung"
#TypeError:'tuple' object does not support item assignment

letras = ("A","B","C","D","E","F","G","H")
print(letras[0])
#Selecionando o último elemento de uma tupla:
letras = ("A","B","C","D","E","F","G","H")
print(letras[-1])



#Imprimindo todos os elementos de uma tupla (um elemento por linha)
cinema = ("Sony Pictures", "Walt Disney", "Universal Pictures", "Warner")
for estudio in cinema:
    print(estudio)

#Criando uma tupla de forma iterativa.
n =int(input("Quantos números serão lidos?"))
tupla = ()
for i in range(n):
    x = int(input("Entre com um número:"))
    tupla = tupla + tuple([x])
print(tupla)
