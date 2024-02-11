from abc import ABCMeta, abstractmethod
from tqdm import tqdm
from enum import Enum
from typing import Any
from colorama import init, Fore

from time import sleep


class TestResult(Enum):
    SUCCESS = 1
    FAILED = 2


class Test:
    def __init__(self, test_index: int, actual_output: Any, expected_output: Any, result: TestResult):
        self.test_index = test_index
        self.actual_output = actual_output
        self.expected_output = expected_output
        self.result = result

    def show_failed_test(self):
        if self.result == TestResult.FAILED:
            print(f" -------- Test {self.test_index} is ", end="")
            print(Fore.RED + "FAILED ", end="")
            print("--------")

            print(" EXPECTED: ", end="")
            print(Fore.RED + str(self.expected_output))
            print(" ACTUAL:   ", end="")
            print(Fore.RED + str(self.actual_output))
            print()


class Validator(metaclass=ABCMeta):
    def __init__(self, break_on_fail: bool = True) -> None:
        self.header_text = "Conducting testing"
        self.break_on_fail = break_on_fail

    def validate(self, num_of_test: int):
        test = tqdm(range(1, num_of_test+1), colour="green", desc="Executing", unit="tests")
        test.write(self.header_text)
        failed_tests = []
        init(autoreset=True)
        for test_index in test:
            sample_data = self._generate_sample()
            actual_output = self._get_actual_output(sample_data)
            expected_output = self._get_expected_output(sample_data)
            test_result = self._compare_equal(actual_output, expected_output)
            if not test_result:
                failed_test = Test(test_index, actual_output, expected_output, TestResult.FAILED)
                if not self.break_on_fail:
                    failed_tests.append(failed_test)
                else:
                    print(Fore.RED + " Failed test encountered. Testing stopped.")
                    failed_test.show_failed_test()
                    break
            else:
                # Release memory
                del sample_data, actual_output, expected_output
        if not self.break_on_fail:
            self._print_test_result(num_of_test, failed_tests)
        else:
            self._print_successful_test(num_of_test, failed_tests)
        print()
        
    @abstractmethod
    def _generate_sample(self):
        raise NotImplementedError("validator.py-Validator/Abstract method _generate_sample is not implemented in base class.")
            
    @abstractmethod
    def _get_expected_output(self, sample: Any):
        raise NotImplementedError("validator.py-Validator/Abstract method _get_expected_output is not implemented in base class.")
    
    @abstractmethod
    def _get_actual_output(self, sample: Any):
        raise NotImplementedError("validator.py-Validator/Abstract method _get_actual_output is not implemented in base class.")
    
    @abstractmethod
    def _compare_equal(self, actual_output: Any, expected_output: Any) -> bool:
        raise NotImplementedError("validator.py-Validator/Abstract method _generate_sample is not implemented in base class.")

    def _print_successful_test(self, num_of_test: int, failed_test: list):
        num_of_successful_tests = num_of_test - len(failed_test)
        if num_of_successful_tests == num_of_test:
            print(f" All {num_of_successful_tests} tests finished with ", end="")
        else:
            print(f" The other {num_of_successful_tests} tests finished with ", end="")
        print(Fore.GREEN + "SUCCESS")

    def _print_test_result(self, num_of_test: int, failed_test: list):
        print("\nTest Result - ")
        for test in failed_test:
            test.show_failed_test()
        self._print_successful_test(num_of_test, failed_test)
