#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import time
import importlib.util
import subprocess
import sys

#from classes.menu import Menu
from utils.bib import Funcao_Global

#==============================================================================
def splash():
    bib = Funcao_Global()
    bib.limpar_tela()
    print('=-' * 19)
    print('+----  +---+  +---+  +---+  +---  +----')
    print('|      |   |  |   |  |   |  |     |    ')
    print('|  --  |---   |---|  |---|  |     |--  ')
    print('|   |  | \\    |   |  |   |  |     |    ')
    print('|___|  |  \\   |   |  |   |  |___  |____')
    print('=-' * 19)
    print('  Aplicativo de Controle de Estoque')
    print('=-' * 19)
    del(bib)
# Fim - splash

#==============================================================================
def verificar_e_instalar(pacote):
    # Verificar e instalar o pacote, se necessário
    if importlib.util.find_spec(pacote) is None:
        print(f"Pacote '{pacote}' não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

#==============================================================================
if __name__ == '__main__':
    splash()
    
    verificar_e_instalar("tabulate")

    from classes.log import Log
    log = Log()
    log.preparar_ambiente()

    log.registrar('Inicializacao', 'ACE inicializado')

    time.sleep(1)

    from classes.relatorio import Relatorio
    rel = Relatorio()
    rel.listar_abaixo_estoque_minimo(False)

    from classes.menu import Menu
    menu = Menu()
    try:
        menu.exibir_solicitar_executar()
    except Exception as e:
        msg_retorno = f"Erro sem tratamento: {e}"
        log.registrar('ERRO', msg_retorno)
        print('Ocorreu um erro na execução do ACE, e o mesmo foi registrado no log. Solicite auxilio do suporte.')
    finally:
        log.registrar('Encerramento', 'ACE encerrado')

