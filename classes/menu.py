import os
from utils.bib import GlobalFunctions

class Menu:
    def __init__(self, operation = None):
        self.__operation = operation
        self.GF = GlobalFunctions()
    
    def show_menu(self):
        len_row = 55
        self.GF.limpar_tela()
        print(len_row * '═')
        print('Bem-vindo ao ACE - Aplicativo de Controle de Estoque')
        print(len_row * '═')
        print('1 - Adicionar Produto')
        print('2 - Visualizar Estoque')
        print('3 - Alterar Estoque')
        print('4 - Remover Estoque')
        print('5 - Adicionar quantidade do item no estoque')
        print('6 - Remover quantidade do item no Estoque')
        print('7 - Log do Estoque')
        print('0 - Sair')
        print(len_row * '═')

    def selecionar_operacao(self):
        self.__operation = int(input('selecione uma operação: '))
        return self.__operation