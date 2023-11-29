import sqlite3

from model.jogador import Jogador
from database.config_db import ConfigDB

class JogadorDB:

    _lista_de_jogadores = []
    
    def lista_todos_os_jogadores(self):
        return self._lista_de_jogadores
    
    def listar_jogador(self):
        # lê do banco de dados listnado os jogadores
        with sqlite3.connect("batalha_naval.db") as conn:

            cursor = conn.cursor()
            res = cursor.execute("SELECT id, nome, email, senha, pontuacao FROM Jogadores")

            for r in res:
                jogador = Jogador(
                    nome=r[1],
                    email=r[2],
                    senha=r[3]
                )
                jogador.pontuacao = r[4]
                self._lista_de_jogadores.append(jogador)
                
    def __init__(self):
            
        if(ConfigDB.get_fonte_dados() == "Banco"):
            self.listar_jogador()
