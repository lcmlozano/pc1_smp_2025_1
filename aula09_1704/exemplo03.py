'''Faça um programa em Python que calcule e mostre a 
média de uma quantidade indeterminada de números inteiros 
digitados pelo usuário. Para sair o usuário deverá
digitar 0. Use lista e exiba no final os números digitados.
'''
num = []
soma = 0

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 0:
        break
    num.append(n)
    soma += n
    #soma = soma + n

media = soma / len(num)
print(f"Media: {round(media,2)}")
print(num)
