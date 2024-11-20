#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from definicoes_de_tabelas.def_produto import Def_Produto
from utils.bib import Funcao_Global

class Produto():
    def __init__(self):
        self.__produto = Def_Produto()
        self.__fg = Funcao_Global()

    def cadastrar_produto(self):
        print('entrou no cadastrar_produto')
        input('<enter> para prosseguir')

        return 'Produto cadastrado'
