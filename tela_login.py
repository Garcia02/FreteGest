import os
import logging
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, PhotoImage
import re
import bcrypt
import database

# Configuração do logging
logging.basicConfig(level=logging.ERROR, filename='fretgest.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Constantes
DARK_GRAY = 'darkgray'
LIGHT_GRAY = 'lightgray'
TITLE_FONT = ('Arial Black', 18, 'bold')
SUBTITLE_FONT = ('Arial', 10)
LABEL_FONT = ('Arial', 12)
BUTTON_FONT = ('Arial', 12, 'bold')

class FreteGestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("FreteGest")
        self.master.resizable(width=False, height=False)

        self.icon = PhotoImage(file=os.path.join(os.getcwd(), 'FreteGest', 'caminhao.png'))
        self.master.iconphoto(False, self.icon)

        # Capturar o userID do sistema
        self.system_userID = os.path.join(os.path.expanduser("~"), "Downloads").split(os.sep)[2]

        # Obter dados do usuário
        self.user_data = self.get_user()

        # Decidir qual tela abrir
        if self.user_data:
            self.criar_tela_login()
        else:
            self.abrir_tela_cadastro()

    def funcionalidade_1(self):
        # Aqui você pode adicionar o que esta funcionalidade deve fazer
        print("Funcionalidade 1 foi chamada!")
        messagebox.showinfo("Funcionalidade 1", "Esta funcionalidade está em desenvolvimento.")

    def funcionalidade_2(self):
        # Aqui você pode adicionar o que esta funcionalidade deve fazer
        print("Funcionalidade 2 foi chamada!")
        messagebox.showinfo("Funcionalidade 1", "Esta funcionalidade está em desenvolvimento.")

    def get_user(self):
        userID = os.path.join(os.path.expanduser("~"), "Downloads").split(os.sep)[2]

        conexao = database.get_connection()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute("SELECT * FROM users WHERE userID = %s", (userID,))
                    registro = cursor.fetchone()

                if registro:
                    # Retorne os dados do usuário como um dicionário
                    return {
                        'userID': userID,
                        'apelido': registro[1],
                        'nome': registro[2],
                        'email': registro[3],
                        'senha_hash': registro[4],
                        'data_cadastro': registro[5],
                    }
                else:
                    # Retorne None se o usuário não for encontrado
                    return None
            except database.get_mysql_error() as err:
                logging.error(f"Erro ao acessar o banco de dados: {err}")
                messagebox.showerror("Erro", "Ocorreu um erro ao acessar o banco de dados. Por favor, tente novamente mais tarde.")
                return None
            finally:
                database.close_connection(conexao)
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return None

    def criar_tela_login(self):
        self.limpar_tela()

        largura_janela = 320
        altura_janela = 335
        self.centralizar_janela(largura_janela, altura_janela)

        self.frame_cima = tk.Frame(self.master, width=largura_janela-10, height=80, bg='darkgray')
        self.frame_cima.pack_propagate(False)
        self.frame_cima.pack()

        tk.Label(self.frame_cima, text="FRETGEST", bg='darkgray', fg='black', font=('Arial Black', 18, 'bold')).pack(pady=(10, 0))
        tk.Label(self.frame_cima, text="Sistema de Gestão de Custos de Transporte", bg='darkgray', fg='black', font=('Arial', 10)).pack(pady=(0, 10))

        self.frame_baixo = tk.Frame(self.master, width=largura_janela - 30, height=altura_janela-85, bg='lightgray')
        self.frame_baixo.pack_propagate(False)
        self.frame_baixo.pack()

        tk.Label(self.frame_baixo, text='Login', bg='lightgray', font=('Arial', 20)).pack(pady=(0, 10))

        tk.Label(self.frame_baixo, text='UserID*', bg='lightgray', font=('Arial', 12), anchor='w').pack(fill='x', padx=10, pady=(5, 0))
        self.entry_userID = tk.Entry(self.frame_baixo)
        self.entry_userID.pack(fill='x', padx=10, pady=(0, 5))

        # Preencher automaticamente o campo UserID com o ID do sistema
        system_userID = os.path.join(os.path.expanduser("~"), "Downloads").split(os.sep)[2]
        self.entry_userID.insert(0, system_userID)

        tk.Label(self.frame_baixo, text='Senha*', bg='lightgray', font=('Arial', 12), anchor='w').pack(fill='x', padx=10, pady=(30, 0))
        self.entry_senha = tk.Entry(self.frame_baixo, show='*')
        self.entry_senha.pack(fill='x', padx=10, pady=(0, 5))

        frame_botoes = tk.Frame(self.frame_baixo, bg='lightgray')
        frame_botoes.pack(pady=(30, 0))

        tk.Button(frame_botoes, text="Entrar", command=self.fazer_login, font=('Arial', 12, 'bold'), bg='#607D8B', fg='white', width=10, height=1).pack(side='left', padx=(0, 10))
        tk.Button(frame_botoes, text="Cadastro", command=self.abrir_tela_cadastro, font=('Arial', 12, 'bold'), bg='#BDBDBD', fg='black', width=10, height=1).pack(side='left')

    def abrir_tela_cadastro(self):
        self.limpar_tela()

        largura_janela = 320
        altura_janela = 550
        self.centralizar_janela(largura_janela, altura_janela)

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

        # Preencher automaticamente o campo UserID
        self.entry_userID.insert(0, self.system_userID)

        frame_botoes = tk.Frame(self.frame_baixo, bg='lightgray')
        frame_botoes.pack(side='bottom', pady=10)

        tk.Button(frame_botoes, text="Salvar", command=self.salvar_cadastro, font=('Arial', 12, 'bold'), bg='#607D8B', fg='white', width=10, height=1).pack(side='left', padx=(0, 10))
        tk.Button(frame_botoes, text="Voltar", command=self.criar_tela_login, font=('Arial', 12, 'bold'), bg='#BDBDBD', fg='black', width=10, height=1).pack(side='left')

    def fazer_login(self):
        userID = self.entry_userID.get()
        senha = self.entry_senha.get()

        if not userID or not senha:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        conexao = database.get_connection()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute("SELECT * FROM users WHERE userID = %s", (userID,))
                    user = cursor.fetchone()

                if user and self.verificar_senha(senha, user[4]):  # Assumindo que a senha hash está na posição 4
                    self.user_data = {
                        'userID': user[0],
                        'apelido': user[1],
                        'nome': user[2],
                        'email': user[3],
                        'senha_hash': user[4],
                        'data_cadastro': user[5]
                    }
                    messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                    self.abrir_tela_principal()
                else:
                    messagebox.showerror("Erro", "UserID ou senha incorretos!")
            except database.get_mysql_error() as err:
                logging.error(f"Erro ao fazer login: {err}")
                messagebox.showerror("Erro", "Ocorreu um erro ao fazer login. Por favor, tente novamente mais tarde.")
            finally:
                database.close_connection(conexao)
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

    def abrir_tela_principal(self):
        self.limpar_tela()

        largura_janela = 500
        altura_janela = 400
        self.centralizar_janela(largura_janela, altura_janela)

        self.frame_principal = tk.Frame(self.master, width=largura_janela, height=altura_janela, bg='lightgray')
        self.frame_principal.pack_propagate(False)
        self.frame_principal.pack()

        tk.Label(self.frame_principal, text=f"Bem-vindo, {self.user_data['apelido']}!", bg='lightgray', font=('Arial', 20)).pack(pady=(20, 10))

        tk.Button(self.frame_principal, text="Editar Perfil", command=self.abrir_tela_editar_perfil, font=('Arial', 12)).pack(pady=10)
        tk.Button(self.frame_principal, text="Funcionalidade 1", command=self.funcionalidade_1, font=('Arial', 12)).pack(pady=10)
        tk.Button(self.frame_principal, text="Funcionalidade 2", command=self.funcionalidade_2, font=('Arial', 12)).pack(pady=10)
        tk.Button(self.frame_principal, text="Sair", command=self.fazer_logout, font=('Arial', 12)).pack(pady=10)

    def abrir_tela_editar_perfil(self):
        self.limpar_tela()

        largura_janela = 320
        altura_janela = 550
        self.centralizar_janela(largura_janela, altura_janela)

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

        # Preencher campos com dados atuais
        self.entry_nome.insert(0, self.user_data['nome'])
        self.entry_apelido.insert(0, self.user_data['apelido'])
        self.entry_email.insert(0, self.user_data['email'])

        tk.Button(self.frame_editar, text="Salvar Alterações", command=self.salvar_edicao_perfil, font=('Arial', 12, 'bold'), bg='#607D8B', fg='white').pack(pady=10)
        tk.Button(self.frame_editar, text="Voltar", command=self.abrir_tela_principal, font=('Arial', 12)).pack(pady=10)

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

        conexao = database.get_connection()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    if self.user_data:
                        query = "UPDATE users SET apelido = %s, nome = %s, email = %s, senha = %s WHERE userID = %s"
                        values = (apelido, nome, email, senha_hash, userID)
                    else:
                        query = "INSERT INTO users (userID, apelido, nome, email, senha, data_cadastro) VALUES (%s, %s, %s, %s, %s, %s)"
                        values = (userID, apelido, nome, email, senha_hash, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    
                    cursor.execute(query, values)
                    conexao.commit()
                
                messagebox.showinfo("Sucesso", "Usuário salvo com sucesso!")
                self.user_data = self.get_user()
                self.criar_tela_login()
            except database.get_mysql_error() as err:
                logging.error(f"Erro ao salvar os dados: {err}")
                messagebox.showerror("Erro", "Ocorreu um erro ao salvar os dados. Por favor, tente novamente mais tarde.")
            finally:
                database.close_connection(conexao)
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

    def salvar_edicao_perfil(self):
        nome = self.entry_nome.get()
        apelido = self.entry_apelido.get()
        email = self.entry_email.get()
        nova_senha = self.entry_nova_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()

        if not nome or not apelido or not email:
            messagebox.showerror("Erro", "Nome, Apelido e E-mail são obrigatórios!")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        if nova_senha:
            if not self.validar_senha(nova_senha):
                messagebox.showerror("Erro", "A nova senha deve ter pelo menos 8 caracteres, incluindo letras e números!")
                return
            if nova_senha != confirmar_senha:
                messagebox.showerror("Erro", "As senhas não coincidem!")
                return

        conexao = database.get_connection()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    if nova_senha:
                        senha_hash = self.hash_senha(nova_senha)
                        query = "UPDATE users SET apelido = %s, nome = %s, email = %s, senha = %s WHERE userID = %s"
                        values = (apelido, nome, email, senha_hash, self.user_data['userID'])
                    else:
                        query = "UPDATE users SET apelido = %s, nome = %s, email = %s WHERE userID = %s"
                        values = (apelido, nome, email, self.user_data['userID'])
                    
                    cursor.execute(query, values)
                    conexao.commit()
                
                messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso!")
                self.user_data = self.get_user()  # Atualiza os dados do usuário
                self.abrir_tela_principal()
            except database.get_mysql_error() as err:
                logging.error(f"Erro ao atualizar perfil: {err}")
                messagebox.showerror("Erro", "Ocorreu um erro ao atualizar o perfil. Por favor, tente novamente mais tarde.")
            finally:
                database.close_connection(conexao)
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

    def fazer_logout(self):
        self.user_data = None
        messagebox.showinfo("Logout", "Você saiu do sistema.")
        self.criar_tela_login()

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def centralizar_janela(self, largura, altura):
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)
        self.master.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

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

    @staticmethod
    def verificar_senha(senha, hash_armazenado):
        return bcrypt.checkpw(senha.encode('utf-8'), hash_armazenado.encode('utf-8'))

if __name__ == "__main__":
    root = tk.Tk()
    app = FreteGestApp(root)
    root.mainloop()