# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class CarroEletrico:
    def __init__(self, modelo, km, bateria=100):
        self.modelo = modelo
        self.bateria = bateria
        self.km = km
    
    def __str__(self):
        # só para o print ficar bonito
        return f"Modelo: {self.modelo}\nQuilometragem: {self.km}\nBateria: {self.bateria}%"

    def dirigir(self, distancia):
        # verifica se a bateria esta zerada
        if self.bateria <= 0:
            print(f"A bateria está esgotada. Nível atual: {self.bateria}%\n")
        else:
            # decresce a bateria
            self.bateria -= distancia // 10
            print(f"Nível de bateria: {self.bateria}%\n")
            # caso a bateria fique com numero negativo, ela zera
            if self.bateria < 0:
                self.bateria = 0
    
    def carregar(self):
        # volta a bateria pro estado inicial
        self.bateria = 100
        print(f"Bateria totalmente carregada. Nível: {self.bateria}%\n")

carro1 = CarroEletrico("BYD", 500)
carro1.dirigir(100)
carro1.carregar()
print(carro1)
