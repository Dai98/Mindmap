# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(current_folder))

from base import DataStructureTemplate
from typing import Any


class Heap(DataStructureTemplate):

    def __init__(self) -> None:
        super().__init__()
        self.size = 0
        self.data = []

    """
        Time Complexity O(log n)
    """
    def heap_insert(self, value: Any) -> None:
        current_index = self.size
        parent_index = (current_index - 1) // 2
        self.data.append(value)
        while self.data[parent_index] < self.data[current_index]:
            self._swap(current_index, current_index)
            current_index = parent_index
            parent_index = (current_index - 1) // 2
        self.size += 1

    """
        Time Complexity O(log n)
    """
    def heapify(self, index: int) -> None:
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        while left_index < self.size:
            larger_index = right_index if right_index < self.size and self.data[right_index] > self.data[left_index] else left_index
            if self.data[larger_index] <= self.data[index]:
                break
            else:
                self._swap(larger_index, index)
            index = larger_index
            left_index = index * 2 + 1
            right_index = index * 2 + 2

    def clear(self) -> None:
        self.size = 0
        self.data = []

    def _swap(self, index1: int, index2: int) -> None:
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp