#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from definicoes_de_tabelas.def_movimentacao import Def_Movimentacao_Estoque
from utils.bib import Funcao_Global

class Movimentacao_Estoque():
    def __init__(self):
        self.__movimentacao = Def_Movimentacao_Estoque()
        self.__fg = Funcao_Global()