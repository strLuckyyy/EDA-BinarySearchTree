from BinarySearchTreeADT import BinarySearchTreeADT
from Node import Node

class BinarySearchTree(BinarySearchTreeADT):
    def __init__(self) -> None:
        self._root: Node = None
    
    
    def __str__(self) -> str:
        return '[empty]' if self.is_empty() else self._str_tree()
    
    
    def _str_tree(self) -> str:
        def _str_tree(current: Node, is_right: bool, tree: str, ident: str) -> str:
            if current.right:
                tree = _str_tree(current.right, True, tree, ident + (' ' * 8 if is_right else ' |' + ' ' * 6))
            tree += ident + (' /' if is_right else ' \\') + "----- " + str(current) + '\n'
            
            if current.left:
                tree = _str_tree(current.left, False, tree, ident + (' |' + ' ' * 6 if is_right else ' ' * 8))            
            return tree
        
        tree: str = ''
        
        if self._root.right:
            tree = _str_tree(self._root.right, True, tree, '')
        tree += str(self._root) + '\n'
        
        if self._root.left:
            tree = _str_tree(self._root.left, False, tree, '')    
        return tree
    
    
    def _get_parent(self, key: object) -> Node:
        parent = None
        current: Node = self._root
        while current and key != current.key:
            parent = current
            current = current.next(key)
        return parent, current
    

    # Implementação dos métodos da interface BinarySearchTreeADT
    
    def clear(self) -> None:
        self._root = None
    
    
    def is_empty(self) -> bool:
        return self._root is None
    
    
    def search(self, key: object) -> object: 
        def search(current: Node, key: object) -> object:
            if current is None:
                return None
            elif key == current.key:
                return current.value
            return search(current.next(key), key)
        
        return search(self._root, key)


    def insert(self, key: object, value: object) -> None: 
        def insert(current: Node, key: object, value: object) -> Node:
            if current is None:
                return Node(key, value)
            elif key > current.key:
                current.right = insert(current.right, key, value)
            elif key < current.key:
                current.left = insert(current.left, key, value)
        
            return current
        
        self._root = insert(self._root, key, value)


    def delete(self, key: object) -> bool: 
        return self._delete_by_copying(key)


    def pre_order_traversal(self) -> None: 
        def pre_order_traversal(current: Node) -> None:
            if current:
                print(current.key, end=' ')
                pre_order_traversal(current.left)
                pre_order_traversal(current.right)
        pre_order_traversal(self._root)


    def in_order_traversal(self) -> None: 
        def in_order_traversal(current: Node) -> None:
            if current:
                in_order_traversal(current.left)
                print(current.key, end=' ')
                in_order_traversal(current.right)
        in_order_traversal(self._root)


    def post_order_traversal(self) -> None: 
        def post_order_traversal(current: Node) -> None:
            if current:
                post_order_traversal(current.left)
                post_order_traversal(current.right)
                print(current.key, end=' ')
        post_order_traversal(self._root)


    def level_order_traversal(self) -> None: 
        if self._root:
            queue = [self._root]
            while queue:
                current: Node = queue.pop(0)
                print(current.key, end=' ')
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)


# Métodos para desenvolver
    # Este método deve retornar o número de nós internos da árvore
    def count_internal(self) -> int:
        def count_internal(current: Node) -> int:
            if current is None: 
                return 0 # Caso o nodo atual seja nulo, retorna 0   
            
            count = 0 # Contador de nós filhos, inicializa em 0 e se tiver filho na esquerda ou direita, soma 1
            if current.left: count += 1
            if current.right: count += 1
            
            # Recursão para garantir que percorre toda a árvore
            return count + count_internal(current.left) + count_internal(current.right)
        
        return count_internal(self._root)


    # Este método deve retornar o grau de um nó da árvore
    def degree(self, key: object) -> int: 
        def degree(current: Node, key: object) -> int: # Função recursiva para calcular o grau do nó         
            if current is None: return -1 # Caso o nodo seja nulo, retorna -1
            
            if key == current.key: # Se o nó for encontrado, verifica o grau. 
                # Se o nó tiver filhos à esquerda e à direita, retorna 2
                if current.left and current.right: 
                    return 2
                
                # Se o nó tiver apenas um filho (à esquerda ou à direita), retorna 1
                elif (current.left and not current.right) or (current.right and not current.left): 
                    return 1
                
                else: # Se o nó não tiver filhos, retorna 0
                    return 0
            
            # Se o nó não for encontrado, continua a busca na subárvore esquerda ou direita
            return degree(current.next(key), key)
        
        return degree(self._root, key)


    # Este método deve retornar a altura de um nó da árvore
    def height(self, key: object) -> int:
        def _height(current: Node) -> int: # Função recursiva para retornar a altura do nó
            if current is None:
                return -1 # Caso o nó seja nulo, retorna -1
            
            # Retorna a altura do nó especificado, verificando o maior entre a altura da subárvore esquerda e direita
            # Adiciona 1 para contar o nó atual
            return 1 + max(_height(current.left), _height(current.right))
        
        # Função que pesquisa o nodo pela arvore e retorna-o.
        # Funciona como o search() mas retornando apenas o current ao invés do current.value ou None 
        def find_node(current: Node, key: object) -> Node:      
            if current is None or key == current.key:
                return current
            if key < current.key:
                return find_node(current.left, key)
            else:
                return find_node(current.right, key)
    
        target_node = find_node(self._root, key)     
        
        if target_node is None: # Se o nodo não for encontrado, retorna -1
            return -1
    
        return _height(target_node)
            

    # Este método deve informar qual o nível de um nodo
    def level(self, key: object) -> int:
        def level(current: Node, key: object, current_level: int) -> int:
            if current is None: # Se o nodo for None, retorna -1
                return -1
            if key == current.key: # Caso encontre o Nodo
                return current_level
            
            # Caso não encontre, verifica o filho esquerdo do nodo(caso exista)
            left_level = level(current.left, key, current_level + 1)
            if left_level != -1:
                return left_level
            
            # Caso contrario verifica o filho direito do nodo (caso exista)
            return level(current.right, key, current_level + 1)
        
        return level(self._root, key, 0)


    # Este método deve informar os ancestrais do Nodo especificado. 
    # Seu retorno é baseado em tupla, a decisão foi feita para facilitar a "montagem" da string
    def ancestor(self, key: object) -> str:
        def find_ancestors(current: Node, key: object) -> tuple:
            if current is None: # Caso o Nodo seja nulo, ele retorna falso
                return (False, "")
            
            if key == current.key: # Caso o Nodo seja encontrado, retorna true. 
                return (True, "")
            
            # Verificando a parte esquerda da arvore
            left_found, left_ancestors = find_ancestors(current.left, key)
            if left_found:
                return (True, f"{current.key} {left_ancestors}")
            
            # Verificando a parte direita da arvore
            right_found, right_ancestors = find_ancestors(current.right, key)
            if right_found:
                return (True, f"{current.key} {right_ancestors}")
            
            return (False, "")
        
        found, ancestors = find_ancestors(self._root, key)
        return ancestors.strip() if found else None
    
    
    def _delete_by_copying(self, key: object) -> bool:
        parent: Node; current: Node
        parent, current = self._get_parent(key)
        
        if current is None:
            return False
        # Case 3
        elif current.left and current.right:
            at_the_right: Node = current.left
        
            while at_the_right.right:
                at_the_right = at_the_right.right
        
            self._delete_by_copying(at_the_right.key)
            current.key, current.value = at_the_right.key, at_the_right.value
        # Case 1/2
        else:
            next_node: Node = current.left or current.right
            if current == self._root:
                self._root = next_node

            elif current == parent.left:
                parent.left = next_node

            else:
                parent.right = next_node
        return True