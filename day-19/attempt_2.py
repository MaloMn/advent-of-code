from typing import Tuple
from utils import get_lines
import re
import sys

sys.setrecursionlimit(15000)


def gather_rules(file):
    output = {}
    for line in file:
        nb = line.split(':')[0]
        values = line.split(':')[1]
        values = values.replace(' ', '')
        values = values.replace('"', '')
        values = list(values)
        output[nb] = values
    return output


def apply_rules(rules_set: dict, rule: str) -> str:
    # print('f', rule, text)
    output = "("
    next_rules = rules_set[rule]

    try:
        pipe = next_rules.index('|')
        # print('Pipe in list')
    except ValueError:
        # print('Pipe not in list')
        pipe = len(next_rules)

    for r in next_rules[:pipe]:
        if re.match(r'[^0-9]+', r) is not None:
            output += r
        else:
            output += apply_rules(rules_set, r)

    if len(next_rules[pipe + 1:]) == 0:
        return output[1:]

    output += '|'
    for r in next_rules[pipe + 1:]:
        if re.match(r'[^0-9]+', r) is not None:
            output += r
        else:
           output += apply_rules(rules_set, r)

    return output + ')'


if __name__ == "__main__":
    data = get_lines('message.txt')
    rules = gather_rules(data[:data.index('')])

    pattern = apply_rules(rules, '0')
    print(pattern)
    texts = data[data.index('') + 1:]

    result = 0
    for z in texts:
        match = re.match(pattern, z)
        if match is not None and match.span()[1] == len(z):
            result += 1

    print(result)
