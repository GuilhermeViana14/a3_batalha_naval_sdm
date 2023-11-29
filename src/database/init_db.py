import sqlite3

# Conectar ao banco de dados (o arquivo será criado se não existir)
conn = sqlite3.connect('batalha_naval.db')

# Criar um cursor
cursor = conn.cursor()

# Definir o comando SQL para criar a tabela Jogador
sql_create_table_jogador = '''
    CREATE TABLE Jogadores(
        id INTEGER,
        pontuacao INTEGER,
        nome TEXT,
        email TEXT,
        senha TEXT,
        PRIMARY KEY(id)
    );
'''
#executa o cursor para assim criar a tabela
cursor.execute(sql_create_table_jogador)

#fecha a conexao
conn.close()