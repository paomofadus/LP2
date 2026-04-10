# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class Heroi:
    def __init__(self, nome, vida=100, nivel=1):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel

    def __str__(self):
        return f"Nome: {self.nome}\nVida: {self.vida}\nNível: {self.nivel}\n"

    # decresce a vida com base no dano
    def tomar_dano(self, quantidade):
        self.vida -= quantidade
        print(f"Vida atual: {self.vida} HP")
        # se o dano zerar a vida, exibe a derrota
        if self.vida <= 0:
            print(f"O personagem {self.nome} foi derrotado.\n")
    
    # aumenta o nivel do heroi com base em pontos
    def ganhar_experiencia(self, pontos):
        self.nivel += pontos
        print(f"Nível atual: {self.nivel}\n")
    
    # volta a vida para o estado inicial
    def curar(self):
        self.vida = 100
        print(f"O personagem foi totalmente curado. Vida: {self.vida}\n")

sonic = Heroi("Sonic")
sonic.tomar_dano(20)
sonic.ganhar_experiencia(5)
sonic.curar()
print(sonic)

mario = Heroi("Mario")
mario.tomar_dano(150)
mario.curar()
mario.ganhar_experiencia(10)
print(mario)