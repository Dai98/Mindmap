# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(current_folder))

from abc import abstractmethod
from typing import Any
from linkedlist import SingleLinkedNode
from base import DataStructureTemplate


class QueueTemplate(DataStructureTemplate):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def pop(self) -> Any:
        raise NotImplementedError("queue.py-QueueTemplate/Abstract method pop is not implemented in base class.")
    
    @abstractmethod
    def push(self, element: Any) -> None:
        raise NotImplementedError("queue.py-QueueTemplate/Abstract method push is not implemented in base class.")
    
    @abstractmethod
    def get_size(self) -> int:
        raise NotImplementedError("queue.py-QueueTemplate/Abstract method size is not implemented in base class.")
    
    @abstractmethod
    def peek_front(self) -> Any:
        raise NotImplementedError("queue.py-QueueTemplate/Abstract method peek_front is not implemented in base class.")
    
    @abstractmethod
    def peek_rear(self) -> Any:
        raise NotImplementedError("queue.py-QueueTemplate/Abstract method peek_rear is not implemented in base class.")
    

class Queue(QueueTemplate):
    """
        This class implements a native queue with fixed length
        When n elements have been pushed into this queue with size n,
        no other operations are allowed
    """

    def __init__(self, size: int) -> None:
        super().__init__()
        self.front = 0
        self.rear = 0
        self.data = [None] * size

    def pop(self) -> Any:
        if self.front == self.rear:
            return None
        else:
            element = self.data[self.front]
            self.front += 1
            return element

    def push(self, element: Any) -> None:
        if self.rear == len(self.data):
            raise ValueError(f"queue.py-Queue/Queue has conducted {len(self.data)} operations, no new push allowed.")
        else:
            self.data[self.rear] = element
            self.rear += 1

    def get_size(self) -> int:
        return self.rear - self.front
    
    @property
    def size(self) -> int:
        return self.rear - self.front
    
    def peek_front(self) -> Any:
        return self.data[self.front]
    
    def peek_rear(self) -> Any:
        if self.front == self.rear:
            return None
        else:
            return self.data[self.rear-1]
        
    def clear(self):
        self.front = 0
        self.rear = 0
        self.data = [None for _ in self.data]

    def __str__(self):
        return f"[{'-'.join([str(element) for element in self.data])}]"


class CircularQueue(QueueTemplate):
    """
        https://leetcode.com/problems/design-circular-queue/
    """
    def __init__(self, size: int) -> None:
        super().__init__()
        self.front = 0
        self.rear = 0
        self.data = [None] * size
        self.size = 0
        self.max_size = len(self.data)

    def pop(self) -> Any:
        if self.size <= 0:
            return None
        else:
            element = self.data[self.front]
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return element

    def push(self, element: Any) -> None:
        if self.size == self.max_size:
            raise ValueError(f"queue.py-CircularQueue/Circular queue has stored {self.max_size} elements, please pop before pushing new element.")
        else:
            self.data[self.rear] = element
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1

    def get_size(self) -> int:
        return self.size
    
    def peek_front(self) -> Any:
        return self.data[self.front]
    
    def peek_rear(self) -> Any:
        if self.size == 0:
            return None
        else:
            rear_index = (self.rear - 1 + self.max_size) % self.max_size
            return self.data[rear_index]
        
    def clear(self):
        self.front = 0
        self.rear = 0
        self.data = [None for _ in self.data]
        self.size = 0

    def __str__(self):
        return f"[{'-'.join(self.data)}]"


class LinkedQueue(QueueTemplate):
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0

    def pop(self) -> Any:
        if self.tail is None:
            return None
        else:
            element = self.head.value
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return element

    def push(self, element: Any) -> None:
        if self.tail is None:
            self.head = SingleLinkedNode(element, None)
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = SingleLinkedNode(element, None)
            self.head.next = self.tail
        else:
            self.tail.next = SingleLinkedNode(element, None)
            self.tail = self.tail.next
        self.size += 1

    def get_size(self) -> int:
        return self.size
    
    def peek_front(self) -> Any:
        return self.head.value if self.head is not None else None
    
    def peek_rear(self) -> Any:
        return self.tail.value if self.tail is not None else None
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        cur = self.head
        while cur is not None:
            elements.append(cur.value)
            cur = cur.next

        return f"[{'-'.join(elements)}]"
    

class StackQueue:
    """
        https://leetcode.com/problems/implement-queue-using-stacks/
    """
    def __init__(self) -> None:
        super().__init__()
        self.in_stack = []
        self.out_stack = []

    def push(self, value: Any) -> None:
        self.in_stack.insert(0, value)

    def pop(self) -> Any:
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                element = self.in_stack.pop(0)
                self.out_stack.insert(0, element)
        element = self.out_stack.pop(0)
        return element
        
    def peek(self) -> Any:
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                element = self.in_stack.pop(0)
                self.out_stack.insert(0, element)
        element = self.out_stack[0]
        return element

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
