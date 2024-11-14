import os

class Menu:
    def __init__(self, opcao = none):
        self.__opcao = opcao

#Inicio - Cria a função Menu   
    def show_menu(self):
        print(50 * '═')
        print('\nBem-vindo ao ACE - Aplicativo de Controle de Estoque')
        print(50 * '═')
        print('1 - Adicionar Produto')
        print('2 - Visualizar Estoque')
        print('3 - Alterar estoque')
        print('4 - Remover Estoque')
        print('5 - Log do Estoque')
        print('0 - Sair')
        print(50 * '═')

#Inicio - Cria a função de selecionar as opções
        def choose_option(self):
        self.__choose_option = input('\nEscolha uma das opções: ')
        return self.__choose_option
        
        if option not in ['0', '1', '2', '3', '4', '5']:
            print('\nOpção inválida!')
        return option

#Cria a funcão para limpar a tela
    def limpar_tela(self):
        os.system('cls') if os.name == 'nt' else 'clear'