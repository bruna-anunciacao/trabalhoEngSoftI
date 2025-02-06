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
        self.observadores = [] 
    
    def adicionar_exemplar(self, codigo_exemplar):
        self.exemplares.append(Exemplar(codigo_exemplar, 'Disponível', None, self))
    
    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)
        if len(self.reservas) > 2:
            nomes_usuarios = [reserva.usuario.nome for reserva in self.reservas]
            self.notificar_observadores(nomes_usuarios)
                    
    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, nomes_usuarios):
        for observador in self.observadores:
            observador.update(self, nomes_usuarios)