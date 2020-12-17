from utils import get_lines
import re
from typing import List


class Memory:
    def __init__(self):
        self.mem = dict()

    def insert(self, index: int, value: int):
        # print(index, value)
        self.mem[index] = value

    def sum(self):
        return sum(self.mem.values())


def bin_to_dec(binary: str) -> int:
    output = 0
    for j, p in enumerate(binary[::-1]):
        output += 2**j * int(p)
    return output


def dec_to_bin(decimal: int) -> str:
    bits = 35
    output = ''
    for p in range(bits, -1, -1):
        if decimal - 2**p >= 0:
            output += '1'
            decimal = decimal - 2**p
        else:
            output += '0'
    return output


def apply_mask(nb: int, m: str) -> List[int]:
    nb_binary = dec_to_bin(nb)
    nb_binary = list(nb_binary)

    # Applying the mask
    floating = []
    for j, c in enumerate(m):
        if c == '1':
            nb_binary[j] = '1'
        elif c == 'X':
            floating.append(j)

    output = []
    for line in gray_code(len(floating)):
        for index, position in enumerate(floating):
            nb_binary[position] = str(line[index])
        output.append(''.join(nb_binary))

    if len(output) == 0:
        output = [''.join(nb_binary)]

    return [bin_to_dec(a) for a in output]


def gray_code(nb_bits):
    if nb_bits == 1:
        return [(0,), (1,)]
    else:
        piece = gray_code(nb_bits - 1)
        output = []
        for line in piece:
            output.append((0,) + line)
        for line in piece[::-1]:
            output.append((1,) + line)
        return output


if __name__ == "__main__":
    data = get_lines("docking.txt")
    mem = Memory()
    mask = 'X'*32
    for d in data:
        if "mask" in d:
            mask = d[7:]
        else:
            i, n = re.findall(r'\d+', d)
            locations = apply_mask(int(i), mask)
            for loc in locations:
                mem.insert(loc, int(n))

    print(mem.sum())
