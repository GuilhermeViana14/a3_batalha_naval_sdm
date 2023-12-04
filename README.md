# A3_BATALHA_NAVAL_SDM

Projeto feit para ser um jogo de batalha naval em python e com requests utilizando fastapi para a unidade curricular de sistemas distribuidos e mobile

Para rodar o codigo crie uma maquina virtual com o comando: python -m venv .venv
acesse a sua venv com o comando: .\.venv\Scripts\Activate.ps1 
Acesse a pasta batalha_naval utilizando o comando: cd .\batalha_naval\
rode o init_db para criar o arquivo do banco de dados: python init_db.py
Rode o codigo com o comando: uvicorn main:app --host 0.0.0.0 --port 8000/3000 --reload
Assim pode testar os request no http://127.0.0.1:8000/docs ou utilizando o Postman