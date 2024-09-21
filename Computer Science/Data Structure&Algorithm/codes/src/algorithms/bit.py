

class Bit:
    def __init__(self) -> None:
        pass

    """
        Getting a decimal number's Two's Complement

        Args:
            num (int) - A decimal number to convert
            truncate (bool) - Whether to remove the padding bits, default True
            bits (int) - How many bits at most, default 32
        
        Return:
            A string of Two's Complement of the input decimal number
    """
    @staticmethod
    def get_twos_complement(num: int, truncate: bool = True, bits: int = 32) -> str:
        bits_list = []
        is_padding = True
        for i in range(bits-1, -1, -1):
            bit = 0 if num & (1 << i) == 0 else 1
            # If the bit doesn't mean anything at the start (0 for positive and zero, 1 for negative numbers)
            # Then no need to store them if we want to truncate the padding bits
            if is_padding and ((truncate and num >= 0 and bit == 0) or (truncate and num < 0 and bit == 1)):
                continue
            else:
                bits_list.append(str(bit))
                is_padding = False
        # Insert the sign bit, 1 for negative and 0 for non-negative
        bits_list.insert(0, '1' if num < 0 else '0')
        
        return ''.join(bits_list)

    """
    Change binary 0 to 1 and 1 to 0

    Args:
        num (int) - 0 or 1
    Return:
        1 if input number is 0, and 0 if input number is 1
    """
    @staticmethod()
    def flip(num: int) -> int:
        return num ^ 1
    
    """
    Implementation of logical/unsigned right shift equivalent of num >>> n in Java

    E.g. 101111 >>> 3 = 000101

    Args:
        num (int) - Input number for logical right shift. Note that num will truncate to 32 bits
        n (int) - How many bits to right shift
    Return:
        Result integer after logical right shift
    """
    @staticmethod()
    def right_logical_shift(num: int, n: int) -> int:
        """
        If forget about higher bits, num is 1(31bits) for negative or 0(31bits) for positive
        The modulus of 2^32 will get the 31 bits of the number, which is the unsigned part
        """ 
        unsiged_num = num % 0x100000000
        return unsiged_num >> n
    
    """
    Return 0 for non-negative, and 1 for negative numbers
    
    Args:
        num (int) - Input number for to extract sign
    Return:
        0 for non-negative, and 1 for negative numbers
    """
    @staticmethod()
    def sign(num: int) -> int:
        # Move sign bit to the LSB
        return Bit.right_logical_shift(num, 31)
    
    """
    Get the larger number without comparison, Implementation 1

    If num1 - num2 <= 0, then num1 <= num2; If num1 - num2 > 0, then num1 > num2

    Args:
        num1 (int) - Input number 1 for comparison
        num2 (int) - Input number 2 for comparison
    Return:
        The larger number
    """
    @staticmethod()
    def get_max1(num1: int, num2: int) -> int:
        # Some languages (e.g. Java, C++, etc.) might overflow in this step
        # If num1 is a large positive number, and num2 is a very small negative number
        # diff might be larger than 2^32
        diff = num1 - num2
        a = Bit.flip(Bit.sign(diff))
        b = Bit.flip(a)
        """
        If diff >= 0, then a is 1 and b is 0
        If diff < 0, then a is 0 and b is 1
        """
        return a * num1 + b * num2
    
    """
    Get the larger number without comparison, Implementation 2
    This version will not have overflow issue

    If num1 - num2 <= 0, then num1 <= num2; If num1 - num2 > 0, then num1 > num2

    Args:
        num1 (int) - Input number 1 for comparison
        num2 (int) - Input number 2 for comparison
    Return:
        The larger number
    """
    @staticmethod()
    def get_max2(num1: int, num2: int) -> int:
        # diff might have overflow
        diff = num1 - num2

        sign1 = Bit.sign(num1)
        sign2 = Bit.sign(num2)
        sign_d = Bit.sign(diff)

        diff_sign = sign1 ^ sign2
        same_sign = Bit.flip(diff_sign)
        """
        If num1 and num2 have different signs, then same_sign is 0 and diff_sign is 1
        If num1 and num2 have the same sign, then same_sign is 1 and diff_sign is 0
        
        When to return num1:
            1. num1 and num2 have different signs, and num1 is non-negative
            2. num1 and num2 have the same sign, c is non-negative (c will not overflow in this case)
        """
        a = diff_sign * Bit.flip(sign1) + same_sign * Bit.flip(sign_d)
        b = Bit.flip(a)

        return a * num1 + b * num2
    
    """
    For an array of n distinct numbers ranged from [0, n], find the missing number (Leetcode 268)

    If a ^ b = c, then a = c ^ b (Reflexivity)

    Set a = missing number, b = XOR of all remaining numbers, c = XOR of all numbers from 0 to n-1
    Then a = c ^ b

    Args:
        nums (list) - Array with n numbers
    Return:
        The missing number
    """
    @staticmethod()
    def missing_number(nums: list) -> int:
        n = len(nums)
        total_xor = 0
        num_xor = nums[0]
        for i in range(1, n):
            num_xor ^= nums[i]
            total_xor ^= i
        total_xor ^= n
        return total_xor ^ num_xor
    
    """
    Given a non-empty array of integers nums, every element appears for even times except for one. Find that single number (Leetcode 136)

    For number that shows even times, calculation of its XOR is (a ^ a) for n times, where n >= 0, which will be 0 for n times
    For number that shows odd times, calculation of its XOR is ((b ^ b) for n times) ^ b = 0 ^ b = b, where n >= 0

    Therefore, xor = XOR of all numbers in the array = 0 ^ 0 ^ ... ^ 0 ^ b = b, where b is the number that shows for odd times

    Args:
        nums (list) - Array with n numbers, with one number that shows for odd times and the rest shows for even times
    Return:
        The single number that shows for odd times
    """
    @staticmethod()
    def find_single_number(nums: list) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor
    
    """
    Implementation of Brian Kernigan's Algorithm. Find the right most 1 in a number's binary form
    E.g.
        10110100 -> 00000100
        01101000 -> 00001000
    
    Args:
        num (int) - The number to find the rightmost 1 bit
    Return:
        The number that only keeps the rightmost 1 bit as 1, and set rest of bits as 0
    """
    @staticmethod()
    def brian_kernigan(num: int) -> int:
        return num & (-num)
    
    """
    (See missing_number first)
    Given a non-empty array of integers nums, two different elements appear for odd times and the rest appear for even times. Find those two numbers (Leetcode 260)
    
    Define xor1 = XOR of all numbers in the array, and a, b are two numbers that show for odd number of times, then
    xor1 = a ^ b, and a != b

    Since a != b, xor1 = a ^ b != 0, therefore there is at least 1 bit that is not 0 in binary form of xor1
    Therefore, a and b are different on the bit that is 1 in xor1

    In order to separate a and b, calculate xor2, which is the XOR of a subset of numbers in the array
    The subset are the numbers that are either all 0 or all 1 on the rightmost bit that is non-zero in binary form of xor1
    Use Brian Kernighan's algorithm to find the mask of xor1 with rightmost bit that is non-zero (01101000 -> 00001000)

    Then xor2 = XOR of the subset, and xor2 is either a or b, because the other number will not be in the subset
    And the numbers that show for even times will eliminate themselves during calculation of XOR

    If xor2 = a, then b = xor1 ^ xor2 = a ^ b ^ a = a ^ a ^ b = b
    If xor2 = b, then a = xor1 ^ xor2 = a ^ b ^ b = a

    Therefore, two numbers that show for odd times in the array are xor2 and xor1 ^ xor2

    Args:
        num (int) - The array of numbers that contains two numbers with odd frequency, and the rest of the numbers show for even times
    Return:
        Two numbers that show for odd times
    """
    @staticmethod()
    def find_two_numbers(nums: list) -> list:
        # Set two numbers are a and b
        xor1 = 0
        for num in nums:
            xor1 ^= num
        # xor1 = a ^ b
        # Brian Kernighan's Algorithm, find rightmost 1 bit
        # E.g. 01101000 -> 00001000
        m = xor1 & (-xor1)
        xor2 = 0
        for num in nums:
            if m & num == 0:
                xor2 ^= num
        # xor2 is a or b, the other one is xor1 ^ xor2
        return [xor2, xor1 ^ xor2]
    
    """
    Given a non-empty array of integer nums, all elements appear m times except for one element, which appears less than m times
    Find this element (Leetcode 137)

    Count the frequency sum of each bit by looping through the array
    For numbers that appear for m times, they will contribute m times in non-zero bits
    For the number that appear for k times, where k < m, it will contribute to k times to each non-zero bit, 
    making it t * m + k, where t % m != 0

    Therefore, after getting the frequency sum, we can check the frequency of which bit are not divisible by m
    If so, then this bit should be 1 for the number that appear less than m times

    Args:
        nums (list) - The list of numbers where all numbers show for m times, except for one shows for less tham m times
        m (int) - The number of times that each element shows up except for one element
    Return:
        The integer that shows less than m times
    """
    @staticmethod()
    def find_less_frequent_number(nums: list, m: int) -> int:
        bit_freq = [0] * 32
        # Get frequency of each bits of all numbers
        for num in nums:
            for n in range(0, 32):
                bit_freq[n] += (num >> n) & 1
        # Get the result by adding the bits that are not divisible by m times
        # Because they show up in the number that show less than m times
        ans = 0
        for i in range(0, 32):
            if bit_freq[i] % m != 0:
                # Avoid overflow
                ans = ans | (1 << i)
        # Add this for Python to avoid overflow
        # Python has arbitrary precison
        # Negative value = 2^n - value
        if ans >= (1 << 31):
            ans = ans - (1 << 32)
        return ans
    