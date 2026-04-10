# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class Pedido:
    def __init__(self, numero_pedido, item_escolhido, preco_unidade, quantidade):
        self.numero_pedido = numero_pedido
        self.item_escolhido = item_escolhido
        self.preco_unidade = preco_unidade
        self.quantidade = quantidade
    
    # retorna o valor total e imprime
    def calcular_total(self):
        print(f"R$ {self.preco_unidade * self.quantidade}\n")
        return self.preco_unidade * self.quantidade
    
    # aplica o desconto no atributo do objeto através do percentual
    def aplicar_desconto(self, porcentagem):
        self.preco_unidade -= self.preco_unidade * (porcentagem/100)
        print(f"Preço: R$ {self.preco_unidade}\n")

    # comprovante com todos os dados do objeto
    def exibir_comprovante(self):
        print(f"RESUMO\nNúmero do pedido: {self.numero_pedido}\nItem: {self.item_escolhido}\nPreço: {self.preco_unidade}\nQuantidade: {self.quantidade}\n")

cappucino = Pedido(155, "Cappucino", 5, 2)
cappucino.calcular_total()
cappucino.aplicar_desconto(50)
cappucino.exibir_comprovante()

gourmet = Pedido(155, "Gourmet", 7, 3)
gourmet.calcular_total()
gourmet.aplicar_desconto(50)
gourmet.exibir_comprovante()