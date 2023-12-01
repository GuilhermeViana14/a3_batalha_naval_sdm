from typing import Union
from fastapi import FastAPI, HTTPException
from model.autenticacao_login import LoginRequest
from pydantic import BaseModel
from controller.fila_controller import FilaEspera


from controller.jogador_controller import JogadorController
app = FastAPI()


@app.post("/login")
def login(login_request: LoginRequest):
    jogador_controller = JogadorController.get_instance()
    if jogador_controller.verificar_credenciais(login_request.nome, login_request.senha):
        return {"message": "Login feito com sucesso!"}
    else:
        raise HTTPException(status_code=401, detail="Nome ou Senha inválido.")


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

fila_espera = FilaEspera()

@app.post("/join_queue/{nome}")
async def join_queue(nome: str):
    # Chama o método join_queue da instância da FilaEspera
    fila_espera.join_queue(nome)
    return {"message": f"Jogador {nome} entrou na fila de espera."}





