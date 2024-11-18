# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
sys.path.append(str(src_folder))

from src.data_structure.linkedlist import SingleLinkedList, DoubleLinkedList
from src.utils.validator.data_structure_validator import DataStructureValidator


def get_single_linkedlist_data(linkedlist):
    cur = linkedlist.head
    data = []
    while cur is not None:
        data.append(cur.value)
        cur = cur.next
    return data


def get_double_linkedlist_data(linkedlist):
    data = []
    cur_node = linkedlist.head
    while cur_node != linkedlist.tail:
        data.append(cur_node.value)
        cur_node = cur_node.next
    if linkedlist.tail is not None:
        data.append(linkedlist.tail.value)
    return data


if __name__ == "__main__":
    # Tests for Single Linked List 
    single_linkedlist = SingleLinkedList()
    validator = DataStructureValidator(
        data_structure=single_linkedlist,
        action_space=["add", "remove", "insert"],
        action_map={
            "add": lambda x, value: x.append(value),
            "remove": lambda x, value: x.remove(value),
            "insert": lambda x, index, value: x.insert(index, value)
        },
        action_value_map={
            "add": [None],
            "remove": ["element"],
            "insert": ["length", None]
        },
        add_actions=["add", "insert"],
        remove_actions=["remove"],
        get_data=get_single_linkedlist_data,
        lower_length=3,
        upper_length=10,
        length_seed=1111,
        action_seed=2222,
        break_on_fail=True,
        header_text="Conducting tests for Single Linked List"
    )
    validator.validate(num_of_test=5000)

    # Tests for Double Linked List
    double_linkedlist = DoubleLinkedList()
    validator = DataStructureValidator(
        data_structure=double_linkedlist,
        action_space=["add", "remove", "insert"],
        action_map={
            "add": lambda x, value: x.append(value),
            "remove": lambda x, value: x.remove(value),
            "insert": lambda x, index, value: x.insert(index, value) if index < len(x) else x.append(value)
        },
        action_value_map={
            "add": [None],
            "remove": ["element"],
            "insert": ["length", None]
        },
        add_actions=["add", "insert"],
        remove_actions=["remove"],
        get_data=get_double_linkedlist_data,
        lower_length=3,
        upper_length=50,
        length_seed=3456,
        action_seed=4567,
        break_on_fail=True,
        header_text="Conducting tests for Double Linked List"
    )
    validator.validate(5000)