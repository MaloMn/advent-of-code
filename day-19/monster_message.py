from typing import Tuple
from utils import get_lines
import re


def gather_rules(file):
    output = {}
    for line in file:
        nb = line.split(':')[0]
        values = line.split(':')[1]
        values = values.replace('"', '')
        values = re.findall(r'(\d+|\||\w+)', values)
        output[nb] = values
    return output


def apply_rules(rules_set: dict, rule: str, text: str) -> bool:
    # print('f', rule, text)

    text_base = text

    if len(text) == 0:
        return True

    first_is_correct = True
    next_rules = rules_set[rule]

    try:
        pipe = next_rules.index('|')
        # print('Pipe in list')
    except ValueError:
        # print('Pipe not in list')
        pipe = len(next_rules)

    for r in next_rules[:pipe]:
        # print('-->', r, text)
        current_text, text = text, text[1:]
        if re.match(r'[^0-9]+', r) is not None:
            # print(r, current_text[0], r == current_text[0])
            first_is_correct &= r == current_text[0]
        else:
            first_is_correct &= apply_rules(rules_set, r, current_text)

    if len(next_rules[pipe + 1:]) == 0:
        return first_is_correct

    text = text_base
    snd_is_correct = True
    for r in next_rules[pipe + 1:]:
        # print('-->', r, text)
        current_text, text = text, text[1:]
        if re.match(r'[^0-9]+', r) is not None:
            print(r, current_text[0], r == current_text[0])
            snd_is_correct &= r == current_text[0]
        else:
            snd_is_correct &= apply_rules(rules_set, r, current_text)

    # print('first', first_is_correct, 'second', snd_is_correct)
    return first_is_correct or snd_is_correct


if __name__ == "__main__":
    data = get_lines('message.txt')
    rules = gather_rules(data[:data.index('')])

    result = 0
    texts = data[data.index('') + 1:]
    for z in texts:
        if apply_rules(rules, '0', z):
            result += 1

    print(result)
