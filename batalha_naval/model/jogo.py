from model.jogador import Jogador

class Jogo:
    @staticmethod
    def start_game(jogador_1: Jogador, jogador_2: Jogador):
        # Implemente a lógica da partida aqui
        print(f"Partida iniciada! Jogador 1: {jogador_1.nome}, Jogador 2: {jogador_2.nome}")
        # Pode ser necessário notificar os jogadores ou executar a lógica do jogo