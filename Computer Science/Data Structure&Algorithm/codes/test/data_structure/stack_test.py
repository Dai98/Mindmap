# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
sys.path.append(str(src_folder))

from src.data_structure.stack import Stack
from src.utils.validator.data_structure_validator import DataStructureValidator


if __name__ == "__main__":
    stack = Stack()
    validator = DataStructureValidator(
        data_structure=stack,
        action_space=["pop", "push", "peek"],
        action_map={
            "pop": lambda x: x.pop(),
            "push": lambda x, value: x.append(value),
            "peek": lambda x: x[-1] if len(x) > 0 else None
        },
        action_value_map={
            "pop": [],
            "push": [None],
            "peek": []
        },
        add_actions=["push"],
        remove_actions=["pop"],
        get_data=lambda stack: [element for index, element in enumerate(stack.data) if element is not None and index < stack.index],
        lower_length=3,
        upper_length=50,
        length_seed=1333,
        action_seed=1344,
        break_on_fail=False,
        header_text="Conducting tests for Stack"
    )
    validator.validate(2000)

