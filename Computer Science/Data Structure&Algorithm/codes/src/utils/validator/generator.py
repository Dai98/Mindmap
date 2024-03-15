from abc import ABC, abstractmethod
import random


class Generator(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def generate(self):
        raise NotImplementedError("generator.py-Generator/Abstract method generate is not implemented in base class.")
    

class RandomNumberGenerator(Generator):
    """
        A generator for random number between lower and upper (inclusive)

        Attr:
            lower (int) - The lower bound for a random number
            upper (int) - The upper bound for a random number
            seed (int) - The seed for random number generation
    """

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

    """
        The generate interface implemented to generate a random integer

        Args:
            None
        Return:
            int, a random integer
    """
    def generate(self):
        return random.randint(self.lower, self.upper)


class ArrayGenerator(Generator):
    """
        A generator to generate an array with random length and random values

        Attr:
            lower_length (int) - The lower bound of random length
            upper_length (int) - The upper bound of random length
            lower_value (int) - The lower bound of random value
            upper_value (int) - The upper bound of random value
            length_seed (int) - The random seed for generating length of the array
            value_seed (int) - The random seed for generating values of the array
    """
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

    """
        The generate interface implemented to generate a random array

        Args:
            None
        Return:
            An array, with random length and random values
    """
    def generate(self):
        length = self.length_generator.generate()
        array = []
        for _ in range(length):
            array.append(self.value_generator.generate())
        return array
    

class ActionGenerator(Generator):
    """
        A generator to generate an array of random actions of a data structure to test its functionalities
        An action is a method of a data structure

        Attr:
            action_space (list) - A list of string method names of the data structure
            add_action_name (list) - A list of string method names that will increment the length of the data structure
            remove_action_name (list) - A list of string method names that will decrement the length of the data structure
            lower_length (int) - The lower bound of the length of action array
            upper_length (int) - The upper bound of the length of action array
            length_seed (int) - The random seed for generating length of the action array
            action_seed (int) - The random seed for generating actions of the action array
    """
    def __init__(self, 
                 action_space: list,
                 add_action_name: list,
                 remove_action_name: list,
                 lower_length: int = 3,
                 upper_length: int = 30,
                 length_seed: int = None,
                 action_seed: int = None) -> None:
        super().__init__()
        # add_num is a simulated virtual length of a data structure
        self.add_num = 0
        self.action_space = action_space
        self.add_action = add_action_name
        self.remove_action = remove_action_name
        self.length_generator = RandomNumberGenerator(lower=lower_length, upper=upper_length, seed=length_seed)
        self.action_generator = RandomNumberGenerator(lower=0, upper=len(action_space)-1, seed=action_seed)

    """
        The generate interface implemented to generate a random array of actions

        Args:
            None
        Return:
            An array, each element is a tuple, with
            (action_name, current_length)

            Action name is the randomly selected method of the data structure, 
            and the virtual length when the action was selected is also returned along with method name
            This will be used to assist generate data/parameters for the selected methods
    """
    def generate(self):
        # Before each generation of random actions, reset the virtual length to 0
        self._reset_state()
        num_of_actions = self.length_generator.generate()
        actions = []
        for _ in range(num_of_actions):
            action_index = self.action_generator.generate()
            # If there are no data added into the data structure, then no remove action is allowed
            # If remove action generated, then generate another random action until it is not a remove action anymore
            if self.action_space[action_index] in self.remove_action and self.add_num == 0:
                while self.action_space[action_index] in self.remove_action:
                    action_index = self.action_generator.generate()
                if self.action_space[action_index] in self.add_action:
                    self.add_num += 1
            # Only when there are data in data structure, remove actions are allowed
            elif self.action_space[action_index] in self.remove_action and self.add_num > 0:
                self.add_num -= 1
            # If an add action is generated, increment the virtual length by 1
            elif self.action_space[action_index] in self.add_action:
                self.add_num += 1
            else:
                pass
            actions.append((self.action_space[action_index], self.add_num))
        return actions
    
    def _reset_state(self):
        self.add_num = 0
