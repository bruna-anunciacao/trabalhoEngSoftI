from .Usuario import Usuario

class Professor(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        
    def periodo_emprestimo(self):
        return 8