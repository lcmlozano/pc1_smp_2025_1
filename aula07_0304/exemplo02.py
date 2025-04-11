'''
 Faça um algoritmo que solicite ao usuário 10 números reais, 
 calcule e mostre a soma dos números digitados. 
 Use a estrutura de repetição for
'''
soma = 0.0

for i in range(10):
    num = float(input(f"Digite o numero {i+1} =  "))
    soma = soma + num

print(f'O resultado da soma é: {soma}')