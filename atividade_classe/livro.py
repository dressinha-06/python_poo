class Livro:

    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    def exibirinformacoes(self):
        print(f"O titulo do livro é {self.titulo}, escrito pelo autor {self.autor} e foi publicado do ano {self.anoPublicacao}")

    

l1 = Livro("Amores passados", "vida", "2006")
l1.exibirinformacoes()