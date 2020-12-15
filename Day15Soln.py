def last_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))

    
def main():
    puzzle_input = [14, 3, 1, 0, 9, 5]
    number_indices = {puzzle_input[i]: [i] for i in range(len(puzzle_input))}
    last_num = puzzle_input[-1]
    for i in range(len(puzzle_input), 30000000):
        if len(number_indices[last_num]) == 1:
            last_num = 0
            number_indices[last_num].append(i)
            continue
        
        last_num = number_indices[last_num][-1] - number_indices[last_num][-2]
        if last_num in number_indices:
            number_indices[last_num].append(i)
        else:
            number_indices[last_num] = [i]
    
    print(last_num)

if __name__ == "__main__":
    main()
