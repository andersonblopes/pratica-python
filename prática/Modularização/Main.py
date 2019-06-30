import Aleatorio as a
import Media as m

lista = a.geraListaInteiros(10)
print("Minha lista: "+ str(lista))

#Calculando a média 
media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)



print("Média: "+ str(media))
print("Mediana: "+ str(mediana))
print("Moda: "+ str(moda))