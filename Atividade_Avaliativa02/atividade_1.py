# Atividade 1
# Nomes: Alessandro da Silva Moreira, Gabriel Anselmo, Leon Antonio
# Turma: 2º Informática

"""
    1) O "Hacker" do Ônibus

        a) O erro cometido foi não tornar o atributo "saldo" como privado. O uso de atributo privado impediria esse problema,
        uma vez que o uso de atributos privados impede sua alteração por qualquer um.

        b) código abaixo.
"""

class CartaoTransporte:
    def __init__(self, id, saldo=0):
        self.id = id
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self.__saldo = valor
        else:
            print(f"Impossível adicionar valores negativos!")

meu_cartao = CartaoTransporte(505)
meu_cartao.saldo = 50
print(meu_cartao.saldo)
