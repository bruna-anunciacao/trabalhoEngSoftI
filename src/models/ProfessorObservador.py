from .Observador import Observador

class ProfessorObservador(Observador):
    def __init__(self, professor):
        self.professor = professor
        self.contador_notificacoes = 0

    def update(self, livro, nomes_usuarios):
        self.contador_notificacoes += 1
        print(f"Notificação {self.contador_notificacoes}: O livro {livro.titulo} tem mais de 2 reservas.")
