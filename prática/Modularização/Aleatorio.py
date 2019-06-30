import random

def geraListaInteiros(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(random.randint(0, tamanho))
    return lista
