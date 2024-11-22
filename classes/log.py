#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import os
from datetime import datetime

class Log:
    #==============================================================================
    def __init__(self):
        # Defina o caminho do arquivo de log
        self.arquivo_log = 'log.txt'  # Caminho relativo, você pode usar um caminho absoluto
        self.criar_arquivo_log()  # Cria o arquivo de log se não existir
    # Fim - init

    #==============================================================================
    def criar_arquivo_log(self):
        # Cria o arquivo de log se ele não existir
        if not os.path.exists(self.arquivo_log):
            with open(self.arquivo_log, 'w') as f:
                f.write("Início do log\n")  # Escreve uma linha de início no arquivo
    # Fim - criar arquivo

    #==============================================================================
    def registrar(self, acao, mensagem):
        try:
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{data_hora_atual}] {acao} - {mensagem}\n"
            with open(self.arquivo_log, 'a') as f:  # Abre em modo 'a' para adicionar ao arquivo
                f.write(log_message)
        except Exception as e:
            print(f"Erro ao registrar no log: {e}")
    # Fim - registrar
