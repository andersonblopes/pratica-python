# 1 - Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.  
idade = int(input("Digite sua idade:"))

if idade < 0:
    print("Idade inválida!")
elif idade  > 18:
    print("Você é de maior!")
else:
    print("Você é de menor!")