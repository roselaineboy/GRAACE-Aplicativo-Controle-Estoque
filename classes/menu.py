#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from configuracoes.config import Definicao
from utils.bib import Funcao_Global
from classes.produto import Produto
from classes.movimentacao_estoque import Movimentacao_Estoque
from classes.relatorio import Relatorio

class Menu(Definicao):
    def __init__(self, opcao_selecionada = None):
        self.__opcao_selecionada = opcao_selecionada
        self.fg = Funcao_Global()
        self.produto = Produto()
        self.movimentacao = Movimentacao_Estoque()
        self.relatorio = Relatorio()

    def exibir_menu(self):
        len_row = 55
        self.fg.limpar_tela()
        print(len_row * '═')
        print('Bem-vindo ao ACE - Aplicativo de Controle de Estoque')
        print(len_row * '═')
        print("1 - Cadastrar Produto")
        print("2 - Atualizar Produto")
        print("3 - Deletar Produto")
        print("4 - Listar Produtos")
        print("5 - Entrada de Estoque")
        print("6 - Saída de Estoque")
        print("7 - Listar Produtos Abaixo do Estoque Mínimo")
        print('8 - teste')
        print("0 - Sair")
        print(len_row * '═')

    def escolha_a_opcao(self):
        self.exibir_menu()

        option = ''
        msg_text = ''

        while option != '0':
            self.exibir_menu()
            if msg_text != '':
                print(f'{msg_text}')
                msg_text = ""

            option = input('\nEscolha uma das opções: ')
        
            if option not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                msg_text = 'Opção inválida!'
            else:
                if option == '1':
                    #ace.to_add()
                    msg_text = self.produto.cadastrar_produto()
                    msg_text = 'Msg ao Adicionar Produto: ' + msg_text
                elif option == '2':
                    msg_text = self.produto.atualizar_produto()
                    msg_text = 'Msg ao Atualizar Produto: ' + msg_text
                elif option == '3':
                    msg_text = self.produto.deletar_produto()
                    msg_text = 'Msg ao Deletar Produto: ' + msg_text
                elif option == '4':
                    msg_text = self.produto.listar_produtos()
                    msg_text = 'Msg ao Consultar Produto: ' + msg_text
                elif option == '5':
                    msg_text = self.movimentacao.entrada()
                    msg_text = 'Msg ao Dar Entrada de Produto: ' + msg_text
                elif option == '6':
                    msg_text = self.movimentacao.saida()
                    msg_text = 'Msg ao Dar Saida de Produto: ' + msg_text
                elif option == '7':
                    msg_text = self.relatorio.listar_abaixo_estoque_minimo()
                    msg_text = 'Msg ao Listar Ponto de Pedido: ' + msg_text
                elif option == '8':
                    msg_text = self.produto.buscar_produto_por_codigo("A002")
                else:
                    msg_text = msg_text + '\npressione enter para exibir o menu novamente'

        # fim while option
    
        self.fg.limpar_tela()
        print('\nObrigado volte sempre!')
    
    def chamarlistagem():
        relatorio = Relatorio()
        relatorio.listar_abaixo_estoque_minimo()

    def exibir_solicitar_executar(self):
        self.exibir_menu()
        self.escolha_a_opcao()

if __name__ == "__main__":
    menu = Menu()
    menu.exibir_solicitar_executar()
