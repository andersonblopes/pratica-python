# Install matplotlib
# PS C:\Dev\Projects\python> & C:/Users/andlopes/AppData/Local/Programs/Python/Python37-32/python.exe -m pip install matplotlib
import matplotlib.pyplot as plt

#Coordenadas X e Y
marcas = ["Ferrari", "BMW", "Fiat", "Toyota", "Honda", "Renault"]
matriz = [120, 345, 500, 250, 450, 600]
filial = [90, 200, 50, 89, 350, 120]

#Legendas
titulo = "Vendas de automóveis - 2018"
eixoX = "Marcas"
eixoY = "Quantidade vendidas"

plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

#Desenha gráfico de barras
plt.bar(marcas, matriz, label = "Matriz")
plt.bar(marcas, filial, label = "Filial")
plt.legend()

#Mostra gráfico
plt.show()
