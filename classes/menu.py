#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import time
from configuracoes.config import Definicao

from utils.bib import Funcao_Global
from classes.produto import Produto
from classes.movimentacao_estoque import Movimentacao
from classes.relatorio import Relatorio
from classes.log import Log

class Menu(Definicao):
    #==============================================================================
    def __init__(self, opcao_selecionada = None):
        self.__opcao_selecionada = opcao_selecionada
        self.fg = Funcao_Global()
        self.produto = Produto()
        self.movimentacao = Movimentacao()
        self.relatorio = Relatorio()
        self.log = Log()
    # Fim - init

    #==============================================================================
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
        print('8 - Listar Movimentações de Produto')
        print('9 - Listar Log')
        print("0 - Sair")
        print(len_row * '═')
    # Fim - exibir_menu

    #==============================================================================
    def chamarlistagem():
        relatorio = Relatorio()
        relatorio.listar_abaixo_estoque_minimo()
    # Fim - chamar listagem

    #==============================================================================
    def exibir_solicitar_executar(self):
        option = ''
        msg_text = ''

        while option != '0':
            self.exibir_menu()
            if msg_text != '':
                print(f'{msg_text}')
                msg_text = ""

            option = input('\nEscolha uma das opções: ')
        
            if option not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                msg_text = 'Opção inválida!'
            else:
                if option == '1':
                    self.produto.cadastrar_produto()
                elif option == '2':
                    self.produto.atualizar_produto()
                elif option == '3':
                    self.produto.deletar_produto()
                elif option == '4':
                    self.relatorio.listar_produtos()
                elif option == '5':
                    self.movimentacao.entrada()
                elif option == '6':
                    self.movimentacao.saida()
                elif option == '7':
                    self.relatorio.listar_abaixo_estoque_minimo()
                elif option == '8':
                    self.movimentacao.listar_movimentacoes_produto_por_codigo()
                elif option == '9':
                    self.relatorio.listar_log()
                else:
                    msg_text = msg_text + '\npressione enter para exibir o menu novamente'

        # fim while option
    
        self.fg.limpar_tela()
        print('=-' * 19)
        print(' ' * 8 + 'Obrigado volte sempre!')
        print('=-' * 19)
    # Fim - exibir solicitar executar