media = float(input('Digite a média do aluno: '))
frequencia = float(input('Digite o percentual de frequência do aluno: '))

if frequencia < 75:
    print('Reprovado por falta')
else:
    if media < 6:
        print('Reprovado por nota')
    else:
        print('Aprovado')
        

