from utils import get_lines


def _check_is_sum(numbers, nb):
    for a in numbers:
        for b in numbers:
            if a + b == nb and a != b:
                return True
    return False


def _find_contiguous_set(lines, result):
    for j in range(len(lines)):
        compound = 0
        output = []

        for k in range(j, len(lines)):
            # print(compound)
            compound += lines[k]
            output.append(lines[k])

            if compound >= result:
                break

        if compound == result and len(output) >= 2:
            return output
    return None


if __name__ == "__main__":
    preamble = 25
    data = get_lines('encoding-error.txt')
    data = [int(a) for a in data]
    invalid = 0
    for i in range(preamble, len(data)):
        if not _check_is_sum(data[i - preamble:i], data[i]):
            invalid = data[i]
            break

    print(invalid)
    contiguous = _find_contiguous_set(data, invalid)
    print(sum([min(contiguous), max(contiguous)]))
