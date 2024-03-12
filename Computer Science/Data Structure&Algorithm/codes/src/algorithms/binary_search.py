


class BinarySearchAlgo:

    def __init__(self) -> None:
        pass

    """
        Find the index of a given element in a sorted array

        Args:
            arr (list) - A sorted array
            num (int) - A given number to find index
        Return:
            int, the index of the given number in the array, or -1 if not found
    """
    @staticmethod
    def binary_search_index(arr: list, num: int) -> int:
        if arr is None or len(arr) == 0:
            return -1
        left = 0
        right = len(arr) - 1
        while left <= right:
            # Avoid overflowing in some languages like Java (not in Python)
            mid = left + int((right - left) / 2)
            if arr[mid] == num:
                return mid
            elif arr[mid] < num:
                left = mid + 1
            else:
                # arr[mid] > num
                right = mid - 1
        return -1
    
    """
        Find the smallest/leftmost number that is greater than or equal to a given number in a sorted array
    """
    @staticmethod
    def binary_search_leftmost_greater_index(arr: list, num: int) -> int:
        if arr is None or len(arr) == 0:
            return -1
        left = 0
        right = len(arr) - 1
        index = -1
        while left <= right:
            # Avoid overflowing in some languages like Java (not in Python)
            mid = left + int((right - left) / 2)
            if arr[mid] >= num:
                index = mid
                right = mid - 1
            elif arr[mid] < num:
                left = mid + 1
        return index
    
    """
        Find the largest/rightmost number that is less than or equal to a given number in a sorted array
    """
    @staticmethod
    def binary_search_rightmost_less_index(arr: list, num: int) -> int:
        if arr is None or len(arr) == 0:
            return -1
        left = 0
        right = len(arr) - 1
        index = -1
        while left <= right:
            # Avoid overflowing in some languages like Java (not in Python)
            mid = left + int((right - left) / 2)
            if arr[mid] <= num:
                index = mid
                left = mid + 1
            elif arr[mid] > num:
                right = mid - 1
        return index
    
    """
        Find any peak in a not sorted array
        A peak is a number that on index i, it is greater than its adjacent numbers (numbers on index i-1 and i+1 )
        
        We define numbers on index -1 or on len(arr) are negative infinity,
        so numbers on index 0 or at the end of the arr are also able to be a peak

        https://leetcode.com/problems/find-peak-element/description/

        Args:
            arr (list) - An unsorted array
        Return:
            index of any peaks in this array
    """
    @staticmethod
    def binary_search_peak(arr: list) -> int:
        if arr is None or len(arr) == 0:
            return -1
        elif len(arr) == 1:
            return 0
        
        def is_peak(arr: list, index: int) -> bool:
            n = len(arr)
            if index == 0 and arr[0] > arr[1]:
                return True
            elif index == n - 1 and arr[n-1] > arr[n-2]:
                return True
            elif arr[index - 1] < arr[index] and arr[index] > arr[index + 1]:
                return True
            else:
                return False

        if is_peak(arr, 0):
            return 0
        elif is_peak(arr, len(arr)-1):
            return len(arr)-1
        else:
            left = 1
            right = len(arr) - 2

            while left <= right:
                mid = left + int((right - left) / 2)
                if is_peak(arr, mid):
                    break
                elif arr[mid - 1] > arr[mid]:
                    right = mid - 1
                elif arr[mid + 1] > arr[mid]:
                    left = mid + 1
            return mid



if __name__ == "__main__":
    index = BinarySearchAlgo.binary_search_rightmost_less_index([3, 6, 8, 13, 19, 27, 31], 10)
    print(index)
