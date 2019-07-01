# 4 - Escreva um programa que ordene uma lista numérica com três elementos.  
# Implementando algoritmo select sort

lista = [8,12,-34,45,-987,9087,6,5]

print(lista)

for i in range(len(lista)):
    menor = i
    for j in range(i+1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
print(lista)