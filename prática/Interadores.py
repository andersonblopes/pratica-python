# Define encoding
# -*- coding: utf-8 -*-


# Laço while
x = 0;

print("==================================")
print("Laço WHILE")
print("==================================")
while x < 10:
    print(x)
    x += 4

#Laço for

lista = [0,1,2,3,4,5]
lista2 = ["Olá", "Python", "!"]
lista3 = [0, "Lista", 3.5, True]
print("==================================")
print("Laço FOR")
print("==================================")
print("Laço FOR")
print("---------- Lista 1 ----------")
for i in lista:
    print(i)

print("---------- Lista 2 ----------")
for i in lista2:
    print(i)

print("- Lista com tipos diferentes -")
for i in lista3:
    print(i)


print("==================================")
print("Interador RANGE")
print("==================================")

#Delimitando fim
print("- Delimitando fim -")
for i in range(5):
    print(i)

#Delimitando intervalo
print("- Delimitando intervalo -")
for i in range(20,25):
    print(i)

#Delimitando incremento
print("- Delimitando incremento -")
for i in range(20, 30, 5):
    print(i)