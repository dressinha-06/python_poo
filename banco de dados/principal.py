from funcionario_poo import Funcionario

f1 = Funcionario()
nome = input("Informe o nome do funcionário: ")
salario = float(input("Infome o salário do funcionário: "))
cargo = input("informe o cargo do funcionário: ")

f1.inserir(nome, salario, cargo)

f1.consulta()