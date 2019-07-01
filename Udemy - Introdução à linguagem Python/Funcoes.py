# Define encoding
# -*- coding: utf-8 -*-

def somar(x, y):
    return x + y

def produto(x, y):
    return x * y

#funcao str() para transformar variavel int em String e permitir a concatenação
print("2 + 2 = " + str(somar(2,2)))
print("3 X 3 = " + str(produto(3,3)))
print(somar(2,2) + produto(3,3))