from calculadora import Calculadora

ope = input("Qual a operação?")
n1Calculadora = int(input("Digite o valor 1: "))
n2Calculadora = int(input("Digite o valor 2: "))
valorCalculadora = int(input("Diga um valor: "))

v1 = Calculadora(n1Calculadora, n2Calculadora)
if ope == "soma":
    v1.somar()
if ope == "subtração":
    v1.subtrair()
if ope == "multiplicação":
    v1.multiplicar()
if ope == "divisão":
    v1.dividir()
if ope == "potencia":
    v1.potencia()
    
v1.verificaParImpar(valorCalculadora)