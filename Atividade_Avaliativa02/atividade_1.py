# Atividade 1
# Nomes: Alessandro da Silva Moreira, Gabriel Anselmo e Leon Antonio
# Turma: 2º Informática

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
