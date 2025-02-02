import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from models.Biblioteca import Biblioteca
from models.ComandoEmprestar import ComandoEmprestar
from models.ComandoDevolver import ComandoDevolver
from models.ComandoReservar import ComandoReservar
from models.ComandoInformacoesLivro import ComandoInformacoesLivro
from models.ComandoInformacoesUsuario import ComandoInformacoesUsuario
from models.ComandoObservar import ComandoObservar
from models.ComandoNotificacoes import ComandoNotificacoes

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