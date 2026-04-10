# Atividade 1
# Nomes: Alessandro da Silva Moreira, Gabriel Anselmo e Leon Antonio
# Turma: 2º Informática

class PatineteEletrico:
    def __init__(self, id, velocidade=0):
        self.id = id
        self.__velocidade = velocidade
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def definir_velocidade(self, nova_velocidade):
        if 0 < nova_velocidade < 20:
            self.__velocidade = nova_velocidade
        elif nova_velocidade > 20:
            self.__velocidade = 20
        else:
            print(f"Valor inválido!")

patinete = PatineteEletrico(5)
patinete.definir_velocidade = 15
print(patinete.velocidade)