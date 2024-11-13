#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import os

class Inicialize():

    def limpar_tela(self):
        """Limpa a tela do terminal, dependendo do sistema operacional."""
        sistema = os.name  # 'posix' para Unix-based, 'nt' para Windows
        if sistema == 'posix':  # Unix-based (Linux/macOS)
            os.system('clear')
        elif sistema == 'nt':  # Windows
            os.system('cls')
    # Fim - limpar_tela

    def show_menu(self):
        self.limpar_tela();
        print(50 * '═')

        print('Bem-vindo ao ACE - Aplicativo de Controle de Estoque')
        print(50 * '═')
        print('1 - Adicionar Produto')
        print('2 - Visualizar Produto')
        print('3 - Sair')
        print(50 * '═')
    # Fim - show_menu

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')
        
        if option not in ['1', '2', '3']:
            print('\nOpção inválida!')
        
        return option
    # fim - choose_option

if __name__ == '__main__':
    #__main__ é herança do py para saber de onde partir
    ace = Inicialize()

    option = ''

    while option != '3':
        ace.show_menu()
        option = ace.choose_option()
        
        if option == '1':
            #ace.to_add()
            print('selecionado adicionar')
        elif option == '2':
            #ace.to_view()
            print('selecionado visualizar')
        elif option == '3':
            #ace.to_go_out()
            print('selecionado sair')
        input('pressione entre para exibir o menu novamente')
    # fim while option
    ace.limpar_tela();
    print('\nObrigado volte sempre!')