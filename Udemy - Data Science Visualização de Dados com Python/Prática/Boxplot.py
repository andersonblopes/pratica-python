import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    aleatorio = random.randint(0,20)
    vetor.append(aleatorio)

plt.boxplot(vetor)
plt.title("Meu Boxplot")
plt.show()