
from funcionario import Funcionario, Engenheiro,Supervisor

f1 = Funcionario("Jorginho", 3000)
engenheiro1 = Engenheiro("Koala", 3000)


f1.informacoes()

supervisor1 = Supervisor("Carlinhos",4770)
supervisor1.relatorio()
engenheiro1.bonusEngenheiro()
engenheiro1.informacoes()