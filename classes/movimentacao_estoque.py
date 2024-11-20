#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from definicoes_de_tabelas.def_movimentacao import Def_Movimentacao_Estoque
from utils.bib import Funcao_Global
from definicoes_de_tabelas.def_movimentacao import Def_Movimentacao_Estoque
from utils.bib import Funcao_Global
from definicoes_de_tabelas.def_produto import DefProduto
from classes.log import Log  

class Movimentacao:
    def __init__(self):
        self.__produtos = []  
        self.__log = Log()    

    def adicionar_produto(self, produto):
        """Adiciona um novo produto ao estoque."""
        if isinstance(produto, DefProduto):
            self.__produtos.append(produto)
            self.__log.registrar("ADICIONAR", f"Produto {produto.nome} (Código {produto.codigo}) adicionado ao estoque.")
        else:
            self.__log.registrar("ERRO", "Tentativa de adicionar um objeto inválido ao estoque.")

    def listar_produtos(self):
        """Lista todos os produtos cadastrados no estoque."""
        if not self.__produtos:
            print("Nenhum produto cadastrado no estoque.")
            self.__log.registrar("LISTAR", "Tentativa de listar produtos em um estoque vazio.")
            return

        print("Produtos cadastrados no estoque:")
        for produto in self.__produtos:
            produto.view()

    def remover_produto(self, codigo):
        """Remove um produto do estoque pelo código."""
        for produto in self.__produtos:
            if produto.codigo == codigo:
                self.__produtos.remove(produto)
                self.__log.registrar("REMOVER", f"Produto {produto.nome} (Código {produto.codigo}) removido do estoque.")
                print(f"Produto com código {codigo} removido com sucesso.")
                return
        print(f"Produto com código {codigo} não encontrado.")
        self.__log.registrar("ERRO", f"Tentativa de remover produto com código {codigo}, que não existe no estoque.")

    def buscar_produto(self, codigo):
        """Busca um produto no estoque pelo código."""
        for produto in self.__produtos:
            if produto.codigo == codigo:
                print("Produto encontrado:")
                produto.view()
                self.__log.registrar("BUSCAR", f"Produto {produto.nome} (Código {produto.codigo}) encontrado.")
                return
        print(f"Produto com código {codigo} não encontrado.")
        self.__log.registrar("ERRO", f"Produto com código {codigo} não encontrado no estoque.")