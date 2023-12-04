import sqlite3

class ConfigDB():
    
    @classmethod
    def get_fonte_dados(cls):
        return "Banco"
    
    
    # Conectar ao banco de dados
    def executa_sql(codigo_sql, value):
        # Codigo para conectar ao banco de dados
        with sqlite3.connect("batalha_naval.db") as conn:
            try:
                # Cria um cursor
                cursor = conn.cursor()
                
                #executa o cursor passsando 2 parametros 
                res = cursor.execute(codigo_sql, value)
                conn.commit()
                return res
            except sqlite3.Error as e:
                print(e)
                

