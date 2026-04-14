# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"{self.nome} - R${self.preco}"

class CarrinhoDeCompras:
    def __init__ (self):
        self.lista_produtos =[]
    
    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)

    def calcular_total(self):
        soma = 0
        for produto in self.lista_produtos:
            soma += produto.preco
        return soma

#TESTE

p1 = Produto("Mouse", 50)
p2 = Produto("Teclado", 100)
p3 = Produto("Monitor", 500)

carrinho = CarrinhoDeCompras()

carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)

print(carrinho.calcular_total()) # total contido no carrinho

# for produto in carrinho.lista_produtos:
#    print(produto)
