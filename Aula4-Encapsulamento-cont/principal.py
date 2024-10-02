from funcionario import Funcionario

funt1 = Funcionario("Karlita", 3000)
print("Seu nome é ", funt1.getNome())

funt1.setNome("Kayron")

print("Seu nome é ", funt1.getNome())

print("Seu salário atual é: ", funt1.salario)

funt1.salario = -5000

print("Seu salário atual é: ", funt1.salario)