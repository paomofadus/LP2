# Nomes: Alessandro da Silva Moreira e Dante Venga Dias
# Turma: 2º Informática

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
            return(f"Nome: {self.nome}   Matricula: {self.matricula}")

class Turma:
    def __init__(self, nome_turma, capacidade_maxima, alunos_matriculados):
        self.alunos_matriculados = []
        self.alunos_matriculados = alunos_matriculados
        self.nome_turma = nome_turma
        self.capacidade_maxima = capacidade_maxima
    
    def matricular_aluno(self, aluno):
        if len(self.alunos_matriculados) < self.capacidade_maxima:
            self.alunos_matriculados.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos_matriculados:
             print(aluno)

#TESTE

t1 = Turma("Turma 301", 1, [])

a1 = Aluno("Joaquim", 34203)
a2 = Aluno("Cleber", 12309)
a3 = Aluno("Joao", 98778)
a4 = Aluno("Emanuel", 23490)
a5 = Aluno("Carlos", 90291)

t1.matricular_aluno(a1) # único aluno a ser matriculado na turma
t1.matricular_aluno(a2)
t1.matricular_aluno(a3)
t1.matricular_aluno(a4)
t1.matricular_aluno(a5)

t1.listar_alunos() # aparece somente o aluno Joaquim
