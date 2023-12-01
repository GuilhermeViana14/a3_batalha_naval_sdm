from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Lista de jogadores em espera
waiting_players = []


class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id


@app.post("/join_queue/{player_id}")
async def join_queue(player_id: int):
    # Verifica se o jogador já está na fila
    for player in waiting_players:
        if player.player_id == player_id:
            raise HTTPException(status_code=400, detail="Jogador já está na fila.")

    # Adiciona o jogador à fila de espera
    waiting_players.append(Player(player_id=player_id))

    # Verifica se há dois jogadores na fila
    if len(waiting_players) >= 2:
        # Pega os dois primeiros jogadores da fila
        player_1 = waiting_players.pop(0)
        player_2 = waiting_players.pop(0)

        # Inicia a partida (pode ser uma função ou lógica específica)
        start_game(player_1, player_2)

    return {"message": f"Jogador {player_id} entrou na fila de espera."}
    
    

def start_game(player_1: Player, player_2: Player):
    # Implemente a lógica da partida aqui
    print(f"Partida iniciada! Jogador 1: {player_1.player_id}, Jogador 2: {player_2.player_id}")
    # Pode ser necessário notificar os jogadores ou executar a lógica do jogo
