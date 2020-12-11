from utils import get_lines
from typing import Tuple
from copy import deepcopy

occupied = '#'
empty = 'L'


def _is_seat_correct(position: Tuple[int, int], size: Tuple[int, int]) -> bool:
    return 0 <= position[0] < size[0] and 0 <= position[1] < size[1]


def adjacent_seats(position: Tuple[int, int], size: Tuple[int, int]):
    offsets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    seats = [(offset[0] + position[0], offset[1] + position[1]) for offset in offsets]
    return [seat for seat in seats if _is_seat_correct(seat, size)]


def becomes_occupied(layout, position: Tuple[int, int], size: Tuple[int, int]) -> bool:
    seats = adjacent_seats(position, size)
    values = [layout[a[0]][a[1]] for a in seats]
    return occupied not in values


def becomes_empty(layout, position: Tuple[int, int], size: Tuple[int, int]) -> bool:
    seats = adjacent_seats(position, size)
    values = [layout[a[0]][a[1]] for a in seats]
    return values.count(occupied) >= 4


def _print_layout(layout):
    print('\n'.join([''.join(a) for a in layout]))


if __name__ == "__main__":
    data = get_lines("seating-system.txt")
    data = [list(a) for a in data]
    size = (len(data), len(data[0]))
    print(size)

    old_data = deepcopy(data)
    while True:
        # _print_layout(data)
        # print('\n')
        for x in range(size[0]):
            for y in range(size[1]):
                if old_data[x][y] == occupied and becomes_empty(old_data, (x, y), size):
                    data[x][y] = empty
                elif old_data[x][y] == empty and becomes_occupied(old_data, (x, y), size):
                    data[x][y] = occupied

        # _print_layout(data)

        if old_data != data:
            old_data = deepcopy(data)
        else:
            break

    print(sum([a.count(occupied) for a in data]))


