from typing import List, Optional

from trabalhoEngSoftI.src.models.Livro import Livro
from trabalhoEngSoftI.src.models.Usuario import Usuario

class Repositorio:
    _instancia: Optional['Repositorio'] = None
    
    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.livros: List[Livro] = []
    
    @classmethod
    def obter_instancia(cls) -> 'Repositorio':
        if not cls._instancia:
            cls._instancia = Repositorio()
        return cls._instancia
    
    def obter_usuario_por_codigo(self, codigo: str) -> Optional[Usuario]:
        return None
    
    def obter_livro_por_codigo(self, codigo: str) -> Optional[Livro]:
        return None