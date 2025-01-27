from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from trabalhoEngSoftI.src.models.CarregadorParametros import CarregadorParametros
from trabalhoEngSoftI.src.models.Repositorio import Repositorio  

class Comando(ABC):
    @abstractmethod
    def executar(self, carregador_parametros: 'CarregadorParametros') -> None:
        pass

class ConsultarUsuarioComando(Comando):
    def executar(self, carregador_parametros: 'CarregadorParametros') -> None:
        repositorio = Repositorio.obter_instancia()
        codigo = carregador_parametros.get_parametro_um()
        usuario = repositorio.obter_usuario_por_codigo(codigo)

class EmprestarComando(Comando):
    def executar(self, carregador_parametros: 'CarregadorParametros') -> None:
        repositorio = Repositorio.obter_instancia()
        usuario = repositorio.obter_usuario_por_codigo(carregador_parametros.get_parametro_um())
        livro = repositorio.obter_livro_por_codigo(carregador_parametros.get_parametro_dois())
