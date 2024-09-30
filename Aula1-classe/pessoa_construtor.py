class pessoa:
    # Criar o método construtor
    def __init__(self, nome, altura, idade):
        #estamos criando os atributos da classe ultilizando o método construtor. Nesse caso presisamos passar os 
        # parâmetros que serão usados como valores dos atributos
        self.nome = nome
        self.altura = altura
        self.idade = idade

    #criando os métodos
    def exibirDados(seft):
        print(f"Olá {seft.nome}, sua sua altura é {seft.altura} e sua idade é {seft.idade}")

# Criando os objetos
p1 = pessoa("Getúlio",1.87, 99)
p2 = pessoa("Dilma",1.69, 60)

p1.exibirDados()
p2.exibirDados()