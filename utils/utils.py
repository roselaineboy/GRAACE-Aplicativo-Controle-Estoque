import pandas as pd
from datetime import date
from configurations.config import Settings 

class Utils():
    def __init__(self):
        self.__configurations = Settings() 

    def ler_arquivo_json(self):
        # Acessa o arquivo de produtos a partir da configuração
        self.produto = pd.read_json(self.__configurations.produtos_repository)
        self.produto = self.produto.sort_values('id')
        return self.produto

    def ler_log_json(self):
        # Acessa o arquivo de log a partir da configuração
        self.logs = pd.read_json(self.__configurations.log_repository)
        return self.logs

    def escreve_arquivo_json(self):
        columns = ['id', 'codigo', 'descricao', 'quantidade', 'minimo']
        produto = pd.DataFrame(columns=columns)

        produto.to_json(self.__configurations.produtos_repository, index=False)

    def escreve_log_json(self):
        columns = ['Data', 'Ação', 'Item Alterado']
        logs = pd.DataFrame(columns=columns)

        logs.to_json(self.__configurations.log_repository, index=False)

    def atualiza_produto(self, id, codigo, descricao, quantidade, minimo):
        produto = self.ler_arquivo_json()
        logs = self.ler_log_json()

        data = {
            'id': [id],
            'codigo': [codigo],
            'descricao': [descricao],
            'quantidade': [quantidade],
            'minimo': [minimo]
        }

        new_line = pd.DataFrame(data)

        if int(id) not in produto['id'].values:
            print("ID inválido. Não foi possível encontrar o ID fornecido.")
        else:
            produto.loc[produto['id'] == id, 'codigo'] = codigo
            produto.loc[produto['id'] == id, 'descricao'] = descricao
            produto.loc[produto['id'] == id, 'quantidade'] = quantidade
            produto.loc[produto['id'] == id, 'minimo'] = quantidade

            produto.to_csv(self.__configurations.produtos_repository, index=False)

            # Gerando o log da ação
            logs_data = {'Data': [date.today()], 
                         'Ação': ['Atualização dos dados'],
                         'Item Alterado': [id]}
            
            new_line_logs = pd.DataFrame(logs_data)
            logs = pd.concat([logs, new_line_logs], ignore_index=True)
            logs.to_json(self.__configurations.log_repository, index=False)

    def adiciona_produto(self, id, codigo, descricao, quantidade, minimo):
        produto = self.ler_arquivo_json()
        logs = self.ler_log_json()

        data = {
            'id': [id],
            'codigo': [codigo],
            'descricao': [descricao],
            'quantidade': [quantidade],
            'minimo': [minimo]
        }
    
        new_line = pd.DataFrame(data)
        
        produto = pd.concat([produto, new_line], ignore_index=True)

        produto.to_json(self.__configurations.produtos_repository, index=False)
        
        logs_data = {
            'Data': [date.today()], 
            'Ação': ['Adição de um novo item'],
            'Item Alterado': [id]
        }
            
        new_line_logs = pd.DataFrame(logs_data)
        logs = pd.concat([logs, new_line_logs], ignore_index=True)
        logs.to_json(self.__configurations.log_repository, index=False)

    def remover_produto(self, id):
        logs = self.ler_log_json()
        produto = self.ler_arquivo_json()
        
        if id not in produto['id'].values:
            print("ID inválido. Não foi possível encontrar o ID fornecido.")
        else:
            ind = produto[produto['id'] == id].index
            produto = produto.drop(index=ind)
            produto.to_json(self.__configurations.produtos_repository, index=False)

            logs_data = {'Data': [date.today()], 
                         'Ação': ['Remoção de item'],
                         'Item Alterado': [id]}
            
            new_line_logs = pd.DataFrame(logs_data)
            logs = pd.concat([logs, new_line_logs], ignore_index=True)
            logs.to_json(self.__configurations.log_repository, index=False)

    def estoque_baixo(self):
        produto = self.ler_arquivo_json()
        baixo = produto[produto['quantidade'] <= produto['minimo']]

        if baixo.empty:
            print("Nenhum item abaixo da quantidade mínima.")
        else:
            print("Itens com estoque baixo:")
            print(baixo)

    def adicionar_quantidade(self, id, quantidade_adicional):
        logs = self.ler_log_json()
        produto = self.ler_arquivo_json()
        
        if id in produto['id'].values:
            produto.loc[produto['id'] == id, 'quantidade'] += quantidade_adicional
            produto.to_csv(self.__configurations.produtos_repository, index=False)
            print('Valor adicionado com sucesso')
            
            # Converter a quantidade adicional para string
            quantidade_adicional_str = str(quantidade_adicional)
            
            # Adicionar registro ao log
            logs_data = {
                'Data': [date.today()], 
                'Ação': ['subtraindo a quantidade ' + quantidade_adicional_str],
                'Item Alterado': [id]
            }
            
            new_line_logs = pd.DataFrame(logs_data)
            logs = pd.concat([logs, new_line_logs], ignore_index=True)
            logs.to_json(self.__configurations.log_repository, index=False)
        else:
            print(f"ID {id} não encontrado.")

    def remover_quantidade(self, id, subtrair_quantidade):
        logs = self.ler_log_json()
        produto = self.ler_arquivo_json()

        if id in produto['id'].values:
            produto.loc[produto['id'] == id, 'quantidade'] -= subtrair_quantidade
            
            if (produto.loc[produto['id'] == id, 'quantidade'] < 0).any():
                print("Erro: A quantidade não pode ser menor que zero. Nenhuma alteração necessária.")
            else:
                print(f"Quantidade subtraída do ID {id}.")
                produto.to_json(self.__configurations.produtos_repository, index=False)
                
                # Converter a quantidade subtraída para string
                subtrair_quantidade_str = str(subtrair_quantidade)
                
                # Adicionar registro ao log
                logs_data = {
                    'Data': [date.today()], 
                    'Ação': ['subtraindo a quantidade ' + subtrair_quantidade_str],
                    'Item Alterado': [id]
                }
                
                new_line_logs = pd.DataFrame(logs_data)
                logs = pd.concat([logs, new_line_logs], ignore_index=True)
                logs.to_json(self.__configurations.log_repository, index=False)
        else:
            print(f"ID {id} não encontrado.")

    def ver_produto(self):
        try:
            # Lê os produtos do arquivo JSON
            produto = self.ler_arquivo_json()
        
        #    Verifica se há produtos cadastrados
            if produto.empty:
                print("Nenhum produto cadastrado.")
            else:
                print("Produtos cadastrados:")
                print(produto.to_string(index=False))
        except Exception as e:
                print(f"Erro ao exibir os produtos: {e}")
