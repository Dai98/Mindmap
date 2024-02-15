from abc import ABCMeta, abstractmethod
import random


class Generator(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def generate(self):
        raise NotImplementedError("generator.py-Generator/Abstract method generate is not implemented in base class.")
    

class RandomNumberGenerator(Generator):

    def __init__(self, 
                 lower: int = -200, 
                 upper:int = 200,
                 seed:int = None) -> None:
        super().__init__()
        self.seed = seed
        self.lower = lower
        self.upper = upper
        if seed is not None:
            random.seed(self.seed)

    def generate(self):
        return random.randint(self.lower, self.upper)


class ArrayGenerator(Generator):
    def __init__(self,
                 lower_length: int = 2,
                 upper_length: int = 500,
                 lower_value: int = -200,
                 upper_value: int = 200,
                 length_seed: int = None,
                 value_seed: int = None) -> None:
        super().__init__()
        self.lower_length = lower_length
        self.upper_length = upper_length
        self.lower_value = lower_value
        self.upper_value = upper_value
        self.length_seed = length_seed
        self.value_seed = value_seed

        self.length_generator = RandomNumberGenerator(lower_length, upper_length, length_seed)
        self.value_generator = RandomNumberGenerator(lower_value, upper_value, value_seed)

    def generate(self):
        length = self.length_generator.generate()
        array = []
        for _ in range(length):
            array.append(self.value_generator.generate())
        return array
