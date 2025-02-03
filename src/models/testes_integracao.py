import sys
import os
from datetime import datetime, timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from models.Biblioteca import Biblioteca
from models.AlunoGraduacao import AlunoGraduacao
from models.AlunoPos import AlunoPos
from models.Professor import Professor
from models.ManipuladorConsole import ManipuladorConsole
from models.Livro import Livro

biblioteca = Biblioteca.get_instance()
biblioteca.usuarios.append(AlunoGraduacao("123", "João da Silva"))
biblioteca.usuarios.append(AlunoPos("456", "Luiz Fernando Rodrigues"))
biblioteca.usuarios.append(AlunoGraduacao("789", "Pedro Paulo"))
biblioteca.usuarios.append(Professor("100", "Carlos Lucena"))

livro1 = Livro("100", "Engenharia de Software", "Addison Wesley", "Ian Sommerville", "6ª", 2000)
livro1.adicionar_exemplar("01")
livro1.adicionar_exemplar("02")
livro1.adicionar_exemplar("03")
biblioteca.livros.append(livro1)

livro2 = Livro("101", "UML - Guia do Usuário", "Campus", "Grady Booch, James Rumbaugh, Ivar Jacobson", "7ª", 2000)
livro2.adicionar_exemplar("03")
livro2.adicionar_exemplar("04")
livro2.adicionar_exemplar("05")
biblioteca.livros.append(livro2)

livro3 = Livro("200", "Code Complete", "Microsoft Press", "Steve McConnell", "2ª", 2014)
livro3.adicionar_exemplar("04")
livro3.adicionar_exemplar("05")
livro3.adicionar_exemplar("06")
biblioteca.livros.append(livro3)

livro4 = Livro("201", "Agile Software Development, Principles, Patterns and Practices", "Prentice Hall", "Robert Martin", "1ª", 2002)
livro4.adicionar_exemplar("05")
livro4.adicionar_exemplar("06")
livro4.adicionar_exemplar("07")
biblioteca.livros.append(livro4)

manipulador = ManipuladorConsole()

print("\n=== TESTE 1: Registrar professor como observador ===")
print("obs 100 100") 
manipulador.executar_comando("obs 100 100")  # Professor observando livro 100

print("\n=== TESTE 2: Reservas que disparam notificação ===")
print("res 123 100")
manipulador.executar_comando("res 123 100")  # Reserva 1
print("res 123 100")
manipulador.executar_comando("res 456 100")  # Reserva 2
print("res 789 100")
manipulador.executar_comando("res 789 100")  # Reserva 3 → Notificação

print("\n=== TESTE 3: Consultar notificações ===")
print("ntf 100")
manipulador.executar_comando("ntf 100")  

print("\n=== TESTE 4: Empréstimos para diferentes usuários ===")
print("emp 123 100")
manipulador.executar_comando("emp 123 100")  # Aluno Graduação
print("emp 456 101")    
manipulador.executar_comando("emp 456 101")  # Aluno Pós
print("emp 100 200")
manipulador.executar_comando("emp 100 200")  # Professor

print("\n=== TESTE 5: Limite de empréstimos ===")
print("emp 123 101")
manipulador.executar_comando("emp 123 101")  # 2º empréstimo para Aluno Graduação
print("emp 123 200")
manipulador.executar_comando("emp 123 200")  # Deve falhar

print("\n=== TESTE 6: Devolução e novo empréstimo ===")
print("dev 123 100")
manipulador.executar_comando("dev 123 100")  # Devolução
print("emp 123 200")
manipulador.executar_comando("emp 123 200")  # Novo empréstimo deve funcionar

print("\n=== TESTE 7: Consulta de informações LIVRO ===")
print("liv 100")
manipulador.executar_comando("liv 100")  # Informações do livro

print("\n=== TESTE 8: Consulta de informações USUARIO ===")
print("usu 123")
manipulador.executar_comando("usu 123")  # Empréstimos do usuário

print("\n=== TESTE 9: Comando inválido ===")
print("xyz 123")
manipulador.executar_comando("xyz 123")  

print("\n=== TESTE 10: Empréstimo com atraso ===")
print("emp 789 201")
manipulador.executar_comando("emp 789 201") 

# Acessa o último empréstimo do usuário 789 e modifica datas
usuario = biblioteca.encontrar_usuario("789")
if usuario and usuario.emprestimos:
    emprestimo = usuario.emprestimos[-1]
    emprestimo.data_emprestimo = datetime.now() - timedelta(days=10)  # Empréstimo feito há 10 dias
    emprestimo.data_devolucao = emprestimo.data_emprestimo + timedelta(days=7)  # Devolução prevista há 3 dias

    print("emp 789 100")
    manipulador.executar_comando("emp 789 100")  
else:
    print("Erro: Empréstimo não encontrado para teste de atraso.")