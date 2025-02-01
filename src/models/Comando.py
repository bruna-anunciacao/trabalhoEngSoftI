from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self, *args):
        pass

class ComandoEmprestar(Comando):
    def init(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.emprestar_livro(codigo_usuario, codigo_exemplar)

class ComandoDevolver(Comando):
    def init(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.devolver_livro(codigo_usuario, codigo_exemplar)

class ComandoReservar(Comando):
    def init(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.reservar_livro(codigo_usuario, codigo_exemplar)

class ComandoInformacoesLivro(Comando):
    def init(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_exemplar):
        return self.biblioteca.informacoes_livro(codigo_exemplar)

class ComandoInformacoesUsuario(Comando):
    def init(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario):
        return self.biblioteca.informacoes_usuario(codigo_usuario)
    