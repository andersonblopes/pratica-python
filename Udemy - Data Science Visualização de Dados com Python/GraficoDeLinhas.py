# Install matplotlib
# PS C:\Dev\Projects\python> & C:/Users/andlopes/AppData/Local/Programs/Python/Python37-32/python.exe -m pip install matplotlib
import matplotlib.pyplot as plt

#Coordenadas X e Y
x = [1, 2]
y = [2, 3]
plt.plot(x, y)

plt.show()

#Salva gráfico como imagem
plt.savefig("GraficoDeLinhas.png")
