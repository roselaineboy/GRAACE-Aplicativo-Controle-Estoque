#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import os
from IPython.display import clear_output
import json
import pandas as pd

class Funcao_Global():
    
    #==============================================================================
    def limpar_tela(self):
        """Limpa a tela do terminal, dependendo do sistema operacional."""

        sistema = os.name  # 'posix' para Unix-based, 'nt' para Windows
        if sistema == 'posix':  # Unix-based (Linux/macOS)
            eh_colab = False
            try:
                import google.colab
                eh_colab = True
            except ImportError:
                eh_colab = False

            if eh_colab:
                clear_output()
            else:
                os.system('clear')
        elif sistema == 'nt':  # Windows
            os.system('cls')
    # Fim - limpar_tela

    #==============================================================================
    def verifica_arquivo(self, caminho):
        mensagem_retorno = ''
        # Verifica se o diretório existe, caso contrário, cria
        diretorio = os.path.dirname(caminho)
        diretorio_ok = False

        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                diretorio_ok = True
            except Exception as e:
                mensagem_retorno = f'Erro ao criar o diretorio: {e}'
                # a fazer: adicionar mensagem no log
        else:
            diretorio_ok = True

        # Verifica se o arquivo existe
        if diretorio_ok:
            if not os.path.exists(caminho):
                # Separa a extensão do arquivo
                _, extensao = os.path.splitext(caminho)

                try:
                    if extensao == ".json":
                    # Cria o arquivo JSON vazio caso ele não exista
                        with open(caminho, 'w') as arquivo:
                            lista_vazia = pd.DataFrame()
                            lista_vazia.to_json(caminho, orient='records', indent=4)
                    elif extensao == ".txt":
                    # Cria um arquivo TXT vazio
                        with open(caminho, 'w', encoding='utf-8') as arquivo:
                            arquivo.write("")
                except Exception as e:
                    mensagem_retorno = mensagem_retorno + ' ' + f'Erro ao criar o arquivo: {e}'

        return mensagem_retorno
    # Fim - verifica_arquivo

    #==============================================================================
    def eh_numero(self, s):
        if isinstance(s, str):
            if (s.startswith('-') or s.startswith('+') ):
                s = s[1:]  # Remove o sinal para verificar o restante
            s = s.replace('.', '')  # Remove o ponto decimal, pois estamos no Brasil
            s = s.replace(',', '.') # Trocando a vírgula pelo ponto decima, pois estamos no Brasil, mas o python não sabe disso

            if '.' in s:
                partes = s.split('.')
                if len(partes) != 2 or not partes[0].isdigit() or not partes[1].isdigit():
                    return False
            else:
                if not s.isdigit():
                    return False
        elif isinstance(s, (int, float)):
            return True                
        return True
    # Fim - eh_numero

    #==============================================================================
    def transforma_em_float(self, s):
        if isinstance(s, str):
            s = s.replace('.', '')  # Remove o ponto decimal, pois estamos no Brasil
            s = s.replace(',', '.') # Trocando a vírgula pelo ponto decima, pois estamos no Brasil, mas o python não sabe disso

        return float(s)
    # Fim - transforma_em_float

    #==============================================================================
    def transforma_em_int(self, s):
        if isinstance(s, str):
            s = s.replace('.', '')  # Remove o ponto decimal, pois estamos no Brasil
            s = s.replace(',', '.') # Trocando a vírgula pelo ponto decima, pois estamos no Brasil, mas o python não sabe disso

        return int(s)
    # Fim - transforma_em_int