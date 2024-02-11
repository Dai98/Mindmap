

class Bit:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getTwosComplement(num: int, truncate: bool = True, bits: int = 32) -> str:
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
    

if __name__ == "__main__":
    print(Bit.getTwosComplement(-5))