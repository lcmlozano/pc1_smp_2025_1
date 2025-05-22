def calcularIMC(argPeso, argAltura):
    imc = argPeso / (argAltura **2)
    print(f"O imc é : {imc}")
    return imc

def classificarIMC(argImc):
    if argImc < 18.5:
        print("Abaixo do peso ideal")
    elif argImc < 25:
        print("Peso ideal")
    else:
        print("Acima do peso")

def entradaDados():
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    ret = calcularIMC(peso, altura)
    classificarIMC(ret)
 
entradaDados()