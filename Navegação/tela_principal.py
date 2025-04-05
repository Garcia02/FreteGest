"""
Arquivo: tela_principal.py
Descrição: Este arquivo contém a classe TelaPrincipal, que cria e gerencia a interface principal do sistema FreteGest após o login do usuário.

Funcionalidades principais:
1. Criar a interface gráfica da tela principal
2. Fornecer acesso às principais funcionalidades do sistema
3. Gerenciar a navegação para outras telas (como edição de perfil)

O que este arquivo faz:
- Define a aparência e o layout da tela principal
- Exibe uma mensagem de boas-vindas personalizada para o usuário
- Fornece botões para acessar diferentes funcionalidades do sistema
- Inclui opções para editar perfil e fazer logout

Possíveis melhorias futuras:
1. Implementar um dashboard com informações relevantes para o usuário
2. Adicionar um menu lateral ou superior para melhor organização das funcionalidades
3. Incluir notificações ou alertas importantes para o usuário
4. Personalizar a interface com base no tipo de usuário ou permissões
5. Adicionar atalhos de teclado para navegação rápida

Observações adicionais:
- As funcionalidades 1 e 2 são apenas placeholders e precisam ser implementadas
- A tela principal poderia se beneficiar de mais informações e funcionalidades relevantes para o negócio
- Considerar a adição de um sistema de ajuda ou tour guiado para novos usuários
"""

import tkinter as tk
from tkinter import messagebox

class TelaPrincipal:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.criar_tela_principal()

    def criar_tela_principal(self):
        self.app.limpar_tela()

        largura_janela = 500
        altura_janela = 400
        self.app.centralizar_janela(largura_janela, altura_janela)

        self.frame_principal = tk.Frame(self.master, width=largura_janela, height=altura_janela, bg='lightgray')
        self.frame_principal.pack_propagate(False)
        self.frame_principal.pack()

        tk.Label(self.frame_principal, text=f"Bem-vindo, {self.app.user_data['apelido']}!", bg='lightgray', font=('Arial', 20)).pack(pady=(20, 10))

        tk.Button(self.frame_principal, text="Editar Perfil", command=self.app.abrir_tela_editar_perfil, font=('Arial', 12)).pack(pady=10)
        tk.Button(self.frame_principal, text="Funcionalidade 1", command=self.funcionalidade_1, font=('Arial', 12)).pack(pady=10)
        tk.Button(self.frame_principal, text="Funcionalidade 2", command=self.funcionalidade_2, font=('Arial', 12)).pack(pady=10)
        tk.Button(self.frame_principal, text="Sair", command=self.app.fazer_logout, font=('Arial', 12)).pack(pady=10)

    def funcionalidade_1(self):
        print("Funcionalidade 1 foi chamada!")
        messagebox.showinfo("Funcionalidade 1", "Esta funcionalidade está em desenvolvimento.")

    def funcionalidade_2(self):
        print("Funcionalidade 2 foi chamada!")
        messagebox.showinfo("Funcionalidade 2", "Esta funcionalidade está em desenvolvimento.")