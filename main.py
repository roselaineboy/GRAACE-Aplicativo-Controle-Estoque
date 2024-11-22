#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import time
#from classes.menu import Menu
from classes.relatorio import Relatorio
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
# Fim - splash

#==============================================================================
if __name__ == '__main__':
    splash()
    
    from classes.menu import Menu

    time.sleep(1)

    rel = Relatorio()
    rel.listar_abaixo_estoque_minimo(False)

    menu = Menu()
    menu.exibir_solicitar_executar()


