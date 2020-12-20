from utils import get_lines
import re


def _find_next_op(formula):
    match = re.search(r'\d+[+*]\d+', formula)
    end = match.span()[1]
    f = match.group()
    a, b = re.findall(r'\d+', f)
    op = re.search(r'[+*]', f).group()
    return a, op, b, end


def compute(calculation) -> int:
    calculation = calculation.replace(' ', '')
    return _compute(calculation)


def _compute(formula) -> int:
    # print('f', formula)
    if '(' in formula:
        start = len(formula) - formula[::-1].find('(')
        end = formula[start:].find(')') + start
        sub_result = _compute(formula[start:end])
        formula = formula[:start - 1] + str(sub_result) + formula[end + 1:]
        return _compute(formula)

    elif '+' in formula or '*' in formula:
        a, op, b, end = _find_next_op(formula)

        if op == '+':
            temp = int(a) + int(b)
        else:
            temp = int(a) * int(b)

        return _compute(str(temp) + formula[end:])

    else:
        return int(formula)


if __name__ == "__main__":
    data = get_lines('operation.txt')

    output = 0
    for line in data:
        output += compute(line)

    print(output)
