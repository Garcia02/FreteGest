"""
Arquivo: database_manager.py
Descrição: Este arquivo contém a classe DatabaseManager, que atua como uma camada de abstração para operações de banco de dados no sistema FreteGest.

Funcionalidades principais:
1. Gerenciar conexões com o banco de dados
2. Executar operações de CRUD (Create, Read, Update, Delete) para usuários
3. Lidar com erros de banco de dados e logging

O que este arquivo faz:
- Fornece métodos para buscar, salvar e atualizar informações de usuários no banco de dados
- Encapsula a lógica de acesso ao banco de dados, separando-a da lógica de negócios
- Lida com erros de banco de dados e registra logs para facilitar a depuração

Possíveis melhorias futuras:
1. Implementar um sistema de cache para melhorar o desempenho de consultas frequentes
2. Adicionar suporte para transações de banco de dados para operações complexas
3. Implementar métodos para outras entidades do sistema além de usuários
4. Adicionar suporte para migrações de banco de dados
5. Implementar um sistema de pooling de conexões para melhor gerenciamento de recursos

Observações adicionais:
- A classe utiliza o módulo 'database' para operações de baixo nível, o que pode ser expandido ou substituído conforme necessário
- Considerar a implementação de um ORM (Object-Relational Mapping) para um mapeamento mais robusto entre objetos e o banco de dados
- A segurança poderia ser melhorada com a implementação de prepared statements para todas as queries
- Adicionar mais métodos de consulta específicos conforme as necessidades do sistema crescem
"""

import logging
from BaseDados import database

class DatabaseManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_user(self, userID):
        query = "SELECT * FROM users WHERE userID = %s"
        try:
            result = database.execute_query(query, (userID,), fetch=True)
            if result:
                return {
                    'userID': result[0][0],
                    'apelido': result[0][1],
                    'nome': result[0][2],
                    'email': result[0][3],
                    'senha_hash': result[0][4],
                    'data_cadastro': result[0][5],
                }
            return None
        except database.get_mysql_error() as err:
            self.logger.error(f"Erro ao buscar usuário: {err}")
            return None

    def save_user(self, user_data):
        query = """
        INSERT INTO users (userID, apelido, nome, email, senha, data_cadastro) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            database.execute_query(query, tuple(user_data.values()))
            return True
        except database.get_mysql_error() as err:
            self.logger.error(f"Erro ao salvar usuário: {err}")
            return False

    def update_user(self, user_data):
        if 'senha_hash' in user_data:
            query = """
            UPDATE users SET apelido = %s, nome = %s, email = %s, senha = %s 
            WHERE userID = %s
            """
            values = (user_data['apelido'], user_data['nome'], user_data['email'], user_data['senha_hash'], user_data['userID'])
        else:
            query = """
            UPDATE users SET apelido = %s, nome = %s, email = %s 
            WHERE userID = %s
            """
            values = (user_data['apelido'], user_data['nome'], user_data['email'], user_data['userID'])
        
        try:
            database.execute_query(query, values)
            return True
        except database.get_mysql_error() as err:
            self.logger.error(f"Erro ao atualizar usuário: {err}")
            return False