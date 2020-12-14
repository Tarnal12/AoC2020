def main():
    with open("Day13Input.txt", "r") as f:
        (start_time, busses) = f.readlines()
        start_time = int(start_time)

    shortest_wait = (-1, 999)
    for bus_id in busses.split(','):
        if bus_id == 'x':
            continue

        bus_id = int(bus_id)
        wait_time = bus_id - (start_time % bus_id)
        if wait_time < shortest_wait[1]:
            shortest_wait = (bus_id, wait_time)
    print(f"Part 1: {shortest_wait[0] * shortest_wait[1]}")

    # Need a number where bus_id - (start_time % bus_id) = 0
    # bus_id - (start_time % bus_id_2) = 1
    # etc. (ignore x's)
    bus_offsets = []
    i = 0
    for bus_id in busses.split(','):
        if bus_id.isnumeric():
            bus_offsets.append((int(bus_id), i))
        i += 1
    bus_offsets.sort(reverse=True)
            
    jackpot = False
    step_size = bus_offsets[0][0]
    possible_t = 0 - bus_offsets[0][1]
    conditions_fulfilled = 1

    possible_t = 581588423192424
    step_size = 323681
    conditions_fulfilled = 2

    while not jackpot:
        possible_t += step_size
        jackpot = True
        for bus in bus_offsets[conditions_fulfilled:]:
            tmp = possible_t % bus[0]
            if (bus[0] - (possible_t % bus[0]) != bus[1]) and (tmp != 0 or bus[1] != 0):
                jackpot = False
                break
            else:
                step_size = step_size * bus[0]
                conditions_fulfilled += 1
    print(possible_t)

if __name__ == "__main__":
    main()
