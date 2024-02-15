# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
sys.path.append(str(src_folder))

from src.algorithms.sort import SelectionSort, BubbleSort, InsertionSort
from src.utils.validator.sort_validator import SortValidator


if __name__ == "__main__":
    # Testing for Selection Sort
    selection_validator = SortValidator(SelectionSort(), length_seed=1, value_seed=2, header_text="Conducting tests for Selection Sort")
    selection_validator.validate(1000)

    # Testing for Bubble Sort
    bubble_validator = SortValidator(BubbleSort(), length_seed=3, value_seed=4, header_text="Conducting tests for Bubble Sort")
    bubble_validator.validate(1000)

    # Testing for Insertion Sort
    insertion_validator = SortValidator(InsertionSort(), length_seed=5, value_seed=6, header_text="Conducting tests for Insertion Sort")
    insertion_validator.validate(1000)
