import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from datetime import datetime

from models.Reserva import Reserva
from models.Emprestimo import Emprestimo
from models.VerificaEmprestimoAluno import VerificaEmprestimoAluno
from models.VerificaEmprestimoProfessor import VerificaEmprestimoProfessor
from models.AlunoGraduacao import AlunoGraduacao
from models.AlunoPos import AlunoPos
from models.Professor import Professor
from models.ProfessorObservador import ProfessorObservador

class Biblioteca:
    _instance = None
    
    @staticmethod
    def get_instance():
        if Biblioteca._instance is None:
            Biblioteca._instance = Biblioteca()
        return Biblioteca._instance
    
    def __init__(self):
        if Biblioteca._instance is not None:
            raise Exception("This class is a singleton!")
        self.usuarios = []
        self.livros = []
    
    def emprestar_livro(self, codigo_usuario, codigo_exemplar):
        usuario = self.encontrar_usuario(codigo_usuario)
        livro = self.encontrar_livro(codigo_exemplar)

        if not usuario:
            print("Usuário não encontrado.")
            return
        if not livro:
            print("Livro não encontrado.")
            return

        exemplar_disponivel = next((exemplar for exemplar in livro.exemplares if exemplar.status == 'Disponível'), None)
        if exemplar_disponivel is None:
            print("Não há exemplares disponíveis para empréstimo.")
            return

        verificadores = {
            AlunoGraduacao: VerificaEmprestimoAluno,
            AlunoPos: VerificaEmprestimoAluno,
            Professor: VerificaEmprestimoProfessor
        }

        classe_verificadora = verificadores.get(type(usuario))
        if not classe_verificadora:
            print("Tipo de usuário não suportado para empréstimos.")
            return

        emprestimo = classe_verificadora()
        permitido, mensagem = emprestimo.verificar_condicoes(usuario, livro)

        if permitido:
            emprestimo = Emprestimo(usuario, exemplar_disponivel)
            usuario.emprestimos.append(emprestimo)
            exemplar_disponivel.status = 'Emprestado'
            exemplar_disponivel.emprestimo = emprestimo
            usuario.reservas = [reserva for reserva in usuario.reservas if reserva.livro != livro]
            livro.reservas = [reserva for reserva in livro.reservas if reserva.usuario != usuario]
            print(f"O livro {livro.titulo} foi emprestado para o usuário {usuario.nome}")
        else:
            print(f"Empréstimo não realizado: {mensagem}")

    def devolver_livro(self, codigo_usuario, codigo_exemplar):
        usuario = self.encontrar_usuario(codigo_usuario)
        livro = self.encontrar_livro(codigo_exemplar)
        
        if usuario and livro:
            emprestimo = next((emp for emp in usuario.emprestimos if emp.exemplar in livro.exemplares), None)
            if emprestimo:
                emprestimo.exemplar.status = 'disponível'
                emprestimo.data_devolucao = datetime.now()
                emprestimo.status_emprestimo = 'Finalizado'
                print(f"Devolução realizada: {usuario.nome} - {livro.titulo}")
                return
        elif not usuario:
            print("Usuário não encontrado.")
            return
        else:
            print("Livro não encontrado.")
            return
        return print("Empréstimo não encontrado.")

    def reservar_livro(self, codigo_usuario, codigo_exemplar):
        usuario = self.encontrar_usuario(codigo_usuario)
        livro = self.encontrar_livro(codigo_exemplar)
        
        if usuario and livro:
            if len(usuario.reservas) < 3:
                if usuario.possui_reserva_para_livro(livro):
                    print(f"O usuário {usuario.nome} já possui uma reserva para o livro {livro.titulo}")
                    return
                reserva = Reserva(usuario, livro)
                usuario.reservas.append(reserva)
                livro.adicionar_reserva(reserva)
                print(f"O livro {livro.titulo} foi reservado para o usuário {usuario.nome}")
            else:
                print(f"O usuário {usuario.nome} já possui 3 reservas")
            return
        elif not usuario:
            print("Usuário não encontrado.")
            return
        else:
            print("Livro não encontrado.")
            return

    def informacoes_livro(self, codigo_exemplar):
        livro = self.encontrar_livro(codigo_exemplar)
        if livro:
            print(f"Título: {livro.titulo}")
            print(f"Reservas: {len(livro.reservas) > 0 and ', '.join([reserva.usuario.nome for reserva in livro.reservas]) or 'Nenhuma reserva'}")
            for exemplar in livro.exemplares:
                if exemplar.status == 'Emprestado' and exemplar.emprestimo is not None:
                    status = f"Emprestado para {exemplar.emprestimo.usuario.nome} ({exemplar.emprestimo.data_emprestimo.strftime('%d/%m/%Y')} até {exemplar.emprestimo.data_devolucao.strftime('%d/%m/%Y')})"
                else:
                    status = 'Disponível'
                print(f"Exemplar {exemplar.codigo}: {status}")
            return
        return print("Livro não encontrado.")

    def informacoes_usuario(self, codigo_usuario):
        usuario = self.encontrar_usuario(codigo_usuario)
        if usuario:
            print(f"Usuário: {usuario.nome}")
            print("Empréstimos:")
            for emprestimo in usuario.emprestimos:
                if emprestimo.status_emprestimo == 'Em curso':
                    print(f"- {emprestimo.exemplar.livro.titulo} ({emprestimo.data_emprestimo.strftime('%d/%m/%Y')} até {emprestimo.data_devolucao.strftime('%d/%m/%Y')}) - Em curso")    
                else:
                    print(f"- {emprestimo.exemplar.livro.titulo} ({emprestimo.data_emprestimo.strftime('%d/%m/%Y')} até {emprestimo.data_devolucao.strftime('%d/%m/%Y')}) - Devolvido")
            print("Reservas:")
            for reserva in usuario.reservas:
                print(f"- {reserva.livro.titulo} ({reserva.data_reserva.strftime('%d/%m/%Y')})")
            return
        return print("Usuário não encontrado.")

    def encontrar_usuario(self, codigo_usuario):
        return next((usuario for usuario in self.usuarios if usuario.codigo == codigo_usuario), None)

    def encontrar_livro(self, codigo_exemplar):
        return next((livro for livro in self.livros if livro.codigo == codigo_exemplar), None)
    
    def total_notificacoes(self, codigo_usuario):
        total = 0
        for livro in self.livros:
            for observador in livro.observadores:
                if isinstance(observador, ProfessorObservador) and observador.professor.codigo == codigo_usuario:
                    total += observador.contador_notificacoes
        return total