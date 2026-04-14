# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class Carga:
    def __init__(self, descricao, peso_kg):
        self.descricao = descricao
        self.peso = peso_kg
    
    def __str__(self):
        return(f"Descricao: {self.descricao}, Peso: {self.peso}")

class Caminhao:
    def __init__(self, placa, capacidade_maxima_kg):
        self.placa = placa
        self.capacidade = capacidade_maxima_kg
        self.carga = []
    
    def carregar_item(self, carga_objeto):
        peso = 0
        for carga in self.carga:
            peso += carga.peso
        if (peso + carga_objeto.peso) < self.capacidade:
            self.carga.append(carga_objeto)
            print("Carga adicionada!")
        else:
            print("Carga nao adicionada.")

    def exibir_relatorio(self):
        print(f"Placa: {self.placa}")
        for carga in self.carga:
            print(carga)

#TESTE

c1 = Caminhao(89807, 1000)
carga_1 = Carga("Renault Sandeiro", 600)
carga_2 = Carga("Fiat Uno", 500)
c1.carregar_item(carga_1)
c1.carregar_item(carga_2) # o programa impede o carregamento dessa carga
c1.exibir_relatorio()
