# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
sys.path.append(str(src_folder))

from src.algorithms.sort import SelectionSort, BubbleSort, InsertionSort, MergeSort, HeapSort, QuickSort, HeapSort, RadixSort
from src.utils.validator.sort_validator import SortValidator


if __name__ == "__main__":

    # Testing for Selection Sort
    selection_validator = SortValidator(SelectionSort(), length_seed=1, value_seed=2, header_text="Conducting tests for Selection Sort")
    selection_validator.validate(5000)

    # Testing for Bubble Sort
    bubble_validator = SortValidator(BubbleSort(), length_seed=3, value_seed=4, header_text="Conducting tests for Bubble Sort")
    bubble_validator.validate(5000)

    # Testing for Insertion Sort
    insertion_validator = SortValidator(InsertionSort(), length_seed=5, value_seed=6, header_text="Conducting tests for Insertion Sort")
    insertion_validator.validate(5000)

    # Testing for Merge Sort
    # Test recursive
    merge_validator = SortValidator(MergeSort('recursive'), length_seed=6, value_seed=7, header_text="Conducting tests for Merge Sort with recursive implementation")
    merge_validator.validate(5000)

    # Test non-recursive
    merge_validator = SortValidator(MergeSort('non-recursive'), length_seed=8, value_seed=9, header_text="Conducting tests for Merge Sort with non-recursive implementation")
    merge_validator.validate(5000)

    # Testing for Quick Sort
    # Test Naive Partition
    quick_validator = SortValidator(QuickSort(mode='naive'), length_seed=10, value_seed=11, header_text="Conducting tests for Quick Sort with naive partition")
    quick_validator.validate(5000)

    # Test optimized partition with Dutch National Flag problem
    quick_validator = SortValidator(QuickSort(mode='dutch'), length_seed=12, value_seed=13, header_text="Conducting tests for Quick Sort with dutch partition")
    quick_validator.validate(5000)
    
    # Testing for Heap Sort
    heap_validator = SortValidator(HeapSort(), length_seed=14, value_seed=15, header_text="Conducting tests for Heap Sort")
    heap_validator.validate(5000)

    # Testing for Radix Sort
    radix_validator = SortValidator(RadixSort(), length_seed=16, value_seed=17, header_text="Conducting tests for Radix Sort")
    radix_validator.validate(5000)
