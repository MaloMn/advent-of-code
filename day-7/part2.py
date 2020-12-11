import re
from utils import get_lines, product
from typing import Dict, List


def rec_color(bags_dict, c) -> int:
    return _rec_color(bags_dict, c) - 1


def _rec_color(bags_dict, c) -> int:
    print("rec_color(bags_dist, {})".format(c))
    output = 0
    for key, value in bags_dict[c].items():
        a = _rec_color(bags_dict, key)
        print(value, a)
        a *= value
        output += a if a > 0 else value

    print("output of rec_color(bags_dist, {}) = {}".format(c, output))
    return output + 1


if __name__ == "__main__":

    data = get_lines('bags.txt')

    bags: Dict[str, Dict[str, int]] = dict()
    # Collecting the colors
    pattern = r'\d*\s?\w* \w* bag'
    for line in data:
        bag = re.findall(pattern, line)
        bag_dict: Dict[str, int] = dict()
        for color in bag[1:]:
            # Number of bags of that color
            nb: str = color.split(' ')[0]
            # Color of the bag
            color = ' '.join(color.split(' ')[1:])
            color = color.replace(' bag', '')
            # Removing empty values
            if color != "no other":
                bag_dict[color] = int(nb)

        bags[bag[0].replace(' bag', '')] = bag_dict

    print(rec_color(bags, 'shiny gold'))


