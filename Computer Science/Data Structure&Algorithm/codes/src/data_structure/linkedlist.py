from typing import Any
from abc import abstractmethod, ABC


class LinkedNode:
    def __init__(self, value: Any) -> None:
        self.value = value
    def __str__(self):
        return f"LinkedNode<{str(self.value)}>"


class SingleLinkedNode(LinkedNode):
    def __init__(self, value: Any, next: LinkedNode) -> None:
        super().__init__(value)
        self.next = next


class DoubleLinkedNode(LinkedNode):
    def __init__(self, value: Any, prev: LinkedNode, next: LinkedNode) -> None:
        super().__init__(value)
        self.prev = prev
        self.next = next


class LinkedList(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add(self, value: Any) -> None:
        raise NotImplementedError("linkedlist.py-LinkedList/Abstract method add is not implemented in base class.")
    
    @abstractmethod
    def remove(self, value:Any) -> None:
        raise NotImplementedError("linkedlist.py-LinkedList/Abstract method remove is not implemented in base class.")
    
    @abstractmethod
    def insert(self, index: int, value: Any) -> None:
        raise NotImplementedError("linkedlist.py-LinkedList/Abstract method insert is not implemented in base class.")
    

class SingleLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.length = 0

    def add(self, value: Any) -> None:
        if self.head is None:
            self.head = SingleLinkedNode(value, None)
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = SingleLinkedNode(value, None)
        self.length += 1

    def remove(self, value: Any) -> None:
        if self.head is None or value is None:
            return
        else:
            if self.head.value == value:
                self.head = self.head.next
            else:
                cur_node = self.head
                while cur_node.next is not None and cur_node.next.value != value:
                    cur_node = cur_node.next
                if cur_node.next is not None and cur_node.next.value == value:
                    cur_node.next = cur_node.next.next
                else:
                    return
                
    def insert(self, index: int, value: Any) -> None:
        if index > self.length or index < 0:
            raise ValueError(f"linkedlist.py-SingleLinkedList/Index out of bound, cannot insert element to index {index}.")
        elif index == self.length:
            self.add(value)
        elif index == 0:
            new_head = SingleLinkedNode(value, self.head)
            self.head = new_head
        else:
            cur_index = 0
            cur_node = self.head
            while cur_index < index-1:
                cur_node = cur_node.next
                cur_index += 1
            new_node = SingleLinkedNode(value, cur_node.next)
            cur_node.next = new_node

    def __str__(self) -> str:
        node_values = []
        cur_node = self.head
        while cur_node != None:
            node_values.append(str(cur_node.value))
            cur_node = cur_node.next
        return f"[{'->'.join(node_values)}]"

    
class DoubleLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value: Any) -> None:
        if self.length == 0:
            self.head = DoubleLinkedNode(value, None, None)
        elif self.length == 1:
            self.tail = DoubleLinkedNode(value, self.head, self.head)
            self.head.prev = self.tail
            self.head.next = self.tail
        else:
            new_node = DoubleLinkedNode(value, self.tail, self.head)
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
    
    def remove(self, value:Any) -> None:
        if self.head is None or value is None:
            return
        else:
            if self.head.value == value:
                self.head = self.head.next
                self.head.prev = self.tail
            elif self.tail.value == value:
                self.head.prev = self.tail.prev
                self.tail = self.tail.prev
                self.tail.next = self.head
            else:
                cur_node = self.head
                while cur_node.next is not None and cur_node.next.value != value:
                    cur_node = cur_node.next
                if cur_node.next is not None and cur_node.next.value == value:
                    cur_node.next = cur_node.next.next
                    cur_node.next.prev = cur_node
                else:
                    return
    
    def insert(self, index: int, value: Any) -> None:
        if index > self.length or index < 0:
            raise ValueError(f"linkedlist.py-DoubleLinkedList/Index out of bound, cannot insert element to index {index}.")
        elif index == self.length:
            self.add(value)
        elif index == 0:
            new_head = DoubleLinkedNode(value, self.tail, self.head)
            self.tail.next = new_head
            self.head.prev = new_head
            self.head = new_head
        else:
            cur_index = 0
            cur_node = self.head
            while cur_index < index-1:
                cur_node = cur_node.next
                cur_index += 1
            new_node = DoubleLinkedNode(value, cur_node, cur_node.next)
            cur_node.next = new_node
            cur_node.next.next.prev = new_node

    def __str__(self):
        node_values = []
        cur_node = self.head
        while cur_node != self.tail:
            node_values.append(str(cur_node.value))
            cur_node = cur_node.next
        if self.tail is not None:
            node_values.append(str(self.tail.value))
        return f"[{'<->'.join(node_values)}]"
