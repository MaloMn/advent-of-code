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
        values = values.replace('"', '')
        values = re.findall(r'(\d+|\||\w+)', values)
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
        if rule != '0':
            return output[1:]
        else:
            return output[1:]

    output += '|'
    for r in next_rules[pipe + 1:]:
        if re.match(r'[^0-9]+', r) is not None:
            output += r
        else:
           output += apply_rules(rules_set, r)

    if rule in ['42', '31']:
        return output + ')' + '+'
    else:
        return output + ')'


if __name__ == "__main__":
    data = get_lines('message.txt')
    rules = gather_rules(data[:data.index('')])
    # print(rules)

    pattern = apply_rules(rules, '0')
    # pattern = r'((b(a(bb|ab)|b(a|b)(a|b))|a(bbb|a(bb|a(a|b))))b|(((aa|ab)a|bbb)b|((a|b)a|bb)aa)a)+((b(a(bb|ab)|b(a|b)(a|b))|a(bbb|a(bb|a(a|b))))b|(((aa|ab)a|bbb)b|((a|b)a|bb)aa)a)+(b(b(aba|baa)|a(b(ab|(a|b)a)|a(ba|ab)))|a(b((ab|(a|b)a)b|((a|b)a|bb)a)|a(bab|(ba|bb)a)))+((b(a(bb|ab)|b(a|b)(a|b))|a(bbb|a(bb|a(a|b))))b|(((aa|ab)a|bbb)b|((a|b)a|bb)aa)a)+((b(a(bb|ab)|b(a|b)(a|b))|a(bbb|a(bb|a(a|b))))b|(((aa|ab)a|bbb)b|((a|b)a|bb)aa)a)+(b(b(aba|baa)|a(b(ab|(a|b)a)|a(ba|ab)))|a(b((ab|(a|b)a)b|((a|b)a|bb)a)|a(bab|(ba|bb)a)))+((b(a(bb|ab)|b(a|b)(a|b))|a(bbb|a(bb|a(a|b))))b|(((aa|ab)a|bbb)b|((a|b)a|bb)aa)a)+((b(a(bb|ab)|b(a|b)(a|b))|a(bbb|a(bb|a(a|b))))b|(((aa|ab)a|bbb)b|((a|b)a|bb)aa)a)+(b(b(aba|baa)|a(b(ab|(a|b)a)|a(ba|ab)))|a(b((ab|(a|b)a)b|((a|b)a|bb)a)|a(bab|(ba|bb)a)))+'
    print(pattern)
    print(pattern.count('+'))
    texts = data[data.index('') + 1:]

    result = 0
    for z in texts:
        match = re.match(pattern, z)
        if match is not None and match.span() == (0, len(z)):
            result += 1
            # print(z)

    print(result)
