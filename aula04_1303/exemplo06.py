'''
Crie um programa em Python que solicite duas notas de um aluno ao 
usuário, calcule a média e mostre se o mesmo está aprovado 
(média >=6.0) ou reprovado caso contrário.
'''
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2)/2
if media >= 6.0:
    print(f"Aprovado!!! Sua média é {media}")
else:
    print(f"Reprovado!!! Sua média é {media}")
    