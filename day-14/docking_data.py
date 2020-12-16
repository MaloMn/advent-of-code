from utils import get_lines
import re


class Memory:

    def __init__(self):
        self.mem = []

    def insert(self, index, value):
        if index >= len(self.mem):
            self.mem += [0]*(index - len(self.mem) + 1)
        self.mem[index] = value

    def sum(self):
        return sum(self.mem)


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


def apply_mask(nb: int, m: str) -> int:
    nb_binary = dec_to_bin(nb)
    nb_binary = list(nb_binary)
    print(nb_binary, len(nb_binary))

    # Applying the mask
    for i, c in enumerate(m):
        if c != 'X':
            nb_binary[i] = c

    return bin_to_dec(''.join(nb_binary))


if __name__ == "__main__":
    data = get_lines("docking.txt")
    mem = Memory()
    mask = 'X'*32
    for d in data:
        if "mask" in d:
            mask = d[7:]
        else:
            i, n = re.findall(r'\d+', d)
            n = apply_mask(int(n), mask)
            mem.insert(int(i), n)

    print(mem.sum())
