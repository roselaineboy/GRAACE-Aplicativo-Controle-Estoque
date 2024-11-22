#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from classes.log import Log

class DefLog:
    #==============================================================================
    def __init__(self, log_file="log.json"):
        self.__log = Log(log_file)
    # Fim - init

    #==============================================================================
    def registrar_log(self, acao, mensagem):
        self.__log.registrar(acao, mensagem)
    # Fim - registrar log

    #==============================================================================
    def exibir_todos_logs(self):
        self.__log.exibir_logs()
    # Fim - exibir todos os logs
