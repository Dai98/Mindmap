from abc import abstractmethod, ABC
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(src_folder))

from src.data_structure.heap import Heap

"""
All the sorting algorithms will sort elements ascendingly
"""


class Sort(ABC):
    def __init__(self):
        pass
    
    """
        The abstract interface of sort for all the sorting algorithm
    """
    @abstractmethod
    def sort(self, array: list) -> list:
        raise NotImplementedError("sort.py-Sort/Abstract method sort is not implemented in base class.")
    
    """
        Swap the element in a list

        Args:
            array (list) - The list to swap elements in
            index1 (int) - The index of the first element to swap
            index2 (int) - The index of the second element to swap

        Return:
            None, swapping will be done on the original list object
            And it will take effect because list is passed by reference
    """
    @staticmethod
    def swap(array: list, index1: int, index2: int) -> None:
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp


# Selection Sorting
class SelectionSort(Sort):
    
    def __init__(self):
        super().__init__()

    """
        Implementation of Selection Sort
        For index i on an array with n elements, find minimum value on range (i+1, n-1) and put it on index i, and repeat this process

        Args:
            array (list) - The array to sort

        Return:
            list, the sorted array
    """
    def sort(self, array: list) -> list:
        n = len(array)
        # i to n is the unsorted area
        # 0 to i-1 is the sorted area
        for i in range(0, n):
            min_index = i
            # Find the index of the minimum value in unsorted area
            for k in range(i+1, n):
                if array[min_index] > array[k]:
                    min_index = k
            # Put the minimum element on index i
            SelectionSort.swap(array, i, min_index)
        return array


# Bubble Sorting
class BubbleSort(Sort):
    
    def __init__(self):
        super().__init__()

    """
        Implementation of Bubble Sort
        For index i on an array with n elements, swap adjacent elements with incorrect order, 
        until the largest element goes to the end on range (0, i), and continue this process on (0, i-1)

        Args:
            array (list) - The array to sort
            
        Return:
            list, the sorted array
    """
    def sort(self, array: list) -> list:
        n = len(array)
        # i to n-1 is the sorted area
        # 0 to i-1 is the not sorted area
        for i in range(n-1, 0, -1):
            swapped = False
            for k in range(0, i):
                # if the element on the left is larger than the element on the right
                # Then swap them
                if array[k] > array[k+1]:
                    BubbleSort.swap(array, k, k+1)
                    swapped = True
            if not swapped:
                # If all elements are checked and no swapping happened
                # Then all elements are in the correct order, no need to continue the sorting
                break
        return array   


# Insertion Sorting
class InsertionSort(Sort):
    
    def __init__(self):
        super().__init__()

    """
        Implementation of Insertion Sort
        For index i ranged (1, n-1) on an array with n element
        Put the i-th element in the correct position in range (0, i-1) and repeat this process

        Args:
            array (list) - The array to sort
            
        Return:
            list, the sorted array
    """
    def sort(self, array: list) -> list:
        n = len(array)
        # 0 to i-1 is the sorted area
        # i to n-1 is the unsorted area
        # i starts from 1 because 0 to 0 is definitely sorted
        for i in range(1, n):
            for k in range(i-1, -1, -1):
                # Get the first element in unsorted area (on index i initially)
                # And find the correct place to insert it
                # By moving larger elements backwards and moving i-th element forward using swapping
                if array[k] > array[k+1]:
                    InsertionSort.swap(array, k, k+1)
                else:
                    # If the i-th element find the correct position
                    # Then no necessary to check forward
                    break
        return array
    

class MergeSort(Sort):
    """
        https://leetcode.com/problems/sort-an-array/description/
    """
    def __init__(self, mode="recursive"):
        super().__init__()
        if mode.lower() not in ("recursive", "non-recursive"):
            raise ValueError("sort.py-MergeSort/Invalid merge sort mode, please pass 'recursive' or 'non-recursive'.")
        self.mode = mode.lower()

    def sort(self, array: list) -> list:
        if self.mode == "recursive":
            self._merge_recur(array, 0, len(array)-1)
        else:
            self.sort_nonrecursive(array)
        return array

    def _merge_recur(self, array: list, left: int, right: int) -> None:
        if left == right:
            return
        middle = left + (right - left) // 2
        self._merge_recur(array, left, middle)
        self._merge_recur(array, middle+1, right)
        self._merge(array, left, middle, right)

    def _merge(self, array: list, left: int, middle: int, right: int) -> None:
        cur1 = left
        cur2 = middle+1
        helper = []

        while cur1 <= middle and cur2 <= right:
            if array[cur1] <= array[cur2]:
                value = array[cur1]
                cur1 += 1
                helper.append(value)
            else:
                value = array[cur2]
                cur2 += 1
                helper.append(value)

        while cur1 <= middle:
            helper.append(array[cur1])
            cur1 += 1

        while cur2 <= right:
            helper.append(array[cur2])
            cur2 += 1

        for index in range(0, len(helper)):
            array[left + index] = helper[index]

    def sort_nonrecursive(self, array: list) -> list:
        step = 1
        n = len(array)

        while step < n:
            left = 0
            while left < n:
                middle = left + step - 1
                if middle + 1 >= n:
                    break
                right = min(left + step + step - 1, n-1)
                self._merge(array, left, middle, right)
                left = right + 1
            step *= 2


class HeapSort(Sort):
    def __init__(self):
        super().__init__()
        self.heap = Heap()

    def sort(self, array: list) -> list:
        n = len(array)
        self.heap.data = array
        self.heap.size = n
        # Heapify from bottom to top
        # Time Complexity O(n)
        for index in range(n-1, -1, -1):
            self.heap.heapify(index)
        # sort
        while self.heap.size > 1:
            self.heap._swap(0, self.heap.size-1)
            self.heap.size -= 1
            self.heap.heapify(0)

        return self.heap.data
