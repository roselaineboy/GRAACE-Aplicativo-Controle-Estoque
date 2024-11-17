import os

class GlobalFunctions():
    
    def limpar_tela(self):
        """Limpa a tela do terminal, dependendo do sistema operacional."""
        sistema = os.name  # 'posix' para Unix-based, 'nt' para Windows
        if sistema == 'posix':  # Unix-based (Linux/macOS)
            os.system('clear')
        elif sistema == 'nt':  # Windows
            os.system('cls')
    # Fim - limpar_tela
    