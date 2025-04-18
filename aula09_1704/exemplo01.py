'''
 Faça um programa em Python que calcule a média de um 
 aluno a partir de cinco notas previamente armazenadas em 
 uma lista.
Utilize: notas = [6, 7, 6.5, 4.8, 8]
'''

notas = [6, 7, 6.5, 4.8, 8]
soma = 0

'''
for i in range(5):
    soma = soma + notas[i]
'''
for i in notas:
    soma += i

media = soma / 5
print(f"Média: {round(media,2)}")
