class DefProduto():
    def __init__(self, codigo=0, nome='', categoria='', valor_unitario=0.00, local_armazenamento=''):
        self.__codigo = codigo
        self.__nome = nome
        self.__categoria = categoria
        self.__valorunitario = valor_unitario
        self.__localarmazenamento = local_armazenamento

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
    def localarmazenamento(self):
        return self.__localarmazenamento
    @localarmazenamento.setter
    def localarmazenamento(self, localarmazenamento):
        self.__localarmazenamento = localarmazenamento
    
    def validar_conteudo(self):

        msg = ''
        if type(self.__codigo) != int and int(self.__codigo) <= 0:
            msg = msg + '\nO código deve ser um número maior que zero'

        if not self.__nome or len(self.__nome) == 0:
            msg = msg + '\nO nome deve ser preenchido'

        if not self.__nome or len(self.__nome) == 0:
            msg = msg + '\nO nome deve ser preenchido'

        if not self.__categoria or len(self.__categoria) == 0:
            msg = msg + '\nA categoria deve ser preenchida'
        
        if not self.__localarmazenamento or len(self.__localarmazenamento) == 0:
            msg = msg + '\nO local de armazenamento deve ser preenchido'

        if type(self.__valorunitario) != float and float(self.__valorunitario) <= 0:
            msg = msg + '\nO valor unitário deve ser um decimal maior que zero'

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
