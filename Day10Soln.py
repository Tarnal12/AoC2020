from typing import List

def count_possibilities(adapters: List[int]) -> int:
    if len(adapters) <= 2:
        return 1

    adapter_copy = adapters.copy()
    adapter_copy.remove(adapters[0])

    possibilities = 0
    if adapters[0] + 1 in adapters:
        sub_possibilities = count_possibilities(adapter_copy)
        possibilities = possibilities + sub_possibilities
        adapter_copy.remove(adapters[0] + 1)

    if adapters[0] + 2 in adapters:
        sub_possibilities = count_possibilities(adapter_copy)
        possibilities = possibilities + sub_possibilities
        adapter_copy.remove(adapters[0] + 2)

    if adapters[0] + 3 in adapters:
        sub_possibilities = count_possibilities(adapter_copy)
        possibilities = possibilities + sub_possibilities
        adapter_copy.remove(adapters[0] + 3)

    return possibilities

if __name__ == "__main__":
    with open("Day10Input.txt", "r") as f:
        adapters = list(map(int, f.read().split('\n')))
        adapters.append(0)
        adapters.append(max(adapters) + 3)
        adapters.sort()

    diff_count = {
        1: 0,
        2: 0,
        3: 0
    }
    diff_of_three_indices = []
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        diff_count[diff] = diff_count[diff] + 1
        if diff == 3:
            diff_of_three_indices.append(i + 1)

    # Part 1
    print(diff_count)
    print(diff_count[1] * diff_count[3])

    # Part 2
    prev_i = 0
    total_possibilities = 1
    for i in diff_of_three_indices:
        subset = adapters[prev_i:i]
        subset_possibilities = count_possibilities(subset)
        print(f"{subset} can be arranged {subset_possibilities} ways")
        total_possibilities = total_possibilities * subset_possibilities
        prev_i = i
    print(total_possibilities)
