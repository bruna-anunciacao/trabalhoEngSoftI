import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from models.Biblioteca import Biblioteca

class ManipuladorConsole:
    def __init__(self):
        self.biblioteca = Biblioteca.get_instance()
        self.comandos = {
            'emp': self.emprestar_livro,
            'dev': self.devolver_livro,
            'res': self.reservar_livro,
            'liv': self.informacoes_livro,
            'usu': self.informacoes_usuario,
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
            resultado = self.comandos[acao](*partes[1:])
        else:
            print("Comando inválido.")

    def emprestar_livro(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.emprestar_livro(codigo_usuario, codigo_exemplar)

    def devolver_livro(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.devolver_livro(codigo_usuario, codigo_exemplar)

    def reservar_livro(self, codigo_usuario, codigo_exemplar):
        return self.biblioteca.reservar_livro(codigo_usuario, codigo_exemplar)
    def informacoes_livro(self, codigo_exemplar):
        return self.biblioteca.informacoes_livro(codigo_exemplar)
    def informacoes_usuario(self, codigo_usuario):
        return self.biblioteca.informacoes_usuario(codigo_usuario)