import os

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads").split(os.sep) [2]

if len(downloads_path) > 2: print(downloads_path[2]) 

else: print("Não foi possível identificar o nome de usuário no caminho.")