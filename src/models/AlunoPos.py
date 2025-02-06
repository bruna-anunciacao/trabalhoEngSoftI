from .Usuario import Usuario

class AlunoPos(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.max_emprestimos = 3
        
    def periodo_emprestimo(self):
        return 5