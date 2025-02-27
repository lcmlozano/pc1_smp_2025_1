#entrada
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
disciplina = input("Digite a disciplina: ")
#processamento
media = (nota1 + nota2) / 2
#saída
print(f"Aluno: {nome}")
print(f"Disciplina: {disciplina}")
print(f"Nota1: {nota1}")
print(f"Nota2: {nota2}")
print(f"Média: {media}")