# Prova Prática - Lab. Linguagem de Programação
# Nomes: Alessandro da Silva Moreira e Gabriel Anselmo da Silva Nascimento
# Turma: 2º Informática

class Livro:
    def __init__(self, titulo, autor, status=True):
        self.__titulo = titulo
        self.__status = status
        self.autor = autor
    
    # resumo do livro, serve como metodo __str__
    def situacao_atual(self):
        print(f"Título: {self.__titulo}\nAutor: {self.autor}\nStatus: {self.__status}\n")

    # metodo getter para o titulo
    @property
    def titulo(self):
        return self.__titulo
    
    # metodo getter para o status
    @property
    def status(self):
        return self.__status
    
    # metodo setter para o status
    @status.setter
    def status(self, valor):
        if isinstance(valor, bool):
            self.__status = valor
        else:
            print("Valor inválido!\n")

# classe para usuarios convencional
class Usuario:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato

# classe filha de Usuario, para amigos de Carina
class UsuarioAmigo(Usuario):
    def __init__(self, nome, contato):
        super().__init__(nome, contato)

# o emprestimo funciona através da classe Emprestimo
class Emprestimo:
    def __init__(self, usuario, data, livro):
        self.usuario = usuario
        self.data = data
        self.livro = livro

        # verifica se o status do livro está disponível
        if livro.status:
            livro.status = False
        else:
            print("Não é possível emprestar!\n")
    
    # altera o status do livro para disponível
    def devolver(self, livro):
        livro.status = True
        print(f"O livro {self.livro.titulo} foi devolvido!\n")
    
    # realiza a consulta caso o usuario solicitante seja um amigo de Carina
    def consulta(self, usuario):
        if isinstance(usuario, UsuarioAmigo):
            print(f"Título: {self.livro.titulo}\n")
        else:
            print(f"O usuário não é amigo!\n")

# livros instanciados
livro1 = Livro("Crime E Castigo", "Fiódor Dostoiéviski")
livro2 = Livro("Manifesto do Partido Comunista", "Karl Marx & Frederich Engels")

# usuarios amigos gostosos
amigo1 = UsuarioAmigo("Alessandro da Silva Moreira", 998151893)
amigo2 = UsuarioAmigo("Gabriel Anselmo da Silva Nascimento", 997180417)

# usuario convencional para teste
usuario = Usuario("Emmanuel Veiga", 67676767)

# emprestimos realizados
emprestimo1 = Emprestimo(amigo1, "14/12/2007", livro1)
emprestimo2 = Emprestimo(amigo2, "22/08/2008", livro2)
emprestimo1.consulta(amigo1)
emprestimo2.consulta(amigo2)

emprestimo2.consulta(usuario)

# verifica a situacao atual, mostrando a indisponibilidade do livro
livro1.situacao_atual()
livro2.situacao_atual()

# emprestimo avisa que deu errado
emprestimo_errado = Emprestimo(amigo1, "15/12/2007", livro2)
