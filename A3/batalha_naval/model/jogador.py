# Classe Jogador
class Jogador:
    nome : str
    email : str
    senha : str
    pontuacao : int
    
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pontuacao = 0 