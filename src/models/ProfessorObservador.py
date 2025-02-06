from .Observador import Observador

class ProfessorObservador(Observador):
    def __init__(self, professor):
        self.professor = professor
        self.contador_notificacoes = 0
        self.notificacoes = []

    def update(self, livro, nomes_usuarios):
        self.contador_notificacoes += 1
        nomes_formatados = ', '.join(nomes_usuarios)  # Junta os nomes com vírgula
        mensagem = (f"Notificação {self.contador_notificacoes}: O livro '{livro.titulo}' tem mais de 2 reservas. Reservado por: {nomes_formatados}.")
        self.notificacoes.append(mensagem)

    def contar_notificacoes(self, codigo_usuario):
        if self.professor.codigo == codigo_usuario:
            return self.contador_notificacoes, self.notificacoes
        return 0, []
