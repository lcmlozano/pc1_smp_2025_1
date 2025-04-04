contador = 1
while contador <=10:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    print(f'A média é do aluno {contador} é {media}')
    contador = contador + 1
