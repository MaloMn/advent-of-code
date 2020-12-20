from utils import get_lines
from typing import List, Tuple


def adapted_gray_code(nb_bits) -> List[Tuple]:
    """Gray code with 3 values for bits: -1, 0, 1"""
    values = [(-1,), (0,), (1,)]
    if nb_bits == 1:
        return values
    else:
        piece = adapted_gray_code(nb_bits - 1)
        output = []
        for a in values:
            for line in piece:
                output.append(a + line)

        return output


offsets = adapted_gray_code(4)
offsets.remove((0, 0, 0, 0))


def add(a, b):
    output = tuple()
    for i in range(0, len(a)):
        output += (a[i] + b[i],)
    return output


def neighbours(cube: Tuple[int, int, int, int]) -> List[Tuple[int, int, int, int]]:
    neigh = [add(a, cube) for a in offsets]
    return neigh


if __name__ == "__main__":
    data = get_lines("conway.txt")
    data = [list(a) for a in data]

    cycles = 6
    cubes = {(i, j, 0, 0) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == '#'}
    old_cubes = list(cubes)

    for cycle in range(cycles):
        # Running through the active cells
        inactive_cubes = []
        for c in old_cubes:
            neighbour = neighbours(c)
            inactive = [a for a in neighbour if a not in old_cubes]
            if len(inactive) not in [77, 78]:
                cubes.remove(c)
            inactive_cubes += inactive

        inactive_cubes = list(set(inactive_cubes))
        # Activating inactive cubes
        for c in inactive_cubes:
            others = [n for n in neighbours(c) if n in old_cubes]
            if len(others) == 3:
                cubes.add(c)

        old_cubes = list(cubes)

        print(len(cubes))
