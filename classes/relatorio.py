#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import pandas as pd
from tabulate import tabulate

from configuracoes.config import Definicao
from utils.bib import Funcao_Global
from classes.log import Log



class Relatorio():
    #==============================================================================
    def __init__(self):
        self.bib = Funcao_Global()
        self.definicao = Definicao()
        self.log = Log()
        self.__lista_produtos = pd.DataFrame([])
    # Fim - init

    #==============================================================================
    def carrega_lista_produto(self):

        caminho_arquivo = self.definicao.db_produtos

        arquivo_ok = self.bib.verifica_arquivo(caminho_arquivo)
        if arquivo_ok == '':
            dados = pd.read_json(caminho_arquivo)
            self.__lista_produtos = pd.DataFrame(dados)
    # Fim - carrega_lista_produto

    #==============================================================================
    def listar_abaixo_estoque_minimo_original(self, imprimir_mesmo_que_vazio = True):
        self.bib.limpar_tela()
        self.carrega_lista_produto()

        if not self.__lista_produtos.empty:
            produtos_baixo_estoque = self.__lista_produtos[ (self.__lista_produtos['saldo_estoque'] < self.__lista_produtos['qtde_minimaestoque']) | 
                                                            (self.__lista_produtos['saldo_estoque'] == 0)
                                                          ].copy()
            if imprimir_mesmo_que_vazio or not produtos_baixo_estoque.empty:
                # Adicionar a nova coluna 'qtde_a_repor'
                produtos_baixo_estoque['qtde_a_repor'] = produtos_baixo_estoque['qtde_minimaestoque'] - produtos_baixo_estoque['saldo_estoque']
                print(produtos_baixo_estoque)
                
                print('<ENTER> para prosseguir')
                input('...')

            elif imprimir_mesmo_que_vazio:
                print('Todos os Produtos estão acima de seus estoques mínimo. Não há necessidade de reposição')
                print('<ENTER> para prosseguir')
                input('...')
        elif imprimir_mesmo_que_vazio:
                print('Todos os Produtos estão acima de seus estoques mínimo. Não há necessidade de reposição')
                print('<ENTER> para prosseguir')
                input('...')
        
        return
    # Fim - listar abaixo estoque minimo

    #==============================================================================    
    def imprimir_cabecalho(self, titulo):
        len_row = 55
        self.bib.limpar_tela()
        print(len_row * '-')
        print('ACE - Aplicativo de Controle de Estoque')
        print(titulo)
        print(len_row * '-')
    # Fim - imprimir cabecalho

    #==============================================================================
    def listar_abaixo_estoque_minimo(self, imprimir_mesmo_que_vazio = True):
        self.bib.limpar_tela()
        self.carrega_lista_produto()

        if not self.__lista_produtos.empty:

            produtos_baixo_estoque = self.__lista_produtos[ (self.__lista_produtos['saldo_estoque'] < self.__lista_produtos['qtde_minimaestoque']) | 
                                                            (self.__lista_produtos['saldo_estoque'] == 0)
                                                          ].copy()

            if imprimir_mesmo_que_vazio or not produtos_baixo_estoque.empty:
                # Definição dos nomes amigáveis das colunas
                cabecalho_exibicao = {  'codigo': "Código"
                                      , 'nome'  : "Nome"
                                      , 'categoria': "Categoria"
                                      , 'valor_unitario': "Valor Unitário"
                                      , 'qtde_minimaestoque': "Qtde Mínima do Estoque"
                                      , 'saldo_estoque': "Saldo Em Estoque"
                                      , 'qtde_a_repor': "Qtde à Repor"
                                      , 'valor_da_reposicao': "Valor da Reposição"
                                     }

                # Adicionar a nova coluna 'qtde_a_repor'
                produtos_baixo_estoque['qtde_a_repor'] = produtos_baixo_estoque['qtde_minimaestoque'] - produtos_baixo_estoque['saldo_estoque']
                produtos_baixo_estoque['valor_da_reposicao'] = ( produtos_baixo_estoque['qtde_minimaestoque'] - produtos_baixo_estoque['saldo_estoque'] )\
                                                                      * produtos_baixo_estoque['valor_unitario']
                
                produtos_baixo_estoque.sort_values(by='qtde_a_repor', ascending=False)

                # Trocar os nomes das colunas antes de imprimir
                produtos_baixo_estoque = produtos_baixo_estoque[list(cabecalho_exibicao.keys())].rename(columns=cabecalho_exibicao)

                #print(produtos_baixo_estoque)
                self.imprimir_cabecalho('Listagem de Produtos Com Necessidade de Reposição')
                print(tabulate(produtos_baixo_estoque, headers="keys", tablefmt="grid"))
                
                print('<ENTER> para prosseguir')
                input('...')

            elif imprimir_mesmo_que_vazio:
                print('Todos os Produtos estão acima de seus estoques mínimo. Não há necessidade de reposição')
                print('<ENTER> para prosseguir')
                input('...')
        elif imprimir_mesmo_que_vazio:
                print('Todos os Produtos estão acima de seus estoques mínimo. Não há necessidade de reposição')
                print('<ENTER> para prosseguir')
                input('...')
        
        return
    # Fim - listar abaixo estoque minimo

    #==============================================================================    
    def listar_produtos(self):
        self.bib.limpar_tela()

        self.carrega_lista_produto()

        produtos_cadastrados = self.__lista_produtos.copy()
        produtos_cadastrados.sort_values(by='codigo')
        
        # Definição dos nomes amigáveis das colunas
        cabecalho_exibicao = {  'codigo': "Código"
                              , 'nome'  : "Nome"
                              , 'categoria': "Categoria"
                              , 'valor_unitario': "Valor Unitário"
                              , 'qtde_minimaestoque': "Qtde Mínima do Estoque"
                              , 'saldo_estoque': "Saldo Em Estoque"
                             }

        # Trocar os nomes das colunas antes de imprimir
        produtos_cadastrados = produtos_cadastrados[list(cabecalho_exibicao.keys())].rename(columns=cabecalho_exibicao)

        self.imprimir_cabecalho('Listagem de Produtos Cadastrados')

        print(tabulate(produtos_cadastrados, headers="keys", tablefmt="grid"))

        self.log.registrar("LISTAR", "Produtos listados com sucesso.")
        print('Pressione <ENTER> para para voltar ao menu')
        input('...')
    # Fim - listar_produto
         
    #==============================================================================
    def listar_log(self):

        caminho_arquivo = self.definicao.db_log
        dados_log = pd.read_csv(caminho_arquivo, delimiter=" - ", header=None, encoding='utf-8')
        
        self.imprimir_cabecalho('Listagem do Log')
        print(tabulate(dados_log, headers="keys", tablefmt="grid"))

        print('Pressione <ENTER> para para voltar ao menu')
        input('...')

    # Fim - listar_log
