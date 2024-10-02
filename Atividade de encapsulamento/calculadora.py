class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2 

    def construtor(self):
        print(f"valor 1 {self.__num1} e o valor 1 é {self.__num2}" )
    
    def somar(self):
        print(f"O valor {self.__num1} somado ao valor {self.__num2} é igual a {self.__num1+self.__num2}")
    
    def subtrair(self):
        print(f"O valor {self.__num1} subtraido pelo o valor {self.__num2} é igual a {self.__num1-self.__num2}")
    
    def multiplicar(self):
        print(f"O valor {self.__num1} multiplicado o valor {self.__num2} é igual a {self.__num1*self.__num2}")
    
    def dividir(self):
        print(f"O valor {self.__num1} dividido pelo valor {self.__num2} é igual a {self.__num1/self.__num2 :.2f}")
    
    def potencia(self):
        print(f"O potencia de {self.__num1} ** {self.__num2} é igual a {self.__num1**self.__num2 :.2f}")
    
    def verificaParImpar(self, valor):
        if valor  % 2 == 0:
            print(f"O valor escolhido é par")
        else:
            print(f"O valor escolhido é impar")
