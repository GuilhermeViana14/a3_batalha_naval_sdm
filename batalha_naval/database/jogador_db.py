import sqlite3

from model.jogador import Jogador
from database.config_db import ConfigDB

class JogadorDB:

    _lista_de_jogadores = []
    
    def lista_todos_os_jogadores(self):
        return self._lista_de_jogadores
    
    # Metodo que lê o banco de dados listando os jogadores
    def listar_jogador(self):
        
        with sqlite3.connect("batalha_naval.db") as conn:

            cursor = conn.cursor()
            res = cursor.execute("SELECT id, nome, email, senha, pontuacao FROM Jogadores")
            conn.commit()
            for r in res:
                jogador = Jogador(
                    nome=r[1],
                    email=r[2],
                    senha=r[3]
                )
                jogador.pontuacao = r[4]
                jogador.id = r[0]
                self._lista_de_jogadores.append(jogador)
    
     # Metodo para registrar um novo jogador na tabela Jogadores no banco de dados
    def registrar_jogador(self, jogador: Jogador):
        ConfigDB.executa_sql("""INSERT INTO Jogadores (nome, senha, email, pontuacao) VALUES (?, ?, ?, ?);""", (jogador.nome, jogador.senha, jogador.email, jogador.pontuacao,))
        self._lista_de_jogadores.append(jogador)
        return jogador
    
    # Metodo para editar a senha do jogador utilizando o email para pegar o jogador especifico no banco de dados e editar sua senha
    def editar_jogador_senha(self, jogador: Jogador):
        ConfigDB.executa_sql(""" UPDATE Jogadores SET senha = ? WHERE email = ?""", (jogador.senha, jogador.email))
        self._lista_de_jogadores.append(jogador)
        return jogador      
    
    # Metodo para deletar algum jogador especifico da tabela utilizando seu nome de usuario
    def deletar_jogador(self, nome : str):
        self._lista_de_jogadores = [
            d for d in self._lista_de_jogadores 
                if d.nome != nome
        ]
        ConfigDB.executa_sql("""DELETE FROM Jogadores where nome = ? """, (nome,))
        return self._lista_de_jogadores
    
   # Metodo que pega o id de cada jogador no banco de dados
    def get_id(self, id : int):
        res = ConfigDB.executa_sql("""SELECT id, nome, email, senha, pontuacao FROM Jogadores where id = ? """,(id))
        for item in res:
            
            jogador = Jogador(nome=item[1],email = item[2], senha = item[3])
            jogador.pontuacao = item[4]
            return jogador

    def __init__(self):
            
        if(ConfigDB.get_fonte_dados() == "Banco"):
            self.listar_jogador()
