import sqlite3

from model.jogador import Jogador
from database.config_db import ConfigDB

class JogadorDB:

    _lista_de_jogadores = []
    
    def lista_todos_os_jogadores(self):
        return self._lista_de_jogadores
    
    def listar_jogador(self):
        # lê do banco de dados listando os jogadores
        with sqlite3.connect("batalha_naval.db") as conn:

            cursor = conn.cursor()
            res = cursor.execute("SELECT id, nome, email, senha, pontuacao FROM Jogadores")

            for item in res:
            
                jogador = Jogador(nome=item[1],email = item[2], senha = item[3])
                jogador.pontuacao = item[4]
                jogador.id = item[0]
                self._lista_de_jogadores.append(jogador)
    
    def registrar_jogador(self, jogador: Jogador):
         # Inserir jogador na tabela Jogadores
        ConfigDB.executa_sql("""INSERT INTO Jogadores (id, nome, senha, email, pontuacao) VALUES (?, ?, ?, ?);""", (jogador.nome, jogador.senha, jogador.email, jogador.pontuacao))
        self._lista_de_jogadores.append(jogador)
        return jogador
    
    def editar_jogador_senha(self, jogador: Jogador):
        
        #edita a senha do jogador utilizando o email para pegar o jogador especifico no banco de dados
        # assim editando a senha salva no banco especifico do jogador que possuir o email editado
        ConfigDB.executa_sql(""" UPDATE Jogadores SET senha = ? WHERE email = ?""", (jogador.senha, jogador.email))
        self._lista_de_jogadores.append(jogador)
        return jogador      
    
    def deletar_jogador(self, nome : str):
        #deletar jogador da tabela utilizando o usuario dele
        self._lista_de_jogadores = [
            d for d in self._lista_de_jogadores 
                if d.nome != nome
        ]
        ConfigDB.executa_sql("""DELETE FROM Jogadores where nome = ? """, (nome))
        return "Usuario excluido!"
    
    #Da get id dos jogadores no banco de dados
    def get_id(self, id : int):
        res = ConfigDB.executa_sql("""SELECT id, nome, email, senha, pontuacao FROM Jogadores where id = ? """,(id))
        for item in res:
            
            jogador = Jogador(nome=item[1],email = item[2], senha = item[3])
            jogador.pontuacao = item[4]
            return jogador

    def __init__(self):
            
        if(ConfigDB.get_fonte_dados() == "Banco"):
            self.listar_jogador()
