from typing import Optional

class CarregadorParametros:
    def __init__(self, parametro_um: str, parametro_dois: Optional[str] = None):
        self._parametro_um = parametro_um
        self._parametro_dois = parametro_dois
    
    def get_parametro_um(self) -> str:
        return self._parametro_um
    
    def get_parametro_dois(self) -> Optional[str]:
        return self._parametro_dois