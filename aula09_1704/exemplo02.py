'''
 Vamos criar um programa em Python que solicite ao usuário o 
 nomes de 5 pessoas e armazene em uma lista.
Em seguida o programa deve solicitar ao usuário um número 
de 0 a 4, correspondendo ao índice, e o programa deverá 
mostrar nome armazenado nesse índice
'''

nomes = []
for i in range(5):
    n = input("Digite um nome: ")
    nomes.append(n)

print(nomes)
n = int(input("Digite um número: "))
print(nomes[n])



