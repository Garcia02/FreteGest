import mysql.connector
from mysql.connector import pooling
import logging
import configparser
import os

# Configuração do logging
logging.basicConfig(level=logging.ERROR, filename='fretgest_database.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Leitura do arquivo de configuração
config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

if not os.path.exists(config_file):
    raise FileNotFoundError(f"O arquivo de configuração 'config.ini' não foi encontrado em {os.path.dirname(__file__)}")

config.read(config_file)

# Configurações do banco de dados
DB_CONFIG = {
    'host': config['DATABASE']['host'],
    'user': config['DATABASE']['user'],
    #'password': config['DATABASE']['password'],
    'database': config['DATABASE']['database'],
    'port': config['DATABASE'].getint('port', 3306)  # Porta padrão 3306 se não especificada
}

# Pool de conexões
connection_pool = None

def initialize_pool():
    """Inicializa o pool de conexões."""
    global connection_pool
    try:
        connection_pool = pooling.MySQLConnectionPool(
            pool_name="fretgest_pool",
            pool_size=5,
            **DB_CONFIG
        )
        logging.info("Pool de conexões inicializado com sucesso.")
    except mysql.connector.Error as erro:
        logging.error(f"Erro ao criar pool de conexões: {erro}")
        raise

def get_connection():
    """Obtém uma conexão do pool."""
    if connection_pool is None:
        initialize_pool()
    try:
        return connection_pool.get_connection()
    except mysql.connector.Error as erro:
        logging.error(f"Erro ao obter conexão do pool: {erro}")
        return None

def close_connection(conexao, cursor=None):
    """Fecha a conexão e o cursor, se fornecido."""
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()

def execute_query(query, params=None, fetch=False):
    """
    Executa uma query SQL.
    
    :param query: A query SQL a ser executada.
    :param params: Parâmetros para a query (opcional).
    :param fetch: Se True, retorna os resultados da query.
    :return: Resultados da query se fetch=True, caso contrário None.
    """
    conexao = get_connection()
    if not conexao:
        return None

    try:
        with conexao.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            if fetch:
                return cursor.fetchall()
            else:
                conexao.commit()
                return cursor.rowcount
    except mysql.connector.Error as erro:
        logging.error(f"Erro ao executar query: {erro}")
        conexao.rollback()
        raise
    finally:
        close_connection(conexao)

def get_mysql_error():
    """Retorna a classe de erro do MySQL."""
    return mysql.connector.Error

# Funções específicas para operações comuns

def get_user_by_id(user_id):
    """Busca um usuário pelo ID."""
    query = "SELECT * FROM users WHERE userID = %s"
    results = execute_query(query, (user_id,), fetch=True)
    return results[0] if results else None

def create_user(user_data):
    """Cria um novo usuário."""
    query = """
    INSERT INTO users (userID, apelido, nome, email, senha, data_cadastro) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_query(query, tuple(user_data.values()))

def update_user(user_data):
    """Atualiza os dados de um usuário existente."""
    query = """
    UPDATE users SET apelido = %s, nome = %s, email = %s, senha = %s 
    WHERE userID = %s
    """
    return execute_query(query, (
        user_data['apelido'], 
        user_data['nome'], 
        user_data['email'], 
        user_data['senha'], 
        user_data['userID']
    ))

# Função para inicializar o banco de dados (criar tabelas, etc.)
def initialize_database():
    """Inicializa o banco de dados criando as tabelas necessárias."""
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        userID VARCHAR(50) PRIMARY KEY,
        apelido VARCHAR(50) NOT NULL,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        senha VARCHAR(255) NOT NULL,
        data_cadastro DATETIME NOT NULL
    )
    """
    execute_query(create_users_table)
    logging.info("Banco de dados inicializado com sucesso.")

# Inicialização do pool de conexões e do banco de dados
try:
    initialize_pool()
    initialize_database()
except Exception as e:
    logging.critical(f"Falha na inicialização do banco de dados: {e}")
    raise

if __name__ == "__main__":
    print("Módulo de banco de dados carregado com sucesso.")
    # Aqui você pode adicionar testes ou verificações adicionais