# Install matplotlib
# PS C:\Dev\Projects\python> & C:/Users/andlopes/AppData/Local/Programs/Python/Python37-32/python.exe -m pip install matplotlib
import matplotlib.pyplot as plt

#Coordenadas X e Y
horas = [6, 8, 10, 12, 14, 16, 18]
temperatura = [14, 16, 17, 19, 23, 22, 21]

#Título
plt.title("Temperatura em Lisboa")

#Legendas dos eixos
plt.xlabel("Horas")
plt.ylabel("Temperatura")

#Desenha gráfico
plt.plot(horas, temperatura)

#Mostra gráfico
plt.show()
