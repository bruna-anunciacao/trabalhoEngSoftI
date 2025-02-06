from .Usuario import Usuario
from .VerificaEmprestimoAluno import VerificaEmprestimoAluno

class AlunoGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.max_emprestimos = 2
        
    def periodo_emprestimo(self):
        return 4
    
    def estrategia_emprestimo(self):
        return VerificaEmprestimoAluno()
    