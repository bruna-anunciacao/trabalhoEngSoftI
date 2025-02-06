from .Usuario import Usuario
from .VerificaEmprestimoProfessor import VerificaEmprestimoProfessor

class Professor(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        
    def periodo_emprestimo(self):
        return 8
    
    def estrategia_emprestimo(self):
        return VerificaEmprestimoProfessor()