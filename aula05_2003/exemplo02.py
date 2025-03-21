qtdDiarias = int(input('Digite a quantidade de diárias: '))
tipo = input('Digite o tipo de hospedagem: (S, D ou T)')

if tipo == 's' or tipo == 'S':
    print(f"Valor a pagar R$ {(qtdDiarias * 255.50)}")
elif tipo == 'd' or tipo == 'D':
    print(f"Valor a pagar R$ {(qtdDiarias * 305.50)}")
elif tipo == 't' or tipo == 'T':
    print(f"Valor a pagar R$ {(qtdDiarias * 360.50)}")
else:
    print('Tipo de diária inválido')