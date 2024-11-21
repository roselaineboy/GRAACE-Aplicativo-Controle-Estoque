import pandas as pd
import json

from definicoes_de_tabelas.def_produto import Def_Produto
from utils.bib import Funcao_Global
from configuracoes.config import Definicao

class Produto():
    #==============================================================================
    def __init__(self):
        self.__produto = Def_Produto()
        self.bib = Funcao_Global()
        self.definicao = Definicao()
        self.__lista_produtos = pd.DataFrame([])
        self.carrega_lista_produto()
    #Fim - init

    #==============================================================================
    def carrega_lista_produto(self):
        caminho_arquivo = self.definicao.db_produtos
        arquivo_ok = self.bib.verifica_arquivo(caminho_arquivo)

        if arquivo_ok == '':
            dados = pd.read_json(caminho_arquivo)
            if not dados.empty:
                # Converte os dados para um DataFrame do pandas
                self.__lista_produtos = pd.DataFrame(dados)
    # fim - carrega_lista_produto

    #==============================================================================
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

    #==============================================================================
    def buscar_produto_por_codigo(self, codigo="A001"):
        # Buscar o produto pelo código
        produto = self.__lista_produtos[self.__lista_produtos['codigo'].str.upper() == codigo.upper()]
        return produto
    # Fim buscar_produto_por_codigo

    #==============================================================================
    def preencher_produto(self, produto):
        self.__produto.codigo = produto['codigo'][0]
        self.__produto.nome = produto['nome'][0]
        self.__produto.categoria = produto['categoria'][0]
        self.__produto.valorunitario = produto['valor_unitario'][0]
        self.__produto.qtde_minimaestoque = produto['qtde_minimaestoque'][0]
        self.__produto.saldo_estoque = produto['saldo_estoque'][0]
    # Fim - preencher_produto

    #==============================================================================
    def limpar_produto(self):
        self.__produto.codigo = ''
        self.__produto.nome = ''
        self.__produto.categoria = ''
        self.__produto.valorunitario = 0
        self.__produto.qtde_minimaestoque = 0
        self.__produto.saldo_estoque = 0
    # Fim - limpar_produto

    #==============================================================================
    def ver_produto(self):
        self.bib.limpar_tela()
        self.__produto.view()
    # Fim - ver_produto

    #==============================================================================
    def cadastrar_produto(self):
        msg_validacao = 'Informe os dados do produto'
        produto_existe = False

        while msg_validacao != '':
            self.bib.limpar_tela()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao == ''
            print('Ps.: para desistir digite -1 no código do produto e deixe os demais campos em branco')
            self.limpar_produto();
            self.__produto.codigo = input('Código: ')

            produtosencontrados = self.buscar_produto_por_codigo(self.__produto.codigo)

            # Verificar se o produto foi encontrado
            if not produtosencontrados.empty:
                produto_existe = True
                print('Produto já cadastrado:')
                print(produtosencontrados)
                print('<ENTER> para tentar outro código')
                input('...')
                msg_validacao = 'Produto já cadastrado, escolha outro código.'
            else:
                produto_existe = False

            if self.__produto.codigo != '-1' and not produto_existe:
                self.__produto.nome = input('Nome: ')
                self.__produto.categoria = input('Categoria: ')
                self.__produto.valorunitario = input('Valor Unitário: ')
                self.__produto.qtde_minimaestoque = input('Quantidade Minima de Estoque: ')
                self.__produto.saldo_estoque = input('Saldo Inicial do Estoque: ')
            
            if self.__produto.codigo == '-1':
                msg_validacao = ''
            elif not produto_existe:
                msg_validacao = self.__produto.validar_conteudo()
                if msg_validacao == "":
                    self.__lista_produtos = pd.concat([self.__lista_produtos, pd.DataFrame(self.__produto.linha_produto)], ignore_index=True)
                    msg_validacao = self.salva_lista_produto()
                    if msg_validacao == "":
                        self.ver_produto()
                        print('Produto incluido com sucesso, pressione <ENTER> para iniciar a inclusão de novo produto, ou MENU para voltar ao menu')
                        msg_validacao = input('')
                        if msg_validacao.upper == "MENU":
                            msg_validacao = ''
                        else:
                            msg_validacao = 'Informe os dados do produto'
        # fim - while
        self.bib.limpar_tela()

        return
    # fim Cadastro Produto

    #==============================================================================
    def atualizar_produto(self):
        print('executou atualizar_produto')

    # Fim - atualizar_produto

    #==============================================================================
    def deletar_produto(self):
        print('executou deletar_produto')
    # Fim - deletar_produto

    #==============================================================================
    def listar_produtos(self):
        self.bib.limpar_tela()
        print(self.__lista_produtos)
        print('Pressione <ENTER> para para voltar ao menu')
        input('...')
    # Fim - listar_produto
