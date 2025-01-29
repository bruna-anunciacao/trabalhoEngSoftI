from .VerificaEmprestimo import VerificaEmprestimo

class VerificaEmprestimoProfessor(VerificaEmprestimo):
    def verificar_condicoes(self, usuario, livro):
        if usuario.tem_livro_atrasado():
            return False, "Usuário possui livros em atraso."

        return True, "Empréstimo permitido."
