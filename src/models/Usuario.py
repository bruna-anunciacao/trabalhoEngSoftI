from abc import ABC, abstractmethod
from datetime import datetime
class Usuario(ABC):
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []
        self.reservas = []

    @abstractmethod
    def periodo_emprestimo(self):
        pass
    
    def estrategia_emprestimo(self):
        pass

    def tem_livro_atrasado(self):
        for emprestimo in self.emprestimos:
            if emprestimo.status_emprestimo == 'Em curso' and emprestimo.data_devolucao < datetime.now():
                return True
        return False

    def tem_emprestimo_do_livro(self, livro):
        return any(emprestimo.exemplar.livro == livro for emprestimo in self.emprestimos)

    def possui_reserva_para_livro(self, livro):
        return any(reserva.livro == livro for reserva in self.reservas)
