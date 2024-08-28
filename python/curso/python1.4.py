nomes = ['Maria', 'Helena', 'Julia']
nome1, nome2, nome3 = nomes

print(nome1)

#####################################

lista = ['Maria', 'Helena', 'Julia']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)