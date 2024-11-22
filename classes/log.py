#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import os
from datetime import datetime
import pytz  # Biblioteca para lidar com fusos horários

class Log:
    # ==============================================================================
    def __init__(self):
        # Defina o caminho da pasta e do arquivo de log
        self.pasta_dados = 'dados'
        self.arquivo_log = os.path.join(self.pasta_dados, 'log.txt')
        self.fuso_horario = pytz.timezone('America/Sao_Paulo')  # Ajuste para o seu fuso horário
        self.preparar_ambiente()  # Configura a pasta e o arquivo de log
    # Fim - init

    # ==============================================================================
    def preparar_ambiente(self):
        # Cria a pasta 'dados' se não existir
        if not os.path.exists(self.pasta_dados):
            os.makedirs(self.pasta_dados)
        
        # Move o arquivo de log existente, se necessário
        log_antigo = 'log.txt'  # Caminho antigo do log
        if os.path.exists(log_antigo) and not os.path.exists(self.arquivo_log):
            os.rename(log_antigo, self.arquivo_log)
        
        # Cria o arquivo de log se não existir
        if not os.path.exists(self.arquivo_log):
            with open(self.arquivo_log, 'w') as f:
                f.write("Início do log\n")
    # Fim - preparar_ambiente

    # ==============================================================================
    def registrar(self, acao, mensagem):
        try:
            # Obtém o horário atual no fuso horário correto
            data_hora_atual = datetime.now(self.fuso_horario).strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{data_hora_atual}] {acao} - {mensagem}\n"
            with open(self.arquivo_log, 'a') as f:  # Abre em modo 'a' para adicionar ao arquivo
                f.write(log_message)
        except Exception as e:
            print(f"Erro ao registrar no log: {e}")
    # Fim - registrar
