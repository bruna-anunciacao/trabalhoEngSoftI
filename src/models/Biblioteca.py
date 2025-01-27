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