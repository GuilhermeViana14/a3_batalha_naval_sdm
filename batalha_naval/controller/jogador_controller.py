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
    @classmethod
    def registrar_jogadores_banco(cls, nome :str, email : str , senha : str):
        jogador : Jogador = Jogador(nome, email, senha)
        return cls.get_instance()._db.registrar_jogador(jogador)
    
    #delete jogadores que ja foram cadastrados
    @classmethod
    def deletar_jogador(cls, nome : str):
        return cls.get_instance()._db.deletar_jogador(nome)
    
    #editar senha do jogador
    @classmethod
    def editar_senha_jogador(cls, nome : str ,email : str, senha : str):
        jogador : Jogador = Jogador(nome, email, senha)
        return cls.get_instance()._db.editar_jogador_senha(jogador)
    
    #lista todos os jogadores cadastrados
    def lista_todos_os_jogadores(self):
        return self._db.lista_todos_os_jogadores()
    
    
    def lista_ranking_top(self):
        jogadores = self._db.lista_todos_os_jogadores()
        
        # on the fly (em tempo de execução)
        jogadores_dto = []
        for jogador in jogadores:

            jogadores_dto.append({
                "nome": jogador.nome,
                "pontuacao": int(jogador.pontuacao)
            })

        def criterio(jogador_dto):
            return - jogador_dto["pontuacao"]

        # ordenar o vetor, do maior ao menor, pelo score
        v_ordenado = sorted(jogadores_dto, key=criterio)

        # DTO => data transfer object
        return v_ordenado[:5]
        