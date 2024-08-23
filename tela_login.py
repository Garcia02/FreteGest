from tkinter import *
from tkinter import PhotoImage
import database  # Importe o arquivo de conexão
from tkinter import messagebox

# Função para centralizar a janela
def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

def criar_tela_login():
    global tela_Login, frame_cima, frame_baixo, texto_login, texto_usuario, entry_usuario, texto_senha, entry_senha, frame_botoes, botao_login, botao_cadastro

    # Criando janela
    tela_Login = Tk()
    tela_Login.title("")
    tela_Login.resizable(width=False, height=False)
    icon = PhotoImage(file='caminhao.png')
    tela_Login.iconphoto(False, icon)

    # Definindo tamanho da janela
    largura_janela = 320
    altura_janela = 335

    # Centralizando a janela
    centralizar_janela(tela_Login, largura_janela, altura_janela)

    # Parte superior em cinza escuro (titulo e subtitulo)
    frame_cima = Frame(tela_Login, width=310, height=80, bg='darkgray')  
    frame_cima.pack_propagate(False)
    frame_cima.pack()

    # Adicionando título e subtítulo ao frame superior
    texto_titulo = Label(frame_cima, text="FRETGEST", 
                         bg='darkgray', fg='black', font=('Arial Black', 18, 'bold'))
    texto_titulo.pack(pady=(10, 0))

    texto_subTitulo = Label(frame_cima, text="Sistema de Gestão de Custos de Transporte", 
                            bg='darkgray', fg='black', font=('Arial', 10))
    texto_subTitulo.pack(pady=(0, 10))

    # Parte inferior em cinza claro
    frame_baixo = Frame(tela_Login, width=310, height=250, bg='lightgray')
    frame_baixo.pack_propagate(False)
    frame_baixo.pack()

    # Texto Login
    texto_login = Label(frame_baixo, text='Login', 
                        bg='lightgray', font=('Arial', 20))
    texto_login.pack(pady=(0, 10))

    # Texto usuario
    texto_usuario = Label(frame_baixo, text='Usuario*', 
                          bg='lightgray', font=('Arial', 12), anchor='w')
    texto_usuario.pack(fill='x', padx=10, pady=(5, 0))
    # Campo de entrada para usuario
    entry_usuario = Entry(frame_baixo)
    entry_usuario.pack(fill='x', padx=10, pady=(0, 5))

    # Texto senha
    texto_senha = Label(frame_baixo, text='Senha*', 
                        bg='lightgray', font=('Arial', 12), anchor='w')
    texto_senha.pack(fill='x', padx=10, pady=(30, 0))
    # Campo de entrada para senha
    entry_senha = Entry(frame_baixo, show='*')
    entry_senha.pack(fill='x', padx=10, pady=(0, 5))

    # Frame para os botões
    frame_botoes = Frame(frame_baixo, bg='lightgray')
    frame_botoes.pack(pady=(30, 0))

    # Botão de Login
    botao_login = Button(frame_botoes, text="Entrar", command=abrir_Login, 
                     font=('Arial', 12, 'bold'), bg='#607D8B', fg='white',
                     width=10, height=1)
    botao_login.pack(side='left', padx=(0, 10))

    # Botão para chamar a janela de cadastro
    botao_cadastro = Button(frame_botoes, text="Cadastro", command=abrir_tela_cadastro, 
                     font=('Arial', 12, 'bold'), bg='#BDBDBD', fg='black',
                     width=10, height=1)
    botao_cadastro.pack(side='left')

def abrir_tela_cadastro():
    global entry_nome, entry_UserID, entry_senhaConfirm

    if botao_cadastro['text'] != 'Cadastrar':
        # Definindo tamanho da janela
        largura_janela = 320
        altura_janela = 450

        # Centralizando a janela
        centralizar_janela(tela_Login, largura_janela, altura_janela)

        #ajusta o tamanho do frame principal
        frame_baixo.config(height=365)

        #remove o campo de Usuario
        texto_usuario.pack_forget()
        entry_usuario.pack_forget()

        # cria um novo campo para nome
        texto_nome = Label(frame_baixo, text='Nome*', 
                            bg='lightgray', font=('Arial', 12), anchor='w')
        texto_nome.pack(fill='x', padx=10, pady=(0, 0))
        # Campo de entrada para nome
        entry_nome = Entry(frame_baixo)
        entry_nome.pack(fill='x', padx=10, pady=(0, ))

        # cria um novo campo para UserID
        texto_UserID = Label(frame_baixo, text='UserID*', 
                            bg='lightgray', font=('Arial', 12), anchor='w')
        texto_UserID.pack(fill='x', padx=10, pady=(0, 0))
        # Campo de entrada para UserID
        entry_UserID = Entry(frame_baixo)
        entry_UserID.pack(fill='x', padx=10, pady=(0, 0))

        # Reposiciona o campo de senha
        texto_senha.pack_forget()
        entry_senha.pack_forget()
        texto_senha.pack(fill='x', padx=10, pady=(40, 0))
        entry_senha.pack(fill='x', padx=10, pady=(0, 5))

        # cria um novo campo para confimação de senha
        texto_senhaConfirm = Label(frame_baixo, text='Confirmar senha*', 
                            bg='lightgray', font=('Arial', 12), anchor='w')
        texto_senhaConfirm.pack(fill='x', padx=10, pady=(0, 0))
        # Campo de entrada para senha
        entry_senhaConfirm = Entry(frame_baixo,show='*')
        entry_senhaConfirm.pack(fill='x', padx=10, pady=(0, 0))

        #renomeia o botão cadastro e Reposicionar o frame
        frame_botoes.pack(side='bottom', pady=10)
        botao_cadastro.config(text="Cadastrar", bg="#607D8B", fg='white')
        botao_login.config(text="Login", bg="#BDBDBD", fg='black')

        texto_login['text'] = 'Cadastrar'

    else:
        # Obter os valores dos campos de entrada
        nome = entry_nome.get()
        userID = entry_UserID.get()
        senha = entry_senha.get()
        senha_confirm = entry_senhaConfirm.get()

        # Validar os dados
        if not nome or not userID or not senha or not senha_confirm:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        if senha != senha_confirm:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return
        
                # Salvar os dados no MySQL
        conexao = database.get_connection()
        if conexao:
            try:
                cursor = conexao.cursor()
                
                # Verificar se o userID já existe
                cursor.execute("SELECT * FROM usuarios WHERE userID = %s", (userID,))
                if cursor.fetchone():
                    messagebox.showerror("Erro", "Este UserID já está em uso!")
                    return

                # Inserir novo usuário
                query = "INSERT INTO usuarios (nome, userID, senha) VALUES (%s, %s, %s)"
                values = (nome, userID, senha)
                
                cursor.execute(query, values)
                conexao.commit()
                
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                
                # Limpar os campos após o cadastro
                entry_nome.delete(0, END)
                entry_UserID.delete(0, END)
                entry_senha.delete(0, END)
                entry_senhaConfirm.delete(0, END)

            except database.get_mysql_error()  as err:
                messagebox.showerror("Erro", f"Ocorreu um erro ao salvar os dados: {err}")
            finally:
                database.close_connection(conexao, cursor)

        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

def abrir_Login():
    if botao_login['text'] == 'Entrar':
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if not usuario or not senha:
            messagebox.showerror('Erro', 'Por favor preencha todos os campos!')
            return
        
        conexao = database.get_connection()
        if conexao:
            try:
                cursor = conexao.cursor()
                    
                # Verificar as credenciais do usuário
                query = "SELECT * FROM usuarios WHERE userID = %s AND senha = %s"
                cursor.execute(query, (usuario, senha))
                usuario_info = cursor.fetchone()

                if usuario_info:
                    messagebox.showinfo("Sucesso", f"Olá {usuario_info[1]}, login realizado com sucesso!")
                    tela_Login.destroy()

                else:
                    messagebox.showerror("Erro", "Credenciais inválidas!")

            except database.mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Ocorreu um erro ao verificar as credenciais: {err}")
            finally:
                database.close_connection(conexao, cursor)
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
    else:
        tela_Login.destroy()
        criar_tela_login()

# Iniciar o programa criando a tela de login
criar_tela_login()

# Iniciar o loop principal
tela_Login.mainloop()