#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

class Settings():
    def __init__(self):
        self.__repository_produtos = './data/produtos.json'
        self.__repository_estoques = './data/estoques.json'

    @property
    def produtos_repository(self):
        return self.__repository_produtos

    @property
    def estoques_repository(self):
        return self.__repository_produtos