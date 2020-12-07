from typing import List


def get_tree_map(puzzle_input: str) -> List[List[bool]]:
    full_map = []
    for line in puzzle_input.split('\n'):
        row = []
        for cell in line:
            row.append(cell == "#")
        full_map.append(row)
    #print(full_map)
    return full_map


if __name__ == "__main__":
    with open("Day3Inputs.txt", "r") as f:
        contents = f.read()
        all_inputs = [block for block in contents.split('\n\n')]

    for puzzle_input in all_inputs:
        print("   >>> NEW PUZZLE INPUT")
        tree_map = get_tree_map(puzzle_input)

        tree_count_soln = 1
        for angle in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
            map_width = len(tree_map[0])
            tree_count = 0
            tick = 0
            for row in tree_map:
                if tick * angle[1] > len(tree_map):
                    break

                y = tick * angle[1]
                x = (tick * angle[0]) % map_width
                tree_count = tree_count + int(tree_map[y][x])
                tick = tick + 1
            tree_count_soln = tree_count_soln * tree_count
            print(f"{tree_count} trees encountered going {angle[0]} right and {angle[1]} down (product = {tree_count_soln})")
