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
biblioteca.usuarios.append(Professor("100", "Carlos Lucena"))

livro1 = Livro("100", "Engenharia de Software", "Addison Wesley", "Ian Sommerville", "6ª", 2000)
livro1.adicionar_exemplar("01")
livro1.adicionar_exemplar("02")
biblioteca.livros.append(livro1)

manipulador = ManipuladorConsole()
manipulador.executar_comando("emp 123 100")