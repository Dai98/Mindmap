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

    def __init__(self, 
                 data_structure: Any,
                 action_space: list,
                 action_map: dict,
                 action_value_map: dict,
                 add_action: str,
                 remove_action: str,
                 get_data: callable,
                 lower_length: int = 3,
                 upper_length: int = 20,
                 length_seed: int = None,
                 action_seed: int = None,
                 lower_value: int = -1000,
                 upper_value: int = 1000,
                 value_seed: int = None,
                 break_on_fail: bool = True,
                 header_text: str = None) -> None:
        super().__init__(break_on_fail)
        self.data_structure = data_structure
        self.action_map = action_map
        self.action_value_map = action_value_map
        self.get_data = get_data

        assert add_action in action_space, "data_structure_validator.py-DataStructureValidator/Add action is not in action space."
        assert remove_action in action_space, "data_structure_validator.py-DataStructureValidator/Remove action is not in action space."
        assert len(action_space) == len(action_map), "data_structure_validator.py-DataStructureValidator/Action map doesn't match action space."
        for action in action_map:
            if action not in action_space:
                raise AssertionError(f"data_structure_validator.py-DataStructureValidator/Action space doesn't have method {action}.")
        
        self.action_generator = ActionGenerator(action_space=action_space, add_action_name=add_action, remove_action_name=remove_action,
                                                lower_length=lower_length, upper_length=upper_length, length_seed=length_seed, action_seed=action_seed)
        self.value_generator = RandomNumberGenerator(lower=lower_value, upper=upper_value, seed=value_seed)

        if header_text:
            self.header_text = header_text

    def _generate_sample(self) -> list:
        actions = self.action_generator.generate()
        sample = []
        for action in actions:
            value_ranges = self.action_value_map[action]
            values = []
            for value_range in value_ranges:
                if value_range is None:
                    value = self.value_generator.generate()
                    values.append(value)
                elif isinstance(value_range, tuple):
                    lower, upper = value_range
                    value = random.randint(lower, upper)
                    values.append(value)
                else:
                    raise ValueError("data_structure_validator.py-DataStructureValidator/Invalid value range {value_range}. Use tuple for values with range, use None for values without range.")
            sample.append((action, values))
        return sample

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
    
    def _get_actual_output(self, sample: list):
        self.data_structure.clear()
        actual_return = []
        for action, params in sample:
            action_func = getattr(self.data_structure, action)
            action_return = action_func(*params)
            actual_return.append(action_return)
        actual_data = self.get_data(self.data_structure)
        return actual_data, actual_return
            
    def _compare_equal(self, actual_output: list, expected_output: list) -> bool:
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
