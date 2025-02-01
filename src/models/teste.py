import sys
import os
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
biblioteca.livros.append(livro1)

livro2 = Livro("101", "UML - Guia do Usuário", "Campus", "Grady Booch, James Rumbaugh, Ivar Jacobson", "7ª", 2000)
livro2.adicionar_exemplar("03")
biblioteca.livros.append(livro2)

livro3 = Livro("200", "Code Complete", "Microsoft Press", "Steve McConnell", "2ª", 2014)
livro3.adicionar_exemplar("04")
biblioteca.livros.append(livro3)

livro4 = Livro("201", "Agile Software Development, Principles, Patterns and Practices", "Prentice Hall", "Robert Martin", "1ª", 2002)
livro4.adicionar_exemplar("05")
biblioteca.livros.append(livro4)

manipulador = ManipuladorConsole()
manipulador.iniciar()