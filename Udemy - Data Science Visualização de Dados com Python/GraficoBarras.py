# Install matplotlib
# PS C:\Dev\Projects\python> & C:/Users/andlopes/AppData/Local/Programs/Python/Python37-32/python.exe -m pip install matplotlib
import matplotlib.pyplot as plt

#Coordenadas X e Y
marcas = ["Ferrari", "BMW", "Fiat", "Toyota", "Honda", "Renault"]
quantidade = [120, 345, 500, 250, 450, 600]

#Legendas
titulo = "Vendas de automóveis - 2018"
eixoX = "Marcas"
eixoY = "Quantidade vendidas"

plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

#Desenha gráfico de barras
plt.bar(marcas, quantidade)

#Mostra gráfico
plt.show()

#Salva gráfico como imagem
plt.savefig("GraficoBarras.png")
