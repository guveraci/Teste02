import subprocess
import time

def parar_e_iniciar_servico(nome_servico):
    # Parar o serviço
    subprocess.run(["net", "stop", nome_servico], check=True)

    # Aguardar 5 segundos para garantir que o serviço seja completamente parado
    time.sleep(5)

    # Iniciar o serviço
    subprocess.run(["net", "start", nome_servico], check=True)

    print("Serviço reiniciado com sucesso.")

# Substitua "NOME_DO_SERVIÇO" pelo nome real do serviço que deseja parar e iniciar novamente
nome_do_servico = "NOME_DO_SERVIÇO"

parar_e_iniciar_servico(nome_do_servico)