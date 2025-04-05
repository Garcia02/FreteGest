"""
Arquivo: main.py
Descrição: Este é o arquivo principal do sistema FreteGest, responsável por inicializar a aplicação e gerenciar a navegação entre as diferentes telas.

Funcionalidades principais:
1. Inicializar a janela principal da aplicação
2. Gerenciar a navegação entre as diferentes telas (login, cadastro, principal, edição de perfil)
3. Manter o estado global da aplicação (dados do usuário logado)

O que este arquivo faz:
- Cria a janela principal do Tkinter
- Inicializa a aplicação com a tela de login
- Fornece métodos para alternar entre as diferentes telas
- Gerencia o estado global do usuário logado
- Lida com o processo de logout

Possíveis melhorias futuras:
1. Implementar um sistema de gerenciamento de estado mais robusto (como Redux)
2. Adicionar suporte para temas (modo claro/escuro)
3. Implementar um sistema de plugins para facilitar a extensão de funcionalidades
4. Adicionar suporte para internacionalização (i18n)
5. Implementar um sistema de logging mais abrangente para toda a aplicação

Observações adicionais:
- A classe FreteGestApp atua como um controlador central para a aplicação
- O ícone da aplicação é carregado dinamicamente, o que pode ser expandido para outros recursos
- Considerar a implementação de um sistema de roteamento mais sofisticado para navegação entre telas
- A estrutura atual permite uma fácil expansão para adicionar novas telas e funcionalidades
"""

import tkinter as tk
import os
from LoginInterface.tela_login import TelaLogin
from LoginInterface.tela_cadastro import TelaCadastro
from Navegação.tela_principal import TelaPrincipal
from LoginInterface.tela_editar_perfil import TelaEditarPerfil
from tkinter import PhotoImage
from tkinter import messagebox

class FreteGestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("FreteGest")
        self.master.resizable(width=False, height=False)

        caminho_icon = os.path.join(os.getcwd(), 'Imagens','caminhao.png')
        self.icon = PhotoImage(file=caminho_icon)
        self.master.iconphoto(False, self.icon)

        self.system_userID = os.path.join(os.path.expanduser("~"), "Downloads").split(os.sep)[2]
        self.user_data = None
        self.tela_atual = None
        self.abrir_tela_login()

    def abrir_tela_login(self):
        self.limpar_tela()
        self.tela_atual = TelaLogin(self.master, self)

    def abrir_tela_cadastro(self):
        self.limpar_tela()
        self.tela_atual = TelaCadastro(self.master, self)

    def abrir_tela_principal(self):
        self.limpar_tela()
        self.tela_atual = TelaPrincipal(self.master, self)

    def abrir_tela_editar_perfil(self):
        self.limpar_tela()
        self.tela_atual = TelaEditarPerfil(self.master, self)

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def centralizar_janela(self, largura, altura):
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)
        self.master.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

    def fazer_logout(self):
        self.user_data = None
        messagebox.showinfo("Logout", "Você saiu do sistema.")
        self.abrir_tela_login()

if __name__ == "__main__":
    root = tk.Tk()
    app = FreteGestApp(root)
    root.mainloop()