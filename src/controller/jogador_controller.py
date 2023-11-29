from database.jogador_db import JogadorDB
from model.jogador import Jogador
class JogadorController:
    
    _instance = None
    _db = None

    def __init__(self):
        self._db = JogadorDB()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = JogadorController()
        return cls._instance
    
    #lista todos os jogadores cadastrados
    def lista_todos_os_jogadores(self):
        return self._db.lista_todos_os_jogadores()