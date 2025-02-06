from .Comando import Comando

class ComandoInformacoesLivro(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_exemplar):
        return self.biblioteca.informacoes_livro(codigo_exemplar)