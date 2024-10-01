from academia import Aluno

# Criando objeto

A1 = Aluno("Gabriel", 18, 47.5, 1.78)
A1.exibirinfor()
A1.calcularimc()

# Solicitando dados do usuário
nomeP = input("Informe o seu nome: ")
idadeP = input("Informe sua idade: ")
pesoP = float(input("Infome o seu peso:  "))
alturaP = float(input("Informe a sua altura:  "))

A2 = Aluno(nomeP, idadeP, pesoP, alturaP)
A2.exibirinfor()
A2.calcularimc()