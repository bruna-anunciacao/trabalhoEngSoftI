from .Exemplar import Exemplar
class Livro:
    def __init__(self, codigo, titulo, editora, autor, edicao, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.edicao = edicao
        self.ano = ano
        self.exemplares = []
        self.reservas = []
    
    def adicionar_exemplar(self, codigo_exemplar):
        self.exemplares.append(Exemplar(codigo_exemplar, 'Disponível', None, self))
    
    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)
        self.notificar_observadores()
        
    def notificar_observadores(self):
        for observador in self.observadores:
            observador.atualizar(self)