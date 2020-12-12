from typing import List, Tuple


def get_lines(filename):
    output = []
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            line = line.replace('\n', '')
            output.append(line)
    return output


def product(numbers: List[int]):
    a = 1
    for n in numbers:
        a *= n
    return a
