#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

class Def_Movimentacao_Estoque():
    #==============================================================================
    def __init__(self, codigo=0, tipo_operacao='Entrada', data_movimentacao=None\
                    , saldo_anterior=0, qtde_movimentada=0, saldo_final=0 ):
        self.__codigo = codigo
        self.__tipo_operacao = tipo_operacao
        self.__data_movimentacao = data_movimentacao
        self.__saldo_anterior = saldo_anterior
        self.__qtde_movimentada = qtde_movimentada
        self.__saldo_final = saldo_final
    # Fim - init        

    #==============================================================================
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    #==============================================================================
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    #==============================================================================
    @property
    def categoria(self):
        return self.__categoria
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    #==============================================================================
    @property
    def valorunitario(self):
        return self.__valorunitario
    @valorunitario.setter
    def valorunitario(self, valorunitario):
        self.__valorunitario = valorunitario

    #==============================================================================
    @property
    def qtde_minimaestoque(self):
        return self.__qtde_minimaestoque
    @qtde_minimaestoque.setter
    def qtde_minimaestoque(self, qtde_minimaestoque):
        self.__qtde_minimaestoque = qtde_minimaestoque
    
    #==============================================================================
    @property
    def saldo_estoque(self):
        return self.__saldo_estoque
    @saldo_estoque.setter
    def saldo_estoque(self, saldo_estoque):
        self.__saldo_estoque = saldo_estoque

    #==============================================================================
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
    # Fim - validar_conteudo

    #==============================================================================
    def view(self):
        print(f'Código................: {self.__codigo}')
        print(f'Nome do Produto.......: {self.__nome}')
        print(f'Categoria.............: {self.__categoria}')
        print(f'Valor Unitário........: {self.__valorunitario}')
        print(f'Local de Armazenamento: {self.__localarmazenamento}')
    # Fim - view
    
    #==============================================================================
    def __str__(self):
        self.view(self)
    # Fim - str        
