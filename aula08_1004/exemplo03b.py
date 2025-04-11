'''
 Faça um programa que solicite ao usuário o valor de um produto e 
 exiba o valor acrescido de 5%. A saída deverá exibir o valor no formato: 
 R$ xx.xx
'''
valor = float(input("Digite o valor de um produto : R$ "))
#valor = valor + ((valor * 5) / 100)
valor = valor * 1.05
print('O valor com acrescimo será: R$ %.2f'%valor)
