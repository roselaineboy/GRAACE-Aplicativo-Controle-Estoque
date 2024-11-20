#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

class Def_Produto():
    def __init__(self, codigo=0, nome='', categoria='', valor_unitario=0.00, qtde_minimaestoque=0, saldo_estoque=0.00 ):
        self.__codigo = codigo
        self.__nome = nome
        self.__categoria = categoria
        self.__valorunitario = valor_unitario
        self.__qtde_minimaestoque = qtde_minimaestoque
        self.__saldo_estoque = saldo_estoque

    @property
    def codigo(self):
        return self.__codigo
  
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def categoria(self):
        return self.__categoria
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def valorunitario(self):
        return self.__valorunitario
    @valorunitario.setter
    def valorunitario(self, valorunitario):
        self.__valorunitario = valorunitario

    @property
    def qtde_minimaestoque(self):
        return self.__qtde_minimaestoque
    @qtde_minimaestoque.setter
    def qtde_minimaestoque(self, qtde_minimaestoque):
        self.__qtde_minimaestoque = qtde_minimaestoque
    
    @property
    def saldo_estoque(self):
        return self.__saldo_estoque
    @saldo_estoque.setter
    def saldo_estoque(self, saldo_estoque):
        self.__saldo_estoque = saldo_estoque

    def validar_conteudo(self):

        msg = ''
        if type(self.__codigo) != int and int(self.__codigo) <= 0:
            msg = msg + '\nO código deve ser um número maior que zero'

        if not self.__nome or len(self.__nome) == 0:
            msg = msg + '\nO nome deve ser preenchido'

        if not self.__categoria or len(self.__categoria) == 0:
            msg = msg + '\nA categoria deve ser preenchida'
        
        if type(self.__valorunitario) != float and float(self.__valorunitario) > 0.00:
            msg = msg + '\nO valor unitário deve ser um decimal maior que zero'

        if not self.__qtde_minimaestoque or len(self.__qtde_minimaestoque) >= 1:
            msg = msg + '\nA quantidade mínima em estoque deve ser maior que zero'

        if type(self.__saldo) != int or self.__saldo >= 0:
            msg = msg + '\nO saldo deve ser númerico maior que zero'

        return msg
    #Fim validar_conteudo

    def view(self):
        print(f'Código................: {self.__codigo}')
        print(f'Nome do Produto.......: {self.__nome}')
        print(f'Categoria.............: {self.__categoria}')
        print(f'Valor Unitário........: {self.__valorunitario}')
        print(f'Local de Armazenamento: {self.__localarmazenamento}')
    
    def __str__(self):
        self.view(self)
