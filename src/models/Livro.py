class Livro:
    def __init__(self, codigo, titulo, editora, autor, edicao, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.edicao = edicao
        self.ano = ano

    def adicionar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)

class Exemplar:
    def __init__(self, codigo_exemplar):
        self.codigo_exemplar = codigo_exemplar
        self.disponivel = True
        self.usuario_emprestado = None