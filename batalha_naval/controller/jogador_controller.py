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
    
    
    def verificar_credenciais(self, nome: str, senha: str) -> bool:
            jogadores = self._db.lista_todos_os_jogadores()
            for jogador in jogadores:
                if jogador.nome == nome and jogador.senha == senha:
                    return True
            return False
    
    
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
    
    def lista_ranking_top(self):
        jogadores = self._db.lista_todos_os_jogadores()
        
        # on the fly (em tempo de execução)
        jogadores_dto = []
        for jogador in jogadores:

            # jogador_simplificado = { }
            # jogador_simplificado["apelido"] = jogador._apelido

            jogadores_dto.append({
                "nome": jogador.nome,
                "pontuacao": int(jogador.pontuacao)
            })

        def criterio(jogador_dto):
            return - jogador_dto["pontuacao"]

        # ordenar o vetor, do maior ao menor, pelo score
        v_ordenado = sorted(jogadores_dto, key=criterio)

        # DTO => data transfer object
        return v_ordenado[:5]   # syntax sugar
    
    
        