from datetime import datetime
class Reserva: 
    def __init__(self, usuario, livro):
        self.dataReserva = datetime.now()
        self.usuario = usuario
        self.livro = livro
        