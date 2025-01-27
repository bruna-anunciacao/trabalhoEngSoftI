from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
    
    