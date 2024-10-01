from conta import Conta

minhaConta = Conta(289, "Dona Lurdes", 2009, )

minhaConta.relatorio()

minhaConta.setLimite(8000)
minhaConta.relatorio()

minhaConta.depositar(200)
minhaConta.relatorio()

minhaConta.sacar(150)
minhaConta.relatorio()