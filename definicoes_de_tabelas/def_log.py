#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from classes.log import Log

class DefLog:
    def __init__(self, log_file="log.json"):
        """Inicializa a classe DefLog com o sistema de logs."""
        self.__log = Log(log_file)

    def registrar_log(self, acao, mensagem):
        """Registra uma mensagem de log."""
        self.__log.registrar(acao, mensagem)

    def exibir_todos_logs(self):
        """Exibe todos os logs registrados."""
        self.__log.exibir_logs()
