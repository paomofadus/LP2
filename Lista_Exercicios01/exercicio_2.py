# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class SensorIrrigacao:
    def __init__(self, setor, status_bomba=False):
        self.setor = setor
        self.status_bomba = status_bomba

    def __str__(self):
        return f"Setor: {self.setor}\nStatus: {self.status_bomba}"

    # muda o estado da bomba para ligado
    def ligar_bomba(self):
        self.status_bomba = True
        print("A bomba está ligada.\n")

    # mesma função anterior, só que pra desligar
    def desligar_bomba(self):
        self.status_bomba = False
        print("A bomba está desligada.\n")
    
    # a bomba liga ou desliga, dependendo da umidade
    def verificar_solo(self, umidade):
        if umidade < 30:
            self.status_bomba = True
            print("A umidade está muito baixa! A bomba foi ligada.\n")
        elif umidade > 70:
            self.status_bomba = False
            print("A umidade está muito alta! A bomba foi desligada.\n")

sensor1 = SensorIrrigacao("Soja")
sensor1.ligar_bomba()
sensor1.desligar_bomba()
sensor1.verificar_solo(20)
print(sensor1)