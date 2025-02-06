from .Comando import Comando

class ComandoEmprestar(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.emprestar_livro(codigo_usuario, codigo_exemplar)