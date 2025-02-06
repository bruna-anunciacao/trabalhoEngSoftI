from .VerificaEmprestimo import VerificaEmprestimo

class VerificaEmprestimoAluno(VerificaEmprestimo):
    def verificar_condicoes(self, usuario, livro):
        if usuario.tem_livro_atrasado():
            return False, "Usuário possui livros em atraso."


        if len(usuario.emprestimos) >= usuario.max_emprestimos:
            return False, f"Usuário já atingiu o limite de {usuario.max_emprestimos} empréstimos."

        reservas_do_livro = len(livro.reservas)
        exemplares_disponiveis = sum(1 for exemplar in livro.exemplares if exemplar.status == 'Disponível')

        if reservas_do_livro >= exemplares_disponiveis and not usuario.possui_reserva_para_livro(livro):
            return False, "Todos os exemplares disponíveis estão reservados por outros usuários."

        if usuario.tem_emprestimo_do_livro(livro):
            return False, "Usuário já possui um exemplar deste livro emprestado."

        return True, "Empréstimo permitido."
