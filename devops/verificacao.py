import os
import shutil
import filecmp
from datetime import datetime

def copiar_pasta(origem, destino, log_file):
    # Verifica se a pasta de origem existe
    if not os.path.exists(origem):
        print(f"A pasta de origem '{origem}' não existe.")
        return
    
    # Verifica se a pasta de destino existe, se não, cria
    if not os.path.exists(destino):
        os.makedirs(destino)
    
    with open(log_file, 'a') as log:
        log.write(f"--- Início do Log: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

        # Copia os arquivos e pastas da origem para o destino
        for item in os.listdir(origem):
            origem_arquivo = os.path.join(origem, item)
            destino_arquivo = os.path.join(destino, item)
            
            # Se for um arquivo, copia diretamente
            if os.path.isfile(origem_arquivo):
                if not os.path.exists(destino_arquivo) or \
                    not filecmp.cmp(origem_arquivo, destino_arquivo):
                    shutil.copy2(origem_arquivo, destino_arquivo)
                    log.write(f"Copiado arquivo: {origem_arquivo} -> {destino_arquivo}\n")
            # Se for uma pasta, chama a função recursivamente
            elif os.path.isdir(origem_arquivo):
                copiar_pasta(origem_arquivo, destino_arquivo, log_file)
        
        log.write("--- Fim do Log ---\n")

origem = "Mapfre_Connect"
destino = "..\..\..\..\Documents\TESTE_01"
log_file = "log.txt"

copiar_pasta(origem, destino, log_file)
print("Cópia concluída. Consulte o arquivo de log para detalhes.")