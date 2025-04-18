'''Faça um programa em Python que leia o nome e duas notas 
de n alunos e calcule a média. O usuário deverá 
digitar o número do aluno e o programa exibirá a média e o
resultado, sabendo que o critério para aprovação é 
média igual ou maior que 6.0.
'''

nomes = []
medias = []

x = int(input("Digite a quantidade de alunos: "))
for i in range(x):
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1+n2)/2
    medias.append(media)
    nomes.append(nome)

n = int(input("Digite o numero do aluno que deseja exibir: "))
if medias[n] >= 6.0:
    print(f"O aluno {nomes[n]} foi APROVADO com média {(medias[n])}")
else:
    print(f"O aluno {nomes[n]} foi REPROVADO com média {(medias[n])}")


