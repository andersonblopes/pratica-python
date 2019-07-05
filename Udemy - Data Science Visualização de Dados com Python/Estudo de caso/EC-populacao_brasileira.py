#População Brasileira: 1980 a 2016
#Dados extraídos do DATASUS - populacao-brasileira.csv

#Importando biblioteca de gráficos
import matplotlib.pyplot as plt

#Lendo o arquivo
dados = open("populacao-brasileira.csv").readlines()

#Eixo X
anos = []
#Eixo Y
populacao = []

#Coletando os dados para os eixos do gráfico
for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        anos.append(int(linha[0]))
        populacao.append(int(linha[1]))

#Desenhando gráfico
plt.plot(anos, populacao, color="#A0522D", linestyle="--")
plt.bar(anos,populacao, color="#DEB887")

plt.title("Crescimento da População Brasileira: 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("Populacao x100.000.000")

#Salvando grafico como imagem
plt.savefig("EC-populacao_brasileira.png", dpi=300)

#Mostra gráfico
plt.show()
