from fastapi import FastAPI

from controller.jogador_controller import JogadorController
from controller.partida_controller import PartidaController

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

@app.post("/procura/partida/{id_jogador}")
async def procura_partida(id_jogador):
    return PartidaController.get_instance().acha_jogo(id_jogador)

@app.post("/procura/partida/verifica/{id_jogador}")
async def verifica_partida(id_jogador):
    return PartidaController.get_instance().verifica_se_possui_jogo(id_jogador)

@app.get("/tabuleiro/{id_partida}")
async def tabuleiro(id_partida):
    return PartidaController.get_instance().pegar_tabuleiro(int (id_partida))

# #nao implementado
# @app.put("/tabuleiro/colocar/barco/{lista_barcos}/{id_partida}/{id_jogador}")
# async def colocar_barcos(lista_barco : list , id_partida : int, id_jogador : int ):

