# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
sys.path.append(str(src_folder))

from src.data_structure.queue import Queue, CircularQueue, LinkedQueue
from src.utils.validator.data_structure_validator import DataStructureValidator



def get_queue_data(queue) -> list:
    data = []
    while queue.size != 0:
        data.append(queue.pop())
    return data


if __name__ == "__main__":
    # Tests for basic queue
    queue = Queue(50)
    validator = DataStructureValidator(
        data_structure=queue,
        action_space=["pop", "push", "get_size", "peek_front", "peek_rear"],
        action_map={
            "pop": lambda x: x.pop(0),
            "push": lambda x, value: x.append(value),
            "get_size": lambda x: len(x),
            "peek_front": lambda x: x[0] if len(x) >= 1 else None,
            "peek_rear": lambda x: x[-1] if len(x) >= 1 else None
        },
        action_value_map={
            "pop": [],
            "push": [None],
            "get_size": [],
            "peek_front": [],
            "peek_rear": []
        },
        add_actions=["push"],
        remove_actions=["pop"],
        get_data=get_queue_data,
        lower_length=3,
        upper_length=50,
        length_seed=12345,
        action_seed=23456,
        break_on_fail=True,
        header_text="Conducting tests for Basic Queue"
    )
    validator.validate(num_of_test=5000)
    del queue, validator

    # Tests for circular queue
    circular_queue = CircularQueue(50)
    validator = DataStructureValidator(
        data_structure=circular_queue,
        action_space=["pop", "push", "get_size", "peek_front", "peek_rear"],
        action_map={
            "pop": lambda x: x.pop(0),
            "push": lambda x, value: x.append(value),
            "get_size": lambda x: len(x),
            "peek_front": lambda x: x[0] if len(x) >= 1 else None,
            "peek_rear": lambda x: x[-1] if len(x) >= 1 else None
        },
        action_value_map={
            "pop": [],
            "push": [None],
            "get_size": [],
            "peek_front": [],
            "peek_rear": []
        },
        add_actions=["push"],
        remove_actions=["pop"],
        get_data=get_queue_data,
        lower_length=3,
        upper_length=50,
        length_seed=34567,
        action_seed=45678,
        break_on_fail=True,
        header_text="Conducting tests for Circular Queue"
    )
    validator.validate(num_of_test=5000)
    del circular_queue, validator

    # Tests for linked queue
    linked_queue = LinkedQueue()
    validator = DataStructureValidator(
        data_structure=linked_queue,
        action_space=["pop", "push", "get_size", "peek_front", "peek_rear"],
        action_map={
            "pop": lambda x: x.pop(0),
            "push": lambda x, value: x.append(value),
            "get_size": lambda x: len(x),
            "peek_front": lambda x: x[0] if len(x) >= 1 else None,
            "peek_rear": lambda x: x[-1] if len(x) >= 1 else None
        },
        action_value_map={
            "pop": [],
            "push": [None],
            "get_size": [],
            "peek_front": [],
            "peek_rear": []
        },
        add_actions=["push"],
        remove_actions=["pop"],
        get_data=get_queue_data,
        lower_length=3,
        upper_length=50,
        length_seed=56789,
        action_seed=67890,
        break_on_fail=True,
        header_text="Conducting tests for Linked Queue"
    )
    validator.validate(num_of_test=5000)
    del linked_queue, validator
