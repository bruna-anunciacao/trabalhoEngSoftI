from .Comando import Comando
from .ProfessorObservador import ProfessorObservador

class ComandoObservar(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_livro):
        return self.biblioteca.registrar_observador(codigo_usuario, codigo_livro)