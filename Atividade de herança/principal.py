from biblioteca import Biblioteca, Livro, Revista

l1 = Biblioteca("Moby Dick", "Herman Melville", 1851, 490)
l1.detalhe()
l1.calcidadelivro()
print("="*30)

lipiru = Livro("O Alquimista", "Paulo Coelho", 1988, 202)
lipiru.verificartamanho()
lipiru.detalhe()
print("="*30)

revis = Revista("Revista Galileu", "Nicogo", 2002, 47)
revis.verificaredicao()
revis.detalhe()