# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class Musica:
    def __init__(self, duracao_segundos, artista, titulo):
        self.duracao_segundos = duracao_segundos
        self.artista = artista
        self.titulo = titulo

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracao_segundos}s)"

class Playlist:
    def __init__(self, nome_playlist, musicas):
        self.nome_playlist = nome_playlist
        self.musicas = musicas

    def adicionar_musica(self, musica_objeto):
        self.musicas.append(musica_objeto)

    def exibir_tempo_total(self):
        soma = 0
        for musica in self.musicas:
            soma += musica.duracao_segundos

        minutos = soma / 60
        print(f"Tempo total: {minutos:.2f} minutos")

# TESTE

p1 = Playlist("Street", [])

m1 = Musica(120, "Kendrick", "Monarca")
m2 = Musica(140, "West", "Flashing lights")
m3 = Musica(134, "Eminem", "Mockingbird")

p1.adicionar_musica(m1)
p1.adicionar_musica(m2)
p1.adicionar_musica(m3)

p1.exibir_tempo_total() # tempo aproximado de 6.57 minutos
