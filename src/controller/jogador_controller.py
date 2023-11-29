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
    
    #cadastra o jogador no banco de dados
    def inserir_jogadores_banco(cls, nome :str, email : str , senha : str):
        jogador : Jogador = Jogador(nome, email, senha)
        return cls.get_instance()._db.inserir_jogador(jogador)
    
    #lista todos os jogadores cadastrados
    def lista_todos_os_jogadores(self):
        return self._db.lista_todos_os_jogadores()
    
    #delete jogadores que ja foram cadastrados
    def delete_jogador_por_nome(cls, nome : str):
        return cls.get_instance()._db.delete_jogador_por_nome(nome)
    
    #editar senha do jogador
    def editar_senha_jogador(cls, nome : str ,email : str, senha : str):
        jogador : Jogador = Jogador(nome, email, senha)
        return cls.get_instance()._db.editar_jogador_senha(jogador)
        