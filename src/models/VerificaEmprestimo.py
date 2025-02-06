from abc import ABC, abstractmethod

class VerificaEmprestimo(ABC):
    @abstractmethod
    def verificar_condicoes(self, usuario, livro):
        pass
