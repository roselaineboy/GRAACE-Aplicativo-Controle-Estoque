#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

class Def_Produto():
    def __init__(self, codigo=0):

    @property
    def codigo(self):
        return self.__codigo

    def validar_conteudo(self):

        msg = ''
        if type(self.__codigo) != int and int(self.__codigo) <= 0:
            msg = msg + '\nO código deve ser um número maior que zero'

        return msg
    #Fim validar_conteudo

    def view(self):
        print(f'Código................: {self.__codigo}')
    
    def __str__(self):
        self.view(self)
