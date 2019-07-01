#**
# 2 - Faça um programa que receba duas notas digitadas pelo usuário. 
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.    
#*
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media > 7:
    print("Aluno aprovado com média: %.2f" %(media))
else:
    print("Aluno reprovado com média: %.2f" %(media))