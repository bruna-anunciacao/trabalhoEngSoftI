import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from models.Reserva import Reserva
from models.Biblioteca import Biblioteca
from models.Emprestimo import Emprestimo
from models.VerificaEmprestimoAluno import VerificaEmprestimoAluno
from models.VerificaEmprestimoProfessor import VerificaEmprestimoProfessor
from models.AlunoGraduacao import AlunoGraduacao
from models.AlunoPos import AlunoPos
from models.Professor import Professor

class ManipuladorConsole:
    def __init__(self):
        self.biblioteca = Biblioteca.get_instance()
        
    def iniciar(self):
        print("Sistema de Biblioteca iniciado. Digite um comando ou 'sai' para sair.")
        while True:
            comando = input("Comando: ")
            self.executar_comando(comando)

    def executar_comando(self, comando):
        partes = comando.split()
        acao = partes[0]

        if acao == 'emp':
            self.emprestar_livro(partes[1], partes[2])
        elif acao == 'dev':
            self.devolver_livro(partes[1], partes[2])
        elif acao == 'res':
            self.reservar_livro(partes[1], partes[2])
        elif acao == 'liv':
            self.informacoes_livro(partes[1])
        elif acao == 'usu':
            self.informacoes_usuario(partes[1])
        elif acao == 'sai':
            print("Saindo do sistema...")
            exit()
                
    def emprestar_livro(self, codigo_usuario, codigo_exemplar):
        usuario = self.encontrar_usuario(codigo_usuario)
        livro = self.encontrar_livro(codigo_exemplar)

        if not usuario or not livro:
            print("Usuário ou livro não encontrado.")
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
                usuario.emprestimos.remove(emprestimo)
                print(f"Devolução realizada: {usuario.nome} - {livro.titulo}")
            else:
                print(f"Nenhum empréstimo encontrado para o usuário {usuario.nome} e o livro {livro.titulo}.")
        
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
                print(f"Exemplar {exemplar.codigo}: {status}")
    
    def informacoes_usuario(self, codigo_usuario):
        usuario = self.encontrar_usuario(codigo_usuario)

        if usuario:
            print(f"Usuário: {usuario.nome}")
            print("Empréstimos:")
            for emprestimo in usuario.emprestimos:
                print(f"- Exemplar {emprestimo.exemplar.codigo} do livro {emprestimo.exemplar.livro.titulo} ({emprestimo.data_emprestimo} até {emprestimo.data_devolucao})")
            print("Reservas:")
            for reserva in usuario.reservas:
                print(f"- {reserva.livro.titulo} ({reserva.data_reserva})")
                
    def encontrar_usuario(self, codigo_usuario):
        return next((usuario for usuario in self.biblioteca.usuarios if usuario.codigo == codigo_usuario), None)

    def encontrar_livro(self, codigo_exemplar):
        return next((livro for livro in self.biblioteca.livros if livro.codigo == codigo_exemplar), None)