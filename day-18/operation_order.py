from utils import get_lines
import re


def _find_next_op(formula, op):
    match = re.search(r'\d+[' + op + ']\d+', formula)
    span = match.span()
    f = match.group()
    a, b = re.findall(r'\d+', f)
    return a, op, b, span


def compute(calculation) -> int:
    calculation = calculation.replace(' ', '')
    return _compute(calculation)


def _compute(formula) -> int:
    print('f', formula)
    if '(' in formula:
        start = len(formula) - formula[::-1].find('(')
        end = formula[start:].find(')') + start
        sub_result = _compute(formula[start:end])
        formula = formula[:start - 1] + str(sub_result) + formula[end + 1:]
        return _compute(formula)

    elif '+' in formula:
        a, op, b, span = _find_next_op(formula, '+')
        temp = int(a) + int(b)

        return _compute(formula[:span[0]] + str(temp) + formula[span[1]:])

    elif '*' in formula:
        a, op, b, span = _find_next_op(formula, '*')
        temp = int(a) * int(b)

        return _compute(formula[:span[0]] + str(temp) + formula[span[1]:])

    else:
        return int(formula)


if __name__ == "__main__":
    data = get_lines('operation.txt')

    output = 0
    for line in data:
        output += compute(line)

    print(output)
