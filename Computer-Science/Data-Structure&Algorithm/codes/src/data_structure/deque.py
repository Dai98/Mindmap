# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(current_folder))

from typing import Any
from abc import abstractmethod
from base import DataStructureTemplate
from linkedlist import DoubleLinkedNode


class DequeTemplate(DataStructureTemplate):

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def insert_front(self, element: Any):
        raise NotImplementedError("deque.py-DequeTemplate/Abstract method insert_front is not implemented in base class.")
    
    @abstractmethod
    def insert_last(self, element: Any):
        raise NotImplementedError("deque.py-DequeTemplate/Abstract method insert_last is not implemented in base class.")
    
    @abstractmethod
    def delete_front(self) -> Any:
        raise NotImplementedError("deque.py-DequeTemplate/Abstract method pop_front is not implemented in base class.")
    
    @abstractmethod
    def delete_last(self) -> Any:
        raise NotImplementedError("deque.py-DequeTemplate/Abstract method pop_last is not implemented in base class.")
    
    @abstractmethod
    def get_front(self) -> Any:
        raise NotImplementedError("deque.py-DequeTemplate/Abstract method get_front is not implemented in base class.")

    @abstractmethod
    def get_rear(self) -> Any:
        raise NotImplementedError("deque.py-DequeTemplate/Abstract method get_rear is not implemented in base class.")
    

class Deque(DequeTemplate):
    """
        https://leetcode.com/problems/design-circular-deque/description/
    """

    def __init__(self, max_capacity: int) -> None:
        super().__init__()
        self.max_capacity = max_capacity
        self.data = [None] * max_capacity
        self.left = 0
        self.right = 0
        self.size = 0

    @abstractmethod
    def insert_front(self, element: Any) -> bool:
        if self.is_full():
            return False
        else:
            if self.size == 0:
                self.left = 0
                self.right = 0
                self.data[0] = element
                self.size += 1
            else:
                self.left = (self.left + self.max_capacity - 1) % self.max_capacity
                self.data[self.left] = element
                self.size += 1
            return True
    
    @abstractmethod
    def insert_last(self, element: Any) -> bool:
        if self.is_full():
            return False
        else:
            if self.size == 0:
                self.left = 0
                self.right = 0
                self.data[0] = element
                self.size += 1
            else:
                self.right = (self.right + self.max_capacity + 1) % self.max_capacity
                self.data[self.right] = element
                self.size += 1
            return True
    
    def delete_front(self) -> Any:
        if self.is_empty():
            return None
        else:
            element = self.data[self.left]
            self.data[self.left] = None
            self.left = (self.left + self.max_capacity + 1) % self.max_capacity
            self.size -= 1
            return element
    
    def delete_last(self) -> Any:
        if self.is_empty():
            return None
        else:
            element = self.data[self.right]
            self.data[self.right] = None
            self.right = (self.right + self.max_capacity - 1) % self.max_capacity
            self.size -= 1
            return element
    
    def is_full(self) -> bool:
        return self.size == self.max_capacity

    def is_empty(self) -> bool:
        return self.size == 0

    def get_front(self) -> Any:
        return self.data[self.left]

    def get_rear(self) -> Any:
        return self.data[self.right]

    def clear(self) -> bool:
        self.data = [None] * self.max_capacity
        self.left = 0
        self.right = 0
        self.size = 0


class LinkedDeque(DequeTemplate):
    
    def __init__(self) -> None:
        super().__init__()