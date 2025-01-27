from trabalhoEngSoftI.src.models.VerificaEmprestimo import VerificaEmprestimoAlunoGraduacao, VerificaEmprestimoAlunoPosGraduacao, VerificaEmprestimoProfessor

class Usuario:
    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        
class AlunoGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.tempo_emprestimo = 4
        self.limite_emprestimos = 2
        self.estrategia = VerificaEmprestimoAlunoGraduacao()

class AlunoPosGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.tempo_emprestimo = 5
        self.limite_emprestimos = 3
        self.estrategia = VerificaEmprestimoAlunoPosGraduacao()

class Professor(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.tempo_emprestimo = 8
        self.estrategia = VerificaEmprestimoProfessor()