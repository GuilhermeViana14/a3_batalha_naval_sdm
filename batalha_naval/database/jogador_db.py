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
    
    def inserir_jogador(self, jogador: Jogador):
         # Inserir jogador na tabela Jogadores
        ConfigDB.executa_sql("""INSERT INTO Jogadores (nome, senha, email, pontuacao) VALUES (?, ?, ?, ?);""", (jogador.nome, jogador.senha, jogador.email, jogador.pontuacao))
        self._lista_de_jogadores.append(jogador)
        return jogador
    
    def editar_jogador_senha(self, jogador: Jogador):
        
        #edita a senha buscando o email do jogador e assim editando a senha salva no banco especifico do jogador que possuir o email editado
        ConfigDB.executa_sql(""" UPDATE Jogadores SET senha = ? WHERE email = ?""", (jogador.senha, jogador.email))
        self._lista_de_jogadores.append(jogador)
        return jogador      
    
    def delete_jogador_por_nome(self, nome : str):
        #deletar jogador da tabela
        self._lista_de_jogadores = [
            d for d in self._lista_de_jogadores 
                if d.nome != nome
        ]
        ConfigDB.executa_sql("""DELETE FROM Jogadores where nome = ? """, (nome,))
        return self._lista_de_jogadores
    
    
    def __init__(self):
            
        if(ConfigDB.get_fonte_dados() == "Banco"):
            self.listar_jogador()
