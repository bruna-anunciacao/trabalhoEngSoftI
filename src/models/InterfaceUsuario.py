from typing import Dict
from trabalhoEngSoftI.src.models import CarregadorParametros
from trabalhoEngSoftI.src.models.Comando import Comando, EmprestarComando, ConsultarUsuarioComando

class InterfaceUsuario:
    def __init__(self):
        self.comandos: Dict[str, Comando] = {}
        self.inicializar_comandos()
    
    def inicializar_comandos(self) -> None:
        self.comandos = {
            "emp": EmprestarComando(),
            "usu": ConsultarUsuarioComando()
        }
    
    def executar_comando(self, str_comando: str, parametros: CarregadorParametros) -> None:
        comando = self.comandos.get(str_comando)
        if comando:
            comando.executar(parametros)
