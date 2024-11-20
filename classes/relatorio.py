#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import pandas as pd
from definicoes_de_tabelas.def_produto import Def_Produto
from utils.bib import Funcao_Global

class Relatorio():
    def __init__(self):
        self.__produto = Def_Produto()
        self.__fg = Funcao_Global()

    def listar_abaixo_estoque_minimo(self):
        self.__fg.limpar_tela()

        #produtos_baixo_estoque = self.__produto.df[
        #    (self.__produto.df['saldo_estoque'] <= self.__produto.df['EstoqueMinimo']) | (self.__produto.df['Saldo'] == 0)
        #]
        print('produtos_baixo_estoque')
        input('<ENTER> para prosseguir')
        return ""
