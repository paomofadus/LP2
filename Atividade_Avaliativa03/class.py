# Atividade Avaliativa 3
# Nomes: Alessandro da Silva Moreira e Leon Antonio
# Turma: 2º Informática

class Conta:
    def __init__(self, num, titular, saldo):
        self.num = num
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depositado efetuado. Saldo atual: R$ {self._saldo:.2f}")
        else:
            print("Valor inválido para o depósito.")

    def sacar(self, valor):
        if valor > 0:
            if valor < self._saldo:
                self._saldo -= valor
                print(f"Saque efetuado. Saldo atual: R$ {self._saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar esse saldo.")
        else:
            print("Valor inválido para o saque.")

class ContaCorrente(Conta):
    def __init__(self, num, titular, saldo, limite):
        super().__init__(num, titular, saldo)
        self.__limite = limite
    
    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if valor > 0:
            if valor < self._saldo:
                self._saldo -= valor
                print(f"Saque efetuado. Saldo atual: R$ {self._saldo:.2f}")
            elif valor < self._saldo + self.__limite:
                valor -= self._saldo
                self.__limite -= valor
                self._saldo = 0
                print(f"Saque efetuado. Saldo atual: R$ 00.00. Limite atual: {self.__limite:.2f}.")
            else:
                print(f"Não há saldo e nem limite suficientes!")
        else:
            print("Valor inválido para o saque.")

class ContaPoupanca(Conta):
    def __init__(self, num, titular, saldo):
        super().__init__(num, titular, saldo)
        self.rendimento_mensal = 0.006
    
    def aplicar_rendimento(self):
        self._saldo += self._saldo * self.rendimento_mensal
        print(f"Saldo atual: {self._saldo:.2f}")

class ContaPoupex(ContaPoupanca):
    def __init__(self, num, titular, saldo):
        super().__init__(num, titular, saldo)
        self.rendimento_extra = 0.01
    
    def aplicar_rendimento(self):
        self._saldo += self._saldo * self.rendimento_mensal
        self._saldo += self._saldo * self.rendimento_extra
        print(f"Saldo atual: {self._saldo:.2f}")
