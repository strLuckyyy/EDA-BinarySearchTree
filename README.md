# Trabalho 1 -  Estrutura de Dados Avançada


**Contexto**: É inquestionável a aplicação de estruturas do tipo árvore em diversas áreas conforme visto em
aula. Pensando nisso, você deverá desenvolver alguns métodos baseados na árvore de pesquisa binária
apresentada em aula.

**Classe abstrata**: use a classe abstrata a seguir e isso significa que não deverá ser alterado nenhum nome
de método. Lembre-se que, para a validação de cada método, o professor utiliza testes automatizados e,
portanto, é fundamental que não seja alterado nada.

<hr/>

**Passo 1)** Crie a seguinte classe abstrata e vincule-a à classe BinarySearchTree apresentada em aula.

<div style="border: 1px solid; padding: 10px 15px">

```
    class BinarySearchTreeADT(ABC):
        @abstractmethod
        def clear(self) -> None: ...

        @abstractmethod
        def is_empty(self) -> bool: ...

        @abstractmethod
        def search(self, key: object) -> object: ...

        @abstractmethod
        def insert(self, key: object, value: object) -> None: ...

        @abstractmethod
        def delete(self, key: object) -> bool: ...

        @abstractmethod
        def pre_order_traversal(self) -> None: ...

        @abstractmethod
        def in_order_traversal(self) -> None: ...

        @abstractmethod
        def post_order_traversal(self) -> None: ...

        @abstractmethod
        def level_order_traversal(self) -> None: ...

        # Métodos para desenvolver

        @abstractmethod
        def count_internal(self) -> int: ...

        @abstractmethod
        def degree(self, key: object) -> int: ...

        @abstractmethod
        def height(self, key: object) -> int: ...

        @abstractmethod
        def level(self, key: object) -> int: ...

        @abstractmethod
        def ancestor(self, key: object) -> str: ...

```
</div>
<br/>

**Passo 2)** Desenvolva em Python cada método conforme regra de negócio descrita no Quadro 1. Lembrese que poderá ser criado qualquer método que facilite o desenvolvimento.

**Quadro 1**: Descrição dos Contratos

| Método da API | Objetivo | Parâmetros | Retorno |
| ------------- | -------- | ---------- | ------- |
| count_internal | Retornar a quantidade de nós internos da árvore. Lembre-se que a raiz e as folhas não fazem parte. | Nenhum | Quantidade de nós internos da árvore ou zero caso a árvore esteja vazia ou tenha somente o root. |
| Degree | Retornar o grau de um nó. | **key:** Chave que se deseja retornar o grau | Grau do nó que é representado pela chave. Caso não encontrada a chave, retornar -1. |
| Height | Retornar a altura de um nó. | **key:** Chave que se deseja verificar a altura. | Altura do nó que é representada pela chave. Caso não encontrada a chave, retornar -1. |
| Level | Retornar o nível de um nó. | **key:** Chave que se deseja descobrir o nível. | O nível do nó representado pela chave. Caso não seja encontrada a chave, retornar -1. |
| Ancestor | Retornar os ancestrais (chave) lado a lado. | **key:** Chave que se deseja descobrir os ancestrais. | Lista em texto com as chaves lado a lado (separadas por espaço) que representam os ancestrais. Caso não seja encontrada a chave, retornar None. |

<hr/>

**Organização**

- NÃO SERÁ ACEITO A ENTREGA DO TRABALHO INDIVIDUALMENTE, POIS A ATIVIDADE É EM GRUPO
- Para a entrega, somente um do grupo precisa submetê-lo no EAD. Exporte um arquivo formato ZIP com o seguinte nome: aluno1_aluno2_trabalhofinal.zip, contendo o código do projeto.
- Código o mais claro possível, seguindo boas práticas de nomenclatura e estrutura
- Não será aceito a entrega (via Moodle) do trabalho após a data limite
- Não será aceito trabalho igual ao de outros colegas. Esta prática é chamada de plágio. Inclusive, será verificado se o código foi desenvolvido usando LLMs (e.g. ChatGPT)

