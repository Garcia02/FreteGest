# Arquivo: FretGest.py

# Importações necessárias
from Interfaces.Tela_Login import TelaLogin  # Ajuste o caminho conforme necessário

def main():
    """
    Função principal que inicia a aplicação.
    """
    # Criando uma instância da tela de login
    tela_login = TelaLogin()
    
    # Se a tela de login for uma janela Tkinter, você chama o mainloop aqui
    tela_login.mainloop()  # Se for Tkinter
    
    # Se você estiver usando outra biblioteca de GUI, o método para exibir a janela pode ser diferente
    # Por exemplo, para PyQt5:
    # tela_login.show()
    # sys.exit(app.exec_())

# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()