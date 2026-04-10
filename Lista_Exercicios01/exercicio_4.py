# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class Estacionamento():
    def __init__(self, placa, modelo, hora_entrada, hora_saida=None, total_pagamento=0):
        self.placa = placa
        self.modelo = modelo
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.total_pagamento = total_pagamento

    # o parâmetro da função vai para o atributo do objeto e calcula o pagamento
    def registrar_saida(self, hora_saida):
        self.hora_saida = hora_saida
        self.total_pagamento = (self.hora_saida - self.hora_entrada) * 5
        print(f"Total a pagar: R$ {self.total_pagamento}\n")
    
    # funciona como uma função __str__
    def resumo(self):
        print(f"Placa: {self.placa}\nPagamento: R$ {self.total_pagamento}\n")

via_garden = Estacionamento("HGJ4-F", "Fiat", 15)
via_garden.registrar_saida(20)
via_garden.resumo()

shopping_estacionamento = Estacionamento("FASJ-K", "Honda", 3)
shopping_estacionamento.resumo()
shopping_estacionamento.registrar_saida(10)