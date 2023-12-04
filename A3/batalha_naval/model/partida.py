from model.jogador import Jogador

# Classe Partida
class Partida:
    
    jogador_1 : Jogador
    jogador_2 : Jogador
    matriz_1 = {}
    matriz_2 = {}
    vez : int
    
    def __init__(self, jogador_1, jogador_2):
        self.jogador_1 = jogador_1
        self.jogador_2 = jogador_2
        
        self.vez = 1
        self.matriz_1= {(x,y): 0 for x in range(10) for y in range(10)}
        self.matriz_2= {(x,y): 0 for x in range(10) for y in range(10)}
        
    #----------------------------------------------------------------------------
    # Nao implementado no request
    def atira(self, x : int, y : int, id_jogador : int):
        ## JOGADOR 1 atirou, entao mexeremos na matriz 2
        if id_jogador == 1:
            ponto = self.matriz_2.get((x,y))
            if ponto == 0:
                # Nao acertou
                self.matriz_2[(x,y)] = 2
                return "nao acertou"
                
            elif ponto == 1:
                # Acertou
                self.matriz_2[(x,y)] = 2
                return "acertou"

            elif ponto == 2:
                # Atirou onde ja foi atirado antes
                return "Voce ja atirou aqui"

        ## JOGADOR 2 atirou, entao mexemos na matriz 1
        if id_jogador == 2:
            ponto = self.matriz_1.get((x,y))
            if ponto == 0:
                # Nao acertou
                self.matriz_1[(x,y)] = 2
                return "nao acertou"
            elif ponto == 1:
                # Acertou
                self.matriz_1[(x,y)] = 2
                return "acertou"
            elif ponto == 2:
                # Atirou onde ja foi atirado antes
                return "Voce ja atirou aqui"
            
    
    # Nao implementado no request
    def colocar_barco(self, barco : list, id_jogador : int):
        if id_jogador == 1:
            for x in barco: # x = (x,y) # lista = [(1,1), (1,2), (1,3)]
                self.matriz_1[x] = 1
                
        if id_jogador == 2:
            for x in barco: # x = (x,y) # lista = [(1,1), (1,2), (1,3)]
                self.matriz_2[x] = 1
                    
    # Nao implementado no request
    def verificar_fim(self):
        #verifica qual matriz primeiro nao possui o navio 
        # caso nao possua navio dentro dela diriamos qual dos jogadores ganhou
        tem_jogo = False
        for x in self.matriz_1:
            if self.matriz_1 [x] == 1:
                tem_jogo = True
        
        if not tem_jogo:
            return "jogador 2 ganhou"
        
        for x in self.matriz_2:
            if self.matriz_2 [x] == 1:
                tem_jogo = True
        
        if not tem_jogo:
            return "jogador 1 ganhou"
    #----------------------------------------------------------------------------    
    # Metodo que imprime o tabuleiro atraves da matriz utilizando strings
    def imprimir_tabuleiro(self):
        string_1 = ""
        string_2 = ""
        
        for x in self.matriz_1:
            string_1 += str(self.matriz_1[x])
            if x[1] == 9:
                string_1 += '\n'
        
        for x in self.matriz_2:
            string_2 += str(self.matriz_2[x])
            if x[1] == 9:
                string_2 += '\n'
        return string_1 , string_2
            
                    
                    
                    
            
            
         