#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

import os

class Funcao_Global():
    
    def limpar_tela(self):
        """Limpa a tela do terminal, dependendo do sistema operacional."""
        sistema = os.name  # 'posix' para Unix-based, 'nt' para Windows
        if sistema == 'posix':  # Unix-based (Linux/macOS)
            os.system('clear')
        elif sistema == 'nt':  # Windows
            os.system('cls')
    # Fim - limpar_tela
    