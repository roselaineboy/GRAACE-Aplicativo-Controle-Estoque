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
    def __init__(self):
        #self.__produtos = []  
        self.__log = Log()
        self.bib = Funcao_Global()
        self.definicao = Definicao()
        self.__lista_movimentacoes = pd.DataFrame([])


    #def adicionar_produto(self, produto):
    #    """Adiciona um novo produto ao estoque."""
    #    if isinstance(produto, Def_Produto):
    #        self.__produtos.append(produto)
    #        self.__log.registrar("ADICIONAR", f"Produto {produto.nome} (Código {produto.codigo}) adicionado ao estoque.")
    #    else:
    #        self.__log.registrar("ERRO", "Tentativa de adicionar um objeto inválido ao estoque.")

    #def listar_produtos(self):
    #    """Lista todos os produtos cadastrados no estoque."""
    #    if not self.__produtos:
    #        print("Nenhum produto cadastrado no estoque.")
    #        self.__log.registrar("LISTAR", "Tentativa de listar produtos em um estoque vazio.")
    #        return
    #    print("Produtos cadastrados no estoque:")
    #    for produto in self.__produtos:
    #        produto.view()

    #def remover_produto(self, codigo):
    #    """Remove um produto do estoque pelo código."""
    #    for produto in self.__produtos:
    #        if produto.codigo == codigo:
    #            self.__produtos.remove(produto)
    #            self.__log.registrar("REMOVER", f"Produto {produto.nome} (Código {produto.codigo}) removido do estoque.")
    #            print(f"Produto com código {codigo} removido com sucesso.")
    #            return
    #    print(f"Produto com código {codigo} não encontrado.")
    #    self.__log.registrar("ERRO", f"Tentativa de remover produto com código {codigo}, que não existe no estoque.")

    #def buscar_produto(self, codigo):
    #    """Busca um produto no estoque pelo código."""
    #    for produto in self.__produtos:
    #        if produto.codigo == codigo:
    #            print("Produto encontrado:")
    #            produto.view()
    #            self.__log.registrar("BUSCAR", f"Produto {produto.nome} (Código {produto.codigo}) encontrado.")
    #            return
    #    print(f"Produto com código {codigo} não encontrado.")
    #    self.__log.registrar("ERRO", f"Produto com código {codigo} não encontrado no estoque.")

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

                #movimentacoes_encontradas = self.__lista_movimentacoes[self.__lista_movimentacoes['codigo'].str.upper() == codigo.upper()]
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
        msg_validacao = 'Informe o produto'
        codigo = ''
        prod = Produto()

        while msg_validacao != '' and codigo == '':
            self.bib.limpar_tela()
            prod.limpar_produto()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao == ''
            print('Registrar movimentação de ENTRADA de saldo no estoque.')
            print('Ps.: para voltar ao MENU deixe o código do produto vazio e pressione <ENTER>')
            codigo = input('Código: ')

            if codigo != '':
                produto_encontrado = prod.buscar_produto_por_codigo(codigo)

                if not produto_encontrado.empty:
                    prod.preencher_produto(produto_encontrado)
                    prod.ver_produto()

                    qtde_movimentada = input('Informe a quantidade de entrada:')

                    saldo_anterior = prod.saldo_produto_selecionado
                    saldo_final = float(saldo_anterior) + float(qtde_movimentada)

                    prod.saldo_produto_selecionado = saldo_final
                    prod.atualizar_produto_na_lista()

                    self.registrar_movimentacao_estoque('entrada', codigo, saldo_anterior, qtde_movimentada, saldo_final)
                    prod.salva_lista_produto()

                    prod.listar_produtos()

                    msg_validacao = 'Movimentação registrada com sucesso.'
            # fim - if codigo informado

        del(prod)


    # Fim - buscar_produto_por_codigo


