#Programa desenvolvido por Gabriel. Andressa e Roselaine
#Data de Criação: 22/11/2024
#Curso: Pós Graduação em Ciência de Dados - FACENS
#Disciplina: Python
#Atividade: Trabalho Final
#Docente: Adriano V. S. da Silva

from classes.menu import Menu

if __name__ == '__main__':
    menu = Menu()
    produto = Produto()
    classes.minimo()
    
    while True:
        self.__opcao = opcao
        self.GF = GlobalFunctions()

        if operation == 0:
            print('Saindo :) ....')
            break
        
        elif operation == 1: #Adicionar Produto
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))
            minimo = int(input('Digite o minimo: '))
            produto.receber_dados_novo_produto(id, codigo, descricao, quantidade, minimo)

        elif operation == 2: #Visualizar Produto
            produto.view_produto()

        elif operation == 3: #Alterar estoque
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))
            minimo = int(input('Digite o minimo: '))
            produto.alterar_estoque(id, codigo, descricao, quantidade, minimo)

        elif operation == 4: #Remover estoque
            id = int(input('Digite o id: '))
            produto.remover(id)

        elif operation == 5: #Adiconar quantidade
            id = int(input('Digite o id: '))
            quantidade = int(input('Digite a quantidade: '))
            produto.adicionar_quantidade(id, quantidade)

        elif operation == 6: #Remover quantidade
            id = int(input('Digite o id: '))
            quantidade = int(input('Digite a quantidade: '))
            produto.remover_quantidade(id, quantidade)        
            
        elif operation == 7: #Log do estoque
            produto.log(id, nome)

        print(f'operacao escolhida ${operation}')