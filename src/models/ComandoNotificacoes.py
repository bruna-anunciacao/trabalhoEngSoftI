from .Comando import Comando

class ComandoNotificacoes(Comando):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def executar(self, codigo_usuario):
        total = self.biblioteca.total_notificacoes(codigo_usuario)
        print( f"Total de notificações recebidas pelo usuário {codigo_usuario}: {total}")
        return