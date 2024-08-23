import mysql.connector

def get_connection():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="cadastro"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

def close_connection(conexao, cursor=None):
    if cursor:
        cursor.close()
    if conexao and conexao.is_connected():
        conexao.close()

def get_mysql_error():
    return mysql.connector.Error