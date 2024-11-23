#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva


import pandas as pd
import json
from definicoes_de_tabelas.def_produto import Def_Produto
from utils.bib import Funcao_Global
from configuracoes.config import Definicao
from classes.log import Log

class Produto():
    #==============================================================================
    def __init__(self):
        self.__produto = Def_Produto()
        self.bib = Funcao_Global()
        self.definicao = Definicao()
        self.__lista_produtos = pd.DataFrame([])
        self.carrega_lista_produto()
        self.log = Log()
    #Fim - init

    #==============================================================================
    @property
    def produto_selecionado(self):
        return self.__produto

    #==============================================================================
    @property
    def saldo_produto_selecionado(self):
        return self.__produto.saldo_estoque
    @saldo_produto_selecionado.setter
    def saldo_produto_selecionado(self, saldo_estoque):
        self.__produto.saldo_estoque = saldo_estoque

    #==============================================================================
    def carrega_lista_produto(self, codigo=''):
        caminho_arquivo = self.definicao.db_produtos
        arquivo_ok = self.bib.verifica_arquivo(caminho_arquivo)

        if arquivo_ok == '':
            # se não for informado um codigo, leremos o arquivo inteiro
            if codigo == '':
                dados = pd.read_json(caminho_arquivo)
                if not dados.empty:
                    # Converte os dados para um DataFrame do pandas
                    self.__lista_produtos = pd.DataFrame(dados)
            else:
                #se for informado um codigo, já leremos apenas as linhas do codigo enviado
                with open(caminho_arquivo, 'r') as f:
                    dados_filtrados = [
                        json.loads(linha)
                        for linha in f
                        if json.loads(linha)['codigo'].upper() == codigo.upper()
                    ]
                self.__lista_produtos = pd.DataFrame(dados_filtrados)

    # Fim - carrega_lista_produto

    #==============================================================================
    def salva_lista_produto(self):
        msg_retorno = ''
        caminho_arquivo = self.definicao.db_produtos
        try:
            with open(caminho_arquivo, 'w') as arquivo:
                self.__lista_produtos.to_json(caminho_arquivo, orient='records', indent=4)
        except Exception as e:
            msg_retorno = f"Erro ao salvar o arquivo: {e}"
            self.log.registrar_erro(msg_retorno)
        return msg_retorno
    # Fim - salva_lista_produto

    #==============================================================================
    def buscar_produto_por_codigo(self, codigo=""):
        # Buscar o produto pelo código
        produto = self.__lista_produtos[self.__lista_produtos['codigo'].str.upper() == codigo.upper()].copy()
        return produto
    # Fim - buscar_produto_por_codigo

    #==============================================================================
    def preencher_produto(self, produto):
        if isinstance(produto, pd.DataFrame):
            self.__produto.codigo = produto.iloc[0].codigo
            self.__produto.nome = produto.iloc[0].nome
            self.__produto.categoria = produto.iloc[0].categoria
            self.__produto.valorunitario = produto.iloc[0].valor_unitario
            self.__produto.qtde_minimaestoque = produto.iloc[0].qtde_minimaestoque
            self.__produto.saldo_estoque = produto.iloc[0].saldo_estoque
        else:
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
    def atualizar_produto_na_lista(self):
        # Atualiza os dados do produto no DataFrame
        self.__lista_produtos.loc[self.__lista_produtos['codigo'] == self.__produto.codigo, 'nome'] = self.__produto.nome
        self.__lista_produtos.loc[self.__lista_produtos['codigo'] == self.__produto.codigo, 'categoria'] = self.__produto.categoria
        self.__lista_produtos.loc[self.__lista_produtos['codigo'] == self.__produto.codigo, 'valor_unitario'] = self.__produto.valorunitario
        self.__lista_produtos.loc[self.__lista_produtos['codigo'] == self.__produto.codigo, 'qtde_minimaestoque'] = self.__produto.qtde_minimaestoque
        self.__lista_produtos.loc[self.__lista_produtos['codigo'] == self.__produto.codigo, 'saldo_estoque'] = self.__produto.saldo_estoque
    # Fim - atualizar_produto_na_lista

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
                self.log.registrar("ADICIONAR", f"Produto {self.__produto.codigo} adicionado.")
            if self.__produto.codigo == '-1':
                msg_validacao = ''
            elif not produto_existe:
                msg_validacao = self.__produto.validar_conteudo()
                if msg_validacao == "":
                    self.__lista_produtos = pd.concat([self.__lista_produtos, pd.DataFrame(self.__produto.linha_produto)], ignore_index=True)

                    msg_validacao = self.salva_lista_produto()
                    if msg_validacao == "":
                        self.ver_produto()
                        print('Produto incluido com sucesso, pressione <ENTER> para iniciar a inclusão de novo produto.')
                        msg_validacao = input('')
                        if msg_validacao == "-1":
                            msg_validacao = ''
                        else:
                            msg_validacao = 'Informe os dados do produto'
                    
        # fim - while
        self.bib.limpar_tela()

        return
    # Fim - Cadastro Produto

    #==============================================================================    
    def atualizar_produto(self):
        msg_validacao = 'Informe os dados do produto para atualização'  # Inicializa a variável antes de usar

        while msg_validacao != '':  # A condição de repetição
            self.bib.limpar_tela()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao = ''  # Reinicializa a mensagem de validação

            print('Ps.: para desistir digite -1 no código do produto e deixe os demais campos em branco')

            self.limpar_produto()
            self.__produto.codigo = input('Código do produto a ser atualizado: ')

            # Verifica se o usuário quer desistir
            if self.__produto.codigo == '-1':
                print('Operação cancelada. Retornando ao menu...')
                break

            # Buscar o produto pelo código
            produtosencontrados = self.buscar_produto_por_codigo(self.__produto.codigo)
            self.log.registrar("BUSCA", f"Buscando produto com código {self.__produto.codigo}")

            if produtosencontrados.empty:
                print('Produto não encontrado.')
                print('<ENTER> para tentar outro código')
                input('...')
                msg_validacao = 'Produto não encontrado, escolha outro código.'  # Mensagem de erro
            else:
                produto_atualizado = produtosencontrados.iloc[0]  # Pega a primeira linha do produto encontrado

                self.preencher_produto(produtosencontrados)
                self.ver_produto()

                print('\nVocê pode atualizar os campos com novos conteúdos, e deixar em branco os que quiser manter o conteúdo atual:')

                # Exibe os campos atuais e permite a alteração
                nome_atualizado = input(f'Nome (atual: {produto_atualizado["nome"]}): ')
                categoria_atualizada = input(f'Categoria (atual: {produto_atualizado["categoria"]}): ')
                valor_unitario_atualizado = input(f'Valor Unitário (atual: {produto_atualizado["valor_unitario"]}): ')
                qtde_minimaestoque_atualizada = input(f'Quantidade Mínima de Estoque (atual: {produto_atualizado["qtde_minimaestoque"]}): ')

                # Se o usuário deixar os campos em branco, manterá o valor atual
                self.__produto.nome = nome_atualizado if nome_atualizado else produto_atualizado['nome']
                self.__produto.categoria = categoria_atualizada if categoria_atualizada else produto_atualizado['categoria']
                self.__produto.valorunitario = valor_unitario_atualizado if valor_unitario_atualizado else produto_atualizado['valor_unitario']
                self.__produto.qtde_minimaestoque = qtde_minimaestoque_atualizada if qtde_minimaestoque_atualizada else produto_atualizado['qtde_minimaestoque']
                # Não se pode mexer no saldo assim, apenas através das movimentações de entrada e saída, o saldo será mantido o mesmo.
                self.__produto.saldo_estoque = produto_atualizado['saldo_estoque']

                msg_validacao = self.__produto.validar_conteudo()  # Validação do conteúdo do produto

                if msg_validacao == "":  # Se não houver erros de validação
                    # Atualiza os dados do produto no DataFrame
                    self.atualizar_produto_na_lista()

                    # Salva os dados atualizados no arquivo JSON
                    msg_validacao = self.salva_lista_produto()  # Salva no arquivo
                    if msg_validacao == "":
                        produto_atualizado_data = {
                            'codigo': self.__produto.codigo,
                            'nome': self.__produto.nome,
                            'categoria': self.__produto.categoria,
                            'valor_unitario': self.__produto.valorunitario,
                            'qtde_minimaestoque': self.__produto.qtde_minimaestoque,
                            'saldo_estoque': self.__produto.saldo_estoque
                        }

                        # Registrar a modificação no log
                        self.log.registrar("ATUALIZAR", f"Produto {self.__produto.codigo} atualizado com sucesso.")
                        print(f'Produto {self.__produto.codigo} atualizado com sucesso!')
                    else:
                        print('Erro ao atualizar o produto.')

            # Fim if produto encontrado

        # fim while
        #fim atualizar produto
    #==============================================================================    
    def deletar_produto(self):
        msg_validacao = 'Informe o código do produto a ser deletado'  # Mensagem inicial de validação

        while True:  # Loop para permitir várias tentativas até uma saída válida
            self.bib.limpar_tela()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao = ''  # Reinicializa a mensagem de validação

            print('Ps.: para desistir digite -1 no código do produto')

            self.limpar_produto()
            self.__produto.codigo = input('Código do produto a ser deletado: ')

            # Se o código for '-1', interrompe a operação
            if self.__produto.codigo == '-1':
                print('Operação de deletação cancelada.')
                break  # Sai do loop e encerra o método

            # Buscar o produto pelo código
            produtosencontrados = self.buscar_produto_por_codigo(self.__produto.codigo)

            if produtosencontrados.empty:
                print('Produto não encontrado.')
                print('<ENTER> para tentar outro código')
                input('...')
                msg_validacao = 'Produto não encontrado, escolha outro código.'  # Mensagem de erro
            else:
                produto_deletado = produtosencontrados.iloc[0]  # Pega a primeira linha do produto encontrado
                print(f'Produto encontrado: {produto_deletado["nome"]}')
                confirmacao = input('Tem certeza que deseja deletar este produto? (S/N): ')

                if confirmacao.upper() == 'S':
                # Deleta o produto da lista
                    self.__lista_produtos = self.__lista_produtos[self.__lista_produtos['codigo'] != self.__produto.codigo]
                
                # Salva a lista atualizada no arquivo JSON
                    msg_validacao = self.salva_lista_produto()  # Salva no arquivo
                
                    if msg_validacao == "":
                        produto_deletado_data = {
                            'codigo': produto_deletado['codigo'],
                            'nome': produto_deletado['nome'],
                            'categoria': produto_deletado['categoria'],
                            'valor_unitario': produto_deletado['valor_unitario'],
                            'qtde_minimaestoque': produto_deletado['qtde_minimaestoque'],
                            'saldo_estoque': produto_deletado['saldo_estoque']
                        }
                    
                    # Registrar a modificação no log
                        self.log.registrar('Remover', produto_deletado_data)
                        self.log.registrar("DELETAR", f"Produto {self.__produto.codigo} deletado com sucesso.")
                        print(f'Produto {self.__produto.codigo} deletado com sucesso!')
                    else:
                        print('Erro ao deletar o produto.')
                    break  # Sai do loop após deletar o produto com sucesso
                else:
                    print('Operação de deletação cancelada.')
                    msg_validacao = ''  # Cancela a operação, mas reinicia a busca

            self.bib.limpar_tela()
    # Fim - deletar produto
