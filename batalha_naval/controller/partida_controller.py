from model.partida import Partida
from database.jogador_db import JogadorDB

class PartidaController:
    lista_espera = []
    lista_jogos = []
    _instance = None
    
    def __init__(self):
        self._db = JogadorDB()
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PartidaController()
        return cls._instance
    
    @classmethod
    def acha_jogo(cls, id_jogador : int):
        
      #procura dentro da lista se possui 2 jogadores
      #caso possua ele cria uma partida na lista de jogos com os o id da partida
      jogador = cls.get_instance()._db.get_id(id_jogador)
      if len(cls.lista_espera) >= 1:
          jogador_2 = cls.lista_espera.pop(0)
          partida = Partida(jogador, jogador_2)
          cls.lista_jogos.append(partida)
          print(cls.lista_jogos)
          #define partida do jogador
          return len(cls.lista_jogos) - 1
      else:
          cls.lista_espera.append(jogador)
          return - 1
      
    @classmethod
    def verifica_se_possui_jogo(cls, id_jogador : int):
        #aqui vamos verificar se o jogador possui algum jogo
        jogador = cls.get_instance()._db.get_id(id_jogador)
        for idx, jogo in enumerate(cls.lista_jogos):
            print(jogo.jogador_1.nome)
            print(jogo.jogador_2.nome)
            if jogo.jogador_1.nome == jogador.nome:
                return idx
            if jogo.jogador_2.nome == jogador.nome:
                return idx
        return -1
    
    @classmethod
    #pegamos o tabuleiro atraveis do id da partida e imprimimos ele
    def pegar_tabuleiro(cls, id_partida : int):
        return cls.lista_jogos[id_partida].imprimir_tabuleiro()
    
    
    # Teste para colocar o barco 
    @classmethod
    def colocar_barco(cls, barcos : list, id_partida : int , id_jogador : int):
        jogador = cls.get_instance()._db.get_id(id_jogador)
        jogo = cls.lista_jogos[id_partida]
        id = None
        if jogo.jogador_1.nome == jogador.nome:
            id = 1
        if jogo.jogador_2.nome == jogador.nome:
            id = 2
        jogo.colocar_barco(barcos, id)
        return "sucesso"
        
        
        
    