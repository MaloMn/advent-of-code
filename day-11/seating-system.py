from utils import get_lines
from typing import Tuple
from copy import deepcopy

occupied = '#'
empty = 'L'
floor = '.'


def _grid(size: Tuple[int, int]):
    for a in range(size[0]):
        for b in range(size[1]):
            yield a, b


def _is_seat_correct(position: Tuple[int, int], size: Tuple[int, int]) -> bool:
    return 0 <= position[0] < size[0] and 0 <= position[1] < size[1]


def adjacent_seats(layout, position: Tuple[int, int], size: Tuple[int, int]):
    offsets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    output = []
    for offset in offsets:
        seats_line = []
        current_seat = position
        while True:
            current_seat = (offset[0] + current_seat[0], offset[1] + current_seat[1])

            if not _is_seat_correct(current_seat, size):
                break

            seats_line.append(layout[current_seat[0]][current_seat[1]])
        output.append(seats_line)
    return output


def becomes_occupied(layout, position: Tuple[int, int], size: Tuple[int, int]) -> bool:
    seats = adjacent_seats(layout, position, size)
    seats = [list(filter(lambda a: a != floor, seats_line)) for seats_line in seats]
    seats = list(filter(lambda a: a != [], seats))
    visible_seats = [line[0] for line in seats]

    return occupied not in visible_seats


def becomes_empty(layout, position: Tuple[int, int], size: Tuple[int, int]) -> bool:
    seats = adjacent_seats(layout, position, size)
    seats = [list(filter(lambda a: a != floor, seats_line)) for seats_line in seats]
    seats = list(filter(lambda a: a != [], seats))
    visible_seats = [line[0] for line in seats]

    return visible_seats.count(occupied) >= 5


def _print_layout(layout):
    print('\n'.join([''.join(a) for a in layout]))


if __name__ == "__main__":
    data = get_lines("seating-system.txt")
    data = [list(a) for a in data]
    layout_size = (len(data), len(data[0]))
    print(layout_size)

    steps = 0
    old_data = deepcopy(data)
    while True:
        # _print_layout(data)
        # print('\n')
        for x, y in _grid(layout_size):
            if old_data[x][y] == occupied and becomes_empty(old_data, (x, y), layout_size):
                data[x][y] = empty
            elif old_data[x][y] == empty and becomes_occupied(old_data, (x, y), layout_size):
                data[x][y] = occupied

        # _print_layout(data)

        if old_data != data:
            old_data = deepcopy(data)
        else:
            break

        print(steps)
        steps += 1

    print(sum([a.count(occupied) for a in data]))


