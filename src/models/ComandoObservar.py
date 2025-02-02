from .Comando import Comando
from .ProfessorObservador import ProfessorObservador

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