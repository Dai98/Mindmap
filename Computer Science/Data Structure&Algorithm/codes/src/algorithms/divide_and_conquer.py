

class SmallSum:
    """
        Small sum problem is to calculate, for a given array a, 
        The sum of all the numbers that are on the left of an element in the array, and are smaller or equal to the current value

        For example, array a = [1, 3, 5, 2, 4, 6]

        Sum of numbers on the left of a[0] and are smaller or equal to a[0] = 0
        Sum of numbers on the left of a[1] and are smaller or equal to a[1] = 1
        Sum of numbers on the left of a[2] and are smaller or equal to a[2] = 4
        Sum of numbers on the left of a[3] and are smaller or equal to a[3] = 1
        Sum of numbers on the left of a[4] and are smaller or equal to a[4] = 6
        Sum of numbers on the left of a[5] and are smaller or equal to a[5] = 15

        So the small sum of array a is 0 + 1 + 4 + 1 + 6 + 15 = 27
    """
    def calculate_sum_of_small_sums(self, array: list) -> int:
        return self._small_sum_recur(array, 0, len(array)-1)

    def _small_sum_recur(self, array: list, left_index: int, right_index: int) -> int:
        if left_index == right_index:
            return 0
        middle_index = left_index + (right_index - left_index) // 2
        result = self._small_sum_recur(array, left_index, middle_index) + \
            self._small_sum_recur(array, middle_index+1, right_index) + \
            self._merge(array, left_index, middle_index, right_index)
        return result

    def _merge(self, array: list, left_index: int, middle_index: int, right_index: int) -> int:
        # Count results that across left and right region
        gap_sum = 0
        prev_sum = 0
        cur1 = left_index
        cur2 = middle_index + 1
        while cur2 <= right_index:
            while cur1 <= middle_index and array[cur1] <= array[cur2]:
                prev_sum += array[cur1]
                cur1 += 1
            gap_sum += prev_sum
            cur2 += 1

        # Merge
        helper = []
        cur1 = left_index
        cur2 = middle_index + 1
        while cur1 <= middle_index and cur2 <= right_index:
            if array[cur1] <= array[cur2]:
                helper.append(array[cur1])
                cur1 += 1
            else:
                helper.append(array[cur2])
                cur2 += 1
        
        while cur1 <= middle_index:
            helper.append(array[cur1])
            cur1 += 1

        while cur2 <= middle_index:
            helper.append(array[cur2])
            cur2 += 1

        for index in range(0, len(helper)):
            array[index + left_index] = helper[index]
        return gap_sum


class ReversePair:
    """
        https://leetcode.com/problems/reverse-pairs/description/
    """
    def count_reverse_pairs(self, array: list) -> int:
        return self._count_recur(array, 0, len(array)-1)

    def _count_recur(self, array: list, left_index: int, right_index: int) -> int:
        if left_index == right_index:
            return 0
        middle_index = left_index + (right_index - left_index) // 2
        return self._count_recur(array, left_index, middle_index) + self._count_recur(array, middle_index + 1, right_index) + \
            self._merge(array, left_index, middle_index, right_index)
    
    def _merge(self, array: list, left_index: int, middle_index: int, right_index: int) -> int:
        count = 0
        cur1 = left_index
        cur2 = middle_index + 1

        while cur1 <= middle_index:
            if cur2 <= right_index and array[cur1] > array[cur2] * 2:
                cur2 += 1
            count += cur2 - (middle_index + 1)
            cur1 += 1

        helper = []
        cur1 = left_index
        cur2 = middle_index + 1

        while cur1 <= middle_index and cur2 <= middle_index + 1:
            if array[cur1] <= array[cur2]:
                helper.append(array[cur1])
                cur1 += 1
            else:
                helper.append(array[cur2])
                cur2 += 1
        
        while cur1 <= middle_index:
            helper.append(array[cur1])
            cur1 += 1

        while cur2 <= middle_index:
            helper.append(array[cur2])
            cur2 += 1

        for index in range(0, len(helper)):
            array[index + left_index] = helper[index]
        
        return count
