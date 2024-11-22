#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import os
from datetime import datetime
import pytz  # Biblioteca para lidar com fusos horários

from configuracoes.config import Definicao

class Log:
    # ==============================================================================
    def __init__(self):
        self.definicao = Definicao()
        self.arquivo_log = self.definicao.db_log
        self.fuso_horario = pytz.timezone('America/Sao_Paulo')  # Ajuste para o seu fuso horário
    # Fim - init

    # ==============================================================================
    def preparar_ambiente(self):

        from configuracoes.config import Definicao
        from utils.bib import Funcao_Global

        # Defina o caminho da pasta e do arquivo de log
        definicao = Definicao()
        bib = Funcao_Global()
        retorno = bib.verifica_arquivo(definicao.db_log)

        if retorno == "":
            self.registrar('INICIALIZACAO ACE','Início do log' )

        del(bib)
        del(definicao)
    # Fim - preparar_ambiente

    # ==============================================================================
    def registrar(self, acao, mensagem):
        try:
            # Obtém o horário atual no fuso horário correto
            data_hora_atual = datetime.now(self.fuso_horario).strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{data_hora_atual}] - {acao} - {mensagem}\n"
            with open(self.arquivo_log, 'a', encoding='utf-8') as f:  # Abre em modo 'a' para adicionar ao arquivo
                f.write(log_message)
        except Exception as e:
            print(f"Erro ao registrar no log: {e}")
    # Fim - registrar
