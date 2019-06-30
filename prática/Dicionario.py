#Dicionários em python
familia_lopes = {"Anderson" : "13/12/1981", "Elaine" : "10/05/1988", "Pitoco" : "13/05/2009"} 
print(familia_lopes)

#Imprimir valor obtido através da chave
print(familia_lopes["Pitoco"])

#Interando o dicionário - mostrando o valor da chave
for chave in familia_lopes:
    print(chave)

#Interando o dicionário - mostrando o valor atribuido à chave
for chave in familia_lopes:
    print(familia_lopes[chave])
