# Estamos acessando o arquivo " pessoa" e dentro desse arquivo estamos importando a classe pessoa

from pessoa import Pessoa

# Criando objeto

p1 = Pessoa("joana","corre","Rua dos Alfinetes 2121")
p1.exibirHobby()
p1.mudarHobby("Natação")

# Solicitando dados do usuário
nomePessoa = input("Informe o nome da pessoa: ")
hobbyPessoa = input("Informe o hobby da pessoa: ")
endPessoa = input("Qual o endereço da pessoa?  ")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby()