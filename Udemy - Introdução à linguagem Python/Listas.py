#Lista de um só tipo
minha_lista = ["Ana", "Helena", "Elaine"]
minha_lista2 = [1,2,3,4,5,6,7,8,9]

#Lista de tipos diferentes
minha_lista3 = ["Anderson", True, 2.35, 12]

#Imprime conteúdo da lista
print(minha_lista)
print(minha_lista2)
print(minha_lista3)

#Imprime valor de índice específico
print(minha_lista[2])

#Imprime por item
for item in minha_lista3:
    print(item)

#Recupera tamanho da lista
tamanho = len(minha_lista3)
print(tamanho)

#Adiciona item na lista
minha_lista.append("Anderson")
print(minha_lista)

#Verificando se item está na lista
nome = "Anderson"
if nome in minha_lista:
    print(nome + " está na lista!")

#Remove item da lista
print(minha_lista)
del minha_lista[len(minha_lista) - 1]
print(minha_lista)

#Remove demais ítens a partir de índice
del minha_lista[1:]
print(minha_lista)

#Limpar lista
del minha_lista[:]
print(minha_lista)