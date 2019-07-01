# 5 - Escreva um programa que receba dois números e um sinal, 
# e faça a operação matemática definida pelo sinal.   

resultado = 0
try:
    n1 = int(input("Digite o primeiro número: "))
    operacao = input("Digite o operador: ")
    n2 = int(input("Digite o segundo número: "))
    if operacao == "+":
        resultado = n1 + n2
    elif operacao == "-":
        resultado = n1-n2
    elif operacao == "*":
        resultado = n1*n2
    elif operacao == "/":
        resultado = n1/n2
    elif operacao == "%":
        resultado = n1%n2
    elif operacao == "**":
        resultado = n1 ** n2
    print(resultado)
except:
    print("Uma falha ocorreu na execução do sistema!")
