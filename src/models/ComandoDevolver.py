from .Comando import Comando

class ComandoDevolver(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.devolver_livro(codigo_usuario, codigo_exemplar)