import json
import os
import time
import traceback

class Log:
    def __init__(self):
 #=============caminho================================================================= 
        self.diretorio_logs = "dados"
        os.makedirs(self.diretorio_logs, exist_ok=True)  # Garante que o diretório exista

        self.arquivo_log = os.path.join(self.diretorio_logs, "log.txt")
        self.arquivo_estoque = os.path.join(self.diretorio_logs, "log.json")

        print(f"Arquivo de log será salvo em: {self.arquivo_log}")
        print(f"Arquivo de modificações do estoque será salvo em: {self.arquivo_estoque}")
#============================================================================== 
#================registro_txt============================================================== 
    def registrar(self, tipo, mensagem):
        try:
            with open(self.arquivo_log, 'a') as f:
                f.write(f'{time.ctime()} - {tipo} - {mensagem}\n')
            print("Log TXT registrado com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar log TXT: {e}")
            self.registrar_erro(f"Erro ao registrar log TXT: {e}")
#============================================================================== 

    def registrar_modificacao_estoque(self, tipo_modificacao, produto):
        """Registrar modificações no estoque em um arquivo JSON."""
        modificacao = {
            'data': time.ctime(),
            'tipo_modificacao': tipo_modificacao,
            'codigo_produto': produto['codigo'],
            'nome_produto': produto['nome'],
            'quantidade': produto['quantidade'],
            'valor_unitario': produto['valor_unitario']
        }

        try:
        
            try:
                with open(self.arquivo_estoque, 'r') as f:
                    estoque_atual = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                estoque_atual = []
            estoque_atual.append(modificacao)
            with open(self.arquivo_estoque, 'w') as f:
                json.dump(estoque_atual, f, indent=4)
            print("Modificação de estoque registrada com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar modificação no estoque JSON: {e}")
            self.registrar_erro(f"Erro ao registrar modificação de estoque: {e}")
#============================================================================== 

    def registrar_erro(self, mensagem):
        """Registrar erros ou exceções no log."""
        try:
            erro = {
                'data': time.ctime(),
                'tipo': 'ERRO',
                'mensagem': mensagem,
                'detalhes': traceback.format_exc()
            }
            with open(self.arquivo_log, 'a') as f:
                f.write(f'{erro["data"]} - {erro["tipo"]} - {erro["mensagem"]}\n')
                f.write(f'Detalhes: {erro["detalhes"]}\n')
            print("Erro registrado no log.")
        except Exception as e:
            print(f"Erro ao salvar log de erro: {e}")
#============================================================================== 

    def exibir_logs(self):
        """Exibir todos os logs registrados no arquivo TXT."""
        try:
            with open(self.arquivo_log, 'r') as f:
                logs = f.readlines()
                if logs:
                    print("\nLogs registrados:")
                    for log in logs:
                        print(log.strip())
                else:
                    print("Nenhum log encontrado.")
        except FileNotFoundError:
            print("Arquivo de logs não encontrado.")
 #==============================================================================            

    def exibir_estoque(self):
        """Exibir o histórico de modificações do estoque."""
        try:
            with open(self.arquivo_estoque, 'r') as f:
                modificacoes = json.load(f)
                if modificacoes:
                    print("\nHistórico de modificações no estoque:")
                    for mod in modificacoes:
                        print(mod)
                else:
                    print("Nenhuma modificação registrada.")
        except FileNotFoundError:
            print("Arquivo de modificações no estoque não encontrado.")
