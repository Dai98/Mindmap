


class BinarySearchAlgo:

    def __init__(self) -> None:
        raise NotImplementedError("binary_search.py-BinarySearchAlgo/All methods in this class are static. Do not instantiate this class.")

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

        Args:
            arr (list) - A sorted array
            num (int) - A given number to find index
        Return:
            int, the index of the smallest number greater than or equal to the given number in the array, or -1 if not found
    """
    @staticmethod
    def binary_search_leftmost_greater_index(arr: list, num: int) -> int:
        if arr is None or len(arr) == 0:
            return -1
        left = 0
        right = len(arr) - 1
        index = -1 # Initialize index to be -1 in case no answer is found
        while left <= right:
            # Avoid overflowing in some languages like Java (not in Python)
            mid = left + int((right - left) / 2)
            if arr[mid] >= num:
                # If the middle index number is larger than or equal to the target number
                # First, update the current index to return
                # Then there might be smaller number on the left side, so update right index to shrink the range
                index = mid
                right = mid - 1
            elif arr[mid] < num:
                # If the middle index number is smaller than the target number
                # Then there might be numbers larger than target number on the right side
                # So update left index to shrink the range
                left = mid + 1
        return index
    
    """
        Find the largest/rightmost number that is less than or equal to a given number in a sorted array

        Args:
            arr (list) - A sorted array
            num (int) - A given number to find index
        Return:
            int, the index of the largest number less than or equal to the given number in the array, or -1 if not found
    """
    @staticmethod
    def binary_search_rightmost_less_index(arr: list, num: int) -> int:
        if arr is None or len(arr) == 0:
            return -1
        left = 0
        right = len(arr) - 1
        index = -1 # Initialize index to be -1 in case no answer is found
        while left <= right:
            # Avoid overflowing in some languages like Java (not in Python)
            mid = left + int((right - left) / 2)
            if arr[mid] <= num:
                # If the middle index number is less than or equal to the target number
                # First, update the current index to return
                # Then there might be larger number on the right side, so update left index to shrink the range
                index = mid
                left = mid + 1
            elif arr[mid] > num:
                # If the middle index number is larger than the target number
                # Then there might be numbers less than target number on the left side
                # So update right index to shrink the range
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
            index of any peak in this array
    """
    @staticmethod
    def binary_search_peak(arr: list) -> int:
        if arr is None or len(arr) == 0:
            return -1
        elif len(arr) == 1:
            return 0
        
        # A helper function determines whether a number on an index is a peak
        def is_peak(arr: list, index: int) -> bool:
            n = len(arr)
            # Edge Case: If the first element is larger than the second element, it is a peak
            if index == 0 and arr[0] > arr[1]:
                return True
            # Edge Case: If the last element is larger than the second last element, it is a peak
            elif index == n - 1 and arr[n-1] > arr[n-2]:
                return True
            # General Case: If a number is greater than its adjacent numbers on both side, it is a peak
            elif arr[index - 1] < arr[index] and arr[index] > arr[index + 1]:
                return True
            # It is not a peak
            else:
                return False

        # Check if the first element is a peak
        if is_peak(arr, 0):
            return 0
        # Check if the last element is a peak
        elif is_peak(arr, len(arr)-1):
            return len(arr)-1
        else:
            # If the program doesn't end in the first two if-conditions
            # Then the start of the array is getting bigger and bigger
            # The end of the array is getting smaller and smaller
            # So there must be a peak between indexes (1, n-2)
            left = 1
            right = len(arr) - 2

            while left <= right:
                mid = left + int((right - left) / 2)
                # If the middle index is a peak, break and return value of middle peak
                if is_peak(arr, mid):
                    break
                # If the middle index is not a peak, and the number is getting smaller and smaller on the left side
                # Then there must be a peak on (left, mid-1), so update right index
                elif arr[mid - 1] > arr[mid]:
                    right = mid - 1
                # If the middle index is not a peak, and the number is getting larger and larger on the right side
                # Then there must be a peak on (mid+1, right), so update left index
                elif arr[mid + 1] > arr[mid]:
                    left = mid + 1
            return mid
