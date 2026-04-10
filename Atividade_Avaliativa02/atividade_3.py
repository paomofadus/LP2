class Participante:
    def __init__(self, nome, email, saldo):
        self.nome = nome
        self.email = email
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def adicionar_credito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print(f"Valor inválido!")
    
    def cobrar(self, valor_oficina):
        if self.saldo >= valor_oficina:
            self.__saldo -= valor_oficina
        else:
            print(f"Inscrição inválida!")

class Curso:
    def __init__(self, titulo, preco, vagas):
        self.titulo = titulo
        self.__preco = preco 
        self.__vagas = vagas
    
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            print("Número negativo inválido!")

    @property
    def vagas(self):
        return self.__vagas

    @vagas.setter
    def reservar_vaga(self):
        if self.__vagas > 0:
            self.__vagas -= 1
        else:
            print("Vagas esgotadas!")

class Inscricao:
    def __init__(self):
        pass

    def confirmar(participante, oficina):
        if participante.saldo >= oficina.preco and oficina.vagas > 0:
            oficina.reservar_vaga()
            participante.cobrar()

p1 = Participante("Davi", "davi@email.com", 10.0)
oficina_python = Curso("Python Básico", -50.0, 5)
