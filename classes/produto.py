from utils.bib import GlobalFunctions
from utils.utils import Utils

class Produto:
    def __init__(self):
        self.__gf = GlobalFunctions()
        self.__produto = Utils()

    def ver_produto(self):
        self.__produto.ver_produto()

    def receber_dados_novo_produto(self):
        msg_validacao = 'Informe os dados do produto'

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
        self.__produto.remover(id)
        
    def adicionar_quantidade(self, id, quantidade):
        self.__produto.adicionar_quantidade(id, quantidade)
    
    def remover_quantidade(self, id, quantidade):
        self.__produto.remover_quantidade(id, quantidade)
        
    def log(self):
        log = self.__produto.ler_log_json()
        print("Data       | Ação        | Item Alterado")
        print("-" * 45)
        for ind, row in log.iterrows():
            print(f"{row['Data']:<10}| {row['Ação']:<12}| {row['Item Alterado']}")
    
    def estoque_baixo(self):
        self.__produto.estoque_baixo() 
