from model.jogador import Jogador
class FilaDePartidas:
    
    
    def __init__(self):
        self.fila = []
    
    @classmethod
    def entrar_na_fila(self, jogador : Jogador):
        self.fila.append(jogador)
        return f"Usuário {jogador} entrou na fila."
    
    @classmethod
    def procurar_partida(self):
        if not self.fila:
            return "A fila está vazia. Aguardando usuários..."

        jogador = self.fila.pop(0)
        return f"Procurando partida para o usuário {jogador}."

fila_partidas = FilaDePartidas()