#criando um dicionário
eng2sp = dict()
print(eng2sp)

#adicionando itens ao dicionário
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

print("Buscando pela chave", eng2sp['two'])
#print("Buscando pelo valor", eng2sp['tres'])

print("Buscando com get()", eng2sp.get('two'))

print("Tamanho do dicionário:", len(eng2sp))

print("Verificando chave com in",'one' in eng2sp)
print("Verificando valor com in",'uno' in eng2sp)

vals = eng2sp.values()
print("Verificando valor com values()",'uno' in vals)

eng2sp['four'] = 'cuatro'
print("Adicionando valor", eng2sp)


numeracao = eng2sp.pop('four')
print(numeracao)
print(eng2sp)
#criamos o dicionário
agenda = {}



agenda = {"Maria": 99887766, "Pedro": 92345678,"Joaquim": 99887711}
print(agenda)



print("Buscando um telefone: ", agenda["Maria"])

print("Buscando um telefone com get: ", agenda.get("Joaquim"))



agenda["Pedro"] = 56789098
print("Alterando o telefone de Pedro:",agenda)



agenda["Teresa"] = 65443322
print("Acrescentando o telefone de Teresa:",agenda)

print(eng2sp.popitem())




