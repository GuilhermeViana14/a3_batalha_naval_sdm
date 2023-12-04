import sqlite3

# Codigo para conectar ao banco de dados (o arquivo será criado se não existir)
conn = sqlite3.connect('batalha_naval.db')

# Cria um cursor
cursor = conn.cursor()

# Definir o comando SQL para criar a tabela dos Jogadores com seus atributos
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
# Executa o cursor para assim criar a tabela
cursor.execute(sql_create_table_jogador)

# Fecha a conexao
conn.close()