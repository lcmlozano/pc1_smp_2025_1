'''Faça um programa que conta o número de palavras de um texto: " '''

texto = input("Digite um texto: ")
pontuacao = [".", ",",":",";","!","?"]

# remover os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p," ")

# split devolver lista com palavras como itens
lista = texto.split()
numero_palavras = len(lista)
print("Número de palavras: ", numero_palavras)
print(lista)