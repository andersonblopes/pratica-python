# 3 - Escreva um programa que resolva uma equação de segundo grau.  

from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta) / (2*a)
x2 = (-b - raiz_delta) / (2*a)

print("O valor de X1: %.2f"%(x1))
print("O valor de X2: %.2f"%(x2))