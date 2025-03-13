'''
Crie um programa em Python que solicite ao usuário três valores inteiros
(A,B,C) e verifica se o valor armazenado em B é o menor;
'''
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if b < a and b < c:
    print("O menor valor é B")