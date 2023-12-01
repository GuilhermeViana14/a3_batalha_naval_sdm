from typing import List
from model.jogador import Jogador
from model.jogo import Jogo
from fastapi import HTTPException
from model.partida import Partida

class FilaEspera:
    def __init__(self):
        self.waiting_players = []

    def join_queue(self, nome: str):
        jogador = Jogador(nome=nome, email="", senha="")
        
        # Verifica se o jogador já está na fila
        for jogador_na_fila in self.waiting_players:
            if jogador_na_fila.nome == jogador.nome:
                raise HTTPException(status_code=400, detail="Jogador já está na fila.")

        # Adiciona o jogador à fila de espera
        self.waiting_players.append(jogador)

        # Verifica se há dois jogadores na fila
        if len(self.waiting_players) >= 2:
            # Pega os dois primeiros jogadores da fila
            jogador_1 = self.waiting_players.pop(0)
            jogador_2 = self.waiting_players.pop(0)

            # Inicia a partida
            Jogo.start_game(jogador_1, jogador_2)
            
            
            
    
            
            
        