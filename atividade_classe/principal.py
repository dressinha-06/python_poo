from livro import Livro

# Criando objeto

l1 = Livro("Amores passados", "vida", 2006)
l1.exibirinformacoes()


# Solicitando dados do usuário
tituloLivro = input("Informe o titulo do livro: ")
autorLivro = input("Informe o nome do autor(a): ")
anoPublicacaoLivro = input("Em qual ano o livro foi publicado?  ")

l2 = Livro(tituloLivro, autorLivro, anoPublicacaoLivro)
l2.exibirinformacoes()