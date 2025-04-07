from tkinter import Frame  # Importa a classe Frame do módulo tkinter
from tkinter import Tk  # Importa a classe Tk do módulo tkinter
from tkinter import Label
from . import Config_manager  # Importa o módulo Config_manager do pacote atual

# Criar uma instância do ConfigManager
conf = Config_manager.ConfigManager()

# Constantes - Obtém valores do arquivo de configuração
COR_BODY = conf.get_value('Colors', 'BACKGROUND_COLOR')  # Cor de fundo do corpo
COR_TITLE = conf.get_value('Colors', 'TEXT_COLOR')  # Cor do título
WINDOW_WIDTH = conf.get_int('Layout', 'WINDOW_WIDTH')  # Largura da janela
WINDOW_HEIGHT = conf.get_int('Layout', 'WINDOW_HEIGHT')  # Altura da janela
TITLE_FONT = conf.get_font('Fonts', 'MAIN_TITLE_FONT') # Cor do título
FONT = conf.get_font('Fonts', 'PADRAO_FONT')


class TelaLogin:
    def __init__(self, master):
        self.master = master  # Armazena a referência da janela principal

    def criarInterface(self):
        # Cria o contêiner para o frame superior
        container1 = Frame(self.master,  # 'self.master' é a janela principal
                        bg='black')   # 'bg' define a cor de fundo do contêiner como preta
        
        # Posiciona o contêiner1 na janela
        container1.pack(
            pady=(10, 0),  # Adiciona 10px de espaço acima e 0px abaixo do contêiner
            padx=10,        # Adiciona 10px de espaço à esquerda e à direita do contêiner
            fill='both'     # Preenche o espaço disponível tanto na horizontal quanto na vertical
        )

        # Cria o frame superior dentro do contêiner1
        self.frame1 = Frame(
            container1,                     # Define container1 como o pai deste frame
            width=WINDOW_WIDTH - 10,        # Define a largura do frame (largura da janela menos 30px)
            height=WINDOW_HEIGHT // 4, # Define a altura como 1/3 da altura da janela menos 20px
            bg=COR_TITLE                    # Define a cor de fundo do frame usando a constante COR_TITLE
        )
        
        # Posiciona o frame1 dentro do container1
        self.frame1.pack(
            fill='both',  # Preenche todo o espaço disponível no contêiner
            expand=True,  # Permite que o frame expanda para ocupar espaço extra
            padx=2,       # Adiciona 2px de espaço horizontal entre o frame e o contêiner
            pady=2        # Adiciona 2px de espaço vertical entre o frame e o contêiner
        )

        self.frame1.pack_propagate(False)

        Label(self.frame1,text="FRETGEST", bg='darkgray', fg='black', font=TITLE_FONT).pack(pady=(10, 0))
        Label(self.frame1,text="Sistema de Gestão de Custos de Transporte", bg='darkgray', fg='black', font=FONT).pack()


        # Cria o frame inferior
        self.frame2 = Frame(
            self.master,                                    
            width=WINDOW_WIDTH - 35,                       # Define a largura do frame (largura da janela menos 30px)
            height=WINDOW_HEIGHT - (WINDOW_HEIGHT // 4) - 30, # Define a altura como 2/3 da altura da janela menos 30px
            bg=COR_BODY                                    # Define a cor de fundo do frame usando a constante COR_BODY
        )
        self.frame2.pack_propagate(False)  # Impede que o frame se ajuste ao conteúdo
        self.frame2.pack()

# Cria a janela principal
root = Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # Define o tamanho da janela
root.resizable(False, False)  # Impede o redimensionamento da janela
login_tela = TelaLogin(root)  # Cria uma instância da classe TelaLogin
login_tela.criarInterface()  # Chama o método para criar a interface
root.mainloop()  # Inicia o loop principal da aplicação