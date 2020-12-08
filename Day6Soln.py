from collections import Counter


if __name__ == "__main__":
    with open("Day6Input.txt", "r") as f:
        contents = f.read()
        group_responses = [block for block in contents.split('\n\n')]

    # Part 1
    total_occurences = 0
    for group_resp in group_responses:
        response = list(group_resp.replace('\n', ''))
        unique_answers = Counter(response).keys()
        total_occurences = total_occurences + len(unique_answers)

    print("Sum of answeres where anyone answered yes = ", total_occurences)

    # Part 2
    total_occurences = 0
    for group_resp in group_responses:
        individual_responses = group_resp.split('\n')
        union_of_true_answers = individual_responses[0]
        if len(individual_responses) == 1:
            total_occurences = total_occurences + len(union_of_true_answers)
            continue

        for individual_resp in individual_responses[1:]:
            union_of_true_answers = [char for char in union_of_true_answers if char in individual_resp]
        total_occurences = total_occurences + len(union_of_true_answers)

    print("Sum of answeres where anyone everyone yes = ", total_occurences)
