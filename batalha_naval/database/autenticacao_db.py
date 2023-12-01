from model.autenticacao import Autenticacao
from datetime import datetime, timedelta
import hashlib


class AutenticacaoDB:
    
    sala : list[Autenticacao]
    
    def __init__(self: "AutenticacaoDB"):
        self.sala = []
        
        
    def deletar_sala(self, nome : str):
        self.sala = [s for s in self.sala if s.nome != nome]
    
    def criar_sala(self, nome : str):
        self.deletar_sala(nome)
        
        tempo = datetime.now()
        tempo = tempo + timedelta(minutes=10)
        
        id = hashlib.sha1((nome + str(tempo.timestamp())).encode('utf'))
        
        sessao : Autenticacao = Autenticacao(nome, id.hexdigest(), tempo)
        self.sala.append(sessao)
        
        return sessao.id
        
        