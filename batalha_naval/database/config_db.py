import sqlite3

class ConfigDB():
    
    @classmethod
    def get_fonte_dados(cls):
        return "Banco"
    
    
    # Conectar ao banco de dados
    def executa_sql(codigo_sql, value):
        with sqlite3.connect("batalha_naval.db") as conn:
            try:
                cursor = conn.cursor()
                res = cursor.execute(codigo_sql, value)
            except sqlite3.Error as e:
                print(e)

