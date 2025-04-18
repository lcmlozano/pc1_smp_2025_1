'''
Vamos criar um programa em Python que solicite ao usuário o nome de 
5 pessoas, armazene em uma lista e exiba os nomes digitados e o 
tamanho da lista. 
Em seguida o programa deve solicitar ao usuário um nome, 
e o programa deverá remover o nome armazenado na lista, 
exibir os nomes digitados e o tamanho da lista.
'''
nomes = []

for i in range(5):
    n = input("Digite um nome: ")
    nomes.append(n)

print(nomes)
print(len(nomes))

nome = input("Digite um nome para remover da lista: ")

if nome in nomes:
    nomes.remove(nome)
    print(nomes)
    print(len(nomes))
else:
    print("Nome nao encontrado!")


