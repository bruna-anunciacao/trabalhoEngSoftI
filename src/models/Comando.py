from abc import ABC, abstractmethod
from .ProfessorObservador import ProfessorObservador

class Comando(ABC):
    @abstractmethod
    def executar(self, *args):
        pass