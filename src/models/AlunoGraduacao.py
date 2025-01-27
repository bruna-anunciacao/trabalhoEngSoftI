from src.models.Usuario import Usuario

class AlunoGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.tempo_emprestimo = 4
        self.max_emprestimos = 2