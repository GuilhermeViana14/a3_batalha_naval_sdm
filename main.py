from typing import Union
from fastapi import FastAPI

from model.jogador import Jogador
from database.jogador_db import JogadorDB
from controller.jogador_controller import JogadorController
app = FastAPI()



@app.get("/listar/jogadores")
async def lista_jogadores():
    return JogadorController.get_instance().lista_todos_os_jogadores()