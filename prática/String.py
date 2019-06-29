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

#Métodos do Objeto String

print(concatenar.lower())
print(concatenar.upper())
print(concatenar.capitalize())

concatenar = nome + " " + sobrenome + "\n "
print(concatenar)
print(concatenar.strip()) #Remove caracter especial: por ex:  '\n'

#Transforma string em lista
frase = "O rato roeu a roupa do rei de Roma"
lista = frase.split("r")
print(lista)

#Busca em uma String
busca = frase.find("rei")
print(busca)
print(frase[busca:])

#Substituindo partes da String
frase = frase.replace("o rei","a rainha")
print(frase)