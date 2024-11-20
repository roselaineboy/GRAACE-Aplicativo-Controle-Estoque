#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from classes.relatorio import Relatorio
from classes.menu import Menu

if __name__ == '__main__':
    rel = Relatorio()
    rel.listar_abaixo_estoque_minimo()
    menu = Menu()
    menu.exibir_solicitar_executar()
