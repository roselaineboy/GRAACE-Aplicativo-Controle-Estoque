#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva
from classes.menu import Menu
from classes.produto import Produto
from utils.bib import GlobalFunctions

if __name__ == '__main__':
    menu = Menu()
    produto = Produto()
    produto.estoque_baixo()
    
    while True:
        menu.show_menu()
        operation = menu.selecionar_operacao()
        menu.GF.limpar_tela()

        if operation == 0:
            print('Sistema finalizado...')
            break
        
        elif operation == 1: # Adicionar Produto
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))
            minimo = int(input('Digite o minimo: '))
            produto.receber_dados_novo_produto(id, codigo, descricao, quantidade, minimo)

        elif operation == 2: # ver o estoque
            produto.ver_produto()

        elif operation == 3: # alterar valor
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))
            minimo = int(input('Digite o minimo: '))
            produto.alterar_estoque(id, codigo, descricao, quantidade, minimo)

        elif operation == 4: #remover produto
            id = int(input('Digite o id: '))
            produto.remover(id)

        elif operation == 5: #adicionar quantidade
            id = int(input('Digite o id: '))
            quantidade = int(input('Digite a quantidade: '))
            produto.adicionar_quantidade(id, quantidade)

        elif operation == 6: #retirar quantidade
            id = int(input('Digite o id: '))
            quantidade = int(input('Digite a quantidade: '))
            produto.remover_quantidade(id, quantidade)

        elif operation == 7: # log de Movimentação
            produto.log()