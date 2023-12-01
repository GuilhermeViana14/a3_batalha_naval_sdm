from model.jogador import Jogador
from model.jogo import Jogo

class Partida:
    def __init__(self, jogador1: Jogador, jogador2: Jogador):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabuleiro_jogador1 = [[0] * 10 for _ in range(10)]  # Exemplo de tabuleiro 10x10
        self.tabuleiro_jogador2 = [[0] * 10 for _ in range(10)]  # Exemplo de tabuleiro 10x10
        self.estado_jogo = "Aguardando Posicionamento"

    def obter_estado_partida(self):
        return {
            "estado_jogo": self.estado_jogo,
            "tabuleiro_jogador1": self.tabuleiro_jogador1,
            "tabuleiro_jogador2": self.tabuleiro_jogador2,
            # Outras informações necessárias...
        }

    def posicionar_navios(self, jogador: Jogador, posicoes):
        if jogador == self.jogador1:
            tabuleiro = self.tabuleiro_jogador1
        elif jogador == self.jogador2:
            tabuleiro = self.tabuleiro_jogador2
        else:
            raise ValueError("Jogador inválido.")

        # Lógica para validar as posições e armazenar no tabuleiro.
        for x, y in posicoes:
            # Exemplo simples: atribuir 1 para cada posição do navio
            tabuleiro[x][y] = 1

        # Atualizar o estado do jogo, talvez verificar se ambos os jogadores já posicionaram seus navios, etc.
        self.estado_jogo = "Aguardando Jogada"  # Ou outro estado apropriado

        # Se ambos os jogadores posicionaram os navios, inicie o jogo
        if self.estado_jogo == "Aguardando Jogada":
            Jogo.start_game(self.jogador1, self.jogador2)