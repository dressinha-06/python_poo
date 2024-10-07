class Funcionario:
    def __init__(self, nome, salario):
        # Estamos mudando a visivilidade dos atributos de privado para protegido, 
        # dessa forma as classes filhas poderão acessar os atributos da classe mãe
        self._nome = nome
        self._salario = salario
    
    def informacoes(self):
        print(f"Olá {self._nome}, seu salário atual é {self._salario:.2f}")

# Criando filhas
class Engenheiro(Funcionario): # A classe Engenheiro está herdando as caracteristicas da classe Funcionario, que será sua classe mãe
    def bonusEngenheiro(self):
        self._salario = self._salario*1.1  # Estamos aumentando o salário em 10%

class Supervisor(Funcionario):
    def relatorio(self):
        print(f"Olá {self._nome}, peço que passe no RH as 16h!")
