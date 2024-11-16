from base import DataStructureTemplate

class Bitset(DataStructureTemplate):
    """
    Use bit operation to implement a structure to store state of number in [0, n-1]
    """
    
    def __init__(self, n: int):
        # Each 32 bit integer can store 32 numbers' states
        # So we only need (n // 32 + 1) integers to store states of numbers in [0, n-1]
        self.nums = [0] * (n // 32 + 1)

    """
    If num is not in bitset, put it in the bitset (Set its corresponding bit to 1)

    Args:
        num (int) - The number to be added
    """
    def add(self, num: int):
        self.nums[num // 32] |= (1 << (num % 32))

    def remove(self, num: int):
        self.nums[num // 32] &= ~(1 << (num % 32))

    def flip(self, num: int):
        self.nums[num // 32] ^= (1 << (num % 32))

    def contains(self, num: int):
        return (self.nums[num // 32] >> num % 32) & 1 == 1

    def clear(self):
        self.nums = [0 for _ in self.nums]