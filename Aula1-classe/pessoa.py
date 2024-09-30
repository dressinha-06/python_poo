class pessoa:
    #atributos
    nome = "Fulia"
    peso = 45
    escolaridade = "Ensino Médio"

    #métodos
    def falar(self, texto):
        print(F"Tem algo para te dizer: {texto}")

#Criando os objetos
pessoa1 = pessoa()
print(pessoa1.nome)
pessoa1.falar("Boa tarde, hoje é segunda-feira")