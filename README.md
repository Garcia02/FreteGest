<h1 align="center">
  <img src="images/fretgest_logo.png" alt="FreteGest Logo" width="200">
  <br>
  FreteGest: Sistema de Gestão de Custos de Transporte
</h1>

<p align="center">
  <a href="#visão-geral">Visão Geral</a> •
  <a href="#características">Características</a> •
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#estrutura">Estrutura</a> •
  <a href="#telas">Telas</a> •
  <a href="#sobre-o-projeto">Sobre o Projeto</a> •
  <a href="#contato">Contato</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.x-yellow.svg" alt="Python version">
</p>

## 📊 Visão Geral

FreteGest é um sistema de gestão de custos de transporte desenvolvido em Python, utilizando a interface gráfica Tkinter e banco de dados MySQL. Este sistema visa otimizar o gerenciamento de custos relacionados ao transporte de cargas, oferecendo uma interface intuitiva e funcionalidades robustas.

## 🌟 Características

- 🔐 Sistema de login e cadastro de usuários
- 👤 Gerenciamento de perfis de usuário
- 💾 Armazenamento seguro de dados com MySQL
- 🖥️ Interface gráfica amigável com Tkinter
- 🔄 Operações CRUD para gerenciamento de dados

## 🛠️ Tecnologias

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/bcrypt-2A2A2A?style=for-the-badge" alt="bcrypt">
  <img src="https://img.shields.io/badge/configparser-2A2A2A?style=for-the-badge" alt="configparser">
</p>

## 🚀 Instalação

1. Clone o repositório:
git clone 

github.com


2. Instale as dependências:
pip install -r requirements.txt


3. Configure o banco de dados MySQL:
- Crie um banco de dados chamado `fretgest`
- Atualize o arquivo `credenciais.ini` com suas configurações de banco de dados

4. Execute o script de inicialização:
python main.py


## 📁 Estrutura

<pre>
FRETGEST/
├── BaseDados/
│   ├── __init__.py
│   └── database.py
├── LoginInterface/
│   ├── __init__.py
│   ├── tela_login.py
│   ├── tela_cadastro.py
│   ├── tela_principal.py
│   └── tela_editar_perfil.py
├── Imagens/
│   └── caminhao.png
├── main.py
├── credenciais.ini
└── README.md
</pre>

## 🖥️ Telas

<p align="center">
<img src="images/tela_login.png" alt="Tela de Login" width="30%">
<img src="images/tela_cadastro.png" alt="Tela de Cadastro" width="30%">
<img src="images/tela_principal.png" alt="Tela Principal" width="30%">
</p>

## 🎓 Sobre o Projeto

Este projeto foi desenvolvido como parte do meu processo de aprendizagem em programação e para construir um portfólio visando entrar no mercado de desenvolvimento. O FreteGest é uma aplicação prática que pode potencialmente ser implementada no meu atual ambiente de trabalho, demonstrando habilidades em Python, interface gráfica e gerenciamento de banco de dados.

## 📞 Contato

Para mais informações ou oportunidades de colaboração, entre em contato comigo através dos seguintes canais:

<p align="center">
<a href="https://www.instagram.com/jefersongarcia.l/">
 <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
</a>
<a href="https://www.linkedin.com/in/jeferson-garcia-315270b0">
 <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
</p>

<hr>

<p align="center">
Desenvolvido com ❤️ por Jeferson Garcia
</p>
