from entities.def_produto import DefProduto
from utils.bib import GlobalFunctions

class Produto():
    def __init__(self):
        self.__produto = DefProduto()
        self.__gf = GlobalFunctions()
    
    def view_produto(self):
        self.__produto.view()

    def receber_dados_novo_produto(self):
        msg_validacao = 'Informe os dados do Produtos'

        while msg_validacao != '':
            self.__gf.limpar_tela()

            if len(msg_validacao) > 0:
                print(msg_validacao)
                msg_validacao == ''
            print('Ps.: para desistir digite -1 no código do produto e deixe os demais campos em branco')
            self.__produto.codigo = input('Código: ')
            if self.__produto.codigo != '-1':
                self.__produto.nome = input('Nome: ')
                self.__produto.categoria = input('Categoria: ')
                self.__produto.localarmazenamento = input('Local de Armazenamento: ')
                self.__produto.valorunitario = input('Valor Unitário: ')
            
            if self.__produto.codigo == '-1':
                msg_validacao = ''
            else:
                msg_validacao = self.__produto.validar_conteudo()

        # fim - while
        self.__gf.limpar_tela()

        if msg_validacao == "":
            self.view_produto()
            input('<ENTER>')
            self.__gf.limpar_tela()

        return "Produto cadastrado"

    def minimo(self):
        pass

    def alterar_estoque(self):
        pass

    def remover(self):
        self.__utils.remover(id)
        
    def adicionar_quantidade(self):
        pass
        
    def remover_quantidade(self):
        pass
        
    def log(self):
        pass