#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from configuracoes.config import Definicao

import pandas as pd
from utils.bib import Funcao_Global

class Relatorio():
    def __init__(self):
        self.bib = Funcao_Global()
        self.definicao = Definicao()
        self.__lista_produtos = pd.DataFrame([])


    def carrega_lista_produto(self):

        caminho_arquivo = self.definicao.db_produtos

        arquivo_ok = self.bib.verifica_arquivo(caminho_arquivo)
        if arquivo_ok == '':
            dados = pd.read_json(caminho_arquivo)
            self.__lista_produtos = pd.DataFrame(dados)

        #if arquivo_ok == '':
        #    with open(caminho_arquivo, 'r') as arquivo:
        #        dados = json.load(arquivo)
        # Converte os dados para um DataFrame do pandas
        #self.__lista_produtos = pd.DataFrame(dados)
    # fim - carrega_lista_produto


    def listar_abaixo_estoque_minimo(self, imprimir_mesmo_que_vazio = True):
        self.bib.limpar_tela()
        self.carrega_lista_produto()

        if not self.__lista_produtos.empty:
            produtos_baixo_estoque = self.__lista_produtos[ (self.__lista_produtos['saldo_estoque'] <= self.__lista_produtos['qtde_minimaestoque']) | 
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
