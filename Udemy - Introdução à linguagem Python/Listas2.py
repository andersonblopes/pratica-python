lista = [1,4,5,789,65,34,9,76]
lista_strings = ["Elaine", "Helena", "Anderson"]
print(lista)
print(lista_strings)

#Ordenar a mesma lista
lista.sort()
print(lista)

#Ordena de forma reversa
print(lista_strings)
lista_strings.sort(reverse = True)
print(lista_strings)

#Função sorted exige nova lista para armazenar retorno
lista2 = sorted(lista)
print(lista2)

#Reverte lista sem ordenar
lista2 = [1,4,5,789,65,34,9,76]
print(lista2)
lista2.reverse()
print(lista2)
print(lista_strings)
