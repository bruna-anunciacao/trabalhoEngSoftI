from src.models.Usuario import Usuario

class AlunoPos(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.tempo_emprestimo = 5
        self.max_emprestimos = 3