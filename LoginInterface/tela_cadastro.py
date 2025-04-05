"""
Arquivo: tela_cadastro.py
Descrição: Este arquivo contém a classe TelaCadastro, responsável por criar e gerenciar a interface de cadastro de novos usuários no sistema FreteGest.

Funcionalidades principais:
1. Criar a interface gráfica da tela de cadastro
2. Coletar e validar os dados de entrada do novo usuário
3. Salvar os dados do novo usuário no banco de dados

O que este arquivo faz:
- Define a aparência e o layout da tela de cadastro
- Gerencia a entrada de dados do usuário (nome, apelido, email, UserID, senha)
- Realiza validações dos campos de entrada (formato de email, força da senha, etc.)
- Interage com o DatabaseManager para salvar os dados do novo usuário
- Lida com mensagens de erro e sucesso durante o processo de cadastro

Possíveis melhorias futuras:
1. Implementar verificação de email (envio de link de confirmação)
2. Adicionar opção de cadastro com redes sociais
3. Implementar um sistema de força de senha mais robusto com feedback visual
4. Adicionar campos adicionais relevantes para o negócio (como tipo de usuário, empresa, etc.)
5. Implementar validação em tempo real dos campos (como disponibilidade de UserID)

Observações adicionais:
- A classe utiliza o bcrypt para hash seguro de senhas antes de armazená-las
- Há uma validação básica de formato de email e força de senha
- O UserID é pré-preenchido com o ID do sistema, mas isso pode ser reconsiderado por questões de segurança
- A interface poderia se beneficiar de tooltips ou informações adicionais para ajudar o usuário durante o cadastro
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re
import bcrypt
from .database_manager import DatabaseManager

class TelaCadastro:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.db_manager = DatabaseManager()
        self.criar_tela_cadastro()

    def criar_tela_cadastro(self):
        self.app.limpar_tela()

        largura_janela = 320
        altura_janela = 550
        self.app.centralizar_janela(largura_janela, altura_janela)

        self.frame_cima = tk.Frame(self.master, width=largura_janela-10, height=80, bg='darkgray')
        self.frame_cima.pack_propagate(False)
        self.frame_cima.pack()

        tk.Label(self.frame_cima, text="FRETGEST", bg='darkgray', fg='black', font=('Arial Black', 18, 'bold')).pack(pady=(10, 0))
        tk.Label(self.frame_cima, text="Sistema de Gestão de Custos de Transporte", bg='darkgray', fg='black', font=('Arial', 10)).pack(pady=(0, 10))

        self.frame_baixo = tk.Frame(self.master, width=largura_janela-30, height=altura_janela-85, bg='lightgray')
        self.frame_baixo.pack_propagate(False)
        self.frame_baixo.pack()

        tk.Label(self.frame_baixo, text='Cadastro', bg='lightgray', font=('Arial', 20)).pack(pady=(0, 10))

        campos = [
            ('Nome*', 'entry_nome'),
            ('Apelido*', 'entry_apelido'),
            ('E-mail*', 'entry_email'),
            ('UserID*', 'entry_userID'),
            ('Senha*', 'entry_senha'),
            ('Confirmar senha*', 'entry_senhaConfirm')
        ]

        for label, attr in campos:
            tk.Label(self.frame_baixo, text=label, bg='lightgray', font=('Arial', 12), anchor='w').pack(fill='x', padx=10, pady=(5, 0))
            setattr(self, attr, tk.Entry(self.frame_baixo))
            getattr(self, attr).pack(fill='x', padx=10, pady=(0, 5))

        self.entry_userID.insert(0, self.app.system_userID)

        frame_botoes = tk.Frame(self.frame_baixo, bg='lightgray')
        frame_botoes.pack(side='bottom', pady=10)

        tk.Button(frame_botoes, text="Salvar", command=self.salvar_cadastro, font=('Arial', 12, 'bold'), bg='#607D8B', fg='white', width=10, height=1).pack(side='left', padx=(0, 10))
        tk.Button(frame_botoes, text="Voltar", command=self.app.abrir_tela_login, font=('Arial', 12, 'bold'), bg='#BDBDBD', fg='black', width=10, height=1).pack(side='left')

    def salvar_cadastro(self):
        nome = self.entry_nome.get()
        apelido = self.entry_apelido.get()
        email = self.entry_email.get()
        userID = self.entry_userID.get()
        senha = self.entry_senha.get()
        senha_confirm = self.entry_senhaConfirm.get()

        if not nome or not apelido or not email or not userID or not senha:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        if not self.validar_senha(senha):
            messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres, incluindo letras e números!")
            return

        if senha != senha_confirm:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        senha_hash = self.hash_senha(senha)

        user_data = {
            'userID': userID,
            'apelido': apelido,
            'nome': nome,
            'email': email,
            'senha_hash': senha_hash,
            'data_cadastro': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if self.db_manager.save_user(user_data):
            messagebox.showinfo("Sucesso", "Usuário salvo com sucesso!")
            self.app.user_data = self.db_manager.get_user(userID)
            self.app.criar_tela_login()
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao salvar os dados. Por favor, tente novamente mais tarde.")

    @staticmethod
    def validar_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validar_senha(senha):
        return len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isalpha() for c in senha)

    @staticmethod
    def hash_senha(senha):
        return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())