import json
from datetime import datetime
import os

class Log:
    def __init__(self, log_file="log.json"):
        """Inicializa o sistema de logs com o arquivo especificado."""
        self.log_file = log_file
       
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as file:
                json.dump([], file)

    def registrar(self, acao, mensagem):
        """Registra uma ação ou erro no log."""
        registro = {
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "acao": acao,
            "mensagem": mensagem
        }
        
        with open(self.log_file, "r") as file:
            logs = json.load(file)

       
        logs.append(registro)

      
        with open(self.log_file, "w") as file:
            json.dump(logs, file, indent=4)

    def exibir_logs(self):
        """Exibe todos os logs registrados."""
        if not os.path.exists(self.log_file):
            print("Nenhum log encontrado.")
            return
        
        with open(self.log_file, "r") as file:
            logs = json.load(file)

        if not logs:
            print("Nenhum log registrado.")
            return

        print("=== Logs Registrados ===")
        for log in logs:
            print(f"[{log['data_hora']}] {log['acao']}: {log['mensagem']}")
