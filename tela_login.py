from tkinter import *
import os
from datetime import datetime
import database  # Importe o arquivo de conexão
from tkinter import messagebox

def get_user () :
    global userID, apelido, nome, email, senha, data_cadastro, registro

    #captura o userID conforme o usuario do sistema
    userID = os.path.join(os.path.expanduser("~"), "Downloads").split(os.sep)[2]
    #userID = "600532560"

    # Verifica e captura os dados no MySQL
    conexao = database.get_connection() 
    
    if conexao: 
        try: 
            cursor = conexao.cursor()
                
            # Verificar se o userID já existe
            cursor.execute("SELECT * FROM users WHERE userID = %s", (userID,))
            registro = cursor.fetchone()
            criar_tela_login()
            
            if registro:
                nome = registro[2]   
                apelido = registro[1] 
                email = registro[3]
                senha = registro[4]
                data_cadastro = registro[5].strftime("%d/%m/%Y")

                entry_userID.insert(0,userID)

            else:

                abrir_tela_cadastro()
                entry_userID.insert(0,userID)

            return
            
        finally:
            database.close_connection(conexao, cursor)

    else:
         messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

# Função para centralizar a janela
def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

def criar_tela_login():
    global tela_Login, frame_cima, frame_baixo, texto_login, texto_userID, entry_userID, texto_senha, entry_senha, frame_botoes, botao_login, botao_cadastro

    # Criando janela
    tela_Login = Tk()
    tela_Login.title("")
    tela_Login.resizable(width=False, height=False)
    icon = PhotoImage(file=os.getcwd()+'\FreteGest\caminhao.png')
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
    frame_baixo = Frame(tela_Login, width=altura_janela-25, height=250, bg='lightgray')
    frame_baixo.pack_propagate(False)
    frame_baixo.pack()

    # Texto Login
    texto_login = Label(frame_baixo, text='Login', 
                        bg='lightgray', font=('Arial', 20))
    texto_login.pack(pady=(0, 10))

    # Texto userID
    texto_userID = Label(frame_baixo, text='UserID*', 
                          bg='lightgray', font=('Arial', 12), anchor='w')
    texto_userID.pack(fill='x', padx=10, pady=(5, 0))
    # Campo de entrada para usuario
    entry_userID = Entry(frame_baixo)
    entry_userID.pack(fill='x', padx=10, pady=(0, 5))

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
    global entry_nome, entry_userID, entry_senhaConfirm,texto_apelido,entry_apelido,texto_email,entry_email,texto_data_cadastro,entry_data_cadastro

    # se o botão não for "cadastrar" ele deve executar funções para inputar dados no banco de dados, se não ele de costruir o painel de Cadastro
    if botao_cadastro['text'] =='Cadastro':
        # Definindo tamanho da janela
        largura_janela = 320
        altura_janela = 550

        # Centralizando a janela
        centralizar_janela(tela_Login, largura_janela, altura_janela)

        #ajusta o tamanho do frame principal
        frame_baixo.config(height=altura_janela-85)

        # cria um novo campo para nome
        texto_nome = Label(frame_baixo, text='Nome*', 
                            bg='lightgray', font=('Arial', 12), anchor='w')
        texto_nome.pack(fill='x', padx=10, pady=(0, 0))
        # Campo de entrada para nome
        entry_nome = Entry(frame_baixo)
        entry_nome.pack(fill='x', padx=10, pady=(0, ))
        entry_nome.insert(0, globals().get("nome", "") )

        # cria um novo campo para apelido
        texto_apelido = Label(frame_baixo, text='Apelido*', 
                            bg='lightgray', font=('Arial', 12), anchor='w')
        texto_apelido.pack(fill='x', padx=10, pady=(0, 0))
        # Campo de entrada para apelido
        entry_apelido = Entry(frame_baixo)
        entry_apelido.pack(fill='x', padx=10, pady=(0, 0))
        entry_apelido.insert(0, globals().get("apelido", "") )

        # cria um novo campo para email
        texto_email = Label(frame_baixo, text='E-mail*', 
                            bg='lightgray', font=('Arial', 12), anchor='w')
        texto_email.pack(fill='x', padx=10, pady=(0, 0))
        # Campo de entrada para email
        entry_email = Entry(frame_baixo)
        entry_email.pack(fill='x', padx=10, pady=(0, 0))
        entry_email.insert(0, globals().get("email", "") )

        # cria um novo campo para data de cadastro
        texto_data_cadastro = Label(frame_baixo, text='Data de cadastro*', 
                            bg='lightgray', font=('Arial', 12), anchor='w')
        texto_data_cadastro.pack(fill='x', padx=10, pady=(0, 0))
        # Campo de entrada para data de cadastro
        entry_data_cadastro = Entry(frame_baixo)
        entry_data_cadastro.pack(fill='x', padx=10, pady=(0, 0))
        entry_data_cadastro.insert(0, globals().get("data_cadastro", "") )

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

        # se entry_userID for diferente de vazio quer dizer que o usuario ja esta cadastrado, 
        # sendo assim mudamos a painel de cadastrar para Cadastro e o botão é renomeado para Editar, 
        # podendo executar a função de editar os dados
        if registro:
            texto_login['text'] = 'Cadastro'
            botao_cadastro.config(text="Editar")
            entry_senhaConfirm.pack_forget()
            texto_senhaConfirm.pack_forget()
        else:
            texto_login['text'] = 'Cadastrar'

    else:
        # Obter os valores dos campos de entrada
        nome = entry_nome.get()
        userID = entry_userID.get()
        apelido = entry_apelido.get()
        email = entry_email.get()
        data_cadastro = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        senha_confirm = entry_senhaConfirm.get()

        # Validar os dados
        if not nome or not userID or not apelido or not email or not entry_senha.get() :
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        # se o botão for Editar a condição ira comparar a senha digitada com a senha cadastrada,
        # se não ira compar a senha e a confrimação de senha, seguindo a função de cadastro de um novo usuario
        if botao_cadastro['text'] != 'Editar':
            if entry_senha.get() != senha_confirm:
                messagebox.showerror("Erro", "As senhas não coincidem!")
                return
        else:
            if entry_senha.get() != senha:
                messagebox.showerror("Erro", "Senha incorreta!")
                return
        
        # Salvar os dados no MySQL
        conexao = database.get_connection()
        if conexao:
            try:
                cursor = conexao.cursor()
                
                if botao_cadastro['text'] == 'Editar':
                    # Edita os dados do usuario
                    query = "UPDATE users SET apelido = %s, nome = %s, email = %s, senha = %s WHERE userID = %s" 
                    values = (apelido, nome, email, senha, userID) 

                    cursor.execute(query, values) 
                    conexao.commit()

                else:
                    # Verificar se o userID já existe
                    cursor.execute("SELECT * FROM users WHERE userID = %s", (userID,))
                    if cursor.fetchone():
                        messagebox.showerror("Erro", "Este UserID já está em uso!")
                        return

                    # Inserir novo usuário
                    senha = entry_senha.get()
                    query = "INSERT INTO users (userID, apelido, nome, email, senha, data_cadastro) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (userID, apelido, nome, email, senha, data_cadastro)
                    
                    cursor.execute(query, values)
                    conexao.commit()
                
                # ajustando a condição para informar uma mensagem adeuqada ao usuario conforme a função a ser executada
                if botao_cadastro['text'] != 'Editar':
                    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                else:
                    messagebox.showinfo("Sucesso", "Usuário editado com sucesso!")
                
                # Limpar os campos após o cadastro
                entry_nome.delete(0, END)
                entry_userID.delete(0, END)
                entry_apelido.delete(0, END)
                entry_email.delete(0, END)
                entry_senha.delete(0, END)
                entry_senhaConfirm.delete(0, END)
                entry_data_cadastro.delete(0,END)

            except database.get_mysql_error()  as err:
                messagebox.showerror("Erro", f"Ocorreu um erro ao salvar os dados: {err}")
            finally:
                database.close_connection(conexao, cursor)

        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

def abrir_Login():
    if botao_login['text'] == 'Entrar':
        userID = entry_userID.get()

        if not userID or not entry_senha.get():
            messagebox.showerror('Erro', 'Por favor preencha todos os campos!')
            return
        
        if entry_senha.get() != senha: 
            messagebox.showerror("Erro", "Senha incorreta!") 
            return
        else:
            messagebox.showinfo("Longin","Loging ...")
            tela_Login.destroy()
        
    else:
        tela_Login.destroy()
        get_user()

# Iniciar o programa veirificando se o usuario captura esta cadastrado
get_user()

# Iniciar o loop principal
tela_Login.mainloop()