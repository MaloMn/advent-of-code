from utils import get_lines
import re


def print_g(grid):
    print('\n'.join(['\t'.join([str(i) for i in a]) for a in grid]))


def get_tiles(f):
    return {re.search(r'\d+', f[i]).group(): [list(a) for a in f[i+1:i+11]] for i in range(0, len(f), 12)}


def rotate_clockwise(grid):
    # print('rotating', grid)
    return [[grid[j][i] for j in range(len(grid) - 1, -1, -1)] for i in range(len(grid))]


def flip(grid, direct):
    if direct == 'h':
        return [line[::-1] for line in grid]
    else:
        return grid[::-1]


def neighbours(cell, size):
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neigh = [(cell[0] + offset[0], cell[1] + offset[1]) for offset in offsets]
    return [(a, b) for a, b in neigh if 0 <= a < size and 0 <= b < size]


def compare_sides(loc_a, loc_b, tile_a, tile_b) -> bool:
    # print('compare_sides', loc_a, loc_b, tile_a, tile_b)
    offset = (loc_b[0] - loc_a[0], loc_b[1] - loc_a[1])
    if offset == (0, 1):
        return [line[-1] for line in tile_a] == [line[0] for line in tile_b]
    elif offset == (0, -1):
        return [line[0] for line in tile_a] == [line[-1] for line in tile_b]
    elif offset == (1, 0):
        return tile_a[-1] == tile_b[0]
    elif offset == (-1, 0):
        # print('here')
        return tile_a[0] == tile_b[-1]


if __name__ == "__main__":
    data = get_lines('jurassic.txt')
    tiles = get_tiles(data)

    nb_tiles = len(tiles.keys())
    square_size = int(nb_tiles**(1/2))
    print(square_size)

    full_map = [["" for i in range(square_size * 2 - 1)] for j in range(square_size * 2 - 1)]
    current_tile = list(tiles.keys())[0]
    full_map[square_size - 1][square_size - 1] = current_tile
    tiles[current_tile] = flip(tiles[current_tile], 'v')

    opened_neigh = neighbours((square_size - 1, square_size - 1), square_size * 2 - 1)
    # print(tiles[current_tile])

    opened = list(tiles.keys())
    opened.remove(current_tile)
    closed = [current_tile]
    closed_loc = {(square_size - 1, square_size - 1)}
    # print(closed_loc)

    while True:
        for i in range(len(opened)):
            # For each tile
            for loc in opened_neigh:
                # print(opened[i], loc)
                # For each neighbour location
                is_found = False
                for flipped in ['h', 'v', 'h', 'v']:
                    if not is_found:
                        tiles[opened[i]] = flip(tiles[opened[i]], flipped)
                        for rot in range(4):
                            # print(tiles[opened[i]])
                            # For each rotation
                            if not is_found:
                                tiles[opened[i]] = rotate_clockwise(tiles[opened[i]])
                                for side in neighbours(loc, square_size * 2 - 1):
                                    if full_map[side[0]][side[1]] != "":
                                        if compare_sides(loc, side, tiles[opened[i]], tiles[full_map[side[0]][side[1]]]):
                                            # print('### AMAZING ###', loc, opened[i], side)
                                            # print_g(tiles[opened[i]])
                                            full_map[loc[0]][loc[1]] = opened[i]
                                            closed.append(opened[i])
                                            closed_loc.add(loc)
                                            opened_neigh += neighbours(loc, square_size * 2 - 1)
                                            opened_neigh = list(set(opened_neigh) - closed_loc)
                                            # print(closed, opened[i], opened_neigh, closed_loc)
                                            is_found = True
                                            break
                            else:
                                break
                    else:
                        break

        closed = list(set(closed))
        opened = list(set(opened) - set(closed))

        if len(opened) == 0:
            break

    full_map = [[b for b in a if b != ''] for a in full_map]
    full_map = [a for a in full_map if a != []]
    print(full_map)

    map_image = []

    for line in full_map:
        lines = [[] for i in range(10)]
        for i in line:
            # print(i)
            for j in range(10):
                # print(tiles[i][j])
                lines[j] += tiles[i][j]
        map_image += lines

    map_image = [a[1:len(a)-1] for a in map_image][1:len(map_image) - 1]
    text = '\n'.join([''.join(a) for a in map_image])
    print(text)

    with open('sea_monsters.txt', 'w') as f:
        f.write(text)

