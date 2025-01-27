from datetime import datetime, timedelta
class Emprestimo: 
    def __init__(self, usuario, exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.dataEmprestimo = datetime.now()
        self.dataDevolucao = self.dataEmprestimo + timedelta(days=usuario.periodo_emprestimo())
        self.status = 'Emprestado'