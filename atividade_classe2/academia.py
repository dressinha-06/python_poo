class Aluno:
    # Método costrutor
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    # Criando Métodos
    def exibirinfor(self):
        print(f"Olá {self.nome}, você tem {self.idade}, seu peso é {self.peso} e sua altura é {self.altura} ")

    def calcularimc(self):
        imc = self.peso/(self.altura*self.altura)
        print(f"O seu indice de massa corporal é {imc:.2f} ")

