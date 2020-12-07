from typing import List
from functools import reduce


def find_summing_items_in_list(
    list_to_search: List[int],
    target: int,
    num_items: int) -> List[int]:
    """ Find members of a list that sum together to yield a target number

    Args:
        list_to_search (List[int]): The list to search
        target (int): The target value that items must sum together to meet
        num_items (int): The number of items to pick

    Returns:
        List[int]: The list of values that add together to hit the target
        Returns None if there is no valid combination.
    """
    for item in list_to_search:
        if num_items == 2 and target - item in list_to_search:
            return [item, target - item]
        if num_items > 2:
            list_without_item = list_to_search
            list_without_item.remove(item)
            sub_list = find_summing_items_in_list(
                list_without_item,
                target - item,
                num_items - 1
            )
            if sub_list:
                sub_list.append(item)
                return sub_list
    return None


if __name__ == "__main__":
    with open("Day1Inputs.txt", "r") as f:
        contents = f.read()
        all_inputs = [list(map(int, block.split('\n'))) 
                      for block in contents.split('\n\n')]

    for puzzle_input in all_inputs:
        print("   >>> NEW PUZZLE INPUT")

        ans = find_summing_items_in_list(puzzle_input, 2020, 2)
        print(ans, " => ", reduce((lambda x, y: x * y), ans))

        ans = find_summing_items_in_list(puzzle_input, 2020, 3)
        print(ans, " => ", reduce((lambda x, y: x * y), ans))
