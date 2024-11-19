from configurations.config import Settings
from utils.bib import GlobalFunctions
from classes.produto import Produto

class Menu(Settings):
    def __init__(self, opcao = None):
        self.__opcao = opcao
        self.GF = GlobalFunctions()

    def to_add_product(self):
        msgret = ''
        cadproduto = Produto()
        msgret = cadproduto.receber_dados_novo_produto()
        del(cadproduto)
        return msgret

    #Inicio - Cria a função Menu   
    def show_menu(self):
        len_row = 55
        self.GF.limpar_tela()
        print(len_row * '═')
        print('Bem-vindo ao ACE - Aplicativo de Controle de Estoque')
        print(len_row * '═')
        print('1 - Adicionar Produto')
        print('2 - Visualizar Estoque')
        print('3 - Alterar estoque')
        print('4 - Remover Estoque')
        print('5 - Log do Estoque')
        print('0 - Sair')
        print(len_row * '═')
    #Inicio - Cria a função de selecionar as opções

    def choose_option(self):
        self.show_menu()

        option = ''
        msg_text = ''

        while option != '0':
            self.show_menu()
            if msg_text != '':
                print(f'{msg_text}')
                msg_text = ""

            option = input('\nEscolha uma das opções: ')
        
            if option not in ['0', '1', '2', '3', '4', '5']:
                msg_text = 'Opção inválida!'
            else:
                if option == '1':
                    #ace.to_add()
                    msg_text = self.to_add_product()
                    msg_text = 'Msg ao Adicionar Produto: ' + msg_text
                elif option == '2':
                    #ace.to_view()
                    msg_text = 'Visualizar Estoque'
                elif option == '3':
                    #ace.to_go_out()
                    msg_text = 'Alterar estoque'
                elif option == '4':
                    #ace.to_go_out()
                    msg_text = 'Remover Estoque'
                elif option == '5':
                    #ace.to_go_out()
                    msg_text = 'Log do Estoque'
                else:
                    msg_text = msg_text + '\npressione enter para exibir o menu novamente'

        # fim while option
    
        self.GF.limpar_tela()
        print('\nObrigado volte sempre!')

menu = Menu()
menu.choose_option()
