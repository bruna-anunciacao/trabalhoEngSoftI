from abc import ABC, abstractmethod
from .ProfessorObservador import ProfessorObservador

class Comando(ABC):
    @abstractmethod
    def executar(self, *args):
        pass

class ComandoEmprestar(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.emprestar_livro(codigo_usuario, codigo_exemplar)

class ComandoDevolver(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.devolver_livro(codigo_usuario, codigo_exemplar)

class ComandoReservar(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.reservar_livro(codigo_usuario, codigo_exemplar)

class ComandoInformacoesLivro(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_exemplar):
        return self.biblioteca.informacoes_livro(codigo_exemplar)

class ComandoInformacoesUsuario(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario):
        return self.biblioteca.informacoes_usuario(codigo_usuario)

class ComandoObservar(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario, codigo_livro):
        usuario = self.biblioteca.encontrar_usuario(codigo_usuario)
        livro = self.biblioteca.encontrar_livro(codigo_livro)

        if usuario and livro:
            observador = ProfessorObservador(usuario)
            livro.adicionar_observador(observador)
            print(f"Professor {usuario.nome} registrado como observador do livro {livro.titulo}.")
            return
        print ("Usuário ou livro não encontrado.")
        
class ComandoNotificacoes(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario):
        total = self.biblioteca.total_notificacoes(codigo_usuario)
        print( f"Total de notificações recebidas pelo usuário {codigo_usuario}: {total}")
        return