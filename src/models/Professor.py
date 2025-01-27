from src.models.Usuario import Usuario

class Professor(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.tempo_emprestimo = 8