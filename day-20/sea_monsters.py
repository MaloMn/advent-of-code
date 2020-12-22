from utils import get_lines
from jurassic_jigsaw import flip, rotate_clockwise

sea_monster = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']

monster_size = (len(sea_monster), len(sea_monster[0]))
print(monster_size)


def is_monster(portion):
    # print(portion)
    # print(sea_monster)
    for i in range(len(portion)):
        for j in range(len(portion[0])):
            if sea_monster[i][j] == '#' and portion[i][j] != "#":
                return False
    return True


def section(f, v, h):
    lines = f[v[0]:v[1]]
    lines = [a[h[0]:h[1]] for a in lines]
    return lines


if __name__ == "__main__":
    data = get_lines('sea_monsters.txt')

    for rot in range(4):
        data = rotate_clockwise(data)
        data = [''.join(a) for a in data]
        for flipped in ['h', 'v', 'h', 'v']:
            data = flip(data, flipped)

    # data = rotate_clockwise(data)
    # data = [''.join(a) for a in data]
    # data = flip(data, 'h')

    # print('\n'.join(data))

            monster_nb = 0
            for i in range(len(data) - monster_size[0]):
                for j in range(len(data) - monster_size[1]):
                    # print(i, j)
                    sec = section(data, (i, i+monster_size[0]), (j, j+monster_size[1]))
                    if is_monster(sec):
                        monster_nb += 1
            if monster_nb > 0:
                print(monster_nb, 15*monster_nb, ''.join(data).count('#') - 15*monster_nb)
                break
