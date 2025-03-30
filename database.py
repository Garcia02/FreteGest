import mysql.connector
import logging

# Configuração do logging para nível de erro
logging.basicConfig(level=logging.ERROR)

def get_connection():
    """
    Cria e retorna uma conexão ao banco de dados MySQL.
    """
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="databasefretgest"
        )
        return conexao
    except mysql.connector.Error as erro:
        logging.error(f"Erro ao conectar ao MySQL: {erro}")
        return None

def close_connection(conexao, cursor=None):
    if cursor:
        cursor.close()
    if conexao and conexao.is_connected():
        conexao.close()

def get_mysql_error():
    return mysql.connector.Error