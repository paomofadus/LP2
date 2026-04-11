# Atividade 3
# Nomes: Alessandro da Silva Moreira, Gabriel Anselmo, Leon Antonio
# Turma: 2º Informática

"""
    3 - Refatorando

        a) Alteração do número total de vagas, dos emails dos estudantes e o preço das oficinas

        b) Curso. Pois o número de vagas pode ser alterado dentro da própria classe somente.

        c) Vagas e preço da classe Curso, saldo da classe Participante. Ambos os setters seriam validados se fossem
        maior do que 0.
"""

"""
    4 - Codificar

        código abaixo:
"""

class Participante:
    def __init__(self, nome, email, saldo):
        self.nome = nome
        self.email = email
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
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
        if self.__preco < 0:
            print(f"Erro. O preço da oficina não pode ser negativo!")
            self.__preco = 0
    
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

    def reservar_vaga(self):
        if self.__vagas > 0:
            self.__vagas -= 1
        else:
            print("Vagas esgotadas!")

class Inscricao:
    def __init__(self):
        pass

    def confirmar(self, participante, oficina):
        if participante.saldo >= oficina.preco and oficina.vagas > 0:
            oficina.reservar_vaga()
            participante.cobrar(oficina.preco)
            print(f"\nO participante {participante.nome} foi inscrito.")
            print(f"Saldo do participante: {participante.saldo}")
            print(f"Vagas da oficina {oficina.titulo}: {oficina.vagas}")
        else:
            print(f"\nNão é possível inscrever o participante {participante.nome} em {oficina.titulo}")

# participantes
gabriel_anselmo = Participante("Gabriel Anselmo", "gabrielanselmo@email.com", 50.0)
leon = Participante("Leon", "leontpb@gmail.com", 50)

# cursos
oficina_python = Curso("Python Básico", 30.0, 5)
oficina_cpp = Curso("C++ Básico", 30.0, 1)

# classe complementar
inscricao = Inscricao()
inscricao.confirmar(gabriel_anselmo, oficina_python)

inscricao.confirmar(leon, oficina_cpp)
inscricao.confirmar(gabriel_anselmo, oficina_cpp) # o código avisa que não foi possível escrever

# gabriel_anselmo.__saldo = 10000 - python ignorou
