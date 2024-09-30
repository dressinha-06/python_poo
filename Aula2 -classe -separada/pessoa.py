class Pessoa:
    # Método costrutor
    def __init__(self, nome, hobby, endereco):
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco

    # Criando Métodos
    def exibirHobby(self):
        print(f"Olá, meu hobby é {self.hobby}")

    def mudarHobby(self, novoHobby):
        self.hobby = novoHobby
        print(f"meu hobby mudou para {novoHobby}")

