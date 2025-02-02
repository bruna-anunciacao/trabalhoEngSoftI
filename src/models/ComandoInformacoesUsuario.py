from .Comando import Comando

class ComandoInformacoesUsuario(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario):
        return self.biblioteca.informacoes_usuario(codigo_usuario)