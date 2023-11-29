from fastapi import APIRouter, HTTPException
from database.jogador_db import JogadorDB
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    nome: str
    senha: str

@router.post("/login")
async def login(user: User):
    jogador_db = JogadorDB()

    # Verifica se as credenciais existem no banco de dados
    if jogador_db.verificar_credenciais_por_nome_e_senha(user.nome, user.senha):
        return {"message": "Login feito com sucesso!"}
    else:
        raise HTTPException(status_code=401, detail="Nome ou Senha inválido.")