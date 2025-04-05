"""
Arquivo: tela_editar_perfil.py
Descrição: Este arquivo contém a classe TelaEditarPerfil, responsável por criar e gerenciar a interface de edição de perfil do usuário no sistema FreteGest.

Funcionalidades principais:
1. Criar a interface gráfica da tela de edição de perfil
2. Carregar e exibir os dados atuais do usuário
3. Permitir a edição dos dados do perfil, incluindo a opção de alterar a senha
4. Salvar as alterações no banco de dados

O que este arquivo faz:
- Define a aparência e o layout da tela de edição de perfil
- Carrega os dados atuais do usuário nos campos de entrada
- Gerencia a entrada de dados do usuário para atualização do perfil
- Realiza validações dos campos alterados (como formato de email e força da nova senha)
- Interage com o DatabaseManager para atualizar os dados do usuário
- Lida com mensagens de erro e sucesso durante o processo de atualização

Possíveis melhorias futuras:
1. Adicionar a opção de upload de foto de perfil
2. Implementar histórico de alterações do perfil
3. Adicionar opção de desativar a conta
4. Incluir configurações de privacidade e notificações
5. Implementar validação em tempo real dos campos alterados

Observações adicionais:
- A alteração de senha é opcional, mas quando realizada, passa por validações de segurança
- Considerar a adição de um botão para reverter alterações não salvas
- A interface poderia se beneficiar de feedback visual mais claro sobre quais campos foram alterados
- Implementar confirmação antes de salvar alterações significativas (como mudança de email)
"""

import tkinter as tk
from tkinter import messagebox
from .database_manager import DatabaseManager

class TelaEditarPerfil:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.db_manager = DatabaseManager()
        self.criar_tela_editar_perfil()

    def criar_tela_editar_perfil(self):
        self.app.limpar_tela()

        largura_janela = 320
        altura_janela = 550
        self.app.centralizar_janela(largura_janela, altura_janela)

        self.frame_editar = tk.Frame(self.master, width=largura_janela, height=altura_janela, bg='lightgray')
        self.frame_editar.pack_propagate(False)
        self.frame_editar.pack()

        tk.Label(self.frame_editar, text='Editar Perfil', bg='lightgray', font=('Arial', 20)).pack(pady=(20, 10))

        campos = [
            ('Nome*', 'entry_nome'),
            ('Apelido*', 'entry_apelido'),
            ('E-mail*', 'entry_email'),
            ('Nova Senha', 'entry_nova_senha'),
            ('Confirmar Nova Senha', 'entry_confirmar_senha')
        ]

        for label, attr in campos:
            tk.Label(self.frame_editar, text=label, bg='lightgray', font=('Arial', 12), anchor='w').pack(fill='x', padx=10, pady=(5, 0))
            setattr(self, attr, tk.Entry(self.frame_editar))
            getattr(self, attr).pack(fill='x', padx=10, pady=(0, 5))

        self.entry_nome.insert(0, self.app.user_data['nome'])
        self.entry_apelido.insert(0, self.app.user_data['apelido'])
        self.entry_email.insert(0, self.app.user_data['email'])

        tk.Button(self.frame_editar, text="Salvar Alterações", command=self.salvar_edicao_perfil, font=('Arial', 12, 'bold'), bg='#607D8B', fg='white').pack(pady=10)
        tk.Button(self.frame_editar, text="Voltar", command=self.app.abrir_tela_principal, font=('Arial', 12)).pack(pady=10)

    def salvar_edicao_perfil(self):
        nome = self.entry_nome.get()
        apelido = self.entry_apelido.get()
        email = self.entry_email.get()
        nova_senha = self.entry_nova_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()

        if not nome or not apelido or not email:
            messagebox.showerror("Erro", "Nome, Apelido e E-mail são obrigatórios!")
            return

        if not self.app.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        if nova_senha:
            if not self.app.validar_senha(nova_senha):
                messagebox.showerror("Erro", "A nova senha deve ter pelo menos 8 caracteres, incluindo letras e números!")
                return
            if nova_senha != confirmar_senha:
                messagebox.showerror("Erro", "As senhas não coincidem!")
                return

        user_data = {
            'userID': self.app.user_data['userID'],
            'apelido': apelido,
            'nome': nome,
            'email': email
        }

        if nova_senha:
            user_data['senha_hash'] = self.app.hash_senha(nova_senha)

        if self.db_manager.update_user(user_data):
            messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso!")
            self.app.user_data = self.db_manager.get_user(self.app.user_data['userID'])
            self.app.abrir_tela_principal()
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao atualizar o perfil. Por favor, tente novamente mais tarde.")