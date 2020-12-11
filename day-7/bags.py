import re
from utils import get_lines

data = get_lines('bags.txt')
print(data)

bags = dict()

# Collecting the colors
pattern = r'\w* \w* bag'
for line in data:
    bag = re.findall(pattern, line)
    bag = [a[:len(a) - 4] for a in bag if a != 'no other bag']
    bags[bag[0]] = bag[1:]

# ### PART 1 ###
opened = ['shiny gold']
final = []

while True:
    new = []
    for bag in opened:
        new += [x for x in bags.keys() if bag in bags[x]]

    if len(new) == 0:
        break

    opened = list(set(new))
    final += opened

print(len(set(final)))
