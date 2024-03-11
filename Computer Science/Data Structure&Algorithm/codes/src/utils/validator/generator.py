from abc import ABC, abstractmethod
import random


class Generator(ABC):
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
    

class ActionGenerator(Generator):
    def __init__(self, 
                 action_space: list,
                 add_action_name: list,
                 remove_action_name: list,
                 lower_length: int = 3,
                 upper_length: int = 30,
                 length_seed: int = None,
                 action_seed: int = None) -> None:
        super().__init__()
        self.add_num = 0
        self.action_space = action_space
        self.add_action = add_action_name
        self.remove_action = remove_action_name
        self.length_generator = RandomNumberGenerator(lower=lower_length, upper=upper_length, seed=length_seed)
        self.action_generator = RandomNumberGenerator(lower=0, upper=len(action_space)-1, seed=action_seed)

    def generate(self):
        self._reset_state()
        num_of_actions = self.length_generator.generate()
        actions = []
        for _ in range(num_of_actions):
            action_index = self.action_generator.generate()
            if self.action_space[action_index] in self.remove_action and self.add_num == 0:
                while self.action_space[action_index] in self.remove_action:
                    action_index = self.action_generator.generate()
                if self.action_space[action_index] in self.add_action:
                    self.add_num += 1
            elif self.action_space[action_index] in self.remove_action and self.add_num > 0:
                self.add_num -= 1
            elif self.action_space[action_index] in self.add_action:
                self.add_num += 1
            else:
                pass
            actions.append((self.action_space[action_index], self.add_num))
        return actions
    
    def _reset_state(self):
        self.add_num = 0
