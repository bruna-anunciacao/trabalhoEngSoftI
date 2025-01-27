from datetime import datetime, timedelta
class Emprestimo: 
    def __init__(self, usuario, exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + timedelta(days=usuario.periodo_emprestimo())
        self.status = 'Emprestado'