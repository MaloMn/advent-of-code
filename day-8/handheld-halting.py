from utils import get_lines
import re


def move(index: int, action: str, sign: str, nb: str, acc: int):
    if action == 'nop':
        return index + 1, acc
    nb = int(nb)
    if action == 'acc':
        if sign == '-':
            return index + 1, acc - nb
        if sign == '+':
            return index + 1, acc + nb
    if action == 'jmp':
        if sign == '-':
            return index - nb, acc
        if sign == '+':
            return index + nb, acc


def program(lines):
    index, acc = 0, 0
    index_list = [index]
    while True:
        index, acc = move(index, *lines[index], acc)

        if index not in index_list and index < len(lines):
            index_list.append(index)
        else:
            break
    return index, acc


if __name__ == "__main__":
    data = get_lines('handheld-halting.txt')
    temp = re.compile(r'(\w*)\s([+-])(.*)')
    data = [list(temp.match(d).groups()) for d in data]
    print(data)

    i, a = 0, 0
    index_replace = 0
    while index_replace < len(data):
        if data[index_replace][0] in ['jmp', 'nop']:
            data[index_replace][0] = 'jmp' if data[index_replace][0] == 'nop' else 'nop'
            i, a = program(data)
            # If success
            if i >= len(data):
                break
            else:
                data[index_replace][0] = 'jmp' if data[index_replace][0] == 'nop' else 'nop'

        index_replace += 1

    print('acc =', a)
