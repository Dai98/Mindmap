import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(src_folder))
sys.path.append(str(current_folder))

import random
from typing import Any
from validator import Validator
from generator import ActionGenerator, RandomNumberGenerator


class DataStructureValidator(Validator):

    """
        A validator for testing all data structures

        Attr:
            data_structure (Any) - An object of the data structure to test
            action_space (list) - A list of string methods name of the data structure to test
            action_map (dict) - A dict with string method names as keys and a callable object as values.
                                Each callable method will return an equivalent operation on a list
            action_value_map (dict) - A dict with string method names as keys and lists as values
                                      The elements of the list represents the restriction of generated parameters of the method
                                      Following values can be put in the list - 
                                      * None - No restriction, any numbers
                                      * A tuple with a smaller number and a larger number - A range for number generation, 
                                            an integer will be picked from this range
                                      * 'length' string - A number netween 0 and length-1 will be picked
                                            This is normally for generating an index for data structure
                                      * 'element' string - An existing number element in the data structure
                                            This is normally use to randomly select an existing element from data structure
            add_actions (list) - A list of string method names that will increase number of elements in data structure
            remove_actions (list) - A list of string method names that will reduce number of elements in data structure
            get_data (callable) - A callable function to retrieve all the data from the data structure
                                  Useful for data structures that don't explictly store all data in one property, e.g. Linked List
            lower_length (int) - The minimum number of actions randomly generated
            upper_length (int) - The maximum number of actions randomly generated
            length_seed (int) - The random seed used to generate number of actions
            action_seed (int) - The random seed used to generate actions
            lower_value (int) - The minimum value for data samples generated for data structure
            upper_value (int) - The maximum value for data samples generated for data structure
            value_seed (int) - The random seed used to generate data in data structure
            break_on_fail (bool) - When encounter a failed test, whether to stop whole testing and show this current failed test
                                   Or continue testing and show all failed tests all at once in the end
                                   Pass True to stop testing on failed test, pass False to continue testing
            print_sample_on_fail (bool) - Whether to print failed test samples for failed tests
            header_text (str) - A string that will be printed at the top of progress bar as the header text
    """

    def __init__(self, 
                 data_structure: Any,
                 action_space: list,
                 action_map: dict,
                 action_value_map: dict,
                 add_actions: list,
                 remove_actions: list,
                 get_data: callable,
                 lower_length: int = 3,
                 upper_length: int = 20,
                 length_seed: int = None,
                 action_seed: int = None,
                 lower_value: int = -1000,
                 upper_value: int = 1000,
                 value_seed: int = None,
                 break_on_fail: bool = True,
                 print_sample_on_fail: bool = True,
                 header_text: str = None) -> None:
        super().__init__(break_on_fail, print_sample_on_fail, header_text)
        self.data_structure = data_structure
        self.action_map = action_map
        self.action_value_map = action_value_map
        self.get_data = get_data

        for add_action in add_actions:
            assert add_action in action_space, f"data_structure_validator.py-DataStructureValidator/Add action {add_action} is not in action space."
        for remove_action in remove_actions:
            assert remove_action in action_space, f"data_structure_validator.py-DataStructureValidator/Remove action {remove_action} is not in action space."
        
        assert len(action_space) == len(action_map), "data_structure_validator.py-DataStructureValidator/Action map doesn't match action space."
        for action in action_map:
            if action not in action_space:
                raise AssertionError(f"data_structure_validator.py-DataStructureValidator/Action space doesn't have method {action}.")
        
        self.action_generator = ActionGenerator(action_space=action_space, add_action_name=add_actions, remove_action_name=remove_actions,
                                                lower_length=lower_length, upper_length=upper_length, length_seed=length_seed, action_seed=action_seed)
        self.value_generator = RandomNumberGenerator(lower=lower_value, upper=upper_value, seed=value_seed)

    """
        Generate sample for one test
        Args:
            None
        Return
            A list, each element is (method name, [its corresponding parameters])
    """
    def _generate_sample(self) -> list:
        actions = self.action_generator.generate()
        sample = []
        for action, cur_length in actions:
            # For each action (method), get what parameters does it need
            value_ranges = self.action_value_map[action]
            values = []
            for value_range in value_ranges:
                # If None, then no restriction
                # Any numbers between [lower_value, upper_value] will be returned
                if value_range is None:
                    value = self.value_generator.generate()
                    values.append(value)
                # If an explict tuple is passed, then it is used as a range
                # Then only random numbers within this range will be returned
                elif isinstance(value_range, tuple):
                    lower, upper = value_range
                    value = random.randint(lower, upper)
                    values.append(value)
                # If a string 'length' is passed
                # Then a random number between [0, length-1] will be returned
                # Usually for randomly generated index
                elif isinstance(value_range, str) and value_range == "length":
                    if cur_length == 0:
                        values.append(0)
                    else:
                        value = random.randint(0, cur_length-1)
                        values.append(value)
                # If a string 'element' is passed
                # Then a valid existing element will be returned
                # Usually for randomly selecting an existing element to remove
                elif isinstance(value_range, str) and value_range == "element":
                    add_values = []
                    for prev_action, params in sample:
                        if prev_action in self.action_generator.add_action:
                            add_values.append(params[-1])
                        if prev_action in self.action_generator.remove_action:
                            add_values.remove(params[-1])
                    index = random.randint(0, len(add_values)-1)
                    values.append(add_values[index])
                else:
                    raise ValueError("data_structure_validator.py-DataStructureValidator/Invalid value range {value_range}. Use tuple for values with range, use None for values without range.\n You can also use 'length' to randomly generate a number for a valid index or 'element' to randomly pick an element.")
            sample.append((action, values))
        return sample

    """
        Get expected results
        Args:
            sample (list) - The sample list generated by _generate_sample method
        Return:
            A tuple with two lists as elements, 
            the first list is the final data of the simulated data structure
            the second list is the return values of all actions returned during execution
    """
    def _get_expected_output(self, sample: list):
        self.data_structure.clear()
        expected_return = []
        expected_data = []
        for action, params in sample:
            map_func = self.action_map[action]
            if len(params) == 0:
                map_return = map_func(expected_data)
            else:
                map_return = map_func(expected_data, *params)
            expected_return.append(map_return)
        expected_data = expected_data
        return expected_data, expected_return
    
    """
        Get actual results
        Args:
            sample (list) - The sample list generated by _generate_sample method
        Return:
            A tuple with two lists as elements, 
            the first list is the final data of the actual data structure
            the second list is the return values of all actions returned during execution
    """
    def _get_actual_output(self, sample: list):
        self.data_structure.clear()
        actual_return = []
        for action, params in sample:
            action_func = getattr(self.data_structure, action)
            action_return = action_func(*params)
            actual_return.append(action_return)
        actual_data = self.get_data(self.data_structure)
        return actual_data, actual_return
    
    """
        Compare results between expected and actual results
        Args:
            actual_output (tuple) - The tuple result generated by _get_actual_output method
            expected_output (tuple) - The tuple result generated by _get_expected_output method
        Return:
            A bool value, True means actual result matches with expected results. Otherwise False
    """
    def _compare_equal(self, actual_output: tuple, expected_output: tuple) -> bool:
        actual_data, actual_return = actual_output
        expected_data, expected_return = expected_output
        if len(actual_return) != len(expected_return):
            return False
        if len(actual_data) != len(expected_data):
            return False
        for actual, expected in zip(actual_data, expected_data):
            if actual != expected:
                return False
        for actual, expected in zip(actual_return, expected_return):
            if actual != expected:
                return False
        
        return True
