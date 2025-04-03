from abc import ABC, abstractmethod


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