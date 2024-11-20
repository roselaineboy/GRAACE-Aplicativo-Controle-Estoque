import pandas as pd
import json

from definicoes_de_tabelas.def_produto import Def_Produto
from utils.bib import Funcao_Global
from configuracoes.config import Definicao

class Produto():
    def __init__(self):
        self.__produto = Def_Produto()
        self.bib = Funcao_Global()
        self.definicao = Definicao()
        self.__lista_produtos = pd.DataFrame([])
        self.carrega_lista_produto()

    def carrega_lista_produto(self):
        caminho_arquivo = self.definicao.db_produtos
        arquivo_ok = self.bib.verifica_arquivo(caminho_arquivo)

        if arquivo_ok == '':
            dados = pd.read_json(caminho_arquivo)
            if not dados.empty:
                # Converte os dados para um DataFrame do pandas
                self.__lista_produtos = pd.DataFrame(dados)
    # fim - carrega_lista_produto

    def salva_lista_produto(self):
        msg_retorno = ''
        caminho_arquivo = self.definicao.db_produtos
        try:
            with open(caminho_arquivo, 'w') as arquivo:
                self.__lista_produtos.to_json(caminho_arquivo, orient='records', indent=4)
        except Exception as e:
            msg_retorno = f"Erro ao salvar o arquivo: {e}"
        return msg_retorno
    # Fim - salva_lista_produto


    def ver_produto(self):
        self.bib.limpar_tela()
        self.__produto.view()

    def cadastrar_produto(self):
        msg_validacao = 'Informe os dados do produto'

        while msg_validacao != '':
            self.bib.limpar_tela()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao == ''
            print('Ps.: para desistir digite -1 no código do produto e deixe os demais campos em branco')
            self.__produto.codigo = input('Código: ')
            if self.__produto.codigo != '-1':
                self.__produto.nome = input('Nome: ')
                self.__produto.categoria = input('Categoria: ')
                self.__produto.valorunitario = input('Valor Unitário: ')
                self.__produto.qtde_minimaestoque = input('Quantidade Minima de Estoque: ')
                self.__produto.saldo_estoque = input('Saldo Inicial do Estoque: ')
            
            if self.__produto.codigo == '-1':
                msg_validacao = ''
            else:
                msg_validacao = self.__produto.validar_conteudo()
                if msg_validacao == "":
                    self.__lista_produtos = pd.concat([self.__lista_produtos, pd.DataFrame(self.__produto.linha_produto)], ignore_index=True)
                    msg_validacao = self.salva_lista_produto()
                    if msg_validacao == "":
                        self.ver_produto()
                        print('Produto incluido com sucesso, pressione <ENTER> para iniciar a inclusão de novo produto, ou MENU para voltar ao menu')
                        msg_validacao = input('')
                        if msg_validacao == "MENU":
                            msg_validacao = ''
                        else:
                            msg_validacao = 'Informe os dados do produto'
        # fim - while
        self.bib.limpar_tela()

        return
    # fim Cadastro Produto

    def atualizar_produto(self):
        print('executou atualizar_produto')

    def deletar_produto(self):
        print('executou deletar_produto')

    def listar_produtos(self):
        self.bib.limpar_tela()
        print(self.__lista_produtos)
        print('Pressione <ENTER> para para voltar ao menu')
        input('...')
        
