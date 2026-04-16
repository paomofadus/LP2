# Atividade Avaliativa 03
# Nomes: Alessandro da Silva Moreira
# Turma: 2º Informática

from atividade_avaliativa_02 import *

conta = Conta(150, "Leon", 1000)
conta.depositar(200)
conta.sacar(10000)
conta.sacar(200)

conta_corrente = ContaCorrente(150, "Alex", 1000, 300)
conta_corrente.depositar(200)
conta_corrente.sacar(1400)

conta_poupanca = ContaPoupanca(150, "Gabriel Anselmo", 1000)
conta_poupanca.aplicar_rendimento()

conta_poupex = ContaPoupex(150, "Otavio Augusto", 1000)
conta_poupex.aplicar_rendimento()
