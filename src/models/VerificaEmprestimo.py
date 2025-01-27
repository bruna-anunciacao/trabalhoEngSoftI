class VerificaEmprestimo:
    def pode_emprestar(self, usuario, livro):
        raise NotImplementedError

class VerificaEmprestimoAlunoGraduacao(VerificaEmprestimo):
    def pode_emprestar(self, usuario, livro):
        pass

class VerificaEmprestimoAlunoPosGraduacao(VerificaEmprestimo):
    def pode_emprestar(self, usuario, livro):
        pass

class VerificaEmprestimoProfessor(VerificaEmprestimo):
    def pode_emprestar(self, usuario, livro):
        pass
