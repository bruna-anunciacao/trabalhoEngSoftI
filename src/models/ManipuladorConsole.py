import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from models.Reserva import Reserva
from models.Biblioteca import Biblioteca
from models.Emprestimo import Emprestimo

class ManipuladorConsole:
    def __init__(self):
        self.biblioteca = Biblioteca.get_instance()
        
    def executar_comando(self, comando):
        partes = comando.split(" ")
        acao = partes[0]
        match (acao):
            case "emp":
                self.emprestar_livro(partes[1], partes[2])
            case "dev":
                self.devolver_livro(partes[1], partes[2])
            case "res":
                self.reservar_livro(partes[1], partes[2])
            case "liv":
                self.informacoes_livro(partes[1])
            case "usu":
                self.informacoes_usuario(partes[1])
            case "sai":
                print("Saindo...")
                exit()
                
    def emprestar_livro(self, codigo_usuario, codigo_exemplar):
        usuario = self.encontrar_usuario(codigo_usuario)
        livro = self.encontrar_livro(codigo_exemplar)
        
        if usuario and livro: 
            exemplar_disponivel = next((exemplar for exemplar in livro.exemplares if exemplar.status == 'Disponível'), None)
            if exemplar_disponivel:
                emprestimo = Emprestimo(usuario, exemplar_disponivel)
                usuario.emprestimos.append(emprestimo)
                exemplar_disponivel.status = 'Emprestado'
                print(f"O livro {livro.titulo} foi emprestado para o usuário {usuario.nome}")
            else:
                print(f"Não há exemplares disponíveis do livro {livro.titulo}")
    def devolver_livro(self, codigo_usuario, codigo_exemplar):
        usuario = self.biblioteca.get_usuario(codigo_usuario)
        livro = self.biblioteca.get_livro(codigo_exemplar)
        
        if usuario and livro:
            emprestimo = next((emprestimo for emprestimo in usuario.emprestimos if emprestimo.exemplar.codigo == codigo_exemplar), None)
            if emprestimo:
                emprestimo.exemplar.status = 'Disponível'
                usuario.emprestimos.remove(emprestimo)
                print(f"O livro {livro.titulo} foi devolvido pelo usuário {usuario.nome}")
            else:
                print(f"O usuário {usuario.nome} não possui o livro {livro.titulo} emprestado")
        
    def reservar_livro(self, codigo_usuario, codigo_exemplar):
        usuario = self.biblioteca.get_usuario(codigo_usuario)
        livro = self.biblioteca.get_livro(codigo_exemplar)
        
        if usuario and livro:
            if len(usuario.reservas) < 3:
                reserva = Reserva(usuario, livro)
                usuario.reservas.append(reserva)
                livro.reservas.append(reserva)
                print(f"O livro {livro.titulo} foi reservado para o usuário {usuario.nome}")
            else:
                print(f"O usuário {usuario.nome} já possui 3 reservas")
    
    def informacoes_livro(self, codigo_exemplar):
        livro = self.encontrar_livro(codigo_exemplar)

        if livro:
            print(f"Título: {livro.titulo}")
            print(f"Reservas: {len(livro.reservas)}")
            for exemplar in livro.exemplares:
                status = 'Emprestado' if exemplar.status == 'Emprestado' else 'Disponível'
                print(f"Exemplar {exemplar.id_exemplar}: {status}")
    
    def informacoes_usuario(self, codigo_usuario):
        usuario = self.encontrar_usuario(codigo_usuario)

        if usuario:
            print(f"Usuário: {usuario.nome}")
            print("Empréstimos:")
            for emprestimo in usuario.emprestimos:
                print(f"- {emprestimo.exemplar.id_exemplar} ({emprestimo.data_emprestimo} até {emprestimo.data_devolucao})")
            print("Reservas:")
            for reserva in usuario.reservas:
                print(f"- {reserva.livro.titulo} ({reserva.data})")
                
    def encontrar_usuario(self, codigo_usuario):
        return next((usuario for usuario in self.biblioteca.usuarios if usuario.codigo == codigo_usuario), None)

    def encontrar_livro(self, codigo_exemplar):
        return next((livro for livro in self.biblioteca.livros if livro.codigo == codigo_exemplar), None)