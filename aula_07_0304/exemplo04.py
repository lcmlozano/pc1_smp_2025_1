'''
Faça um algoritmo que calcula e mostra a média de uma quantidade 
indeterminada de números inteiros digitados pelo usuário. 
Use a estrutura de repetição enquanto.
'''
resp = "s"
soma = 0.0
qtde = 0

while resp == "s" or resp == "S":
    num = float(input('Digite um número: '))
    soma = soma + num
    qtde = qtde + 1
    resp = input('Deseja continuar (S/N)?')

media = soma / qtde
print(f"A média dos número é {media}")