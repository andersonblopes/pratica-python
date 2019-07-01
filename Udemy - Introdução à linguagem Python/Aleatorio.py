import random

#Gera número aleatório com base no intervalo informado
numero = random.randint(0,1000)
print(numero)

#Só gera somente uma vez o número aleatório
#random.seed(1)
outro_numero = random.randint(0,1000)
print(outro_numero)

#Estabele valores considerados na geração aleatória
lista_valores_aleatorios = [19,20,50]
numero_aleatorio_controlado = random.choice(lista_valores_aleatorios)
print(numero_aleatorio_controlado)

