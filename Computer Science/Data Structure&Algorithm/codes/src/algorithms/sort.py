from abc import abstractmethod, ABCMeta


class Sort(metaclass=ABCMeta):

    def __init__(self):
        pass
    
    @abstractmethod
    def sort(self, array: list) -> list:
        raise NotImplementedError("sort.py-Sort/Abstract method sort is not implemented in base class.")
    
    @staticmethod
    def swap(array: list, index1: int, index2: int) -> list:
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp


# Selection Sorting
class SelectionSort(Sort):
    
    def __init__(self):
        super().__init__()

    def sort(self, array: list) -> list:
        n = len(array)
        for i in range(0, n):
            min_index = i
            for k in range(i+1, n):
                if array[min_index] > array[k]:
                    min_index = k
            SelectionSort.swap(array, i, min_index)
        return array


# Bubble Sorting
class BubbleSort(Sort):
    
    def __init__(self):
        super().__init__()

    def sort(self, array: list) -> list:
        n = len(array)
        for i in range(n-1, 0, -1):
            swapped = False
            for k in range(0, i):
                if array[k] > array[k+1]:
                    BubbleSort.swap(array, k, k+1)
                    swapped = True
            if not swapped:
                break
        return array   


# Insertion Sorting
class InsertionSort(Sort):
    
    def __init__(self):
        super().__init__()

    def sort(self, array: list) -> list:
        n = len(array)
        for i in range(1, n):
            for k in range(i-1, -1, -1):
                if array[k] > array[k+1]:
                    InsertionSort.swap(array, k, k+1)
                else:
                    break
        return array


if __name__ == "__main__":
    test_arr = [9, 3, 12, 7, 10, 0, -5, 100, -20]
    sort = InsertionSort()
    print(sort.sort(test_arr))
