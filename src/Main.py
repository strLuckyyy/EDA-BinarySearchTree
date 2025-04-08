from BinarySearchTree import BinarySearchTree
import os
from Node import Node

if __name__ == "__main__":

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def wait():
        input('\n\nPressione Enter para continuar...')
        clear()




    def montar_menu():
        opções = [
            'Buscar Nodo',
            'Inserir Nodo',
            'Deletar Nodo',
            'Mostrar Pré-Ordem',
            'Mostrar Em Ordem',
            'Mostrar Pós-Ordem',
            'Ordem em Nível',
            'Contar Internos',
            'Achar Grau',
            'Achar Altura',
            'Achar Nível',
            'Achar Ancestrais',
            'Árvore Está Vazia',
            'Limpar Árvore'
        ]

        lista_menu = '-' * 65 + '\n' + '|' + ' ' * 63 + '|'


        for i in range(len(opções)):
            if (i+1) % 2 == 0:
                #if len(opções) < 30:
                #    opções[i] += (' ') * (30-len(opções))
                #lista_menu += str(f'\t(                              )\n')
                lista_menu += f'{i+1} - {opções[i]}\t|\n|'
                lista_menu += ' ' *63 + '|'
            else:
                opções[i] += (' ') * (15-len(opções[i]))
                #lista_menu += str(f'\n(                              )\t|')
                lista_menu += f'\n|\t{i+1} - {opções[i]}\t|\t'
        
        lista_menu += '\n'+ '-' * 65

        return lista_menu




    def set_key(func):
        k = input(f'\nQual a chave que deseja {func}?\n\n')
        if k.isnumeric() == False:
            print('\nChaves podem ser apenas números\n')
            wait()
            return 0
        else:
            return int(k)




    def set_value():
        v = input(f'\nQual o valor desejado?\n\n')
        if v.isnumeric() == False:
            print('\nValores podem ser apenas números\n')
            wait()
            return 0
        else:
            return int(v)




    def menu(ops):

        clear()

        print('\tEscolha uma opção digitando o número da opção desejada\n')

        print(ops+'\n')

        o = (input())

        if o.isnumeric() == False:
                
                print('\nDigite um número presente na lista\n')

                wait()

                return 0
        
        if 0 >= int(o) or int(o) > 14:
                
                print('\nDigite um número presente na lista\n')

                wait()

                return 0
        
        return int(o)


    def main():

        bst = BinarySearchTree()
      
        clear()

        op_menu = 0

        lista_menu = montar_menu()


        while op_menu != 'out':

            while op_menu == 0:

                op_menu = menu(lista_menu)

            while op_menu == 1:

                clear()

                if bst.is_empty() == False:

                    value = bst.search(set_key('buscar'))

                    if value == None:

                        print('\nNenhum nodo com essa chave foi encontrado.')

                    else:

                        clear()

                        print(f'\nO nodo da chave indicada tem valor {value}.')

                    wait()

                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 2:

                clear()

                bst.insert(set_key('inserir'), set_value())

                op_menu = menu(lista_menu)

            while op_menu == 3:

                clear()

                if bst.is_empty() == False:

                    if bst.delete(set_key('deletar')) == True:

                        print('\nNodo deletado com sucesso.')

                        wait()

                    else:

                        print('\nNenhum nodo com essa chave foi encontrado.')

                        wait()

                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 4:

                clear()

                if bst.is_empty() == False:

                    bst.pre_order_traversal()

                    wait()
                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 5:

                clear()

                if bst.is_empty() == False:

                    bst.in_order_traversal()

                    wait()

                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 6:

                clear()

                if bst.is_empty() == False:

                    bst.post_order_traversal()

                    wait()
                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 7:

                clear()

                if bst.is_empty() == False:

                    bst.level_order_traversal()

                    wait()
                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 8:

                clear()

                if bst.is_empty() == False:

                    bst.count_internal()

                    wait()

                
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 9:

                clear()

                if bst.is_empty() == False:

                    print(bst.degree(set_key('encontrar o grau')))

                    wait()
                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)
    
            while op_menu == 10:

                clear()

                if bst.is_empty() == False:

                    temp = bst.height(set_key('encontrar a altura'))

                    if temp != -1:

                        print(f'A altura do nodo da chave desejada é {temp}.')

                    else:

                        print('\nNenhum nodo com essa chave foi encontrado.')

                    wait()

                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 11:

                clear()

                if bst.is_empty() == False:

                    temp = bst.level(set_key('encontrar o nível'))

                    if temp != -1:

                        print(f'O nível do nodo da chave desejada é {temp}.')

                    else:

                        print('\nNenhum nodo com essa chave foi encontrado.')

                    wait()


                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 12:

                clear()

                if bst.is_empty() == False:

                    temp = bst.ancestor(set_key('encontrar os ancestrais'))

                    if temp != '':

                        print(f'\nOs ancestrais do nodo da chave desejada são: {temp}.')

                    else:

                        print('\nNenhum nodo com essa chave foi encontrado.')

                    wait()

                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 13:

                clear()

                if bst.is_empty() == False:

                    print('A árvore não está vazia')

                    wait()

                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            while op_menu == 14:

                clear()

                if bst.is_empty() == False:

                    bst.clear()

                    print('\nÁrvore limpada com sucesso.')

                    wait()

                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)


    main()

    pass