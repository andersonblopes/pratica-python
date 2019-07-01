#Media, mediana, moda
from statistics import *

def media(lista):
    #utilizando lib statistics
    #return mean(lista)
    media = sum(lista) / float(len(lista)) 
    return media 

def mediana(lista):
    #utilizando lib statistics
    #return median(lista)
    lista_ordenada = sorted(lista)
    tamanho = len(lista)
    if tamanho % 2 == 0:
        mediana = (lista_ordenada[int(tamanho / 2)] + lista_ordenada[int((tamanho / 2) - 1)]) / 2
    elif tamanho % 2 == 1:
        mediana = lista_ordenada[int(tamanho / 2)]
    return mediana

def moda(lista):
    #utilizando lib statistics
    #return mode(lista)


    lista_dicionario = {}
    #Conta ocorrências repetidas na lista
    for l in lista:
        if l not in lista_dicionario:
            lista_dicionario[l] = 1
        else:
            lista_dicionario[l] += 1

    #Obtem valor que mais se repetiu
    maior_repeticao = max(lista_dicionario.values()) 

    #Recupera na lista este valor
    for i in lista_dicionario:
        if lista_dicionario[i] == maior_repeticao:
            moda = i
            break
    return moda
