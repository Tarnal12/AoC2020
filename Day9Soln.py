from typing import List, Tuple
import itertools


def find_summing_parts(possible_values: List[int], target: int) -> List[Tuple[int, int]]:
    return [
        pair for pair in list(itertools.product(possible_values, possible_values))
        if pair[0] != pair[1] and pair[0] + pair[1] == target
    ]

def find_summing_range(possible_values: List[int], target: int) -> List[int]:
    total = 0
    i = 0
    while total < target:
        total = total + possible_values[i]
        i = i + 1
        if total == target:
            return possible_values[:i]
    
    possible_values.pop(0)
    return find_summing_range(possible_values, target)


if __name__ == "__main__":
    with open("Day9Input.txt", "r") as f:
        input_list = list(map(int, f.read().split('\n')))

    preamble_length = 25
    current_preamble = input_list[:preamble_length]
    
    for val in input_list[preamble_length:]:
        valid_summers = find_summing_parts(current_preamble, val)
        if valid_summers:
            (a, b) = valid_summers[0]
            #print(f"{val} is {a} + {b}")
        else:
            print(f"{val} is not possible.")
            summing_range = find_summing_range(input_list, val)
            print(f"{max(summing_range)} + {min(summing_range)} = {max(summing_range) + min(summing_range)}")
            break

        current_preamble.pop(0)
        current_preamble.append(val)
