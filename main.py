from typing import Union
from fastapi import FastAPI

from model.jogador import Jogador
from database.jogador_db import JogadorDB
from controller.jogador_controller import JogadorController
app = FastAPI()

@app.put("/registrar/jogadores/{nome}/{email}/{senha}")
def registrar_jogadores(nome: str, email : str, senha: str):
    return JogadorController.get_instance().inserir_jogadores_banco(nome, email, senha)

@app.get("/listar/jogadores")
async def lista_jogadores():
    return JogadorController.get_instance().lista_todos_os_jogadores()

@app.get("/ranking")
async def ranking():
    return JogadorController.get_instance().lista_ranking_top()

@app.delete("/remover/jogadores/{nome}")
async def delete_jogadores(nome: str):
    return JogadorController.get_instance().delete_jogador_por_nome(nome)

@app.patch("/editar/jogador/senha/{nome}/{email}/{senha}")
async def editar_jogador_senha(nome : str , email : str, senha: str):
    return JogadorController.get_instance().editar_senha_jogador(nome, email , senha)