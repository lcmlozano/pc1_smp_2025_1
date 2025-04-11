'''
Crie um programa que leia uma string e imprima a inversa dela
'''
inversa = ""

string = input("Digite um texto: ")

for x in string:
    inversa = x + inversa

print(inversa)