from collections import defaultdict
import math
from typing import List


class MinSubarrayLength:
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        left = 0
        num_sum = 0
        for right in range(len(nums)):
            num_sum += nums[right]
            # After taking new numbers on right side
            # Keep poping numbers from left side if subarray sum is larger than target
            while num_sum - nums[left] >= target:
                num_sum -= nums[left]
                left += 1
            # Update minimum length
            # Add if to avoid when starting up sum is less than target, then the subarray is not valid
            if num_sum >= target:
                min_length = min(min_length, right-left+1)
        return min_length if min_length != math.inf else 0


class LongestSubstring:
    def length_of_longest_substring(self, s: str) -> int:
        last_index_map = {}
        left = 0
        substr_len = 0
        for right, char in enumerate(s):
            # If right char never appears, use current left as left border and right border will move forward
            # If right char appeared before, start new substring from the next character of last time this character showed up
            # (e.g. a b c b d e f, when right = 3, we encounter b, which already appeared on 1, so now we check the substring starting from 2
            # To include b on right=3 and check if new substring is longer than the existing longest substring)
            # Even if this new substring is shorter, we already got the length stored in substr_len
            # And if the new substring is longer eventually, then we don't need to worry about longer substring with previous start
            # Because this new substring is longer than previous substring, 
            # and previous substring is already the longest before the current substring
            left = max(left, last_index_map.get(char, -1)+1)
            substr_len = max(substr_len, right-left+1)
            last_index_map[char] = right
        return substr_len


class MinSubstring:
    def min_window(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # Count map is the hash map that records how many times each letter shows up
        count_map = defaultdict(int)
        # But for all the letters we need to cover, they have negative appearance
        # We need to keep find them until they has 0 appearance
        # This is to distinguish characters we must find from t (negative frequency), and the inrelevant characters in s (positive frequency)
        for char in t:
            count_map[char] -= 1
        
        min_len = math.inf

        # The start of minimum length substring
        start = 0
        # sliding-window boundary
        left, right = 0, 0
        # How much characters must find in total
        debt = len(t)
        while right < len(s):
            # If current character has negative frequency, then it is one of the character in t
            if count_map[s[right]] < 0:
                # We include that letter in the frequency map and reduce debt by 1 (because we find a target character)
                debt -= 1
            count_map[s[right]] += 1
            # If debt becomes 0, then substring has find all chars that should be covered
            if debt == 0:
                # Move left bound to see if we can make substring shorter
                # It can become shorter if substring has leading inrelevant characters
                # But it cannot remove the characters we need again (the ones with negative frequency), because we need it for the substring
                while count_map[s[left]] > 0:
                    count_map[s[left]] -= 1
                    left += 1
                # The length of current substring is right - left + 1
                if (right-left+1) < min_len:
                    min_len = right - left + 1
                    start = left
            right += 1

        return "" if min_len == math.inf else s[start: start+min_len]
    

class GasStation:
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        left,right = 0,0
        n = len(gas)
        while left < n:
            gas_sum = 0
            while gas_sum + gas[right % n] - cost[right % n] >= 0:
                # If already finish the circle
                if (right - left + 1) == n:
                    return left
                gas_sum += (gas[right % n] - cost[right % n])
                right += 1
            # If get out of the while loop, it means that it didn't goes around a circle
            # But gas is not enough to go to next station
            # Start from the next station again
            # Because if [left, right) + right is not enough to go to next station
            # Then [left1, right) + right (left1 > left) is definitely not enough to go to next station
            left = right + 1
            right = left
        return -1
    

class BalancedString:
    """
    Variation of Leetcode 76
    We need to find the minimum substring that covers all the extra characters
    So that we can change them to get balanced string
    """
    def balanced_string(self, s: str) -> int:
        # Q->0, W->1, E->2, R->3
        n = len(s)
        count_map = defaultdict(int)
        debt = 0
        for char in s:
            count_map[char] += 1
        
        for char in count_map:
            if count_map[char] < (n/4):
                count_map[char] = 0
            else:
                count_map[char] = n/4 - count_map[char]
                debt -= count_map[char]
        
        if debt == 0:
            return 0
        
        result = math.inf
        left, right = 0, 0
        
        while right < n:
            if count_map[s[right]] < 0:
                debt -= 1
            count_map[s[right]] += 1

            if debt == 0:
                while count_map[s[left]] > 0:
                    count_map[s[left]] -= 1
                    left += 1
                result = min(result, right-left+1)
            right += 1

        return result