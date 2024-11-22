#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

class Definicao():
    #==============================================================================
    def __init__(self):
        self.__dados_produtos = './dados/produtos.json'
        self.__dados_movimentacoes = './dados/movimentacoes.json'
        self.__dados_log = './dados/log.txt'
    # Fim - init

    #==============================================================================
    @property
    def db_produtos(self):
        return self.__dados_produtos

    #==============================================================================
    @property
    def db_movimentacoes(self):
        return self.__dados_movimentacoes
    
    #==============================================================================
    @property
    def db_log(self):
        return self.__dados_log    