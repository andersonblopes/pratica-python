# Define encoding
# -*- coding: utf-8 -*-

nome = "Anderson"
sobrenome = "Lopes"

#Concatenação de Strings
concatenar = nome + " " + sobrenome
print(concatenar)

#Tamanho da String
tamanho = len(concatenar)
print(tamanho)

#Obtendo caracter pelo indice
print(sobrenome[0])
print(sobrenome[1])
print(sobrenome[2])
print(sobrenome[3])
print(sobrenome[4])

#Obtendo parte da String
parte_da_string = concatenar[0:5]
print(parte_da_string)

parte_da_string = concatenar[5:8]
print(parte_da_string)

parte_da_string = concatenar[9:]
print(parte_da_string)