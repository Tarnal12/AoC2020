from typing import List
import itertools


def apply_mask(x: int, mask: str) -> int:
    bitstr = to_bitstr(x)
    bitstr = apply_mask_to_bitstr(bitstr, mask)
    return to_int(bitstr)

def apply_mem_decoder(x: int, mask: str) -> List[int]:
    bitstr = to_bitstr(x)
    bitstrs = apply_mem_decoder_to_bitstr(bitstr, mask)
    return [to_int(x) for x in bitstrs]

def to_bitstr(x: int) -> str:
    return format(x, '036b')

def to_int(bitstr: str) -> int:
    return int(bitstr, 2)

def apply_mask_to_bitstr(bitstr: str, mask: str) -> str:
    assert len(bitstr) == len(mask)
    outstr = ""
    for i in range(len(bitstr)):
        if mask[i] == "X":
            outstr += bitstr[i]
        else:
            outstr += mask[i]
    return outstr

def apply_mem_decoder_to_bitstr(bitstr: str, mask: str) -> List[str]:
    assert len(bitstr) == len(mask)
    masked_str = ""
    for i in range(len(bitstr)):
        if mask[i] == "0":
            masked_str += bitstr[i]
        else:
            masked_str += mask[i]
    
    combinations = [masked_str]
    for i in range(masked_str.count('X')):
        new_combinations = []
        for combo in combinations:
            new_combinations.append(combo.replace('X', "1", 1))
            new_combinations.append(combo.replace('X', "0", 1))
        combinations = new_combinations.copy()
    return combinations

def main():
    with open("Day14Input.txt", "r") as f:
        input_data = f.readlines()

    mask = ["X" for i in range(36)]
    mem = {}
    mem2 = {}
    for line in input_data:
        (raw_field, raw_value) = line.split(' = ')
        if raw_field == "mask":
            mask = raw_value.strip('\n')
            continue

        field = int(raw_field.split('[')[1].split(']')[0])
        value = apply_mask(int(raw_value), mask)
        mem[int(field)] = value

        fields = apply_mem_decoder(int(field), mask)
        for field in fields:
            mem2[field] = int(raw_value)
    
    total = 0
    for val in mem:
        total += mem[val]
    print(total)
    
    total2 = 0
    for val in mem2:
        total2 += mem2[val]
    print(total2)

if __name__ == "__main__":
    main()