from datetime import datetime
class Reserva: 
    def __init__(self, usuario, livro):
        self.data_reserva = datetime.now()
        self.usuario = usuario
        self.livro = livro
        