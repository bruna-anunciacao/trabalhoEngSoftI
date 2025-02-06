from .Usuario import Usuario

class AlunoGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.max_emprestimos = 2
        
    def periodo_emprestimo(self):
        return 4
    