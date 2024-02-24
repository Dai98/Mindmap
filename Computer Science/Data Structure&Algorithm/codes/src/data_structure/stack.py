# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(current_folder))

from abc import ABC, abstractmethod
from typing import Any


class StackTemplate(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def pop(self) -> Any:
        raise NotImplementedError("stack.py-StackTemplate/Abstract method pop is not implemented in base class.")
    
    @abstractmethod
    def push(self, element: Any) -> None:
        raise NotImplementedError("stack.py-StackTemplate/Abstract method push is not implemented in base class.")
    

class Stack(StackTemplate):
    def __init__(self, initial_capacity: int = 100) -> None:
        super().__init__()
        self.data = [None] * initial_capacity
        self.size = 0
        self.index = 0

    def pop(self) -> Any:
        if self.size == 0:
            return None
        else:
            element = self.data[self.index]
            self.index -= 1
            self.size -= 1
            return element
        
    def push(self, element: Any) -> None:
        if self.size != len(self.data):
            self.data[self.index] = element
        else:
            self.data.append(element)
        self.size += 1
        self.index += 1

    def peek(self) -> None:
        return self.data[self.size]


class QueueStack(StackTemplate):
    """
        https://leetcode.com/problems/implement-stack-using-queues/description/
    """
    def __init__(self) -> None:
        super().__init__()
        self.queue = []

    def push(self, x: int) -> None:
        size = len(self.queue)
        counter = 0
        self.queue.append(x)
        while counter < size:
            element = self.queue.pop(0)
            self.queue.append(element)
            counter += 1

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    

class MinStack(StackTemplate):
    """
        Implement the ability to get the minimum value based on basic stack
        https://leetcode.com/problems/min-stack/description/
    """
    def __init__(self) -> None:
        super().__init__()
        self.data = []
        self.min_value = []

    def pop(self) -> Any:
        element = self.data.pop()
        self.min_value.pop()
        return element
        
    def push(self, element: Any) -> None:
        if len(self.data) == 0 and len(self.min_value) == 0:
            self.data.append(element)
            self.min_value.append(element)
        elif self.min_value[-1] <= element:
            self.data.append(element)
            self.min_value.append(self.min_value[-1])
        else:
            self.data.append(element)
            self.min_value.append(element)
    
    def peek(self):
        return self.data[-1]
    
    def get_min(self):
        return self.min_value[-1]
