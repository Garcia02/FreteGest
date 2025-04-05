"""
Arquivo: tela_login.py
Descrição: Este arquivo contém a classe TelaLogin, responsável por criar e gerenciar a interface de login do sistema FreteGest.

Funcionalidades principais:
1. Criar a interface gráfica da tela de login
2. Gerenciar o processo de autenticação do usuário
3. Redirecionar para a tela de cadastro, se necessário

O que este arquivo faz:
- Define a aparência e o layout da tela de login
- Gerencia a entrada de dados do usuário (UserID e senha)
- Realiza a validação básica dos campos de entrada
- Interage com o DatabaseManager para verificar as credenciais do usuário
- Lida com mensagens de erro e sucesso durante o processo de login

Possíveis melhorias futuras:
1. Implementar um sistema de recuperação de senha
2. Adicionar opção de "Lembrar-me" para manter o usuário logado
3. Implementar autenticação de dois fatores para maior segurança
4. Adicionar suporte para login com redes sociais ou outros métodos de autenticação
5. Melhorar a acessibilidade da interface, adicionando suporte para leitores de tela

Observações adicionais:
- A classe utiliza o bcrypt para verificação segura de senhas
- O design da interface segue um padrão consistente com outras telas do sistema
- O código poderia beneficiar-se de uma maior modularização, separando a lógica de UI da lógica de negócios
"""

import os
import logging
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, PhotoImage
import bcrypt
from .database_manager import DatabaseManager

# Configuração do logging
logging.basicConfig(level=logging.ERROR, filename='fretgest.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Constantes
DARK_GRAY = 'darkgray'
LIGHT_GRAY = 'lightgray'
TITLE_FONT = ('Arial Black', 18, 'bold')
SUBTITLE_FONT = ('Arial', 10)
LABEL_FONT = ('Arial', 12)
BUTTON_FONT = ('Arial', 12, 'bold')

class TelaLogin:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.db_manager = DatabaseManager()
        self.system_userID = os.path.join(os.path.expanduser("~"), "Downloads").split(os.sep)[2]
        self.user_data = self.db_manager.get_user(self.system_userID)
        self.criar_tela_login()

    def criar_tela_login(self):
        self.app.limpar_tela()

        largura_janela = 320
        altura_janela = 335
        self.app.centralizar_janela(largura_janela, altura_janela)

        self.frame_cima = tk.Frame(self.master, width=largura_janela-10, height=80, bg=DARK_GRAY)
        self.frame_cima.pack_propagate(False)
        self.frame_cima.pack()

        tk.Label(self.frame_cima, text="FRETGEST", bg=DARK_GRAY, fg='black', font=TITLE_FONT).pack(pady=(10, 0))
        tk.Label(self.frame_cima, text="Sistema de Gestão de Custos de Transporte", bg=DARK_GRAY, fg='black', font=SUBTITLE_FONT).pack(pady=(0, 10))

        self.frame_baixo = tk.Frame(self.master, width=largura_janela - 30, height=altura_janela-85, bg=LIGHT_GRAY)
        self.frame_baixo.pack_propagate(False)
        self.frame_baixo.pack()

        tk.Label(self.frame_baixo, text='Login', bg=LIGHT_GRAY, font=('Arial', 20)).pack(pady=(0, 10))

        tk.Label(self.frame_baixo, text='UserID*', bg=LIGHT_GRAY, font=LABEL_FONT, anchor='w').pack(fill='x', padx=10, pady=(5, 0))
        self.entry_userID = tk.Entry(self.frame_baixo)
        self.entry_userID.pack(fill='x', padx=10, pady=(0, 5))
        self.entry_userID.insert(0, self.system_userID)

        tk.Label(self.frame_baixo, text='Senha*', bg=LIGHT_GRAY, font=LABEL_FONT, anchor='w').pack(fill='x', padx=10, pady=(30, 0))
        self.entry_senha = tk.Entry(self.frame_baixo, show='*')
        self.entry_senha.pack(fill='x', padx=10, pady=(0, 5))

        frame_botoes = tk.Frame(self.frame_baixo, bg=LIGHT_GRAY)
        frame_botoes.pack(pady=(30, 0))

        tk.Button(frame_botoes, text="Entrar", command=self.fazer_login, font=BUTTON_FONT, bg='#607D8B', fg='white', width=10, height=1).pack(side='left', padx=(0, 10))
        tk.Button(frame_botoes, text="Cadastro", command=self.app.abrir_tela_cadastro, font=BUTTON_FONT, bg='#BDBDBD', fg='black', width=10, height=1).pack(side='left')

    def fazer_login(self):
        userID = self.entry_userID.get()
        senha = self.entry_senha.get()

        if not userID or not senha:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        user = self.db_manager.get_user(userID)
        if user and self.verificar_senha(senha, user['senha_hash']):
            self.app.user_data = user
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.app.abrir_tela_principal()
        else:
            messagebox.showerror("Erro", "UserID ou senha incorretos!")

    @staticmethod
    def verificar_senha(senha, hash_armazenado):
        return bcrypt.checkpw(senha.encode('utf-8'), hash_armazenado.encode('utf-8'))