from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def update(self, livro):
        pass

    @abstractmethod
    def contar_notificacoes(self, codigo_usuario):
        pass
