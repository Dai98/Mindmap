# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(src_folder))
sys.path.append(str(current_folder))

from validator import Validator
from algorithms.sort import Sort
from generator import ArrayGenerator


class SortValidator(Validator):

    def __init__(self, 
                 sort_algorithm: Sort, 
                 break_on_fail: bool = True,
                 lower_length: int = 10,
                 upper_length: int = 300,
                 lower_value: int = -65535,
                 upper_value: int = 65536,
                 length_seed: int = 42,
                 value_seed: int = 43,
                 header_text: str = None
                ) -> None:
        super().__init__(break_on_fail)
        self.sort = sort_algorithm
        self.generator = ArrayGenerator(lower_length, upper_length, lower_value, upper_value, length_seed, value_seed)

        if header_text != None:
            self.header_text = header_text

    def _generate_sample(self):
        return self.generator.generate()
            
    def _get_expected_output(self, sample: list):
        return sorted(sample)
    
    def _get_actual_output(self, sample: list):
        return self.sort.sort(sample)
    
    def _compare_equal(self, actual_output: list, expected_output: list) -> bool:
        if len(actual_output) != len(expected_output):
            return False
        
        for actual_value, expected_value in zip(actual_output, expected_output):
            if actual_value != expected_value:
                return False
        return True
