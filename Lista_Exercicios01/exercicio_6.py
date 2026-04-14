class Termostato:
    def __init__(self, temperatura_atual):
        self.temperatura_atual = temperatura_atual
        self.temperatura_alvo = temperatura_atual  # começa igual

    def ajustar_alvo(self, nova_temp):
        self.temperatura_alvo = nova_temp
        print(f"Temperatura alvo ajustada para {nova_temp}°C")

    def aquecer(self):
        print("Aquecendo...")
        while self.temperatura_atual < self.temperatura_alvo:
            self.temperatura_atual += 3
            print(f"Temperatura atual: {self.temperatura_atual}°C")

        print("Temperatura alvo atingida!")

    def resfriar(self):
        print("Resfriando...")
        while self.temperatura_atual > self.temperatura_alvo:
            self.temperatura_atual -= 3
            print(f"Temperatura atual: {self.temperatura_atual}°C")

        print("Temperatura alvo atingida!")


# Criando o objeto
termostato = Termostato(20)

# Ajustando alvo
termostato.ajustar_alvo(35)

# Decidindo o que fazer
if termostato.temperatura_atual < termostato.temperatura_alvo:
    termostato.aquecer()
else:
    termostato.resfriar()