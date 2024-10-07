import datetime

class Biblioteca:
    def __init__(self, titulo, autor, anopublicacao, numeropagina):
        self._titulo = titulo
        self._autor = autor
        self._anopublicacao = anopublicacao
        self._numeropagina = numeropagina

    def detalhe(self):
        print(f"O titulo do item é {self._titulo}, foi escrito pelo autor {self._autor} e a obra foi publicada no ano de {self._anopublicacao}")
    
    def calcidadelivro(self):
        ninjo = 2024
        idi = ninjo - self._anopublicacao
        
        if idi > 70:
            print(F"Esse item é antigo")
            print(f"O item que foi citado é {self._titulo}, a obra foi publicada no ano de {self._anopublicacao} e a sua idade é de {idi} anos")

        elif idi >30 and self._idi > 70:
            print(F"Esse item é recente")
            print(f"O item que foi citado é {self._titulo}, a obra foi publicada no ano de {self._anopublicacao} e a sua idade é de {idi} anos")
        
        elif idi < 30:
            print(F"Esse item é comtemporâneo")
            print(f"O item que foi citado é {self._titulo}, a obra foi publicada no ano de {self._anopublicacao} e a sua idade é de {idi} anos")

class Livro(Biblioteca):
    def verificartamanho(self):
        if self._numeropagina > 300:
            print(f"Esse livro {self._titulo} é grande pois possui {self._numeropagina} páginas")
        else:
            print(f"Esse livro {self._titulo} é pequeno pois possui {self._numeropagina} páginas")

class Revista(Biblioteca):
    def verificaredicao(self):
        if self._anopublicacao < 1998:
            print(f"A revista {self._titulo} não é uma edição especial, pois é do ano {self._anopublicacao}")
        else:
            print(f"A revista {self._titulo} é uma edição especial, pois é do ano {self._anopublicacao}")



        