import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from models.Biblioteca import Biblioteca
from models.Comando import ComandoEmprestar
from models.Comando import ComandoDevolver
from models.Comando import ComandoReservar
from models.Comando import ComandoInformacoesLivro
from models.Comando import ComandoInformacoesUsuario
from models.Comando import ComandoObservar
from models.Comando import ComandoNotificacoes

class ManipuladorConsole:
    def __init__(self):
        self.biblioteca = Biblioteca.get_instance()
        self.comandos = {
            'emp': ComandoEmprestar(self.biblioteca),
            'dev': ComandoDevolver(self.biblioteca),
            'res': ComandoReservar(self.biblioteca),
            'liv': ComandoInformacoesLivro(self.biblioteca),
            'usu': ComandoInformacoesUsuario(self.biblioteca),
            'obs': ComandoObservar(self.biblioteca),
            'ntf': ComandoNotificacoes(self.biblioteca)
        }

    def iniciar(self):
        print("Sistema de Biblioteca iniciado. Digite um comando ou 'sai' para sair.")
        while True:
            comando = input("Comando: ")
            self.executar_comando(comando)

    def executar_comando(self, comando):
        partes = comando.split()
        acao = partes[0]
        if acao == 'sai':
            print("Saindo do sistema...")
            exit()
        elif acao in self.comandos:
            resultado = self.comandos[acao].executar(*partes[1:])
        else:
            print("Comando inválido.")

    # def emprestar_livro(self, codigo_usuario, codigo_exemplar):
    #     return self.biblioteca.emprestar_livro(codigo_usuario, codigo_exemplar)

    # def devolver_livro(self, codigo_usuario, codigo_exemplar):
    #     return self.biblioteca.devolver_livro(codigo_usuario, codigo_exemplar)

    # def reservar_livro(self, codigo_usuario, codigo_exemplar):
    #     return self.biblioteca.reservar_livro(codigo_usuario, codigo_exemplar)
    # def informacoes_livro(self, codigo_exemplar):
    #     return self.biblioteca.informacoes_livro(codigo_exemplar)
    # def informacoes_usuario(self, codigo_usuario):
    #     return self.biblioteca.informacoes_usuario(codigo_usuario)
    # def registrar_observador(self, codigo_usuario, codigo_livro):
    #     usuario = self.biblioteca.encontrar_usuario(codigo_usuario)
    #     livro = self.biblioteca.encontrar_livro(codigo_livro)

    #     if usuario and livro:
    #         observador = ProfessorObservador(usuario)
    #         livro.adicionar_observador(observador)
    #         return f"Professor {usuario.nome} registrado como observador do livro {livro.titulo}."
    #     return "Usuário ou livro não encontrado."