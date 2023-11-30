from pydantic import BaseModel

class LoginRequest(BaseModel):
    nome: str
    senha: str