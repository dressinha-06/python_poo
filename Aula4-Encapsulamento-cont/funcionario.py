class Funcionario:
    def __init__(self, nome, salario = 1000):
        self.__nome = nome
        self.__salario = salario

    def getNome(self):
        return self.__nome
    
    def setNome(self, valor):
        self.__nome = valor

    #Iremos ultilizar um recurso único do  python para acessar atributos privados

    #Criando um get  personalizado

    @property #Esse item irar criar um get "mais amigavel"
    def salario(self):
        return self.__salario
    
    @salario.setter #Irar criar um set para o atributo de forma "mais amigavel"
    def salario(self, valor):
        if valor > 0:
            self.__salario = valor 
        else:
            print("Você não pode ter um sálario negativo")