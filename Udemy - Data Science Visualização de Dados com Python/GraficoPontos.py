# Install matplotlib
# PS C:\Dev\Projects\python> & C:/Users/andlopes/AppData/Local/Programs/Python/Python37-32/python.exe -m pip install matplotlib
import matplotlib.pyplot as plt

#Coordenadas X e Y
horas = [6, 8, 10, 12, 14, 16, 18]
temperatura = [14, 16, 17, 19, 23, 22, 21]

#Título do gráfico de pontos
plt.title("Temperatura em Lisboa") #Scatterplot

#Legendas dos eixos
plt.xlabel("Horas")
plt.ylabel("Temperatura")

#Desenha gráfico
plt.scatter(horas, temperatura, label = "Variação", color="r", marker="*", s=200)
plt.plot(horas, temperatura, color="g", linestyle=":")
plt.legend()

#Salva gráfico como imagem
plt.savefig("graficoPontos.png")

#Mostra gráfico
plt.show()