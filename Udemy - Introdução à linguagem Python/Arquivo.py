# Define encoding
# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")
print(arquivo)

#Imprime conteúdo completo
linhas = arquivo.readlines()
print(linhas)

#Imprime linha a linha do arquivo
for linha in linhas:
    print(linha)

#Ler novamente o arquivo
arquivo = open("arquivo.txt")
#Ler texto completo do arquivo
texto_completo = arquivo.read()
print(texto_completo)

#Fecha o arquivo
arquivo.close()


#CRIAR ARQUIVO w - subscreve texto existente
novo_arquivo = open("arquivo2.txt","w")

#Escreve no arquivo
novo_arquivo.write("Este eh o meu arquivo criado.")

novo_arquivo.close()

#CRIAR ARQUIVO a - adiciona texto no fim do arquivo
novo_arquivo3 = open("arquivo3.txt","a")

#Escreve no arquivo
novo_arquivo3.write("Este eh o meu arquivo 3 criado.\n")

novo_arquivo3.close()
