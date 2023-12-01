from database.autenticacao_db import AutenticacaoDB

class AutenticacaoController:
    
    _instance = None
    _ab = None
    
    def __init__(self):
        self._ab = AutenticacaoDB()
        
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AutenticacaoDB()
        return cls._instance