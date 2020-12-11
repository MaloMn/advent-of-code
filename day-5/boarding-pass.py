from typing import List
from utils import get_lines


def get_nb_from_bin(binaries, a, b):
    for nb in binaries:
        if nb == '1':
            a = a + (b - a) // 2 + 1
        else:
            b = a + (b - a) // 2
    return a


def get_inverts(nbs: List[int]):
    return [i for i in range(nbs[0], nbs[-1] + 1) if i not in nbs]


if __name__ == "__main__":
    seats = []
    data = get_lines('boarding-pass.txt')
    for seat in data:
        bin_seat = seat.replace('F', '0')
        bin_seat = bin_seat.replace('B', '1')
        bin_seat = bin_seat.replace('L', '0')
        bin_seat = bin_seat.replace('R', '1')

        row = get_nb_from_bin(bin_seat[:7], 0, 127)
        column = get_nb_from_bin(bin_seat[7:], 0, 7)
        seat_id = row*8 + column

        seats.append(seat_id)

    print(get_inverts(sorted(seats)))

