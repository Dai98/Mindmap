import random


class RandomizedSelection:
    """
        https://leetcode.com/problems/kth-largest-element-in-an-array/description/
    """
    
    def __init__(self) -> None:
        pass
   
    def kth_largest_number(self, array: list, k: int) -> int:
        return self._randomized_select(array, len(array)-k)

    """
        If sort the given array, what will be the value on given index
        Find this value without sorting the array
    """
    def _randomized_select(self, array: list, index: int) -> int:
        left_index = 0
        right_index = len(array) - 1
        value = 0
        while left_index <= right_index:
            pivot = array[random.randint(left_index, right_index)]
            left_bound, right_bound = self._partition(array, left_index, right_index, pivot)
            if index < left_bound:
                right_index = left_bound - 1
            elif index > right_bound:
                left_index = right_bound + 1
            elif left_bound <= index <= right_bound:
                value = array[index]
                break
        return value 

    def _partition(self, array: list, left_index: int, right_index: int, pivot: int) -> tuple:
        left_pointer = left_index
        right_pointer = right_index
        index = left_index
        while index <= right_pointer:
            if array[index] < pivot:
                self._swap(array, index, left_pointer)
                index += 1
                left_pointer += 1
            elif array[index] == pivot:
                index += 1
            else:
                self._swap(array, index, right_pointer)
                right_pointer -= 1
        return left_pointer, right_pointer
    
    def _swap(self, array: list, index1: int, index2: int) -> None:
        if index1 == index2:
            return
        value = array[index1]
        array[index1] = array[index2]
        array[index2] = value
