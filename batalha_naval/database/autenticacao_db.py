from model.autenticacao import Autenticacao
from datetime import datetime, timedelta

class AutenticacaoDB:
    
    sala : list[Autenticacao]
    
    def __init__(self: "AutenticacaoDB"):
        self.sala = []
        
        
    def deletar_sala(self, nome : str):
        self.sala = [s for s in self.sala if s.nome != nome]
    
    def criar_sala(self, nome : str):
        
        