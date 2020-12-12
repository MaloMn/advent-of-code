from utils import get_lines
from typing import Tuple
import math


def add(a: Tuple[int, int], b: Tuple[int, int]):
    return a[0] + b[0], a[1] + b[1]


def int_product(a: Tuple[int, int], b: int)
    return a[0] * b, a[1] * b


def move(pos, direct, steps):
    return add(pos, int_product(direct, steps))

if __name__ == "__main__":
    data = get_lines('rain_risk.txt')
    data = [(a[0], int(a[1:])) for a in data]
    print(data)

    orientation = (1, 0)
    position = (0, 0)

    for d, n in data:
        if d == "N":
            position = move(position, (0, 1), n)
        elif d == "S":
            position = move(position, (0, -1), n)
        elif d == "E":
            position = move(position, (1, 0), n)
        elif d == "W":
            position = move(position, (-1, 0), n)
        elif d == "L":
            pass
        elif d == "R":
            pass
        elif d == "F":
            pass
