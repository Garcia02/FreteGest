import configparser
import os

class ConfigManager:
    def __init__(self, config_file="config.ini"):
        self.config = configparser.ConfigParser()

        # Obtém o diretório do script atual
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Constrói o caminho completo para o arquivo de configuração
        config_path = os.path.join(current_dir, config_file)

        # Verifica se o arquivo existe
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Arquivo de configuração '{config_file}' não encontrado.")

        self.config.read(config_path)

    def get_value(self, section, key):
        return self.config.get(section, key)

    def get_font(self, section, key):
        value = self.config.get(section, key)
        # Divide a string em partes
        parts = [part.strip() for part in value.split(',')]
        
        # O primeiro elemento é sempre o nome da fonte
        font_name = parts[0]
        
        # O segundo elemento, se existir, é o tamanho da fonte
        font_size = int(parts[1]) if len(parts) > 1 else 12  # 12 é um tamanho padrão
        
        # O terceiro elemento, se existir, é o estilo da fonte
        font_style = parts[2] if len(parts) > 2 else ""
        
        return (font_name, font_size, font_style)

    def get_int(self, section, key):
        return self.config.getint(section, key)