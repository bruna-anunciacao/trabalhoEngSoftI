from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []
        self.reservas = []
    
    @abstractmethod
    def periodo_emprestimo(self):
        pass
    