#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from utils.bib import Funcao_Global
from configuracoes.config import Definicao
from classes.produto import Produto
from classes.log import Log  
from datetime import datetime
import json
import pandas as pd


class Movimentacao():
    #==============================================================================
    def __init__(self):  
        self.__log = Log()
        self.bib = Funcao_Global()
        self.definicao = Definicao()
        self.__lista_movimentacoes = pd.DataFrame([])
    # Fim - init

    #==============================================================================
    def registrar_movimentacao_estoque(self, tipo_operacao, codigo, saldo_anterior, qtde_movimentada, saldo_final):
        modificacao = {
                        'data_movimentacao': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'tipo_operacao': tipo_operacao,
                        'codigo': codigo,
                        'saldo_anterior': str(saldo_anterior),
                        'qtde_movimentada': str(qtde_movimentada),
                        'saldo_final': str(saldo_final)
                      }
        
        arquivo_ok = ""
        arquivo_ok = self.bib.verifica_arquivo(self.definicao.db_movimentacoes)
        if arquivo_ok == '':
            try:
                with open(self.definicao.db_movimentacoes, 'a') as arquivo:
                    # Adicionar a linha de movimentação ao final do arquivo
                    arquivo.write(json.dumps(modificacao) + '\n')
                self.__log.registrar("Movimentacao do Estoque", f"o produto :{codigo} teve uma {tipo_operacao} de {qtde_movimentada}")
            except Exception as e:
                print(f"Erro ao salvar modificação no estoque JSON: {e}")
                input('...')
                self.__log.registrar('Movimentacao do Estoque', f"Erro ao registrar modificação de estoque: {e}")
    # Fim - registrar_movimentacao_estoque
                
    #==============================================================================
    def carrega_lista_movimentacoes(self, codigo = ''):
        caminho_arquivo = self.definicao.db_movimentacoes
        arquivo_ok = self.bib.verifica_arquivo(caminho_arquivo)

        if arquivo_ok == '':
            # se não for informado um codigo, leremos o arquivo inteiro
            if codigo == '':
                dados = pd.read_json(caminho_arquivo)
                if not dados.empty:
                    # Converte os dados para um DataFrame do pandas
                    self.__lista_movimentacoes = pd.DataFrame(dados)
            else:
                #se for informado um codigo, já leremos apenas as linhas do codigo enviado
                with open(caminho_arquivo, 'r') as f:
                    dados_filtrados = [
                        json.loads(linha)
                        for linha in f
                        if json.loads(linha)['codigo'].upper() == codigo.upper()
                    ]
                self.__lista_movimentacoes = pd.DataFrame(dados_filtrados)

    # Fim - carrega_lista_movimentacoes

    #==============================================================================
    def listar_movimentacoes_produto_por_codigo(self):
        msg_validacao = 'Informe o produto'
        codigo = ''
        prod = Produto()

        while msg_validacao != '' and codigo != '-1':
            self.bib.limpar_tela()
            prod.limpar_produto()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao == ''
            print('Ps.: para desistir digite -1 no código do produto')
            codigo = input('Código: ')

            produto_encontrado = prod.buscar_produto_por_codigo(codigo)

            if not produto_encontrado.empty:
                self.carrega_lista_movimentacoes(codigo)

                self.__lista_movimentacoes['data_movimentacao'] = pd.to_datetime(self.__lista_movimentacoes['data_movimentacao'])
                self.__lista_movimentacoes = self.__lista_movimentacoes.sort_values(by='data_movimentacao')

                self.bib.limpar_tela()
                print('Produto:')
                print(produto_encontrado)
                # Remover

                print('\nMovimentações:')
                print(self.__lista_movimentacoes)
                print('<ENTER> para prosseguir')
                input('...')
            else:
                self.bib.limpar_tela()
                msg_validacao= 'Produto não encontrado'

        del(prod)


    # Fim - listar_movimentacoes_produto_por_codigo
    #==============================================================================
    def entrada(self):
        self.movimentar('entrada')
    # Fim - entrada

    #==============================================================================
    def saida(self):
        self.movimentar('saída')
    # Fim - saida

    #==============================================================================
    def movimentar(self, tipo_operacao):
        msg_validacao = ''
        codigo = '000'
        prod = Produto()
        tem_saldo = True

        while codigo != '-1':
            self.bib.limpar_tela()
            prod.limpar_produto()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao == ''
                print('-' * 15)

            print('Ps.: para voltar ao MENU deixe o código do produto com -1 e pressione <ENTER>\n')
            print(f'Registrar movimentação de {tipo_operacao} de saldo do estoque.')
            codigo = ''
            codigo = input('Informe o Código: ')

            if codigo != '-1':
                
                produto_encontrado = prod.buscar_produto_por_codigo(codigo)

                if not produto_encontrado.empty:
                    prod.preencher_produto(produto_encontrado)
                    prod.ver_produto()

                    qtde_movimentada = input(f'Informe a quantidade de {tipo_operacao}:')

                    saldo_anterior = prod.saldo_produto_selecionado

                    if tipo_operacao == 'saída':
                        saldo_final = float(saldo_anterior) - float(qtde_movimentada)

                        if saldo_final < 0:
                            print(f'Não há saldo suficiente para a movimentação solicitada. Saldo Atual: {saldo_anterior}.')
                            resposta = input('Deseja ajustar a quantidade à movimentar para {saldo_anterior} e continuar a operação? (S/N)')
                            if resposta.upper() == 'S':
                                saldo_final = 0
                                qtde_movimentada = saldo_anterior
                                tem_saldo = True
                            else:
                                tem_saldo = False
                        else:
                            tem_saldo = True
                    else:
                        tem_saldo = True
                        saldo_final = float(saldo_anterior) + float(qtde_movimentada)

                    if tem_saldo:
                        prod.saldo_produto_selecionado = saldo_final
                        prod.atualizar_produto_na_lista()

                        self.registrar_movimentacao_estoque(tipo_operacao, codigo, saldo_anterior, qtde_movimentada, saldo_final)
                        prod.salva_lista_produto()

                        msg_validacao = 'Movimentação registrada com sucesso.'
                    else:
                        msg_validacao = 'Movimentação cancelada.'
            # fim - if codigo informado

        del(prod)

    # Fim - movimentar


